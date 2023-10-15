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
    global internalMeowBotConfig
    internalMeowBotConfigFile = urlopen("https://gitlab.com/OpenSourceBlackCat/meowbotassets/-/raw/main/config/internalMeowBotSetting.json")
    internalMeowBotConfig = load(internalMeowBotConfigFile)
def addSponsor():
    global newSponsor
    jsonFetch()
    if exists("ini/MeowSponsor.ini") and exists("ini/sponsorSound.ini"):
        MeowSponsor = open("ini/MeowSponsor.ini", "r")
        newSponsor = str(input(Fore.BLUE+"Enter Sponsor's Youtube Channel Link: "+Fore.RESET))
        if "https://www.youtube.com/channel/" in newSponsor or "https://www.youtube.com/c/" in newSponsor:
            newSponsor = newSponsor.replace("https://www.youtube.com/channel/", "")
            newSponsor = newSponsor.replace("https://www.youtube.com/c/", "")
            MeowSponsorRead = MeowSponsor.read()
            if newSponsor not in MeowSponsorRead:
                addMusic()
            else:
                printNor("The Sponsor Is Already In The List!")
                addSponsor()
        else:
            printError("Invalid Channel Url!")
            addSponsor()
    else:
        meowSponsorFile = internalMeowBotConfig["MeowSponsor"]["MeowSponsorTxt"]
        sponsorSoundFile = internalMeowBotConfig["MeowSponsor"]["sponsorSoundFile"]
        get(meowSponsorFile)
        get(sponsorSoundFile)
        meowSponsorFile = get(meowSponsorFile, allow_redirects=True)
        open("ini/MeowSponsor.ini", "wb").write(meowSponsorFile.content)
        sponsorSoundFile = get(sponsorSoundFile, allow_redirects=True)
        open("ini/sponsorSound.ini", "wb").write(sponsorSoundFile.content)
        addSponsor()
def addMusic():
    newSound = str(input(Fore.BLUE+"Enter The Path Of The Music File: "+Fore.RESET))
    newSound = newSound.replace('"', '')
    newSound = newSound.replace("'", "")
    if exists(newSound):
        MeowSponsor = open("ini/MeowSponsor.ini", "a")
        MeowSponsor.write(f"{newSponsor}\n")
        MeowSponsor.close()
        sponsorSound = open("ini/sponsorSound.ini", "a")
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
