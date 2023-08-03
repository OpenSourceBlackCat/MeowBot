import json
import emoji
from colorama import Fore
from googletrans import Translator
from re import subn as resubn, findall as refindall
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
                    emojiMain = list(map(lambda x: x.replace("_", " "), refindall(emojiPattern, chatMessage)))
                    for x in emojiMain:
                        chatMessage = resubn(pattern=emojiPattern, repl=translator.translate(text=x, dest="hi").text, string=chatMessage, count=1)[0]
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