from playsound import playsound
from urllib.request import urlopen
from json import load
from colorama import Fore
from os.path import exists
from requests import get
def printError(text):
    print(Fore.RED, text, Fore.RESET)
def jsonFetch():
    global internalMeowBotConfig, sponsorBotSound
    internalMeowBotConfigFile = urlopen("https://gitlab.com/OpenSourceBlackCat/meowbotassets/-/raw/main/config/internalMeowBotSetting.json")
    internalMeowBotConfig = load(internalMeowBotConfigFile)
    sponsorBotSound = internalMeowBotConfig["MeowSounds"]["sponsorSound"]
def sponsorFileCheck(channelId):
    jsonFetch()
    if exists("ini/MeowSponsor.ini") and exists("ini/sponsorSound.ini"):
        sponsorCheck(channelId)
    else:
        meowSponsorFile = internalMeowBotConfig["MeowSponsor"]["MeowSponsorTxt"]
        sponsorSoundFile = internalMeowBotConfig["MeowSponsor"]["sponsorSoundFile"]
        get(meowSponsorFile)
        get(sponsorSoundFile)
        meowSponsorFile = get(meowSponsorFile, allow_redirects=True)
        open("ini/MeowSponsor.ini", "wb").write(meowSponsorFile.content)
        sponsorSoundFile = get(sponsorSoundFile, allow_redirects=True)
        open("ini/sponsorSound.ini", "wb").write(sponsorSoundFile.content)
        sponsorFileCheck()
        
def sponsorCheck(channelId):
    try:
        MeowSponsor = open("ini/MeowSponsor.ini", "r")
        soundSponsor = open("ini/sponsorSound.ini", "r")
        MeowSponsor = MeowSponsor.read()
        MeowSponsor = MeowSponsor.split("\n")
        soundSponsor = soundSponsor.read()
        soundSponsor = soundSponsor.split("\n")
        if channelId in MeowSponsor:
            for i in range(len(MeowSponsor)):
                if channelId == MeowSponsor[i]:
                    try:
                        playsound(soundSponsor[i], False)
                    except Exception as e:
                        printError("Exception: ", e)
        else:
            playsound(sponsorBotSound, False)
    except Exception as e:
        printError("Error Playing Sound", e)
