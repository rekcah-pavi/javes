from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.tl.types import User
from datetime import datetime
from speedtest import Speedtest
from telethon import functions
from os import remove, execle, path, makedirs, getenv, environ
from shutil import rmtree
import asyncio
import json
from random import choice, randint
from asyncio import sleep
from telethon.events import StopPropagation
from userbot import (AFKREASON, COUNT_MSG, CMD_HELP, ISAFK, BOTLOG,BOTLOG_CHATID, USERS, PM_AUTO_BAN)
from userbot.events import register
from asyncio import sleep
from telethon.errors import rpcbaseerrors
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import register
import os
import subprocess
import time
import math
from pySmartDL import SmartDL
import asyncio
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo
from userbot import LOGS, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
import sys
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from userbot import CMD_HELP, bot, HEROKU_APIKEY, HEROKU_APPNAME, UPSTREAM_REPO_URL
from userbot.events import register
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register
from sqlalchemy.exc import IntegrityError
from userbot import (COUNT_PM, CMD_HELP, BOTLOG, BOTLOG_CHATID, PM_AUTO_BAN,LASTMSG, LOGS)
from userbot.events import register
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ========================= CONSTANTS ============================
UNAPPROVED_MSG = (
    "`Javes: Hello! Sir\n`"
   f"I can't allow you to {DEFAULTUSER}'s PM without his permissions please be patient,Thankyou")
    

@register(incoming=True, disable_edited=True, disable_errors=True)
async def permitpm(event):
    """ Prohibits people from PMing you without approval. \
        Will block retarded nibbas automatically. """
    if PM_AUTO_BAN:
        self_user = await event.client.get_me()
        if event.is_private and event.chat_id != 777000 and event.chat_id != self_user.id and not (
                await event.get_sender()).bot:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
                from userbot.modules.sql_helper.globals import gvarstatus
            except AttributeError:
                return
            apprv = is_approved(event.chat_id)
            notifsoff = gvarstatus("NOTIF_OFF")

            # This part basically is a sanity check
            # If the message that sent before is Unapproved Message
            # then stop sending it again to prevent FloodHit
            if not apprv and event.text != UNAPPROVED_MSG:
                if event.chat_id in LASTMSG:
                    prevmsg = LASTMSG[event.chat_id]
                    # If the message doesn't same as previous one
                    # Send the Unapproved Message again
                    if event.text != prevmsg:
                        async for message in event.client.iter_messages(
                                event.chat_id,
                                from_user='me',
                                search=UNAPPROVED_MSG):
                            await message.delete()
                        await event.reply(UNAPPROVED_MSG)
                    LASTMSG.update({event.chat_id: event.text})
                else:
                    await event.reply(UNAPPROVED_MSG)
                    LASTMSG.update({event.chat_id: event.text})

                if notifsoff:
                    await event.client.send_read_acknowledge(event.chat_id)
                if event.chat_id not in COUNT_PM:
                    COUNT_PM.update({event.chat_id: 1})
                else:
                    COUNT_PM[event.chat_id] = COUNT_PM[event.chat_id] + 1

                if COUNT_PM[event.chat_id] > 4:
                    await event.respond(
                             f"`javes`: I am not going to allow you to spam {DEFAULTUSER}'s PM, Good bye!")
                

                    try:
                        del COUNT_PM[event.chat_id]
                        del LASTMSG[event.chat_id]
                    except KeyError:
                        if BOTLOG:
                            await event.client.send_message(
                                BOTLOG_CHATID,
                                "Count PM is seemingly going retard, plis restart bot!",
                            )
                        LOGS.info("CountPM wen't rarted boi")
                        return

                    await event.client(BlockRequest(event.chat_id))
                    await event.client(ReportSpamRequest(peer=event.chat_id))

                    if BOTLOG:
                        name = await event.client.get_entity(event.chat_id)
                        name0 = str(name.first_name)
                        await event.client.send_message(
                            BOTLOG_CHATID,
                            "[" + name0 + "](tg://user?id=" +
                            str(event.chat_id) + ")" +
                            " i blocked him from your pm due to spam",
                        )


