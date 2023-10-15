nnfrom tkinter import Tk, Label, Button, Canvas, NW
import requests
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
from colorama import Fore
from json import load
from urllib.request import urlopen
from importlib import reload
import MeowChangelog as AC
def printError(text):
    print(Fore.RED, text, Fore.RESET)
def fileLoader():
    global botFiles, botUrls, noUpdateLabel
    try:
        noUpdateLabel.destroy()
    except: pass
    internalMeowBotConfigFile = urlopen("https://gitlab.com/OpenSourceBlackCat/MeowBotAssets/-/raw/main/config/internalMeowBotSetting.json")
    internalMeowBotConfig = load(internalMeowBotConfigFile)
    botFiles = internalMeowBotConfig["MeowBotUpdaterFiles"]["botFiles"]
    botUrls = []
    if float(load(urlopen(internalMeowBotConfig["MeowBotUpdaterFiles"]["versionCheckFile"]))["version"]) > float(AC.versionMain):
        for i in internalMeowBotConfig["MeowBotUpdaterFiles"]["botUrls"]:
            botUrls.append(internalMeowBotConfig["MeowBotUpdaterFiles"]["botUrls"][i])
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
        downloadDone = Label(root, text="MEOW BOT Has Been Updated Successfully.", background='green', foreground='white').pack()
        reload(AC)
        updateversionLabel = Label(root, text=f"Updated Version: {AC.version}", background='green', foreground='white').pack()
        openMeowChannellog()
    except Exception as e:
        printError('Error!', e)
        
def openMeowChannellog():
    def showMeowChannellog():
        def hideMeowChannellog():
            root.geometry("300x300")
            changeslog.destroy()
            closeMeowChannellog.destroy()
            openMeowChannellog()
        root.geometry("300x500")
        openchannellog.destroy()
        closeMeowChannellog = Button(root, text="Hide Channel Log", background='green', foreground='white', command=hideMeowChannellog)
        closeMeowChannellog.pack()
        changeslog = Label(root, text=f"{AC.channellog}", background='green', foreground='white')
        changeslog.pack()
    openchannellog = Button(root, text="Show Channel Log", background='green', foreground='white', command=showMeowChannellog) 
    openchannellog.pack()
def main():
    global root, updateEnter
    root = Tk()
    root.title("MEOW BOT")
    root.geometry("300x300")
    root.resizable(False, False)
    root.configure(bg='green')
    canvas = Canvas(root, width=300, height=100)
    canvas.pack()
    ameyBotLogo = "https://gitlab.com/OpenSourceBlackCat/MeowBotAssets/raw/main/MeowBotUpdater.png"
    image_byt = urlopen(ameyBotLogo).read()
    img_main = Image.open(BytesIO(image_byt))
    img_b = img_main.resize((300, 100))
    img = ImageTk.PhotoImage(img_b)
    canvas.create_image(1,1, anchor=NW, image=img)
    ameyBotLabel = Label(root, text="MEOW BOT", background='green', foreground='white').pack()
    versionLabel = Label(root, text=f"Current Version: {AC.version}", background='green', foreground='white').pack()
    updateEnter = Button(root, text="Check For Updates", background='green', foreground='white', command=fileLoader)
    updateEnter.pack()
    root.mainloop()
if __name__ == '__main__':
    main()
