import tweepy as tp
import time
import os
import random as rd
import json

configF = "configP.json"

with open(configF, 'r') as f:
    configInfo = json.load(f)

    # credentials to login to twitter api
    consumer_key = configInfo["consumer_key"]
    consumer_secret = configInfo["consumer_secret"]
    access_token = configInfo["access_token"]
    access_secret = configInfo["access_secret"]
    
    song_dir = configInfo["song_dir"]

    #log into twitter account api
    auth = tp.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tp.API(auth)

    #Picks song, lyric, and makes tweet text body.
    os.chdir(song_dir)
    numSongs = len(os.listdir('.'))
    songIndex = rd.randint(0,numSongs-1)
    songCounter = 0
    for songFile in os.listdir('.'):
        if songCounter == songIndex:
            print songFile
            with open(songFile,"r") as f:
                primaryArtist = f.readline().replace("\n","")
                album = f.readline().replace("\n","")
                song = f.readline().replace("\n","")
                lyricLines = int(f.readline().replace("\n",""))
                line = f.readline()
                tweetBody = ""
                lyricStartLine = rd.randint(0,lyricLines)
                currLyricLine = 0
                line = f.readline()
                while line:
                    if "[" not in line:
                        if currLyricLine == lyricStartLine:
                            tweetBody += line
                        elif len(tweetBody) != 0:
                            if len(tweetBody)+len(line) < 280:
                                tweetBody += line
                            else:
                                break
                        currLyricLine += 1
                    line = f.readline()
            print tweetBody
        songCounter+=1
        
    api.update_status(tweetBody)