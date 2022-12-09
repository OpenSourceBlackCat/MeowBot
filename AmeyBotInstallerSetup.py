import os, sys
pipList = ["requests", "colorama"]
for pip in pipList:
    os.system(f"pip install {pip}")
from tkinter import Tk, Label, Button, Canvas, PhotoImage, NW
import requests
from urllib.request import urlopen
import base64
from threading import Thread
from colorama import Fore
from json import load
def printError(text):
    print(Fore.RED, text, Fore.RESET)
def fileLoader():
    global botFiles, botUrls, installLabel
    installLabel = Label(root, text="Installing Modules (This May Take A While..)", background='green', foreground='white')
    installLabel.pack()
    try:
        updateEnter.destroy()
    except: pass
    requirePips = sorted(["google-auth-httplib2", "google-api-python-client", "google-auth-oauthlib", "requests", "urllib3", "pybase64", "pillow", "pil-tools", "gtts", "pytchat", "pyjokes", "datetime", "wikipedia", "emoji", "pyttsx3", "playsound==1.2.2", "colorama", "pyfiglet", "winshell", "googletrans==4.0.0rc1"])
    for i in range(len(requirePips)):
        updateLabel = Label(root, text=f"Installing {requirePips[i]}", background='green', foreground='white')
        updateLabel.pack()
        os.system(f"pip install {requirePips[i]}")
        try:
            updateLabel.destroy()
        except: pass
    internalAmeyBotConfigFile = urlopen("https://github.com/Amey-Gurjar/AmeyBotAssets/raw/main/JSON/internalAmeyBotSetting.json")
    internalAmeyBotConfig = load(internalAmeyBotConfigFile)
    botFiles = internalAmeyBotConfig["AmeyBotUpdaterFiles"]["botFiles"]
    botUrls = []
    for i in internalAmeyBotConfig["AmeyBotUpdaterFiles"]["botUrls"]:
        botUrls.append(internalAmeyBotConfig["AmeyBotUpdaterFiles"]["botUrls"][i])
    mainDownload()
def botFileDownloader(botFileUrl, botFileName):
    global dataDir
    homeDir = os.path.expanduser('~')
    if sys.platform == "win32":
        dataDir = os.path.join(homeDir, "AppData", "Local", "AmeyBot")
        if not os.path.exists(dataDir):
            os.mkdir(dataDir)
    else:
        dataDir = os.sep.join(homeDir, "AmeyBot")
        if not os.path.exists(dataDir):
            os.mkdir(dataDir)
    myBotFile = requests.get(botFileUrl, allow_redirects=True)
    open(os.path.join(dataDir, botFileName), "wb").write(myBotFile.content)
def shortCut(name, fileName, dataDir, desktopShortcut=False):
    import winshell, win32com.client, pythoncom
    pythoncom.CoInitialize()
    desktop = winshell.desktop()
    dataDirMain = os.path.join(dataDir, fileName)
    mainPath = os.path.join(desktop, name)
    startPath = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "AmeyBot")
    if not os.path.exists(startPath):
        os.mkdir(startPath)
    shell = win32com.client.Dispatch("WScript.Shell")
    if desktopShortcut == True:
        shortcut = shell.CreateShortCut(mainPath)
        shortcut.WorkingDirectory = f"{dataDir}"
        shortcut.Targetpath = f"{dataDirMain}"
        shortcut.IconLocation = f"{os.path.join(dataDir, 'AmeyBotIcon.ico')}"
        shortcut.save()
    startShortcut = shell.CreateShortCut(os.path.join(startPath, name))
    startShortcut.WorkingDirectory = f"{dataDir}"
    startShortcut.Targetpath = f"{dataDirMain}"
    startShortcut.IconLocation = f"{os.path.join(dataDir, 'AmeyBotIcon.ico')}"
    startShortcut.save()
def mainDownload():
    try:
        for i in range(len(botFiles)):
            updateLabel = Label(root, text=f"Installing {botFiles[i]}", background='green', foreground='white')
            updateLabel.pack()
            botFileDownloader(botFileUrl=botUrls[i], botFileName=botFiles[i])
            try:
                updateLabel.destroy()
            except: pass
        try:
            installLabel.destroy()
        except: pass
        shortCut(name="AmeyBot.lnk", fileName="__init__.py", dataDir=dataDir, desktopShortcut=True)
        shortCut(name="AmeyBotUpdater.lnk", fileName="AmeyBotUpdater.py", dataDir=dataDir, desktopShortcut=True)
        shortCut(name="AmeyBotUninstaller.lnk", fileName="AmeyBotUninstaller.py", dataDir=dataDir)
        downloadDone = Label(root, text="AMEY BOT Installed Successfully.", background='green', foreground='white').pack()
    except Exception as e:
        printError("Error!")
def main():
    global root, updateEnter
    root = Tk()
    root.title("AMEY BOT SETUP")
    root.geometry("300x180")
    root.resizable(False, False)
    root.configure(bg='green')
    canvas = Canvas(root, width=300, height=100)
    canvas.pack()
    ameyBotLogo = "https://github.com/Amey-Gurjar/AmeyBotAssets/raw/main/ameyBotUpdater.png"
    image_byt = urlopen(ameyBotLogo).read()
    image_b64 = base64.encodebytes(image_byt)
    img = PhotoImage(data=image_b64)
    canvas.create_image(1,1, anchor=NW, image=img)
    mainLabel = Label(root, text="Amey Youtube Live Chat Bot", background='green', foreground='white').pack()
    updateEnter = Button(root, text="Install", background='green', foreground='white', command=Thread(target=fileLoader).start)
    updateEnter.pack()
    root.mainloop()
if __name__ == '__main__':
    main()
