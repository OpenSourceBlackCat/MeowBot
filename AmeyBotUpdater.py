from tkinter import Tk, Label, Button, Canvas, PhotoImage, NW
import requests
from urllib.request import urlopen
import base64
from colorama import Fore
from json import load
from urllib.request import urlopen
from importlib import reload
import AmeyChannellog as AC
def printError(text):
    print(Fore.RED, text, Fore.RESET)
def fileLoader():
    global botFiles, botUrls, noUpdateLabel
    try:
        noUpdateLabel.destroy()
    except: pass
    internalAmeyBotConfigFile = urlopen("https://github.com/Amey-Gurjar/AmeyBotAssets/raw/main/JSON/internalAmeyBotSetting.json")
    internalAmeyBotConfig = load(internalAmeyBotConfigFile)
    botFiles = internalAmeyBotConfig["AmeyBotUpdaterFiles"]["botFiles"]
    botUrls = []
    if float(load(urlopen(internalAmeyBotConfig["AmeyBotUpdaterFiles"]["versionCheckFile"]))["version"]) > float(AC.versionMain):
        for i in internalAmeyBotConfig["AmeyBotUpdaterFiles"]["botUrls"]:
            botUrls.append(internalAmeyBotConfig["AmeyBotUpdaterFiles"]["botUrls"][i])
        mainDownload()
    else:
        noUpdateLabel = Label(root, text=f"No Updates Available.", background='green', foreground='red')
        noUpdateLabel.pack()
def botFileDownloader(botFileUrl, botFileName):
    myBotFile = requests.get(botFileUrl, allow_redirects=True)
    open(botFileName, "wb").write(myBotFile.content)
def mainDownload():
    try:
        downloadRate = Label(root, text="0% Done", background='green', foreground='white')
        downloadRate.pack()
        updateEnter.destroy()
        for i in range(len(botFiles)):
            botFileDownloader(botFileUrl=botUrls[i], botFileName=botFiles[i])
        downloadRate.config(text="100% Done...")
        downloadDone = Label(root, text="AMEY BOT Has Been Updated Successfully.", background='green', foreground='white').pack()
        reload(AC)
        updateversionLabel = Label(root, text=f"Updated Version: {AC.version}", background='green', foreground='white').pack()
        openAmeyChannellog()
    except Exception as e:
        printError('Error!', e)
        
def openAmeyChannellog():
    def showAmeyChannellog():
        def hideAmeyChannellog():
            root.geometry("300x300")
            changeslog.destroy()
            closeAmeyChannellog.destroy()
            openAmeyChannellog()
        root.geometry("300x500")
        openchannellog.destroy()
        closeAmeyChannellog = Button(root, text="Hide Channel Log", background='green', foreground='white', command=hideAmeyChannellog)
        closeAmeyChannellog.pack()
        changeslog = Label(root, text=f"{AC.channellog}", background='green', foreground='white')
        changeslog.pack()
    openchannellog = Button(root, text="Show Channel Log", background='green', foreground='white', command=showAmeyChannellog) 
    openchannellog.pack()
def main():
    global root, updateEnter
    root = Tk()
    root.title("AMEY BOT")
    root.geometry("300x300")
    root.resizable(False, False)
    root.configure(bg='green')
    canvas = Canvas(root, width=300, height=100)
    canvas.pack()
    ameyBotLogo = "https://github.com/Amey-Gurjar/AmeyBotAssets/raw/main/ameyBotUpdater.png"
    image_byt = urlopen(ameyBotLogo).read()
    image_b64 = base64.encodebytes(image_byt)
    img = PhotoImage(data=image_b64)
    canvas.create_image(1,1, anchor=NW, image=img)
    ameyBotLabel = Label(root, text="AMEY BOT", background='green', foreground='white').pack()
    versionLabel = Label(root, text=f"Current Version: {AC.version}", background='green', foreground='white').pack()
    updateEnter = Button(root, text="Check For Updates", background='green', foreground='white', command=fileLoader)
    updateEnter.pack()
    root.mainloop()
if __name__ == '__main__':
    main()