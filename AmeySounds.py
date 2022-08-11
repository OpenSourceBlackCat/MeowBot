from playsound import playsound
from colorama import Fore
from urllib.request import urlopen
from json import load
import random
def printError(text):
    print(Fore.RED, text, Fore.RESET)
def jsonFetch():
    global soundBye, funnyBotSounds, funnyBotSoundsRaw ,fartBotSounds
    internalAmeyBotConfigFile = urlopen("https://github.com/Amey-Gurjar/AmeyBotAssets/raw/main/JSON/internalAmeyBotSetting.json")
    internalAmeyBotConfig = load(internalAmeyBotConfigFile)
    soundBye = internalAmeyBotConfig["AmeySounds"]["soundBye"]
    funnyBotSounds = internalAmeyBotConfig["AmeySounds"]["funnySounds"]
    funnyBotSoundsRaw = []
    fartBotSounds = []
    for i in internalAmeyBotConfig["AmeySounds"]["fartSounds"]:
        fartBotSounds.append(internalAmeyBotConfig["AmeySounds"]["fartSounds"][i])
    for i in internalAmeyBotConfig["AmeySounds"]["funnySounds"]:
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