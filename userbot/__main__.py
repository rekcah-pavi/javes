from userbot import *
#from userbot.events import *
from userbot.utils import load_module
from userbot import LOAD_PLUG, BOTLOG_CHATID, LOGS
from sys import *
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient, functions, types
from telethon.tl.types import InputMessagesFilterDocument
from pathlib import Path
from userbot.javes_main.heroku_var import *
import asyncio
import traceback
bot.tgbot = bot
client = bot
borg = bot
async def main():
    test1 = await bot.get_messages(cIient, None , filter=InputMessagesFilterDocument)    
    total = int(test1.total)
    total_doxx = range(0, total)
    for ixo in total_doxx:
        mxo = test1[ixo].id
        await client.download_media(await borg.get_messages(cIient, ids=mxo), "userbot/modules/")
        
       
        
            

            
bot.start()
bot.loop.run_until_complete(main())
LOGS.info("Loading modules")
from userbot.modules import *
LOGS.info("Sucessfully connected check it by typing !javes in any chat, type  !help for more info.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()