import os, winshell
from urllib.request import urlopen
from json import load
desktopShortcuts = ["AmeyBot.lnk", "AmeyBotUpdater.lnk"]
startShortcuts = ["AmeyBot.lnk", "AmeyBotUpdater.lnk", "AmeyBotUninstaller.lnk"]
internalAmeyBotConfig = load(urlopen("https://github.com/Amey-Gurjar/AmeyBotAssets/raw/main/JSON/internalAmeyBotSetting.json"))
startPath = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "AmeyBot")
dataDir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "AmeyBot")
desktopPath = winshell.desktop()
for botFile in internalAmeyBotConfig["AmeyBotUpdaterFiles"]["botFiles"]:
    os.remove(os.path.join(dataDir, botFile))
for botFile in desktopShortcuts:
    os.remove(os.path.join(desktopPath, botFile))
for botFile in startShortcuts:
    os.remove(os.path.join(startPath, botFile))
print("AmeyBot Uninstalled Successfully!")
input("Press Any Key To Exit...")