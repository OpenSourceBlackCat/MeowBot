import os, winshell
from urllib.request import urlopen
from json import load
desktopShortcuts = ["AmeyaBot.lnk", "AmeyaBotaUpdater.lnk"]
startShortcuts = ["AmeyaBot.lnk", "AmeyBotaUpdater.lnk", "AmeyaBotUninstaller.lnk"]
internalAmeyBotConfig = load(urlopen("https://gitlab.com/AmeyaGurjar/ameybotassets/-/raw/main/config/internalAmeyBotSetting.json"))
startPath = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "AmeyaBot")
dataDir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "AmeyaBot")
desktopPath = winshell.desktop()
for botFile in internalAmeyBotConfig["AmeyBotUpdaterFiles"]["botFiles"]:
    os.remove(os.path.join(dataDir, botFile))
for botFile in desktopShortcuts:
    os.remove(os.path.join(desktopPath, botFile))
for botFile in startShortcuts:
    os.remove(os.path.join(startPath, botFile))
print("AmeyBot Uninstalled Successfully!")
input("Press Any Key To Exit...")
