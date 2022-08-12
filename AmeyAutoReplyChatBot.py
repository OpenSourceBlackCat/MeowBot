from json import load
from urllib.request import urlopen
def jsonFetch():
    global ameyBotChatInput, ameyBotChatOutput
    internalAmeyBotConfigFile = urlopen("https://github.com/Amey-Gurjar/AmeyBotAssets/raw/main/JSON/autoReplyChatBot.json")
    internalAmeyBotConfig = load(internalAmeyBotConfigFile)
    ameyBotChatInput = internalAmeyBotConfig["AmeyChatBot"]["chatInput"]
    ameyBotChatOutput = internalAmeyBotConfig["AmeyChatBot"]["chatOutput"]
def mainChatBot(Author, chatMessage, insertComment):
    jsonFetch()
    for i in range(len(ameyBotChatInput)):
        if ameyBotChatInput[i] in chatMessage:
            insertComment(messagetext=f"{Author.name} {ameyBotChatOutput[i]}")
            return None
        else:
            pass