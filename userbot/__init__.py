# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot initialization. """

import os

from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb

from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from dotenv import load_dotenv
from requests import get
from telethon import TelegramClient
from telethon.sessions import StringSession

load_dotenv("config.env")

# Bot Logs setup:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 6:
    LOGS.info("You MUST have a python version of at least 3.6."
              "Multiple features depend on this. Bot quitting.")
    quit(1)

# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

if CONFIG_CHECK:
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    quit(1)

# Telegram App KEY and HASH
API_KEY = os.environ.get("TELEGRAM_API_KEY", None)
API_HASH = os.environ.get("TELEGRAM_API_HASH", None)

# Userbot Session String
STRING_SESSION = os.environ.get("TELEGRAM_STRING_SESSION", None)

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", None))

# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG", "False"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_PROTECTOR", "False"))

# Heroku Credentials for updater.
HEROKU_APPNAME = os.environ.get("HEROKU_APPNAME", None)
HEROKU_APIKEY = os.environ.get("HEROKU_APIKEY", None)


UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/rekcah-pavi/javes")

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# Chrome Driver and Headless Google Chrome Binaries
CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Youtube API key
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

# Default .alive name
ALIVE_NAME = os.environ.get("YOUR_SHORT_NAME", None)

ZALG_LIST = [[
    "?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ?",
    " ",
],
             [
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
             ],
             [
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
                 " ?",
             ]]

EMOJIS = [
    "??",
    "??",
    "??",
    "?",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "????",
    "??",
    "??",
    "??",
    "??",
]

INSULT_STRINGS = [
    "Owww ... Such a stupid idiot.",
    "Don't drink and type.",
    "I think you should go home or better a mental asylum.",
    "Command not found. Just like your brain.",
    "Do you realize you are making a fool of yourself? Apparently not.",
    "You can type better than that.",
    "Bot rule 544 section 9 prevents me from replying to stupid humans like you.",
    "Sorry, we do not sell brains.",
    "Believe me you are not normal.",
    "I bet your brain feels as good as new, seeing that you never use it.",
    "If I wanted to kill myself I'd climb your ego and jump to your IQ.",
    "Zombies eat brains... you're safe.",
    "You didn't evolve from apes, they evolved from you.",
    "Come back and talk to me when your I.Q. exceeds your age.",
    "I'm not saying you're stupid, I'm just saying you've got bad luck when it comes to thinking.",
    "What language are you speaking? Cause it sounds like bullshit.",
    "Stupidity is not a crime so you are free to go.",
    "You are proof that evolution CAN go in reverse.",
    "I would ask you how old you are but I know you can't count that high.",
    "As an outsider, what do you think of the human race?",
    "Brains aren't everything. In your case they're nothing.",
    "Ordinarily people live and learn. You just live.",
    "I don't know what makes you so stupid, but it really works.",
    "Keep talking, someday you'll say something intelligent! (I doubt it though)",
    "Shock me, say something intelligent.",
    "Your IQ's lower than your shoe size.",
    "Alas! Your neurotransmitters are no more working.",
    "Are you crazy you fool.",
    "Everyone has the right to be stupid but you are abusing the privilege.",
    "I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.",
    "You should try tasting cyanide.",
    "Your enzymes are meant to digest rat poison.",
    "You should try sleeping forever.",
    "Pick up a gun and shoot yourself.",
    "You could make a world record by jumping from a plane without parachute.",
    "Stop talking BS and jump in front of a running bullet train.",
    "Try bathing with Hydrochloric Acid instead of water.",
    "Try this: if you hold your breath underwater for an hour, you can then hold it forever.",
    "Go Green! Stop inhaling Oxygen.",
    "God was searching for you. You should leave to meet him.",
    "give your 100%. Now, go donate blood.",
    "Try jumping from a hundred story building but you can do it only once.",
    "You should donate your brain seeing that you never used it.",
    "Volunteer for target in an firing range.",
    "Head shots are fun. Get yourself one.",
    "You should try swimming with great white sharks.",
    "You should paint yourself red and run in a bull marathon.",
    "You can stay underwater for the rest of your life without coming back up.",
    "How about you stop breathing for like 1 day? That'll be great.",
    "Try provoking a tiger while you both are in a cage.",
    "Have you tried shooting yourself as high as 100m using a canon.",
    "You should try holding TNT in your mouth and igniting it.",
    "Try playing catch and throw with RDX its fun.",
    "I heard phogine is poisonous but i guess you wont mind inhaling it for fun.",
    "Launch yourself into outer space while forgetting oxygen on Earth.",
    "You should try playing snake and ladders, with real snakes and no ladders.",
    "Dance naked on a couple of HT wires.",
    "Active Volcano is the best swimming pool for you.",
    "You should try hot bath in a volcano.",
    "Try to spend one day in a coffin and it will be yours forever.",
    "Hit Uranium with a slow moving neutron in your presence. It will be a worthwhile experience.",
    "You can be the first person to step on sun. Have a try.",
]

