from json import load
from urllib.request import urlopen
def jsonFetch():
    global ameyBotChatInput, ameyBotChatOutput
    internalAmeyBotConfigFile = urlopen("https://ameybot.s3.ap-south-1.amazonaws.com/AmeyBotMain/JSON/autoReplyChatBot.json")
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