@register(disable_edited=True, outgoing=True, disable_errors=True)
async def auto_accept(event):
    """ Will approve automatically if you texted them first. """
    if not PM_AUTO_BAN:
        return
    self_user = await event.client.get_me()
    if event.is_private and event.chat_id != 777000 and event.chat_id != self_user.id and not (
            await event.get_sender()).bot:
        try:
            from userbot.modules.sql_helper.pm_permit_sql import is_approved
            from userbot.modules.sql_helper.pm_permit_sql import approve
        except AttributeError:
            return

        chat = await event.get_chat()
        if isinstance(chat, User):
            if is_approved(event.chat_id) or chat.bot:
                return
            async for message in event.client.iter_messages(event.chat_id,
                                                            reverse=True,
                                                            limit=1):
                if message.message is not UNAPPROVED_MSG and message.from_id == self_user.id:
                    try:
                        approve(event.chat_id)
                    except IntegrityError:
                        return

                if is_approved(event.chat_id) and BOTLOG:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "#AUTO-APPROVED\n" + "User: " +
                        f"[{chat.first_name}](tg://user?id={chat.id})",
                    )


@register(outgoing=True, pattern="^\!notifoff$")
async def notifoff(noff_event):
    """ For .notifoff command, stop getting notifications from unapproved PMs. """
    try:
        from userbot.modules.sql_helper.globals import addgvar
    except AttributeError:
        await noff_event.edit("`Running on Non-SQL mode!`")
        return
    addgvar("NOTIF_OFF", True)
    await noff_event.edit("`Notifications from unapproved PM's are silenced!`")


@register(outgoing=True, pattern="^\!notifon$")
async def notifon(non_event):
    """ For .notifoff command, get notifications from unapproved PMs. """
    try:
        from userbot.modules.sql_helper.globals import delgvar
    except AttributeError:
        await non_event.edit("`Running on Non-SQL mode!`")
        return
    delgvar("NOTIF_OFF")
    await non_event.edit("`Notifications from unapproved PM's unmuted!`")


@register(outgoing=True, pattern="^\!allow$")
async def approvepm(apprvpm):
    """ For .approve command, give someone the permissions to PM you. """
    try:
        from userbot.modules.sql_helper.pm_permit_sql import approve
    except AttributeError:
        await apprvpm.edit("`Running `")
        return

    if apprvpm.reply_to_msg_id:
        reply = await apprvpm.get_reply_message()
        replied_user = await apprvpm.client.get_entity(reply.from_id)
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        uid = replied_user.id

    else:
        aname = await apprvpm.client.get_entity(apprvpm.chat_id)
        name0 = str(aname.first_name)
        uid = apprvpm.chat_id

    try:
        approve(uid)
    except IntegrityError:
        await apprvpm.edit("`jaces`You allowed to pm!")
        return

    await apprvpm.edit(f"[{name0}](tg://user?id={uid}) `javes: approved to PM!`")

    async for message in apprvpm.client.iter_messages(apprvpm.chat_id,
                                                      from_user='me',
                                                      search=UNAPPROVED_MSG):
        await message.delete()

    if BOTLOG:
        await apprvpm.client.send_message(
            BOTLOG_CHATID,
            "#APPROVED\n" + "User: " + f"[{name0}](tg://user?id={uid})",
        )


