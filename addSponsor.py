from os.path import exists
from colorama import Fore, init
from os import system
from urllib.request import urlopen
from json import load
from requests import get
def printNor(text):
        print(Fore.BLUE, text, Fore.RESET)
def printGood(text):
    print(Fore.GREEN, text, Fore.RESET)
def printError(text):
    print(Fore.RED, text, Fore.RESET)
def jsonFetch():
    global internalAmeyBotConfig
    internalAmeyBotConfigFile = urlopen("https://github.com/Amey-Gurjar/AmeyBotAssets/raw/main/JSON/internalAmeyBotSetting.json")
    internalAmeyBotConfig = load(internalAmeyBotConfigFile)
def addSponsor():
    global newSponsor
    jsonFetch()
    if exists("AmeySponsor.ini") and exists("sponsorSound.ini"):
        AmeySponsor = open("AmeySponsor.ini", "r")
        newSponsor = str(input(Fore.BLUE+"Enter Sponsor's Youtube Channel Link: "+Fore.RESET))
        if "https://www.youtube.com/channel/" in newSponsor or "https://www.youtube.com/c/" in newSponsor:
            newSponsor = newSponsor.replace("https://www.youtube.com/channel/", "")
            newSponsor = newSponsor.replace("https://www.youtube.com/c/", "")
            AmeySponsorRead = AmeySponsor.read()
            if newSponsor not in AmeySponsorRead:
                addMusic()
            else:
                printNor("The Sponsor Is Already In The List!")
                addSponsor()
        else:
            printError("Invalid Channel Url!")
            addSponsor()
    else:
        ameySponsorFile = internalAmeyBotConfig["AmeySponsor"]["AmeySponsorTxt"]
        sponsorSoundFile = internalAmeyBotConfig["AmeySponsor"]["sponsorSoundFile"]
        get(ameySponsorFile)
        get(sponsorSoundFile)
        ameySponsorFile = get(ameySponsorFile, allow_redirects=True)
        open("AmeySponsor.ini", "wb").write(ameySponsorFile.content)
        sponsorSoundFile = get(sponsorSoundFile, allow_redirects=True)
        open("sponsorSound.ini", "wb").write(sponsorSoundFile.content)
        addSponsor()
def addMusic():
    newSound = str(input(Fore.BLUE+"Enter The Path Of The Music File: "+Fore.RESET))
    newSound = newSound.replace('"', '')
    newSound = newSound.replace("'", "")
    if exists(newSound):
        AmeySponsor = open("AmeySponsor.ini", "a")
        AmeySponsor.write(f"{newSponsor}\n")
        AmeySponsor.close()
        sponsorSound = open("sponsorSound.ini", "a")
        sponsorSound.write(f"{newSound}\n")
        sponsorSound.close()
        printGood("Sponsor Added Successfully")
        input()
    else:
        printError("File Not Found!")
        addSponsor()
if __name__ == '__main__':
    system('cls')
    init()
    addSponsor()