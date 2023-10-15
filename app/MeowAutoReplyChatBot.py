from json import load
from urllib.request import urlopen
def jsonFetch():
    global meowBotChatInput, meowBotChatOutput
    internalMeowBotConfigFile = urlopen("https://gitlab.com/OpenSourceBlackCat/meowbotassets/-/raw/main/config/autoReplyChatBot.json")
    internalMeowBotConfig = load(internalMeowBotConfigFile)
    meowBotChatInput = internalMeowBotConfig["MeowChatBot"]["chatInput"]
    meowBotChatOutput = internalMeowBotConfig["MeowChatBot"]["chatOutput"]
def mainChatBot(Author, chatMessage, insertComment):
    jsonFetch()
    for i in range(len(meowBotChatInput)):
        if meowBotChatInput[i] in chatMessage:
            insertComment(messagetext=f"{Author.name} {meowBotChatOutput[i]}")
            return None
        else:
            pass