@register(outgoing=True, pattern="^\!disallow$")
async def disapprovepm(disapprvpm):
    try:
        from userbot.modules.sql_helper.pm_permit_sql import dissprove
    except BaseException:
        await disapprvpm.edit("`Running on Non-SQL mode!`")
        return

    if disapprvpm.reply_to_msg_id:
        reply = await disapprvpm.get_reply_message()
        replied_user = await disapprvpm.client.get_entity(reply.from_id)
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        dissprove(replied_user.id)
    else:
        dissprove(disapprvpm.chat_id)
        aname = await disapprvpm.client.get_entity(disapprvpm.chat_id)
        name0 = str(aname.first_name)

    await disapprvpm.edit(
        f"[{name0}](tg://user?id={disapprvpm.chat_id}) `Javes: Disaproved to PM!`")

    if BOTLOG:
        await disapprvpm.client.send_message(
            BOTLOG_CHATID,
            f"[{name0}](tg://user?id={disapprvpm.chat_id})"
            " was disapproved to PM you.",
        )


@register(outgoing=True, pattern="^\!block$")
async def blockpm(block):
    """ For .block command, block people from PMing you! """
    if block.reply_to_msg_id:
        reply = await block.get_reply_message()
        replied_user = await block.client.get_entity(reply.from_id)
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        await block.client(BlockRequest(replied_user.id))
        await block.edit("`Javes: You've been blocked!`")
        uid = replied_user.id
    else:
        await block.client(BlockRequest(block.chat_id))
        aname = await block.client.get_entity(block.chat_id)
        await block.edit("`javes: You've been blocked!`")
        name0 = str(aname.first_name)
        uid = block.chat_id

    try:
        from userbot.modules.sql_helper.pm_permit_sql import dissprove
        dissprove(uid)
    except AttributeError:
        pass

    if BOTLOG:
        await block.client.send_message(
            BOTLOG_CHATID,
            "#BLOCKED\n" + "User: " + f"[{name0}](tg://user?id={uid})",
        )


@register(outgoing=True, pattern="^\.unblock$")
async def unblockpm(unblock):
    """ For .unblock command, let people PMing you again! """
    if unblock.reply_to_msg_id:
        reply = await unblock.get_reply_message()
        replied_user = await unblock.client.get_entity(reply.from_id)
        name0 = str(replied_user.first_name)
        await unblock.client(UnblockRequest(replied_user.id))
        await unblock.edit("`Javes: You have been unblocked.`")

    if BOTLOG:
        await unblock.client.send_message(
            BOTLOG_CHATID,
            f"[{name0}](tg://user?id={replied_user.id})"
            " was unblocc'd!.",
        )

""" Userbot module which contains afk-related commands """

from random import choice, randint
from asyncio import sleep

from telethon.events import StopPropagation

from userbot import (AFKREASON, COUNT_MSG, CMD_HELP, ISAFK, BOTLOG,
                     BOTLOG_CHATID, USERS, PM_AUTO_BAN)
from userbot.events import register

try:
    from userbot.modules.sql_helper.globals import gvarstatus, addgvar, delgvar
    afk_db = True
except AttributeError:
    afk_db = False

# ========================= CONSTANTS ============================
AFKSTR = [
    "`Javes: Hello! Sir\n`"
   f"{DEFAULTUSER} is offline just leave your message i will tell him,Thankyou")
    
    
]
# =================================================================