UWUS = [
    "(?`?´?)",
    ";;w;;",
    "owo",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)??",
    "(ô_ô)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(?_?)",
    "*(^O^)*",
    "((+_+))",
]

IWIS = [
    "?(´??)?",
    "?(´??)?",
    "?(´??)?",
    "?(???)?",
    "?(???)?",
    "?(?_?)?",
    "?(´?`)?",
    "?(´??)?",
    "?(???)?",
    "?(???)?",
    "?('?')?",
    "?(??`;)?",
    "?(´??;)?",
    "?( -?-)?",
    "??´?????",
    "?(???o)?",
    "?(~?~ )?",
    "?(~?~;)?",
    "?(-??;)?",
    r"¯\_(?)_/¯",
    r"¯\_(?_??)_/¯",
    r"¯\_? ? ? ? ?_/¯",
    "?( ??  ?? ?? ) ?",
]

FACEREACTS = [
    "???",
    "?(-_- )?",
    "(?????)",
    "(´???)",
    "( ? ?? ?)",
    "(° ???°)???",
    "(??? ??)",
    "(??)?",
    "?(??",
    "(??¯?)?",
    "(???)",
    "( ?? ?? ??)",
    "( ? ?? ?)",
    "(??-´)????.*???",
    "(????????)?",
    "(._.)",
    "{??_??}",
    "(???)",
    "?_?",
    "?.?",
    "????? ",
    "(??_?)",
    "?(??)????",
    "(??????)??",
    "????? ? ? ",
    "(????)?",
    "[¬º-°]¬",
    "(?? ?)",
    "(?????)? ??",
    "?(´?`)????",
    "(?'?-'?)?",
    "?(?????)",
    "? ????? ?",
    "?? ?(??? )?",
    "???????",
    "( ??? )",
    "?_?",
    "(??? ? ???) ",
    "( ? ³?)? ",
    "?(????)",
    "???",
    "?_?",
    "???( ??? )???",
    "?( ? ??)?      ?(?? ?)?",
    "( ??? )?",
    "?(?_?)?",
    "?(???)?",
    "?_?",
    "(???????)?",
    "(?? ??)??( \\o°o)\\",
    "??(´??)??",
    "? ?? ? ???",
    "??( ?????)??",
    "(?? ³?)?",
    "(?.?)7",
    "?( ? )?",
    "t(-_-t)",
    "(???)",
    "?? ??? ??",
    "??? ??? ??? ???",
    "?????",
    "(?_?)",
    "¿?_??",
    "?_?",
    "(´?_?`)",
    "?(ò_ó?)?",
    "???",
    "(?°?°??? ???",
    r"¯\_(???)_/¯",
    "?????",
    "°??°",
    "?(????)?",
    "?(???)?",
    "V???V",
    "q(???)p",
    "?_?",
    "?^???^?",
    "???",
    "? ^_^?o??o?^_^ ?",
    "???",
    "?(´?`)/",
    "???#",
    "( ?° ?? ?°)",
    "???? ?( ?-??)",
    "?(´??)?",
    "?(???)?",
    "?=?=?=?(;*´?`)?",
    "(? ???)",
    "??????(?????)",
    "??? ??(`?´)??? ???",
    r"¯\_(?)_/¯",
    "?????",
    "(`???´)",
    "?????",
    "?(??´?)",
    "???????",
    "??????",
    r"¯\(°_o)/¯",
    "(?????)",
]

