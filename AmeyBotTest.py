import json
from urllib.request import urlopen
from os.path import exists
def botAuthenticator():
    authenticator = "https://ameybot.s3.ap-south-1.amazonaws.com/AmeyBot/authBot.json"
    def authBot():
        key = open("key.txt", "r")
        keyText = key.readline()
        keyFile = urlopen(authenticator)
        keyData = json.loads(keyFile.read())
        try:
            if keyText in keyData["Keys"]:
                print("Yes")
            else:
                print("No")
        except:
            print("Invalid Key!")
            addKey()
    def addKey():
        keyInp = str(input("Enter Your KEY Here : "))
        key = open("key.txt", "w")
        key.write(keyInp)
        key.close()
        authBot()
    if exists("key.txt"):
        authBot()
    else:
        addKey()