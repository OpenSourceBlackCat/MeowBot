from playsound import playsound
from colorama import Fore
from urllib.request import urlopen
from json import load
import random
def printError(text):
    print(Fore.RED, text, Fore.RESET)
def jsonFetch():
    global soundBye, funnyBotSounds, funnyBotSoundsRaw ,fartBotSounds
    internalMeowBotConfigFile = urlopen("https://gitlab.com/OpenSourceBlackCat/meowbotassets/-/raw/main/config/internalMeowBotSetting.json")
    internalMeowBotConfig = load(internalMeowBotConfigFile)
    soundBye = internalMeowBotConfig["MeowSounds"]["soundBye"]
    funnyBotSounds = internalMeowBotConfig["MeowSounds"]["funnySounds"]
    funnyBotSoundsRaw = []
    fartBotSounds = []
    for i in internalMeowBotConfig["MeowSounds"]["fartSounds"]:
        fartBotSounds.append(internalMeowBotConfig["MeowSounds"]["fartSounds"][i])
    for i in internalMeowBotConfig["MeowSounds"]["funnySounds"]:
        funnyBotSoundsRaw.append(i)
    return None
def funnySounds(sponsorVoice, authorName, chatMessage):
    jsonFetch()
    if 'ft' in chatMessage:
        try:
            chatMessage = chatMessage.replace('ft', '')
            fartSound = random.choice(fartBotSounds)
            playsound(fartSound)
            sponsorVoice(f" Hag Diye {authorName}")
        except:
            printError("Error Playing Sound")
    elif chatMessage in funnyBotSoundsRaw:
        try:
            sponsorVoice(f"{authorName} Says")
            playsound(funnyBotSounds[chatMessage])
        except: 
            printError("Error Playing Sound")
