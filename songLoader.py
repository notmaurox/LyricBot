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
    
    recieved_exit = False
    
    DMs = api.direct_messages()
    
    print DMs
        
    