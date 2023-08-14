from playsound import playsound
from urllib.request import urlopen
from json import load
from colorama import Fore
from os.path import exists
from requests import get
def printError(text):
    print(Fore.RED, text, Fore.RESET)
def jsonFetch():
    global internalAmeyBotConfig, sponsorBotSound
    internalAmeyBotConfigFile = urlopen("https://gitlab.com/AmeyaGurjar/ameybotassets/-/raw/main/config/internalAmeyBotSetting.json")
    internalAmeyBotConfig = load(internalAmeyBotConfigFile)
    sponsorBotSound = internalAmeyBotConfig["AmeySounds"]["sponsorSound"]
def sponsorFileCheck(channelId):
    jsonFetch()
    if exists("ini/AmeySponsor.ini") and exists("ini/sponsorSound.ini"):
        sponsorCheck(channelId)
    else:
        ameySponsorFile = internalAmeyBotConfig["AmeySponsor"]["AmeySponsorTxt"]
        sponsorSoundFile = internalAmeyBotConfig["AmeySponsor"]["sponsorSoundFile"]
        get(ameySponsorFile)
        get(sponsorSoundFile)
        ameySponsorFile = get(ameySponsorFile, allow_redirects=True)
        open("ini/AmeySponsor.ini", "wb").write(ameySponsorFile.content)
        sponsorSoundFile = get(sponsorSoundFile, allow_redirects=True)
        open("ini/sponsorSound.ini", "wb").write(sponsorSoundFile.content)
        sponsorFileCheck()
        
def sponsorCheck(channelId):
    try:
        AmeySponsor = open("ini/AmeySponsor.ini", "r")
        soundSponsor = open("ini/sponsorSound.ini", "r")
        AmeySponsor = AmeySponsor.read()
        AmeySponsor = AmeySponsor.split("\n")
        soundSponsor = soundSponsor.read()
        soundSponsor = soundSponsor.split("\n")
        if channelId in AmeySponsor:
            for i in range(len(AmeySponsor)):
                if channelId == AmeySponsor[i]:
                    try:
                        playsound(soundSponsor[i], False)
                    except Exception as e:
                        printError("Exception: ", e)
        else:
            playsound(sponsorBotSound, False)
    except Exception as e:
        printError("Error Playing Sound", e)
