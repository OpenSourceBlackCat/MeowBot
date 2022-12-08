import json
import emoji
from colorama import Fore
from urllib.request import urlopen
from googletrans import Translator
from re import sub as resub, compile as recompile
translator = Translator(service_urls=["translate.google.com", "translate.google.co.in"])
emojiPattern = r":(.*?):"
def printError(text):
    print(Fore.RED, text, Fore.RESET)
def configValidate():
    global timeOutTimeNormal, timeOutTimeMod
    ameyBotConfigFile = open("AmeyBotConfig.json", "r")
    ameyBotConfig = json.load(ameyBotConfigFile)
    emojiLimit = ameyBotConfig["AmeyBotConfig"]["emojiLimit"]
    timeOutTimeNormal = ameyBotConfig["AmeyBotConfig"]["timeOutTimeNormal"]
    timeOutTimeMod = ameyBotConfig["AmeyBotConfig"]["timeOutTimeMod"]
    return int(emojiLimit)
def emojiCheck(timeInMin, chatMod, insert_comment, Author, chatMessage):
        try:
            chatMessage = emoji.emojize(chatMessage)
            counter = emoji.emoji_count(chatMessage)
            if counter <= (configValidate()-1):
                chatMessage = emoji.demojize(chatMessage)
                try:
                    emojiMain = recompile(emojiPattern).search(chatMessage).replace("_", " ")
                    chatMessage = resub(pattern=emojiPattern, repl=translator.translate(text=emojiMain, dest="hi"), string=chatMessage)
                except Exception as e:
                    printError("Some Error In Emoji", e)
            elif counter > configValidate():
                chatMessage = emoji.emojize(chatMessage)
                chatMessage = emoji.replace_emoji(chatMessage, '')
                try:
                    if Author.isChatOwner == False:
                        if Author.isChatModerator == True:
                            chatMod(channelIdBan=Author.channelId, timeoutSec=int(timeOutTimeMod))
                            modremovetext = f"{Author.name} You Are Moderator! Please Avoid Spamming Emojis. [Timeout -> {timeInMin(int(timeOutTimeMod))} Minutes]"
                            insert_comment(messagetext=modremovetext)
                        else:
                            chatMod(channelIdBan=Author.channelId, timeoutSec=int(timeOutTimeNormal))
                            timeouttextnor = f"{Author.name} Please Avoid Spamming Emojis. [Timeout -> {timeInMin(int(timeOutTimeNormal))} Minutes]"
                            insert_comment(messagetext=timeouttextnor)
                    else: 
                        pass
                except:
                    printError("Error Giving Timeout!")
            else:
                pass
            return chatMessage
        except:
            printError("Error In Emoji")