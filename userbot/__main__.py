from userbot import * ;  from sys import * ; from telethon import TelegramClient, functions, types ; from telethon.tl.types import InputMessagesFilterDocument ; from pathlib import Path ; from userbot.javes_main.commands import * ; import asyncio, os, traceback ; javes = tgbot = bot.tgbot = borg = client

LOGS.info("Connecting...") ; o = o2 =o3 = None 
try:
   client.start() ; LOGS.info("client connected") ; o = "client"
except:
	LOGS.info("Telegram String Session Wrong or Expired Please Add new one ") ; quit(1)

if client2:
    try:
      client2.start() ; LOGS.info("client2 connected") ; o2 = "client2"
    except:
       LOGS.info("client2 Session string Wrong/Expired Please add new string session or delete var E2") ; quit(1)
  
if client3:
    try:
       client3.start() ; LOGS.info("client3 connected") ; o3 = "client3"
    except:
       LOGS.info("client3 Session string Wrong/Expired Please add new string  or delete var E3 ") ; quit(1)

javes.loop.run_until_complete(a()); from userbot.javes_main import custom_installer;  from userbot.modules import *; os.system("rm userbot/modules/*.py") ; LOGS.info(f"Sucessfully connected with {o}, {o2}, {o3} check it by typing !javes in any chat, type  !help for more info.")

if len(argv) not in (1, 3, 4):
    javes.disconnect()
else:
    javes.run_until_disconnected()
