# Some Important Python Modules For Runing This Bot.
from gtts import gTTS
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import pytchat
from threading import Thread
from colorama import Fore
import logging as botLog
from pyfiglet import figlet_format
from MeowSounds import funnySounds
from MeowBotSettings import configRun
from updater.MeowChangelog import version
from MeowEmoji import emojiCheck
from MeowAutoReplyChatBot import mainChatBot
import MeowSounds
from MeowSponsors import sponsorFileCheck
import webbrowser
from urllib.request import urlopen
from re import IGNORECASE, search as research
from time import sleep
import pyjokes
import requests, json
import wikipedia
import random
from playsound import playsound
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
#Main Program Starts From Here
botLog.basicConfig(filename="log/MeowBot.log", level=botLog.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
try:
    def printNor(text):
        botLog.info(text)
        print(Fore.BLUE, text, Fore.RESET)
    def printGood(text):
        botLog.info(text)
        print(Fore.GREEN, text, Fore.RESET)
    def printError(text):
        botLog.error(text)
        print(Fore.RED, text, Fore.RESET)
    def authorTimer():
        global countTimnerThread
        if sayDelay != 0:
            authorChannelId = c.author.channelId
            def countTimer():
                countDuration=int(sayDelay)
                try:
                    while countDuration:
                        mins, secs = divmod(countDuration, 60)
                        timer = '{:02d}:{:02d}'.format(mins, secs)
                        sleep(1)
                        countDuration -= 1
                    timedAuthors.remove(authorChannelId)
                except Exception as e:
                    printError(e)
            if c.author.channelId not in timedAuthors:
                timedAuthors.append(c.author.channelId)
                countTimnerThread = Thread(target=countTimer)
                countTimnerThread.start()
                return True
            else:
                insert_comment(messagetext=f"{c.author.name} Say Command Is On Cooldown Please Wait For Some Time.")
                return False
        else:
            return True
    def MeowMainJsonFetch():
        global welcomeFont, BOT_SOUND, API_SERVICE_NAME, API_VERSION, API_SCOPES, API_KEYS, CLIENT_FILES, MeowBotEmojiMain, MeowBotEmojiReplace
        API_CONFIG_FILE = urlopen("https://gitlab.com/OpenSourceBlackCat/meowbotassets/-/raw/main/config/internalMeowBotSetting.json")
        API_CONFIG = json.load(API_CONFIG_FILE)
        # BOT STYLE
        welcomeFont = API_CONFIG["MeowBotStyle"]["welcomeFont"]
        # BOT SOUND
        BOT_SOUND = API_CONFIG["MeowSounds"]["botMainSound"]
        # Meow EMOJI
        meowBotEmojiMain = API_CONFIG["MeowEmoji"]["emojiMain"]
        meowBotEmojiReplace = API_CONFIG["MeowEmoji"]["emojiReplace"]
        # API SERVICE
        API_SERVICE_NAME = API_CONFIG["MEOWBOTAPI"]["API_SERVICE_NAME"]
        API_VERSION = API_CONFIG["MEOWBOTAPI"]["API_VERSION"]
        API_SCOPES = API_CONFIG["MEOWBOTAPI"]["API_SCOPES"]
        # API KEYS
        API_KEYS = API_CONFIG["MEOWBOTAPI"]["botApiKeys"]
        # CLIENT FILES
        CLIENT_FILES = API_CONFIG["MEOWBOTAPI"]["botClientJsonFiles"]
        return None
        
    # def botAuthenticator():
    #     global authenticator
    #     authenticator = "https://github.com/OpenSourceBlackCat/MeowBotAssets/raw/main/JSON/authBot.json"
    #     def authBot():
    #         key = open("key.txt", "r")
    #         keyText = key.readline()
    #         keyFile = urlopen(authenticator)
    #         keyData = json.loads(keyFile.read())
    #         try:
    #             if keyText in keyData["Keys"]:
    #                 printGood("Verification Successfull")
    #                 configValidate()
    #             else:
    #                 printError("Verification Failed!")
    #                 printError("Invalid Key!")
    #                 addKey()
    #         except:
    #             printError("Verification Failed!")
    #             printError("Invalid Key!")
    #             addKey()
    #     def addKey():
    #         keyInp = str(input(Fore.BLUE+"Enter Your KEY Here : "+Fore.RESET))
    #         key = open("key.txt", "w")
    #         key.write(keyInp)
    #         key.close()
    #         authBot()
    #     if exists("key.txt"):
    #         authBot()
    #     else:
    #         addKey()
    def timeInMin(time):
        timeMin = time / 60
        if timeMin == float(f"{int(timeMin)}.0"):
            return int(timeMin)
        else:
            return float(timeMin)
    def authChat():
        global livechatid, livechatrequest, errorInApi
        try:
            # Get credentials and create an API client
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, API_SCOPES)
            credentials = flow.run_local_server()
            os.remove(jsonFileName)
            global youtubeMain
            global youtubeBan
            youtubeMain = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
            youtubeBan = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY, credentials=credentials)
                
            livechatrequest = youtubeMain.liveBroadcasts().list(
                part="snippet,contentDetails,status",
                id=vidlink
            )
            livechatid = livechatrequest.execute()
            print("\n")
            print(livechatid)
            livechatid = livechatid["items"][0]["liveStreamingDetails"]["activeLiveChatId"]
            botNameUpper = botName.upper()
            insert_comment(messagetext=f"{botNameUpper} BOT IS RUNNING SUCCESSFULLY.")
            chatrun()
        except Exception as e:
            printError(e)
            os.remove(jsonFileName)
            apiInp()    
    def insert_comment(messagetext):
        try:
            youtubeMain.liveChatMessages().insert(
                part="snippet",
                body=dict(
                    snippet=dict(
                        liveChatId=livechatid,
                        type="textMessageEvent",
                        textMessageDetails=dict(
                            messageText=messagetext
                        )
                    )
                )
            ).execute()
        except Exception as e:
            printError(e)
            

    def chatMod(channelIdBan, timeoutSec): 
        try:
            if c.author.channelId != botUrl:
                youtubeBan.liveChatBans().insert(
                part="snippet",
                body={
                "snippet": {
                    "liveChatId": livechatid,
                    "type": "temporary",
                    "banDurationSeconds": timeoutSec,
                    "bannedUserDetails": {
                    "channelId": channelIdBan
                        }
                    }
                }
                ).execute()
        except:
            printError("Some Error In TimeOut!")
            
    def subCount():
        channelSubId = c.author.channelId
        try:
            mySubs = youtubeMain.channels().list(
                part="statistics",
                id=channelSubId
            )
            response = mySubs.execute()
            response1 = json.dumps(response)
            response2 = response1.split(',')
            response3 = response2[8]
            response4 = response3.replace('"subscriberCount": "', '')
            mySubCount = response4.replace('"', '')
            insert_comment(messagetext=f"{c.author.name} Has {mySubCount} Subscribers.")
        except:
            printError("Some Error In MySubs!")

    def wordCountCheck():
        try:
            meowreplace = c.message.split(" ")
            for i in range(0, len(meowreplace)):
                wordcount = 1
                for j in range(i + 1, len(meowreplace)):
                    if (meowreplace[i] == (meowreplace[j])):
                        if meowreplace[j] not in meowBotEmojiMain and meowreplace[j] not in meowBotEmojiReplace:
                            wordcount = wordcount + 1
                            meowreplace[j] = "0"
                        else:
                            pass
                if wordcount > int(wordLimit):
                    if c.author.isChatOwner == False:
                        if c.author.isChatModerator == True:
                            chatMod(channelIdBan=c.author.channelId, timeoutSec=int(timeOutTimeMod))
                            modremovetext = f"{c.author.name} You Are Moderator! Please Avoid Spamming Repeated Words. [Timeout -> {timeInMin(int(timeOutTimeMod))} Minutes]"
                            insert_comment(messagetext=modremovetext)
                            return None
                        else:
                            chatMod(channelIdBan=c.author.channelId, timeoutSec=int(timeOutTimeNormal))
                            timeouttextnor = f"{c.author.name} Please Avoid Spamming Repeated Words. [Timeout -> {timeInMin(int(timeOutTimeNormal))} Minutes]"
                            insert_comment(messagetext=timeouttextnor) 
                            return None   
                    else: 
                        pass          
        except:
            printError("Error In Word Count")
    
    def wordSpamCheck():
        try:
            def addChat():
                if c.author.channelId != botUrl and c.author.isChatOwner == False:
                    liveChats[c.author.channelId].append(c.message)
                    if liveChats[c.author.channelId].count(c.message) > int(wordLimit):
                        if c.author.isChatModerator == True:
                            chatMod(channelIdBan=c.author.channelId, timeoutSec=int(timeOutTimeMod))
                            liveChats.pop(c.author.channelId)
                            modremovetext = f"{c.author.name} You Are Moderator! Please Avoid Spamming Repeated Words. [Timeout -> {timeInMin(int(timeOutTimeMod))} Minutes]"
                            insert_comment(messagetext=modremovetext)
                            return None
                        else:
                            liveChats.pop(c.author.channelId)
                            chatMod(channelIdBan=c.author.channelId, timeoutSec=int(timeOutTimeNormal))
                            timeouttextnor = f"{c.author.name} Please Avoid Spamming Repeated Words. [Timeout -> {timeInMin(int(timeOutTimeNormal))} Minutes]"
                            insert_comment(messagetext=timeouttextnor) 
                            return None
                    else:
                        pass
                else: 
                    pass
            if c.author.channelId not in liveChats:
                liveChats.update({c.author.channelId: []})
                addChat()
            else:
                addChat()
        except Exception as e:
            printError(e)

    def mainBot():
        if "!" in c.message:
            botLog.info(f"{c.author.name} - {c.message}")
        if c.author.isChatOwner == True:
            printError(text=f"{c.datetime} - {c.author.name} - {c.message}")
        elif c.author.isChatModerator == True:
            printNor(text=f"{c.datetime} - {c.author.name} - {c.message}")
        elif c.author.isChatSponsor == True:
            printGood(text=f"{c.datetime} - {c.author.name} - {c.message}")
        else:
            print(f"{c.datetime} - {c.author.name} - {c.message}")
        nonSponsor = f"{c.author.name} This Is Feature Is Only For Channel Sponsors! You Can Join The Channel To Use This Feature."
        nonMod = f"{c.author.name} This Is Feature Is Only For Channel Moderators! You Can Join The Channel To Use This Feature."
        if "!say" in c.message or "-say" in c.message:
            def sayBot():
                c.message = c.message.replace('!say', '')
                c.message = c.message.replace('-say', '')
                authorCheck = authorTimer()
                if authorCheck != False:
                    sponsorVoice(f"{c.author.name} Says {c.message}")
                else: 
                    pass
            if readingBot == "all":
                sayBot()
            elif readingBot == "sponsor":
                if c.author.isChatSponsor == True or c.author.isChatOwner == True:
                    sayBot()
                else:
                    insert_comment(messagetext=nonSponsor)
                    pass
            elif readingBot == "mod":
                if c.author.isChatModerator == True or c.author.isChatOwner == True:
                    sayBot()
                else:
                    insert_comment(messagetext=nonMod)
                    pass
            else:
                pass
        elif "!hello" in c.message or "-hello" in c.message:
            botHello = ["How Are You?", "Hope You Are Feeling Good", "How's Your Day Going Today?", "How Do You Do?", "Hope You Are Fine"]
            if welcomeMusic == "sponsor":
                if c.author.isChatSponsor == True or c.author.isChatOwner == True:
                    sponsorFileCheck(channelId=c.author.channelId)
                    welcomeUser = random.choice(botHello)
                    insert_comment(messagetext=f"{c.author.name} Welcome To The Stream, {welcomeUser}")
                    sponsorVoice(f"{c.author.name} Welcome To The Stream, {welcomeUser}")
                else:
                    pass
            elif welcomeMusic == "off":
                pass
            if welcomeBotUser == "all":
                if welcomeMusic != "sponsor" or c.author.isChatSponsor == False and c.author.isChatOwner == False:
                    welcomeUser = random.choice(botHello)
                    insert_comment(messagetext=f"{c.author.name} Welcome To The Stream, {welcomeUser}")
                    sponsorVoice(f"{c.author.name} Welcome To The Stream, {welcomeUser}")
            elif welcomeBotUser == "off": 
                pass
            else: 
                pass
        elif "!joke" in c.message:
            def jokeSend():
                c.message = c.message.replace("!joke", '')
                printNor(f"{c.author.name}")
                try:
                    botJokes()
                except:
                    printError("Error In Jokes!")
            if jokes == "all":
                jokeSend()
            elif jokes == "sponsor":
                if c.author.isChatSponsor == True or c.author.isChatOwner == True:
                    jokeSend()
                else:
                    insert_comment(messagetext=nonSponsor)
                    pass
            elif jokes == "mod":
                if c.author.isChatModerator == True or c.author.isChatOwner == True:
                    jokeSend()
                else:
                    insert_comment(messagetext=nonMod)
                    pass
            else: 
                pass
        elif f"!{botName}bot" in c.message:
            c.message = c.message.replace(f"!{botName}bot", "")
            if autoReplyChatBot == "all":
                mainChatBot(Author=c.author, chatMessage=c.message, insertComment=insert_comment)
            elif autoReplyChatBot == "sponsor":
                if c.author.isChatSponsor == True or c.author.isChatOwner == True:
                    mainChatBot(Author=c.author, chatMessage=c.message, insertComment=insert_comment)
                else: 
                    insert_comment(messagetext=nonSponsor)
            elif autoReplyChatBot == "mod":
                if c.author.isChatModerator == True or c.author.isChatOwner == True:
                    mainChatBot(Author=c.author, chatMessage=c.message, insertComment=insert_comment)
                else:
                    insert_comment(messagetext=nonMod)
            else:
                pass
        elif f"!{botName}" in c.message: 
            if funnyBotSounds == "all":
                c.message = c.message.replace(f"!{botName} ", "")
                funnySounds(sponsorVoice=sponsorVoice, authorName=c.author.name, chatMessage=c.message)
            elif funnyBotSounds == "sponsor":
                if c.author.isChatSponsor == True or c.author.isChatOwner == True:
                    c.message = c.message.replace(f"!{botName} ", "")
                    funnySounds(sponsorVoice=sponsorVoice, authorName=c.author.name, chatMessage=c.message)
                else:
                    insert_comment(messagetext=nonSponsor)
            elif funnyBotSounds == "mod":
                if c.author.isChatModerator == True or c.author.isChatOwner == True:
                    c.message = c.message.replace(f"!{botName} ", "")
                    funnySounds(sponsorVoice=sponsorVoice, authorName=c.author.name, chatMessage=c.message)
                else:
                    insert_comment(messagetext=nonMod)
            else:
                pass
        elif "!bye" in c.message: 
            sponsorBye = ["Have A Nice Day", "Hope You Enjoyed The Stream", "See Ya", "See You Tomorrow", "Catch you later"]
            if (c.author.isChatSponsor == True) or (c.author.isChatOwner == True):
                sponsorsBye = random.choice(sponsorBye)
                insert_comment(messagetext=f"{c.author.name}, {sponsorsBye}")
                MeowSounds.jsonFetch()
                playsound(MeowSounds.soundBye)
                sponsorVoice(f"{c.author.name}, {sponsorsBye}")
            else: 
                sponsorsBye = random.choice(sponsorBye)
                insert_comment(messagetext=f"{c.author.name}, {sponsorsBye}")
        elif '!so' in c.message:
            printNor(f"{c.author.name}")
            shoutOut() 
        elif '!mysubs' in c.message:
            printNor(f"{c.author.name}")
            subCount()
        elif '!weather' in c.message:
            c.message = c.message.replace("!weather", "")
            printNor(f"{c.author.name}")
            weather(c.message)
        elif "!ask" in c.message: 
            try: 
                meowwiki()
            except: 
                printError("Error In MeowWiki")
    def meowwiki():
        def meowwikilang():
            if '-en' in c.message:
                c.message = c.message.replace('-en', '')
                wikipedia.set_lang('en')
            elif '-mr' in c.message:
                c.message = c.message.replace('-mr', '')
                wikipedia.set_lang('mr')
            elif '-kn' in c.message:
                c.message = c.message.replace('-kn', '')
                wikipedia.set_lang('kn')
            else:
                wikipedia.set_lang('en')
        try:
            if '!askser' in c.message:
                meowwikilang()
                c.message = c.message.replace('!askser', '')
                meow = wikipedia.search(c.message, results=5)
                insert_comment(messagetext=f"{c.author.name} {meow}")
            elif '!asksum' in c.message:
                meowwikilang()
                c.message = c.message.replace('!asksum', '')
                meow = wikipedia.summary(c.message, sentences=1)
                insert_comment(messagetext=f"{c.author.name} {str(meow)}")
        except:
            printError('Some Error In Wikipedia')
            pass
    def shoutOut():
        if c.author.isChatSponsor == True or c.author.isChatOwner == True:
            insert_comment(messagetext=f"{c.author.name} Shout Out To You :)")
            sponsorVoice(f"{c.author.name} ShoutOut To You")
        else:
            insert_comment(messagetext=f"{c.author.name} Shout Out To You :)")
            
    def botJokes():
        avijoke = pyjokes.get_joke(language='en',category='all')
        insert_comment(messagetext=f"{c.author.name} {avijoke}")
                
    def weather(location):
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        URL = BASE_URL +"q=" + location + "&appid=" + '9834d7f1a59251031184ca2922593739'
        weatherSlang = ["Right Now In", "In", "Currently In", "Today In"]
        response = requests.get(URL)
        weatherTalkName = random.choice(weatherSlang)
        try:
            if response.status_code == 200:
                data = response.json()
                main = data['main']
                temperature = main['temp'] - 272.15
                report = data['weather']
                temp = f"{(int(temperature))}"
                report = f"{report[0]['description']}"
                global weatherFinal
                weatherFinal = f" {c.author.name} {weatherTalkName} {location}, It's {temp} Degrees Celcius With {report}"
                try:
                    insert_comment(messagetext=weatherFinal)
                except:
                    printError('Error In Weather Chat Send')
        except:
            printError('Some Error In Weather!')
            insert_comment(messagetext="f {c.author.name} Please Enter A Valid Location!")
            

    global sponsorVoice          
    def sponsorVoice(sponsorChat):
        sponsorVoice = gTTS(sponsorChat, lang='hi', tld='co.in', slow=False)
        sponsorVoice.save('sponsorVoice.mp3')
        os.system("tools/mpg123.exe --realtime sponsorVoice.mp3")

    def linkCheck():
        if ":" in c.message or "/" in c.message or "." in c.message:
            pass
        else:
            mainBot()
    def urltojson(jsonurl, jsonfilename):
        global jsonFileName
        jsonurlfile = urlopen(jsonurl)
        json_data = json.loads(jsonurlfile.read())
        jsonFileName = jsonfilename
        with open(jsonfilename, 'w') as jsonfile:
            json.dump(json_data, jsonfile)
            jsonfile.close()
        return jsonFileName
    #Main Chatbot
    def chatBot():
        global vidlink, apiInp
        vidlinkInp = str(input(f"{Fore.BLUE}\nEnter Your Youtube Stream Link: {Fore.RESET}"))
        vidpat = r"https://[wm]+\.youtube\.com/live/([A-Z 0-9]*)|watch\?v=([A-Z 0-9]*)"
        vidlink = research(vidpat, vidlinkInp, IGNORECASE).group(1)
        if vidlink != None:
            def apiInp():
                try:
                    def checkapiversion():
                        global CLIENT_SECRET_FILE, API_KEY
                        inputApiVersion = str(input(Fore.BLUE+"Enter The Api Version (1 To 4, Default 1): "+Fore.RESET))
                        if inputApiVersion == "":
                            inputApiVersion = "1"
                        inputApiVersion = int(inputApiVersion)
                        if inputApiVersion <= len(API_KEYS): 
                            CLIENT_FILES_MAIN = list(CLIENT_FILES.values())
                            API_KEYS_MAIN = list(API_KEYS.values())
                            CLIENT_SECRET_FILE = urltojson(CLIENT_FILES_MAIN[inputApiVersion-1], f"CLIENTJSON{inputApiVersion}.json")
                            API_KEY = API_KEYS_MAIN[inputApiVersion-1]
                            authChat()
                        else:
                            printError("Invalid API! Please Try Again.")
                            checkapiversion()
                except:
                    printError("Wrong")
                checkapiversion()
            apiInp()
        else:
            printError("Something Went Wrong Please Try Again.")
            chatBot()
    def chatrun():
        os.system("cls")
        printGood("Fetching Your YouTube Stream...")
        sleep(1)
        printGood("Fetching Your Live Chats...")
        sleep(2)
        os.system("cls")
        livechat = pytchat.create(video_id=vidlink)
        try:
            playsound(BOT_SOUND, False)
        except:
            printError("Error Playing Sound")
        while livechat.is_alive():
            try:
                global c
                for c in livechat.get().sync_items():
                    c.message = c.message.lower()
                    wordCountCheck()
                    wordSpamCheck()
                    c.message = emojiCheck(timeInMin=timeInMin, chatMod=chatMod, insert_comment=insert_comment, Author=c.author, chatMessage=c.message)
                    linkCheck()
            except Exception as e:
                printError(e)
    def configValidate():
        global botName, botUrl, autoReplyChatBot, wordLimit, sayDelay, liveChats, timedAuthors, readingBot, welcomeBotUser, welcomeMusic, funnyBotSounds, jokes, timeOutTimeNormal, timeOutTimeMod
        configRun()
        meowBotConfigFile = open("config/MeowBotConfig.json", "r")
        meowBotConfig = json.load(meowBotConfigFile)
        botName = meowBotConfig["MeowBotConfig"]["botName"]
        botUrl = meowBotConfig["MeowBotConfig"]["botUrl"]
        readingBot = meowBotConfig["MeowBotConfig"]["readingBot"]
        autoReplyChatBot = meowBotConfig["MeowBotConfig"]["autoReplyChatBot"]
        welcomeBotUser = meowBotConfig["MeowBotConfig"]["welcomeUser"]
        welcomeMusic = meowBotConfig["MeowBotConfig"]["welcomeMusic"]
        funnyBotSounds = meowBotConfig["MeowBotConfig"]["funnySounds"]
        jokes = meowBotConfig["MeowBotConfig"]["jokes"]
        wordLimit = meowBotConfig["MeowBotConfig"]["wordLimit"]
        sayDelay = meowBotConfig["MeowBotConfig"]["sayDelay"]
        liveChats = {}
        timedAuthors = []
        timeOutTimeNormal = meowBotConfig["MeowBotConfig"]["timeOutTimeNormal"]
        timeOutTimeMod = meowBotConfig["MeowBotConfig"]["timeOutTimeMod"]
        chatBot()
    def mainGui():
        MeowMainJsonFetch()
        printNor(figlet_format("MEOW BOT", font=welcomeFont))
        printNor(version)
        configValidate()                                       
except Exception as e:
    botLog.critical(e)
