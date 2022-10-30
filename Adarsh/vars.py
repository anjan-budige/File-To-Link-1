# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = "15914139"
    API_HASH = "f5c54e1dd806604552e211b3841c1ad4"
    BOT_TOKEN = "5371686231:AAH-frIffQw2bAjW802b6Ilk7A6cXiuYqtA"
    API = "8b088f1bec72e5db45502b832a1116b99e11e876"
    SESSION_NAME = 'filetolinkbot'
    SLEEP_THRESHOLD = '60'
    WORKERS = '4'
    BIN_CHANNEL = "-1001767960284"
    PORT = 51691
    BIND_ADRESS = '13.126.125.81'
    PING_INTERVAL = "1200" # 20 minutes
    OWNER_ID =  "1121140181" 
    NO_PORT = False
    APP_NAME = None
    OWNER_USERNAME = "alpha"
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = "alpha"
    
    else:
        ON_HEROKU = False
    FQDN = BIND_ADRESS
    HAS_SSL= False
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = "mongodb+srv://enrich:enrich@cluster0.mhghl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    UPDATES_CHANNEL = None
    BANNED_CHANNELS = None