@register(incoming=True, disable_errors=True)
async def mention_afk(mention):
    """ This function takes care of notifying the people who mention you that you are AFK."""
    global COUNT_MSG
    global USERS
    global ISAFK
    global AFFKREASON
    ISAFK_SQL = False
    AFKREASON_SQL = None
    if afk_db:
        ISAFK_SQL = gvarstatus("AFK_STATUS")
        AFKREASON_SQL = gvarstatus("AFK_REASON")
    EXCUSE = AFKREASON_SQL if afk_db else AFKREASON
    if mention.message.mentioned and not (await mention.get_sender()).bot:
        if ISAFK or ISAFK_SQL:
            if mention.sender_id not in USERS:
                if EXCUSE:
                    await mention.reply(f"I'm AFK right now.\
                    \nReason: `{EXCUSE}`")
                else:
                    await mention.reply(str(choice(AFKSTR)))
                USERS.update({mention.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif mention.sender_id in USERS:
                if USERS[mention.sender_id] % randint(2, 4) == 0:
                    if EXCUSE:
                        await mention.reply(
                            f"In case you didn't notice, I'm still AFK.\
                        \nReason: `{EXCUSE}`")
                    else:
                        await mention.reply(str(choice(AFKSTR)))
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


@register(incoming=True, disable_errors=True)
async def afk_on_pm(sender):
    """ Function which informs people that you are AFK in PM """
    global ISAFK
    global AFFKREASON
    ISAFK_SQL = False
    AFKREASON_SQL = None
    if afk_db:
        ISAFK_SQL = gvarstatus("AFK_STATUS")
        AFKREASON_SQL = gvarstatus("AFK_REASON")
    global USERS
    global COUNT_MSG
    EXCUSE = AFKREASON_SQL if afk_db else AFKREASON
    if sender.is_private and sender.sender_id != 777000 and not (
            await sender.get_sender()).bot:
        if PM_AUTO_BAN:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
                apprv = is_approved(sender.sender_id)
            except AttributeError:
                apprv = True
        else:
            apprv = True
        if apprv and (ISAFK or ISAFK_SQL):
            if sender.sender_id not in USERS:
                if EXCUSE:
                    await sender.reply(f"I'm AFK right now.\
                    \nReason: `{EXCUSE}`")
                else:
                    await sender.reply(str(choice(AFKSTR)))
                USERS.update({sender.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif apprv and sender.sender_id in USERS:
                if USERS[sender.sender_id] % randint(2, 4) == 0:
                    if EXCUSE:
                        await sender.reply(
                            f"In case you didn't notice, I'm still AFK.\
                        \nReason: `{EXCUSE}`")
                    else:
                        await sender.reply(str(choice(AFKSTR)))
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


@register(outgoing=True, pattern="^\.afk(?: |$)(.*)", disable_errors=True)
async def set_afk(afk_e):
    """ For .afk command, allows you to inform people that you are afk when they message you """
    message = afk_e.text
    string = afk_e.pattern_match.group(1)
    global ISAFK
    global AFFKREASON
    ISAFK_SQL = False
    AFKREASON_SQL = None
    if afk_db:
        ISAFK_SQL = gvarstatus("AFK_STATUS")
        AFKREASON_SQL = gvarstatus("AFK_REASON")
    if string:
        if afk_db:
            addgvar("AFK_REASON", string)
        AFKREASON = string
        await afk_e.edit(f"Going AFK!\
        \nReason: `{string}`")
    else:
        await afk_e.edit("Going AFK!")
    if BOTLOG:
        await afk_e.client.send_message(BOTLOG_CHATID, "#AFK\nYou went AFK!")
    if afk_db:
        addgvar("AFK_STATUS", True)
    ISAFK = True
    raise StopPropagation


@register(outgoing=True)
async def type_afk_is_not_true(notafk):
    """ This sets your status as not afk automatically when you write something while being afk """
    global COUNT_MSG
    global USERS
    global ISAFK
    global AFFKREASON
    AFKREASON_SQL = None
    ISAFK_SQL = False
    if afk_db:
        ISAFK_SQL = gvarstatus("AFK_STATUS")
        AFKREASON_SQL = gvarstatus("AFK_REASON")
    if ISAFK or ISAFK_SQL:
        if afk_db:
            delgvar("AFK_STATUS")
            delgvar("AFK_REASON")
        ISAFK = False
        AFKREASON = None
        if BOTLOG:
            await notafk.client.send_message(
                BOTLOG_CHATID,
                "You've recieved " + str(COUNT_MSG) + " messages from " +
                str(len(USERS)) + " chats while you were away",
            )
            for i in USERS:
                name = await notafk.client.get_entity(i)
                name0 = str(name.first_name)
                await notafk.client.send_message(
                    BOTLOG_CHATID,
                    "[" + name0 + "](tg://user?id=" + str(i) + ")" +
                    " sent you " + "`" + str(USERS[i]) + " messages`",
                )
        COUNT_MSG = 0
        USERS = {}