RUNS_STR = [
    "Runs to Thanos..",
    "Runs far, far away from earth..",
    "Running faster than Bolt coz i'mma userbot !!",
    "Runs to Marie..",
    "This Group is too cancerous to deal with.",
    "Cya bois",
    "Kys",
    "I go away",
    "I am just walking off, coz me is too fat.",
    "I Fugged off!",
    "Will run for chocolate.",
    "I run because I really like food.",
    "Running...\nbecause dieting is not an option.",
    "Wicked fast runnah",
    "If you wanna catch me, you got to be fast...\nIf you wanna stay with me, you got to be good...\nBut if you wanna pass me...\nYou've got to be kidding.",
    "Anyone can run a hundred meters, it's the next forty-two thousand and two hundred that count.",
    "Why are all these people following me?",
    "Are the kids still chasing me?",
    "Running a marathon...there's an app for that.",
]

CHASE_STR = [
    "Where do you think you're going?",
    "Huh? what? did they get away?",
    "ZZzzZZzz... Huh? what? oh, just them again, nevermind.",
    "Get back here!",
    "Not so fast...",
    "Look out for the wall!",
    "Don't leave me alone with them!!",
    "You run, you die.",
    "Jokes on you, I'm everywhere",
    "You're gonna regret that...",
    "You could also try /kickme, I hear that's fun.",
    "Go bother someone else, no-one here cares.",
    "You can run, but you can't hide.",
    "Is that all you've got?",
    "I'm behind you...",
    "You've got company!",
    "We can do this the easy way, or the hard way.",
    "You just don't get it, do you?",
    "Yeah, you better run!",
    "Please, remind me how much I care?",
    "I'd run faster if I were you.",
    "That's definitely the droid we're looking for.",
    "May the odds be ever in your favour.",
    "Famous last words.",
    "And they disappeared forever, never to be seen again.",
    "\"Oh, look at me! I'm so cool, I can run from a bot!\" - this person",
    "Yeah yeah, just tap /kickme already.",
    "Here, take this ring and head to Mordor while you're at it.",
    "Legend has it, they're still running...",
    "Unlike Harry Potter, your parents can't protect you from me.",
    "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might "
    "be the next Vader.",
    "Multiple calculations later, I have decided my interest in your shenanigans is exactly 0.",
    "Legend has it, they're still running.",
    "Keep it up, not sure we want you here anyway.",
    "You're a wiza- Oh. Wait. You're not Harry, keep moving.",
    "NO RUNNING IN THE HALLWAYS!",
    "Hasta la vista, baby.",
    "Who let the dogs out?",
    "It's funny, because no one cares.",
    "Ah, what a waste. I liked that one.",
    "Frankly, my dear, I don't give a damn.",
    "My milkshake brings all the boys to yard... So run faster!",
    "You can't HANDLE the truth!",
    "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",
    "Hey, look at them! They're running from the inevitable banhammer... Cute.",
    "Han shot first. So will I.",
    "What are you running after, a white rabbit?",
    "As The Doctor would say... RUN!",
]

HELLOSTR = [
    "Hi !",
    "?Ello, gov'nor!",
    "What?s crackin??",
    "?Sup, homeslice?",
    "Howdy, howdy ,howdy!",
    "Hello, who's there, I'm talking.",
    "You know who this is.",
    "Yo!",
    "Whaddup.",
    "Greetings and salutations!",
    "Hello, sunshine!",
    "Hey, howdy, hi!",
    "What?s kickin?, little chicken?",
    "Peek-a-boo!",
    "Howdy-doody!",
    "Hey there, freshman!",
    "I come in peace!",
    "Ahoy, matey!",
    "Hiya!",
]

SHGS = [
    "?(´??)?",
    "?(´??)?",
    "?(´??)?",
    "?(???)?",
    "?(???)?",
    "?(?_?)?",
    "?(´?`)?",
    "?(´??)?",
    "?(???)?",
    "?(???)?",
    "?('?')?",
    "?(??`;)?",
    "?(´??;)?",
    "?( -?-)?",
    "??´?????",
    "?(???o)?",
    "?(~?~ )?",
    "?(~?~;)?",
    "?(-??;)?",
    r"¯\_(?)_/¯",
    r"¯\_(?_??)_/¯",
    r"¯\_? ? ? ? ?_/¯",
    "?( ??  ?? ?? ) ?",
]

CRI = [
    "???",
    "???",
    "(;?;)",
    "(ToT)",
    "(???)",
    "(???)",
    "?????",
    "(T?T)",
    "?????",
    "(???)",
    "(???)",
    "?????",
    "(´???",
    "(;?;)",
    "?>?<?",
    "(T?T)",
    "(???)",
    "?????",
    "(???)",
    "(?A?)",
    "(?_?)",
    "(T?T)",
    "(?????)",
    "(???)?",
    "(?_??)",
    "(???)",
    "(??_??)",
    "(???`?)",
    "??_??",
    "? ?? ? ???",
]

