import os, winshell
from urllib.request import urlopen
from json import load
desktopShortcuts = ["MeowBot.lnk", "MeowBotaUpdater.lnk"]
startShortcuts = ["MeowBot.lnk", "MeowBotaUpdater.lnk", "MeowBotUninstaller.lnk"]
internalMeowBotConfig = load(urlopen("https://gitlab.com/OpenSourceBlackCat/meowbotassets/-/raw/main/config/internalMeowBotSetting.json"))
startPath = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "MeowBot")
dataDir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "MeowBot")
desktopPath = winshell.desktop()
for botFile in internalMeowBotConfig["MeowBotUpdaterFiles"]["botFiles"]:
    os.remove(os.path.join(dataDir, botFile))
for botFile in desktopShortcuts:
    os.remove(os.path.join(desktopPath, botFile))
for botFile in startShortcuts:
    os.remove(os.path.join(startPath, botFile))
print("MeowBot Uninstalled Successfully!")
input("Press Any Key To Exit...")
