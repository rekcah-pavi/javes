
""" Userbot start point """

from importlib import import_module
from sys import argv
from os import execle

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import LOGS, bot
from userbot.modules import ALL_MODULES


INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\nTip: Use Country Code along with number.' \
             '\nor check your phone number and try again !'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info("You are running Javes [v1.2]")

LOGS.info("Congratulations, javes is now running !!\
          \nTest it by typing !javes in any chat.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
