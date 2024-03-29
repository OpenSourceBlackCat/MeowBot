import os, sys
pipList = ["requests", "colorama", "pillow"]
for pip in pipList:
    os.system(f"pip install {pip}")
from tkinter import Tk, Label, Button, Canvas, NW
from PIL import Image, ImageTk
import requests
from urllib.request import urlopen
from io import BytesIO
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
    requirePips = sorted(["google-api-python-client", "google-auth-httplib2", "google-auth-oauthlib", "googletrans==4.0.0rc1", "requests", "urllib3", "pybase64", "pillow", "pil-tools", "gtts", "pytchat", "pyjokes", "datetime", "wikipedia", "emoji", "pyttsx3", "playsound==1.2.2", "colorama", "pyfiglet", "winshell"])
    for i in range(len(requirePips)):
        updateLabel = Label(root, text=f"Installing {requirePips[i]}", background='green', foreground='white')
        updateLabel.pack()
        os.system(f"pip install {requirePips[i]}")
        try:
            updateLabel.destroy()
        except: pass
    internalMeowBotConfigFile = urlopen("https://gitlab.com/OpenSourceBlackCat/MeowBotAssets/-/raw/main/config/internalMeowBotSetting.json")
    internalMeowBotConfig = load(internalMeowBotConfigFile)
    botFolds = internalMeowBotConfig["MeowBotUpdaterFiles"]["fileFolds"]
    botFiles = internalMeowBotConfig["MeowBotUpdaterFiles"]["botFiles"]
    botUrls = {}
    for botFoldNum, botFold in enumerate(botFolds):
        for botFile in range(len(botFiles[botFold])):
            botUrls[botFolds.keys()[botFoldNum]] = f"{botFolds[botFold]}/{botFiles[botFold][botFile]}"
    mainDownload()
def botFileDownloader(botFileUrl, botFileName):
    global dataDir
    homeDir = os.path.expanduser('~')
    if sys.platform == "win32":
        dataDir = os.path.join(homeDir, "AppData", "Local", "MeowBot")
        if not os.path.exists(dataDir):
            os.mkdir(dataDir)
    else:
        dataDir = os.sep.join(homeDir, "MeowBot")
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
    startPath = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "MeowBot")
    if not os.path.exists(startPath):
        os.mkdir(startPath)
    shell = win32com.client.Dispatch("WScript.Shell")
    if desktopShortcut == True:
        shortcut = shell.CreateShortCut(mainPath)
        shortcut.WorkingDirectory = f"{dataDir}"
        shortcut.Targetpath = f"{dataDirMain}"
        shortcut.IconLocation = f"{os.path.join(dataDir, 'MeowBotIcon.ico')}"
        shortcut.save()
    startShortcut = shell.CreateShortCut(os.path.join(startPath, name))
    startShortcut.WorkingDirectory = f"{dataDir}"
    startShortcut.Targetpath = f"{dataDirMain}"
    startShortcut.IconLocation = f"{os.path.join(dataDir, 'MeowBotIcon.ico')}"
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
        shortCut(name="MeowBot.lnk", fileName="main.py", dataDir=dataDir, desktopShortcut=True)
        shortCut(name="MeowBotUpdater.lnk", fileName="MeowBotUpdater.py", dataDir=dataDir, desktopShortcut=True)
        shortCut(name="MeowBotUninstaller.lnk", fileName="MeowBotUninstaller.py", dataDir=dataDir)
        downloadDone = Label(root, text="MEOW BOT Installed Successfully.", background='green', foreground='white').pack()
    except Exception as e:
        printError("Error!")
def main():
    global root, updateEnter
    root = Tk()
    root.title("MEOW BOT SETUP")
    root.geometry("300x180")
    root.resizable(False, False)
    root.configure(bg='green')
    canvas = Canvas(root, width=300, height=100)
    canvas.pack()
    meowBotLogo = "https://gitlab.com/OpenSourceBlackCat/MeowBotAssets/raw/main/MeowBotUpdater.png"
    image_byt = urlopen(meowBotLogo).read()
    img_main = Image.open(BytesIO(image_byt))
    img_b = img_main.resize((300, 100))
    img = ImageTk.PhotoImage(img_b)
    canvas.create_image(0,0, anchor=NW, image=img)
    mainLabel = Label(root, text="Meow Youtube Live Chat Bot", background='green', foreground='white').pack()
    updateEnter = Button(root, text="Install", background='green', foreground='white', command=Thread(target=fileLoader).start)
    updateEnter.pack()
    root.mainloop()
if __name__ == '__main__':
    main()