SLAP_TEMPLATES = [
    "{hits} {victim} with a {item}.",
    "{hits} {victim} in the face with a {item}.",
    "{hits} {victim} around a bit with a {item}.",
    "{throws} a {item} at {victim}.",
    "grabs a {item} and {throws} it at {victim}'s face.",
    "{hits} a {item} at {victim}.", "{throws} a few {item} at {victim}.",
    "grabs a {item} and {throws} it in {victim}'s face.",
    "launches a {item} in {victim}'s general direction.",
    "sits on {victim}'s face while slamming a {item} {where}.",
    "starts slapping {victim} silly with a {item}.",
    "pins {victim} down and repeatedly {hits} them with a {item}.",
    "grabs up a {item} and {hits} {victim} with it.",
    "starts slapping {victim} silly with a {item}.",
    "holds {victim} down and repeatedly {hits} them with a {item}.",
    "prods {victim} with a {item}.",
    "picks up a {item} and {hits} {victim} with it.",
    "ties {victim} to a chair and {throws} a {item} at them.",
    "{hits} {victim} {where} with a {item}.",
    "ties {victim} to a pole and whips them {where} with a {item}."
    "gave a friendly push to help {victim} learn to swim in lava.",
    "sent {victim} to /dev/null.", "sent {victim} down the memory hole.",
    "beheaded {victim}.", "threw {victim} off a building.",
    "replaced all of {victim}'s music with Nickelback.",
    "spammed {victim}'s email.", "made {victim} a knuckle sandwich.",
    "slapped {victim} with pure nothing.",
    "hit {victim} with a small, interstellar spaceship.",
    "quickscoped {victim}.", "put {victim} in check-mate.",
    "RSA-encrypted {victim} and deleted the private key.",
    "put {victim} in the friendzone.",
    "slaps {victim} with a DMCA takedown request!"
]

ITEMS = [
    "cast iron skillet",
    "large trout",
    "baseball bat",
    "cricket bat",
    "wooden cane",
    "nail",
    "printer",
    "shovel",
    "pair of trousers",
    "CRT monitor",
    "diamond sword",
    "baguette",
    "physics textbook",
    "toaster",
    "portrait of Richard Stallman",
    "television",
    "mau5head",
    "five ton truck",
    "roll of duct tape",
    "book",
    "laptop",
    "old television",
    "sack of rocks",
    "rainbow trout",
    "cobblestone block",
    "lava bucket",
    "rubber chicken",
    "spiked bat",
    "gold block",
    "fire extinguisher",
    "heavy rock",
    "chunk of dirt",
    "beehive",
    "piece of rotten meat",
    "bear",
    "ton of bricks",
]

THROW = [
    "throws",
    "flings",
    "chucks",
    "hurls",
]

HIT = [
    "hits",
    "whacks",
    "slaps",
    "smacks",
    "bashes",
]

WHERE = ["in the chest", "on the head", "on the butt", "on the crotch"]

GAMBAR_TITIT = """
????
??????
  ??????
    ??????
     ??????
       ??????
        ??????
         ??????
          ??????
          ??????
      ????????
 ????????????
 ??????  ??????
    ????       ????
"""


# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", ""))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(api_key=LASTFM_API,
                           api_secret=LASTFM_SECRET,
                           username=LASTFM_USERNAME,
                           password_hash=LASTFM_PASS)
else:
    lastfm = None

# Google Drive Module
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")

# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# 'bot' variable
if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING_SESSION),
                         API_KEY,
                         API_HASH,
                         connection_retries=None,
                         auto_reconnect=False,
                         lang_code='en')
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot",
                         API_KEY,
                         API_HASH,
                         connection_retries=None,
                         auto_reconnect=False,
                         lang_code='en')


async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the private error log storage to work."
        )
        quit(1)

    elif not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the userbot logging feature to work."
        )
        quit(1)

    elif not BOTLOG or not LOGSPAMMER:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if not entity.creator:
        if entity.default_banned_rights.send_messages:
            LOGS.info(
                "Your account doesn't have rights to send messages to BOTLOG_CHATID "
                "group. Check if you typed the Chat ID correctly.")
            quit(1)


with bot:
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file.")
        quit(1)

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
