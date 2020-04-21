from asyncio import sleep
from os import remove
from asyncio import sleep
import asyncio
from telethon import events
from datetime import datetime, timedelta
from telethon.tl.types import UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently, ChannelParticipantsKicked, ChatBannedRights
from telethon.tl import functions, types
from time import sleep
from telethon import events
from telethon.utils import pack_bot_file_id
from userbot.modules.sql_helper.rkwelcome_sql import get_current_rkwelcome_settings, \
    add_rkwelcome_setting, rm_rkwelcome_setting, update_previous_rkwelcome
from telethon import events, utils
from telethon.tl import types
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import javes05
from userbot import CMD_HELP, bot, LOGS, CLEAN_WELCOME, BOTLOG_CHATID
from telethon.events import ChatAction
import datetime
from datetime import datetime
from emoji import emojize
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.utils import get_input_location
from userbot import CMD_HELP
from telethon.tl import functions, types
from telethon import functions
from userbot.events import javes05
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
import html
from telethon.tl.functions.channels import EditBannedRequest
import userbot.modules.sql_helper.warns_sql as sql
from telethon.tl.types import MessageEntityMentionName
from os import remove
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.errors import (BadRequestError, ChatAdminRequiredError,ImageProcessFailedError, PhotoCropSizeSmallError,UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (UserIdInvalidError,MessageTooLongError)
from telethon.tl.functions.channels import (EditAdminRequest,EditBannedRequest,EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (PeerChannel, ChannelParticipantsAdmins,ChatAdminRights, ChatBannedRights,MessageEntityMentionName, MessageMediaPhoto,ChannelParticipantsBots)
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot import CMD_HELP, bot, LOGS, CLEAN_WELCOME, BOTLOG_CHATID
from telethon.events import ChatAction
from asyncio import sleep
import asyncio
import io
import re
import userbot.modules.sql_helper.blacklist_sql as sql
from telethon import events, utils
from telethon.tl import types, functions
from userbot import CMD_HELP, bot
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from asyncio import sleep
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.types import ChatBannedRights
from userbot import CMD_HELP
from re import fullmatch, IGNORECASE, escape
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from requests import get
from telethon.events import ChatAction
from telethon.tl.types import ChannelParticipantsAdmins, Message
import asyncio
import re
from userbot.events import javes05
from telethon import events, utils
from telethon.tl import types
from userbot.modules.sql_helper.rkfilter_sql import get_filter, add_filter, remove_filter, get_all_rkfilters, remove_all_rkfilters
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, ANTI_SPAMBOT, ANTI_SPAMBOT_SHOUT, bot
from telethon.errors import (BadRequestError, ChatAdminRequiredError,ImageProcessFailedError, PhotoCropSizeSmallError,UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (UserIdInvalidError,MessageTooLongError)
from telethon.tl.functions.channels import (EditAdminRequest,EditBannedRequest,EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (PeerChat, PeerChannel,ChannelParticipantsAdmins, ChatAdminRights,ChatBannedRights, MessageEntityMentionName,MessageMediaPhoto, ChannelParticipantsBots)
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot import bot
from userbot.events import admin_cmd, command
from userbot.events import javes05
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.types import ChatBannedRights
from userbot import CMD_HELP
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)

# =================== CONSTANT ===================
PP_TOO_SMOL = f"`{JAVES_NNAME}:`**The image is too small**"
PP_ERROR = f"`{JAVES_NNAME}:`**Failure while processing the image**"
NO_ADMIN = f"`{JAVES_NNAME}:`**Sorry, I can't able to get admin rights here!**"
NO_PERM = f"`{JAVES_NNAME}:`**I don't have sufficient permissions!**"
NO_SQL = f"`{JAVES_NNAME}:`**Running on Non-SQL mode!**"
CHAT_PP_CHANGED = f"`{JAVES_NNAME}:`**Chat Picture Changed**"
CHAT_PP_ERROR = f"`{JAVES_NNAME}:`**Some issue with updating the pic,**" \
                "**maybe coz I'm not an admin,**" \
                "**or don't have enough rights.**"
INVALID_MEDIA = "`Invalid Extension`"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)
# ================================================



DELETE_TIMEOUT = 0
TYPE_TEXT = 0
TYPE_PHOTO = 1
TYPE_DOCUMENT = 2


global last_triggered_rkfilters
last_triggered_rkfilters = {}  # pylint:disable=E0602
#filters logic
@bot.on(events.NewMessage(incoming=True))
async def on_snip(event):
    global last_triggered_rkfilters
    name = event.raw_text
    if event.chat_id in last_triggered_rkfilters:
        if name in last_triggered_rkfilters[event.chat_id]:
            # avoid userbot spam
            # "I demand rights for us bots, we are equal to you humans." -Henri Koivuneva (t.me/UserbotTesting/2698)
            return False
    snips = get_all_rkfilters(event.chat_id)
    if snips:
        for snip in snips:
            pattern = r"( |^|[^\w])" + re.escape(snip.keyword) + r"( |$|[^\w])"
            if re.search(pattern, name, flags=re.IGNORECASE):
                if snip.snip_type == TYPE_PHOTO:
                    media = types.InputPhoto(
                        int(snip.media_id),
                        int(snip.media_access_hash),
                        snip.media_file_reference
                    )
                elif snip.snip_type == TYPE_DOCUMENT:
                    media = types.InputDocument(
                        int(snip.media_id),
                        int(snip.media_access_hash),
                        snip.media_file_reference
                    )
                else:
                    media = None
                message_id = event.message.id
                if event.reply_to_msg_id:
                    message_id = event.reply_to_msg_id
                await event.reply(
                    snip.reply,
                    file=media
                )
                if event.chat_id not in last_triggered_rkfilters:
                    last_triggered_rkfilters[event.chat_id] = []
                last_triggered_rkfilters[event.chat_id].append(name)
                await asyncio.sleep(DELETE_TIMEOUT)
                last_triggered_rkfilters[event.chat_id].remove(name)

@bot.on(ChatAction)
async def welcome_to_chat(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import get_current_welcome_settings
        from userbot.modules.sql_helper.welcome_sql import update_previous_welcome
    except AttributeError:
        return
    cws = get_current_welcome_settings(event.chat_id)
    if cws:
        """user_added=True,
        user_joined=True,
        user_left=False,
        user_kicked=False"""
        if (event.user_joined
                or event.user_added) and not (await event.get_user()).bot:
            if CLEAN_WELCOME:
                try:
                    await event.client.delete_messages(event.chat_id,
                                                       cws.previous_welcome)
                except Exception as e:
                    LOGS.warn(str(e))
            a_user = await event.get_user()
            chat = await event.get_chat()
            me = await event.client.get_me()

            title = chat.title if chat.title else "this chat"
            participants = await event.client.get_participants(chat)
            count = len(participants)
            mention = "[{}](tg://user?id={})".format(a_user.first_name,
                                                     a_user.id)
            my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
            first = a_user.first_name
            last = a_user.last_name
            if last:
                fullname = f"{first} {last}"
            else:
                fullname = first
            username = f"@{a_user.username}" if a_user.username else mention
            userid = a_user.id
            my_first = me.first_name
            my_last = me.last_name
            if my_last:
                my_fullname = f"{my_first} {my_last}"
            else:
                my_fullname = my_first
            my_username = f"@{me.username}" if me.username else my_mention
            file_media = None
            current_saved_welcome_message = None
            if cws and cws.f_mesg_id:
                msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                        ids=int(cws.f_mesg_id))
                file_media = msg_o.media
                current_saved_welcome_message = msg_o.message
            elif cws and cws.reply:
                current_saved_welcome_message = cws.reply
            current_message = await event.reply(
                current_saved_welcome_message.format(mention=mention,
                                                     title=title,
                                                     count=count,
                                                     first=first,
                                                     last=last,
                                                     fullname=fullname,
                                                     username=username,
                                                     userid=userid,
                                                     my_first=my_first,
                                                     my_last=my_last,
                                                     my_fullname=my_fullname,
                                                     my_username=my_username,
                                                     my_mention=my_mention),
                file=file_media)
            update_previous_welcome(event.chat_id, current_message.id)


@bot.on(events.NewMessage(incoming=True))
async def filter_incoming_handler(handler):
    """ Checks if the incoming message contains handler of a filter """
    try:
        if not (await handler.get_sender()).bot:
            try:
                from userbot.modules.sql_helper.filter_sql import get_filters
            except AttributeError:
                await handler.edit("`Running on Non-SQL mode!`")
                return
            name = handler.raw_text
            filters = get_filters(handler.chat_id)
            if not filters:
                return
            for trigger in filters:
                pro = fullmatch(trigger.keyword, name, flags=IGNORECASE)
                if pro and trigger.f_mesg_id:
                    msg_o = await handler.client.get_messages(
                        entity=BOTLOG_CHATID, ids=int(trigger.f_mesg_id))
                    await handler.reply(msg_o.message, file=msg_o.media)
                elif pro and trigger.reply:
                    await handler.reply(trigger.reply)
    except AttributeError:
        pass



@bot.on(events.NewMessage(incoming=True))
async def muter(moot):
    """ gban logic"""
    try:
        from userbot.modules.sql_helper.spam_mute_sql import is_muted
        from userbot.modules.sql_helper.gmute_sql import is_gmuted
    except AttributeError:
        return
    muted = is_muted(moot.chat_id)
    gmuted = is_gmuted(moot.sender_id)
    me = await moot.client.get_me()
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    my_username = f"@{me.username}" if me.username else my_mention
    BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)
    rights = ChatBannedRights(
        until_date=None,
        send_messages=True,
        send_media=True,
        send_stickers=True,
        send_gifs=True,
        send_games=True,
        send_inline=True,
        embed_links=True,
    )
    if muted:
        for i in muted:
            if str(i.sender) == str(moot.sender_id):
                try:
                    await moot.delete()
                    await moot.client(EditBannedRequest(moot.chat_id, moot.sender_id,rights))          
                except (BadRequestError, UserAdminInvalidError,ChatAdminRequiredError, UserIdInvalidError):
                    await moot.client.send_read_acknowledge(
                        moot.chat_id, moot.id)
    if gmuted:
        for i in gmuted:
            if i.sender == str(moot.sender_id):
                try:
                    await moot.delete()
                    await moot.client(EditBannedRequest(moot.chat_id, moot.sender_id,BANNED_RIGHTS))
                    await moot.reply(
                     f"`{JAVES_NNAME}:` ** Gbanned user found in this group, Sucessfully banned user!! **\n\n"            
                     f" `Victim ID:`  **{moot.sender_id}**\n"
                     f" `Gban Admin:`**{my_username}**")
                except (BadRequestError, UserAdminInvalidError,ChatAdminRequiredError, UserIdInvalidError):
                    await moot.client.send_read_acknowledge(
                        moot.chat_id, moot.id)




@bot.on(ChatAction)
async def ANTI_SPAMBOT(welcm):
    try:
        ''' Ban a recently joined user if it
           matches the spammer checking algorithm. '''
        if not ANTI_SPAMBOT:
            return
        if welcm.user_joined or welcm.user_added:
            adder = None
            ignore = False
            users = None

            if welcm.user_added:
                ignore = False
                try:
                    adder = welcm.action_message.from_id
                except AttributeError:
                    return

            async for admin in bot.iter_participants(
                    welcm.chat_id, filter=ChannelParticipantsAdmins):
                if admin.id == adder:
                    ignore = True
                    break

            if ignore:
                return

            elif welcm.user_joined:
                users_list = hasattr(welcm.action_message.action, "users")
                if users_list:
                    users = welcm.action_message.action.users
                else:
                    users = [welcm.action_message.from_id]

            await sleep(5)
            spambot = False

            if not users:
                return

            for user_id in users:
                async for message in bot.iter_messages(welcm.chat_id,
                                                       from_user=user_id):

                    correct_type = isinstance(message, Message)
                    if not message or not correct_type:
                        break

                    join_time = welcm.action_message.date
                    message_date = message.date

                    if message_date < join_time:
                        continue  # The message was sent before the user joined, thus ignore it

                    check_user = await welcm.client.get_entity(user_id)

                    # DEBUGGING. LEAVING IT HERE FOR SOME TIME ###
                    print(
                        f"User Joined: {check_user.first_name} [ID: {check_user.id}]"
                    )
                    print(f"Chat: {welcm.chat.title}")
                    print(f"Time: {join_time}")
                    print(
                        f"Message Sent: {message.text}\n\n[Time: {message_date}]"
                    )
                    ##############################################

                    try:
                        cas_url = f"https://combot.org/api/cas/check?user_id={check_user.id}"
                        r = get(cas_url, timeout=3)
                        data = r.json()
                    except BaseException:
                        print(
                            "CAS check failed, falling back to legacy anti_spambot behaviour."
                        )
                        data = None
                        pass

                    if data and data['ok']:
                        reason = f"[Banned by Combot Anti Spam](https://combot.org/cas/query?u={check_user.id})"
                        spambot = True
                    elif "t.cn/" in message.text:
                        reason = "Match on `t.cn` URLs"
                        spambot = True
                    elif "t.me/joinchat" in message.text:
                        reason = "Potential Promotion Message"
                        spambot = True
                    elif message.fwd_from:
                        reason = "Forwarded Message"
                        spambot = True
                    elif "?start=" in message.text:
                        reason = "Telegram bot `start` link"
                        spambot = True
                    elif "bit.ly/" in message.text:
                        reason = "Match on `bit.ly` URLs"
                        spambot = True
                    else:
                        if check_user.first_name in ("Bitmex", "Promotion",
                                                     "Information", "Dex",
                                                     "Announcements", "Info"):
                            if user.last_name == "Bot":
                                reason = "Known spambot"
                                spambot = True

                    if spambot:
                        print(f"Potential Spam Message: {message.text}")
                        await message.delete()
                        break

                    continue  # Check the next messsage

            if spambot:
                chat = await welcm.get_chat()
                admin = chat.admin_rights
                creator = chat.creator
                if not admin and not creator:
                    if ANTI_SPAMBOT_SHOUT:
                        await welcm.reply(
                            f"`{JAVES_NNAME}`: @admins\n"
                            "`Warning! There is a SPAMBOT Joined In group`\n"                           
                            f"SpamBot Type: {reason}")
                        kicked = False
                        reported = True
                else:
                    try:

                        await welcm.reply(
                            f"`{JAVES_NNAME}`: ** Spambot Detected !!**\n"
                            f"`REASON:` {reason}\n"
                            "Kicking away for now, will log the ID for further purposes.\n"
                            f"`USER:` [{check_user.first_name}](tg://user?id={check_user.id})"
                        )

                        await welcm.client.kick_participant(
                            welcm.chat_id, check_user.id)
                        kicked = True
                        reported = False

                    except BaseException:
                        if ANTI_SPAMBOT_SHOUT:
                            await welcm.reply(
                            f"`{JAVES_NNAME}`: @admins\n"
                            "`Warning! There is a SPAMBOT Joined In group`\n"                           
                            f"SpamBot Type: {reason}")
                            kicked = False
                            reported = True

                if BOTLOG:
                    if kicked or reported:
                        await welcm.client.send_message(
                            BOTLOG_CHATID, "#ANTI_SPAMBOT REPORT\n"
                            f"USER: [{user.first_name}](tg://user?id={check_user.id})\n"
                            f"USER ID: `{check_user.id}`\n"
                            f"CHAT: {welcm.chat.title}\n"
                            f"CHAT ID: `{welcm.chat_id}`\n"
                            f"REASON: {reason}\n"
                            f"MESSAGE:\n\n{message.text}")
    except ValueError:
        pass











@javes05(outgoing=True, disable_errors=True, pattern=r"^\!savewelcome(?: |$)(.*)")
async def save_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import add_welcome_setting
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    msg = await event.get_reply_message()
    string = event.pattern_match.group(1)
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, f"#WELCOME_NOTE\
            \nCHAT ID: {event.chat_id}\
            \nThe following message is saved as the new welcome note for the chat, please do NOT delete it !!"
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            await event.edit(
                f"`{JAVES_NNAME}`: **Saving media as part of the welcome note requires the BOTLOG_CHATID to be set.**"
            )
            return
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = " Welcome note {} for this chat."
    if add_welcome_setting(event.chat_id, 0, string, msg_id) is True:
        await event.edit(success.format('saved'))
    else:
        await event.edit(f"`{JAVES_NNAME}`: **Ops, old welcome message found, i deleted it Sucessfully now you can save new welcome message!**")




@bot.on(admin_cmd(pattern=f"savewelcome(?: |$)(.*)", allow_sudo=True))
async def save_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import add_welcome_setting
    except AttributeError:
        await event.reply("`Running on Non-SQL mode!`")
        return
    msg = await event.get_reply_message()
    string = event.pattern_match.group(1)
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, f"#WELCOME_NOTE\
            \nCHAT ID: {event.chat_id}\
            \nThe following message is saved as the new welcome note for the chat, please do NOT delete it !!"
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            await event.reply(
                f"`{JAVES_NNAME}`: **Saving media as part of the welcome note requires the BOTLOG_CHATID to be set.**"
            )
            return
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = " Welcome note {} for this chat."
    if add_welcome_setting(event.chat_id, 0, string, msg_id) is True:
        await event.reply(success.format('saved'))
    else:
        await event.reply(f"`{JAVES_NNAME}`: **Ops, old welcome message found, i deleted it Sucessfully now you can save new welcome message!**")











@javes05(outgoing=True, disable_errors=True, pattern="^\!checkwelcome$")
async def show_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import get_current_welcome_settings
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    cws = get_current_welcome_settings(event.chat_id)
    if not cws:
        await event.edit(f"`{JAVES_NNAME}`: **No welcome message saved here.**")
        return
    elif cws and cws.f_mesg_id:
        msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                ids=int(cws.f_mesg_id))
        await event.edit(
            f"`{JAVES_NNAME}`: **I am currently welcoming new users with this welcome note.**")
        await event.reply(msg_o.message, file=msg_o.media)
    elif cws and cws.reply:
        await event.edit(
            f"`{JAVES_NNAME}`: **I am currently welcoming new users with this welcome note.**")
        await event.reply(cws.reply)



@bot.on(admin_cmd(pattern=f"checkwelcome$", allow_sudo=True))
async def show_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import get_current_welcome_settings
    except AttributeError:
        await event.reply("`Running on Non-SQL mode!`")
        return
    cws = get_current_welcome_settings(event.chat_id)
    if not cws:
        await event.reply(f"`{JAVES_NNAME}`: **No welcome message saved here.**")
        return
    elif cws and cws.f_mesg_id:
        msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                ids=int(cws.f_mesg_id))
        await event.reply(
            f"`{JAVES_NNAME}`: **I am currently welcoming new users with this welcome note.**")
        await event.reply(msg_o.message, file=msg_o.media)
    elif cws and cws.reply:
        await event.reply(
            f"`{JAVES_NNAME}`: **I am currently welcoming new users with this welcome note.**")
        await event.reply(cws.reply)







@javes05(outgoing=True, disable_errors=True, pattern="^\!clearwelcome$")
async def del_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import rm_welcome_setting
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    if rm_welcome_setting(event.chat_id) is True:
        await event.edit(f"`{JAVES_NNAME}`: **Welcome note deleted for this chat.**")
    else:
        await event.edit(f"`{JAVES_NNAME}`: ** I Didnt have any welcome messages here **")


@bot.on(admin_cmd(pattern=f"clearwelcome$", allow_sudo=True))
async def del_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import rm_welcome_setting
    except AttributeError:
        await event.reply("`Running on Non-SQL mode!`")
        return
    if rm_welcome_setting(event.chat_id) is True:
        await event.reply(f"`{JAVES_NNAME}`: **Welcome note deleted for this chat.**")
    else:
        await event.reply(f"`{JAVES_NNAME}`: ** I Didnt have any welcome messages here **")









@javes05(outgoing=True, disable_errors=True, pattern=r"^\!lock ?(.*)")
async def locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = True
        what = "messages"
    elif input_str == "media":
        media = True
        what = "media"
    elif input_str == "sticker":
        sticker = True
        what = "stickers"
    elif input_str == "gif":
        gif = True
        what = "GIFs"
    elif input_str == "game":
        gamee = True
        what = "games"
    elif input_str == "inline":
        ainline = True
        what = "inline bots"
    elif input_str == "poll":
        gpoll = True
        what = "polls"
    elif input_str == "invite":
        adduser = True
        what = "invites"
    elif input_str == "pin":
        cpin = True
        what = "pins"
    elif input_str == "info":
        changeinfo = True
        what = "chat info"
    elif input_str == "all":
        msg = True
        media = True
        sticker = True
        gif = True
        gamee = True
        ainline = True
        gpoll = True
        adduser = True
        cpin = True
        changeinfo = True
        what = "everything"
    else:
        if not input_str:
            await event.edit(f"`{JAVES_NNAME}`: **I can't lock nothing !!**")
            return
        else:
            await event.edit(f"`Invalid lock type:` {input_str}")
            return

    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id,
                                               banned_rights=lock_rights))
        await event.edit(f"`{JAVES_NNAME}`: **Locked {what} for this chat !!**")
    except BaseException as e:
        await event.edit(
            f"`{JAVES_NNAME}`: **Sorry i can't able to get admin  rights here**\n**Error:** {str(e)}")
        return



@bot.on(admin_cmd(pattern=f"lock ?(.*)", allow_sudo=True))
async def locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = True
        what = "messages"
    elif input_str == "media":
        media = True
        what = "media"
    elif input_str == "sticker":
        sticker = True
        what = "stickers"
    elif input_str == "gif":
        gif = True
        what = "GIFs"
    elif input_str == "game":
        gamee = True
        what = "games"
    elif input_str == "inline":
        ainline = True
        what = "inline bots"
    elif input_str == "poll":
        gpoll = True
        what = "polls"
    elif input_str == "invite":
        adduser = True
        what = "invites"
    elif input_str == "pin":
        cpin = True
        what = "pins"
    elif input_str == "info":
        changeinfo = True
        what = "chat info"
    elif input_str == "all":
        msg = True
        media = True
        sticker = True
        gif = True
        gamee = True
        ainline = True
        gpoll = True
        adduser = True
        cpin = True
        changeinfo = True
        what = "everything"
    else:
        if not input_str:
            await event.reply(f"`{JAVES_NNAME}`: **I can't lock nothing !!**")
            return
        else:
            await event.reply(f"`Invalid lock type:` {input_str}")
            return

    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id,
                                               banned_rights=lock_rights))
        await event.reply(f"`{JAVES_NNAME}`: **Locked {what} for this chat !!**")
    except BaseException as e:
        await event.reply(
            f"`{JAVES_NNAME}`: **Sorry i can't able to get admin  rights here**\n**Error:** {str(e)}")
        return



@javes05(outgoing=True, disable_errors=True, pattern=r"^!unlock ?(.*)")
async def rem_locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = False
        what = "messages"
    elif input_str == "media":
        media = False
        what = "media"
    elif input_str == "sticker":
        sticker = False
        what = "stickers"
    elif input_str == "gif":
        gif = False
        what = "GIFs"
    elif input_str == "game":
        gamee = False
        what = "games"
    elif input_str == "inline":
        ainline = False
        what = "inline bots"
    elif input_str == "poll":
        gpoll = False
        what = "polls"
    elif input_str == "invite":
        adduser = False
        what = "invites"
    elif input_str == "pin":
        cpin = False
        what = "pins"
    elif input_str == "info":
        changeinfo = False
        what = "chat info"
    elif input_str == "all":
        msg = False
        media = False
        sticker = False
        gif = False
        gamee = False
        ainline = False
        gpoll = False
        adduser = False
        cpin = False
        changeinfo = False
        what = "everything"
    else:
        if not input_str:
            await event.edit(f"`{JAVES_NNAME}`: **I can't unlock nothing !!**")
            return
        else:
            await event.edit(f"`Invalid unlock type:` {input_str}")
            return

    unlock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id,
                                               banned_rights=unlock_rights))
        await event.edit(f"`{JAVES_NNAME}`: **Unlocked {what} for this chat !!**")
    except BaseException as e:
        await event.edit(
            f"`{JAVES_NNAME}`: **Sorry i can't able to get admin rights here`\n**Error:** {str(e)}")
        return


@bot.on(admin_cmd(pattern=f"unlock ?(.*)", allow_sudo=True))
async def rem_locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = False
        what = "messages"
    elif input_str == "media":
        media = False
        what = "media"
    elif input_str == "sticker":
        sticker = False
        what = "stickers"
    elif input_str == "gif":
        gif = False
        what = "GIFs"
    elif input_str == "game":
        gamee = False
        what = "games"
    elif input_str == "inline":
        ainline = False
        what = "inline bots"
    elif input_str == "poll":
        gpoll = False
        what = "polls"
    elif input_str == "invite":
        adduser = False
        what = "invites"
    elif input_str == "pin":
        cpin = False
        what = "pins"
    elif input_str == "info":
        changeinfo = False
        what = "chat info"
    elif input_str == "all":
        msg = False
        media = False
        sticker = False
        gif = False
        gamee = False
        ainline = False
        gpoll = False
        adduser = False
        cpin = False
        changeinfo = False
        what = "everything"
    else:
        if not input_str:
            await event.reply(f"`{JAVES_NNAME}`: **I can't unlock nothing !!**")
            return
        else:
            await event.reply(f"`Invalid unlock type:` {input_str}")
            return

    unlock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id,
                                               banned_rights=unlock_rights))
        await event.reply(f"`{JAVES_NNAME}`: **Unlocked {what} for this chat !!**")
    except BaseException as e:
        await event.reply(
            f"`{JAVES_NNAME}`: **Sorry i can't able to get admin rights here`\n**Error:** {str(e)}")
        return







@javes05(outgoing=True, disable_errors=True, pattern="^\!userid$")
async def useridgetter(target):
    """ For .userid command, returns the ID of the target user. """
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.edit(" **Name:** {} \n**User ID:** `{}`".format(
            name, user_id))


@bot.on(admin_cmd(pattern=f"userid$", allow_sudo=True))
async def useridgetter(target):
    """ For .userid command, returns the ID of the target user. """
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.reply(" **Name:** {} \n**User ID:** `{}`".format(
            name, user_id))



@javes05(outgoing=True, disable_errors=True, pattern="^\!link(?: |$)(.*)")
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await mention.edit(f"[{custom}](tg://user?id={user.id})")
    else:
        tag = user.first_name.replace("\u2060",
                                      "") if user.first_name else user.username
        await mention.edit(f"`{JAVES_NNAME}`: [{tag}](tg://user?id={user.id})")


@bot.on(admin_cmd(pattern=f"link(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await mention.reply(f"[{custom}](tg://user?id={user.id})")
    else:
        tag = user.first_name.replace("\u2060",
                                      "") if user.first_name else user.username
        await mention.reply(f"`{JAVES_NNAME}`: [{tag}](tg://user?id={user.id})")



@javes05(outgoing=True, disable_errors=True, pattern="^\!chatid$")
async def chatidgetter(chat):
    """ For .chatid, returns the ID of the chat you are in at that moment. """
    await chat.edit(f"`{JAVES_NNAME}`: Chat ID: `" + str(chat.chat_id) + "`")


@bot.on(admin_cmd(pattern=f"chatid$", allow_sudo=True))
async def chatidgetter(chat):
    """ For .chatid, returns the ID of the chat you are in at that moment. """
    await chat.reply(f"`{JAVES_NNAME}`: Chat ID: `" + str(chat.chat_id) + "`")




@javes05(outgoing=True, disable_errors=True, pattern=r"^\!log(?: |$)([\s\S]*)")
async def log(log_text):
    """ For .log command, forwards a message or the command argument to the bot logs group """
    if BOTLOG:
        if log_text.reply_to_msg_id:
            reply_msg = await log_text.get_reply_message()
            await reply_msg.forward_to(BOTLOG_CHATID)
        elif log_text.pattern_match.group(1):
            user = f"#LOG / Chat ID: {log_text.chat_id}\n\n"
            textx = user + log_text.pattern_match.group(1)
            await bot.send_message(BOTLOG_CHATID, textx)
        else:
            await log_text.edit(f"`{JAVES_NNAME}`: **What am I supposed to log?**")
            return
        await log_text.edit(f"`{JAVES_NNAME}`: **Logged Successfully**")
    else:
        await log_text.edit(f"`{JAVES_NNAME}`: **This feature requires Logging to be enabled!**")
    await sleep(2)
    await log_text.delete()

@bot.on(admin_cmd(pattern=f"log$", allow_sudo=True))
async def iqless(e):
    await e.reply(f"`{JAVES_NNAME}`: **Privacy error! , Sorry sudo users dont have permission to access it!**")






@javes05(outgoing=True, disable_errors=True, pattern="^\!kickme$")
async def kickme(leave):
    """ Basically it's .kickme command """
    await leave.edit(f"`{JAVES_NNAME}`: **My master Didnt like this place......GoodBye!**")
    await leave.client.kick_participant(leave.chat_id, 'me')

@bot.on(admin_cmd(pattern=f"kickme$", allow_sudo=True))
async def iqless(e):
    await e.reply(f"`{JAVES_NNAME}`: **Privacy error! , Sorry sudo users dont have permission to access it!**")







@javes05(outgoing=True, disable_errors=True, pattern="^\!setgpic$", groups_only=True)
async def set_group_photo(gpic):
    if not gpic.is_group:
        await gpic.edit(f"`{JAVES_NNAME}:` **I don't think this is a group.**")
        return
    replymsg = await gpic.get_reply_message()
    chat = await gpic.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None
    if not admin and not creator:
        await gpic.edit(NO_ADMIN)
        return
    if replymsg and replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await gpic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split('/'):
            photo = await gpic.client.download_file(replymsg.media.document)
        else:
            await gpic.edit(INVALID_MEDIA)
    if photo:
        try:
            await gpic.client(
                EditPhotoRequest(gpic.chat_id, await
                                 gpic.client.upload_file(photo)))
            await gpic.edit(CHAT_PP_CHANGED)

        except PhotoCropSizeSmallError:
            await gpic.edit(PP_TOO_SMOL)
        except ImageProcessFailedError:
            await gpic.edit(PP_ERROR)



@bot.on(admin_cmd(pattern=f"setgpic$", allow_sudo=True))
async def set_group_photo(gpic):
    if not gpic.is_group:
        await gpic.reply(f"`{JAVES_NNAME}:` **I don't think this is a group.**")
        return
    replymsg = await gpic.get_reply_message()
    chat = await gpic.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None
    if not admin and not creator:
        await gpic.reply(NO_ADMIN)
        return
    if replymsg and replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await gpic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split('/'):
            photo = await gpic.client.download_file(replymsg.media.document)
        else:
            await gpic.reply(INVALID_MEDIA)
    if photo:
        try:
            await gpic.client(
                EditPhotoRequest(gpic.chat_id, await
                                 gpic.client.upload_file(photo)))
            await gpic.reply(CHAT_PP_CHANGED)

        except PhotoCropSizeSmallError:
            await gpic.reply(PP_TOO_SMOL)
        except ImageProcessFailedError:
            await gpic.reply(PP_ERROR)




@javes05(outgoing=True, disable_errors=True, pattern="^\!promote(?: |$)(.*)", groups_only=True)
async def promote(promt):
    """ For .promote command, promotes the replied/tagged person """
    # Get targeted chat
    chat = await promt.get_chat()
    # Grab admin status or creator in a chat
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, also return
    if not admin and not creator:
        await promt.edit(NO_ADMIN)
        return

    new_rights = ChatAdminRights(add_admins=False,
                                 invite_users=True,
                                 change_info=False,
                                 ban_users=True,
                                 delete_messages=True,
                                 pin_messages=True)

    await promt.edit(f"`{JAVES_NNAME}:` **Promoting User**")
    user, rank = await get_user_from_event(promt)
    if not rank:
        # Just in case.
        rank = "admin"
    if user:
        pass
    else:
        return

    # Try to promote if current user is admin or creator
    try:
        await promt.client(
            EditAdminRequest(promt.chat_id, user.id, new_rights, rank))
        await promt.edit(f"`{JAVES_NNAME}:` **Promoted user [{user.first_name}](tg://user?id={user.id}) to admin  Sucessfully in {promt.chat.title}**")

    # If Telethon spit BadRequestError, assume
    # we don't have Promote permission
    except BadRequestError:
        await promt.edit(NO_PERM)
        return

    # Announce to the logging group if we have promoted successfully
    if BOTLOG:
        await promt.client.send_message(
            BOTLOG_CHATID, "I HAVE PROMOTED\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {promt.chat.title}({promt.chat_id})")



@bot.on(admin_cmd(pattern=f"promote(?: |$)(.*)", allow_sudo=True))
async def promote(promt):
    """ For .promote command, promotes the replied/tagged person """
    # Get targeted chat
    chat = await promt.get_chat()
    # Grab admin status or creator in a chat
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, also return
    if not admin and not creator:
        await promt.reply(NO_ADMIN)
        return

    new_rights = ChatAdminRights(add_admins=False,
                                 invite_users=True,
                                 change_info=False,
                                 ban_users=True,
                                 delete_messages=True,
                                 pin_messages=True)

    await promt.reply(f"`{JAVES_NNAME}:` **Promoting User**")
    user, rank = await get_user_from_event(promt)
    if not rank:
        # Just in case.
        rank = "admin"
    if user:
        pass
    else:
        return

    # Try to promote if current user is admin or creator
    try:
        await promt.client(
            EditAdminRequest(promt.chat_id, user.id, new_rights, rank))
        await promt.reply(f"`{JAVES_NNAME}:` **Promoted user [{user.first_name}](tg://user?id={user.id}) to admin  Sucessfully in {promt.chat.title}**")

    # If Telethon spit BadRequestError, assume
    # we don't have Promote permission
    except BadRequestError:
        await promt.reply(NO_PERM)
        return

    # Announce to the logging group if we have promoted successfully
    if BOTLOG:
        await promt.client.send_message(
            BOTLOG_CHATID, "I HAVE PROMOTED\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {promt.chat.title}({promt.chat_id})")










@javes05(outgoing=True, disable_errors=True, pattern="^\!demote(?: |$)(.*)", groups_only=True)
async def demote(dmod):
    """ For .demote command, demotes the replied/tagged person """
    # Admin right check
    chat = await dmod.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await dmod.edit(NO_ADMIN)
        return

    # If passing, declare that we're going to demote
    await dmod.edit(f"`{JAVES_NNAME}:`** Demoting user......**")
    rank = "admin"  # dummy rank, lol.
    user = await get_user_from_event(dmod)
    user = user[0]
    if user:
        pass
    else:
        return

    # New rights after demotion
    newrights = ChatAdminRights(add_admins=None,
                                invite_users=None,
                                change_info=None,
                                ban_users=None,
                                delete_messages=None,
                                pin_messages=None)
    # Edit Admin Permission
    try:
        await dmod.client(
            EditAdminRequest(dmod.chat_id, user.id, newrights, rank))

    # If we catch BadRequestError from Telethon
    # Assume we don't have permission to demote
    except BadRequestError:
        await dmod.edit(NO_PERM)
        return
    await dmod.edit(f"`{JAVES_NNAME}:` **Demoted user [{user.first_name}](tg://user?id={user.id}) to admin  Sucessfully in {dmod.chat.title}**")

    # Announce to the logging group if we have demoted successfully
    if BOTLOG:
        await dmod.client.send_message(
            BOTLOG_CHATID, "#DEMOTE\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {dmod.chat.title}(`{dmod.chat_id}`)")

@bot.on(admin_cmd(pattern=f"demote(?: |$)(.*)", allow_sudo=True))
async def demote(dmod):
    """ For .demote command, demotes the replied/tagged person """
    # Admin right check
    chat = await dmod.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await dmod.reply(NO_ADMIN)
        return

    # If passing, declare that we're going to demote
    await dmod.reply(f"`{JAVES_NNAME}:`** Demoting user......**")
    rank = "admin"  # dummy rank, lol.
    user = await get_user_from_event(dmod)
    user = user[0]
    if user:
        pass
    else:
        return

    # New rights after demotion
    newrights = ChatAdminRights(add_admins=None,
                                invite_users=None,
                                change_info=None,
                                ban_users=None,
                                delete_messages=None,
                                pin_messages=None)
    # Edit Admin Permission
    try:
        await dmod.client(
            EditAdminRequest(dmod.chat_id, user.id, newrights, rank))

    # If we catch BadRequestError from Telethon
    # Assume we don't have permission to demote
    except BadRequestError:
        await dmod.reply(NO_PERM)
        return
    await dmod.reply(f"`{JAVES_NNAME}:` **Demoted user [{user.first_name}](tg://user?id={user.id}) to admin  Sucessfully in {dmod.chat.title}**")

    # Announce to the logging group if we have demoted successfully
    if BOTLOG:
        await dmod.client.send_message(
            BOTLOG_CHATID, "#DEMOTE\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {dmod.chat.title}(`{dmod.chat_id}`)")






@javes05(outgoing=True, disable_errors=True, pattern="^\!ban(?: |$)(.*)", groups_only=True)
async def ban(bon):
    """ For .ban command, bans the replied/tagged person """
    # Here laying the sanity check
    chat = await bon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await bon.edit(NO_ADMIN)
        return

    user, reason = await get_user_from_event(bon)
    if user:
        pass
    else:
        return

    # Announce that we're going to whack the pest
    await bon.edit(f"`{JAVES_NNAME}:` **Banning user......**")

    try:
        await bon.client(EditBannedRequest(bon.chat_id, user.id,
                                           BANNED_RIGHTS))
    except BadRequestError:
        await bon.edit(NO_PERM)
        return
    # Helps ban group join spammers more easily
    try:
        reply = await bon.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await bon.edit(f"`{JAVES_NNAME}`: **User still banned!**")
        return
    # Delete message and then tell that the command
    # is done gracefully
    # Shout out the ID, so that fedadmins can fban later
    if reason:
        await bon.edit(f"`{JAVES_NNAME}`:  **{user.first_name} was banned in {bon.chat.title}**!!\
        \nID: `{str(user.id)}`\
        \nReason: {reason}**")
    else:
        await bon.edit(f"`{JAVES_NNAME}`: **{user.first_name} was banned in {bon.chat.title}**!!\
        \nUSERID: `{str(user.id)}`")
    # Announce to the logging group if we have banned the person
    # successfully!
    if BOTLOG:
        await bon.client.send_message(
            BOTLOG_CHATID, "#BANNED MEMBER\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {bon.chat.title}(`{bon.chat_id}`)")



@bot.on(admin_cmd(pattern=f"ban(?: |$)(.*)", allow_sudo=True))
async def ban(bon):
    """ For .ban command, bans the replied/tagged person """
    # Here laying the sanity check
    chat = await bon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await bon.reply(NO_ADMIN)
        return

    user, reason = await get_user_from_event(bon)
    if user:
        pass
    else:
        return

    # Announce that we're going to whack the pest
    await bon.reply(f"`{JAVES_NNAME}:` **Banning user......**")

    try:
        await bon.client(EditBannedRequest(bon.chat_id, user.id,
                                           BANNED_RIGHTS))
    except BadRequestError:
        await bon.reply(NO_PERM)
        return
    # Helps ban group join spammers more easily
    try:
        reply = await bon.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await bon.reply(f"`{JAVES_NNAME}`: **User still banned!**")
        return
    # Delete message and then tell that the command
    # is done gracefully
    # Shout out the ID, so that fedadmins can fban later
    if reason:
        await bon.reply(f"`{JAVES_NNAME}`:  **{user.first_name} was banned in {bon.chat.title}**!!\
        \nID: `{str(user.id)}`\
        \nReason: {reason}**")
    else:
        await bon.reply(f"`{JAVES_NNAME}`: **{user.first_name} was banned in {bon.chat.title}**!!\
        \nUSERID: `{str(user.id)}`")
    # Announce to the logging group if we have banned the person
    # successfully!
    if BOTLOG:
        await bon.client.send_message(
            BOTLOG_CHATID, "#BANNED MEMBER\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {bon.chat.title}(`{bon.chat_id}`)")




@javes05(outgoing=True, disable_errors=True, pattern="^\!unban(?: |$)(.*)", groups_only=True)
async def nothanos(unbon):
    """ For .unban command, unbans the replied/tagged person """
    # Here laying the sanity check
    chat = await unbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await unbon.edit(NO_ADMIN)
        return

    # If everything goes well...
    await unbon.edit(f"`{JAVES_NNAME}:` **UnbanningUser........**")

    user = await get_user_from_event(unbon)
    user = user[0]
    if user:
        pass
    else:
        return

    try:
        await unbon.client(
            EditBannedRequest(unbon.chat_id, user.id, UNBAN_RIGHTS))
        await unbon.edit(f"`{JAVES_NNAME}:` **{user.first_name} was unbanned in {unbon.chat.title}**")

        if BOTLOG:
            await unbon.client.send_message(
                BOTLOG_CHATID, "#UNBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {unbon.chat.title}(`{unbon.chat_id}`)")
    except UserIdInvalidError:
        await unbon.edit(f"`{JAVES_NNAME}:` **Uh oh my unban logic broke!**")


@bot.on(admin_cmd(pattern=f"unban(?: |$)(.*)", allow_sudo=True))
async def nothanos(unbon):
    """ For .unban command, unbans the replied/tagged person """
    # Here laying the sanity check
    chat = await unbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await unbon.reply(NO_ADMIN)
        return

    # If everything goes well...
    await unbon.reply(f"`{JAVES_NNAME}:` **UnbanningUser........**")

    user = await get_user_from_event(unbon)
    user = user[0]
    if user:
        pass
    else:
        return

    try:
        await unbon.client(
            EditBannedRequest(unbon.chat_id, user.id, UNBAN_RIGHTS))
        await unbon.reply(f"`{JAVES_NNAME}:` **{user.first_name} was unbanned in {unbon.chat.title}**")

        if BOTLOG:
            await unbon.client.send_message(
                BOTLOG_CHATID, "#UNBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {unbon.chat.title}(`{unbon.chat_id}`)")
    except UserIdInvalidError:
        await unbon.reply(f"`{JAVES_NNAME}:` **Uh oh my unban logic broke!**")




@javes05(outgoing=True, disable_errors=True, pattern="^\!mute(?: |$)(.*)", groups_only=True)
async def spider(spdr):
    """
    This function is basically muting peeps
    """
    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.spam_mute_sql import mute
    except AttributeError:
        await spdr.edit(NO_SQL)
        return

    # Admin or creator check
    chat = await spdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await spdr.edit(NO_ADMIN)
        return

    user, reason = await get_user_from_event(spdr)
    if user:
        pass
    else:
        return

    self_user = await spdr.client.get_me()

    if user.id == self_user.id:
        await spdr.edit(
            f"`{JAVES_NNAME}:`**Sorry, I can't mute my self**")
        return

    # If everything goes well, do announcing and mute
    await spdr.edit(f"`{JAVES_NNAME}:` **Muting user........**")    
    if mute(spdr.chat_id, user.id) is False:
        return await spdr.edit('f"`{JAVES_NNAME}: ` **Error! User probably already muted.**`')
    else:
        try:
            await spdr.client(
                EditBannedRequest(spdr.chat_id, user.id, MUTE_RIGHTS))

            # Announce that the function is done
            if reason:
                await spdr.edit(f"`{JAVES_NNAME}: `**{user.first_name} was muted in {spdr.chat.title}**\n"
                                               f"`Reason:`**{reason}**")
            else:
                await spdr.edit(f"`{JAVES_NNAME}: `**{user.first_name} was muted in {spdr.chat.title}**")


            # Announce to logging group
            if BOTLOG:
                await spdr.client.send_message(
                    BOTLOG_CHATID, "#MUTE\n"
                    f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                    f"CHAT: {spdr.chat.title}(`{spdr.chat_id}`)")
        except UserIdInvalidError:
            return await spdr.edit("`Uh oh my mute logic broke!`")

@bot.on(admin_cmd(pattern=f"mute(?: |$)(.*)", allow_sudo=True))
async def spider(spdr):
    """
    This function is basically muting peeps
    """
    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.spam_mute_sql import mute
    except AttributeError:
        await spdr.reply(NO_SQL)
        return

    # Admin or creator check
    chat = await spdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await spdr.reply(NO_ADMIN)
        return

    user, reason = await get_user_from_event(spdr)
    if user:
        pass
    else:
        return

    self_user = await spdr.client.get_me()

    if user.id == self_user.id:
        await spdr.reply(
            f"`{JAVES_NNAME}:`**Sorry, I can't mute my self**")
        return

    # If everything goes well, do announcing and mute
    await spdr.reply(f"`{JAVES_NNAME}:` **Muting user........**")    
    if mute(spdr.chat_id, user.id) is False:
        return await spdr.reply('f"`{JAVES_NNAME}: ` **Error! User probably already muted.**`')
    else:
        try:
            await spdr.client(
                EditBannedRequest(spdr.chat_id, user.id, MUTE_RIGHTS))

            # Announce that the function is done
            if reason:
                await spdr.reply(f"`{JAVES_NNAME}: `**{user.first_name} was muted in {spdr.chat.title}**\n"
                                               f"`Reason:`**{reason}**")
            else:
                await spdr.reply(f"`{JAVES_NNAME}: `**{user.first_name} was muted in {spdr.chat.title}**")


            # Announce to logging group
            if BOTLOG:
                await spdr.client.send_message(
                    BOTLOG_CHATID, "#MUTE\n"
                    f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                    f"CHAT: {spdr.chat.title}(`{spdr.chat_id}`)")
        except UserIdInvalidError:
            return await spdr.reply("`Uh oh my mute logic broke!`")


      


@javes05(outgoing=True, disable_errors=True, pattern="^\!unmute(?: |$)(.*)", groups_only=True)
async def unmoot(unmot):
    """ For .unmute command, unmute the replied/tagged person """
    # Admin or creator check
    chat = await unmot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await unmot.edit(NO_ADMIN)
        return

    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.spam_mute_sql import unmute
    except AttributeError:
        await unmot.edit(NO_SQL)
        return

    # If admin or creator, inform the user and start unmuting
    await unmot.edit(f"`{JAVES_NNAME}`**unmuting user........**")
    user = await get_user_from_event(unmot)
    user = user[0]
    if user:
        pass
    else:
        return

    if unmute(unmot.chat_id, user.id) is False:
        return await unmot.edit(f"`{JAVES_NNAME}: `**Error! User probably already unmuted.**")
    else:

        try:
            await unmot.client(
                EditBannedRequest(unmot.chat_id, user.id, UNBAN_RIGHTS))
            await unmot.edit(f"`{JAVES_NNAME}: `**{user.first_name} was unmuted in {unmot.chat.title}**")
        except UserIdInvalidError:
            await unmot.edit("`{JAVES_NNAME}: `**Uh oh my unmute logic broke!**")
            return

        if BOTLOG:
            await unmot.client.send_message(
                BOTLOG_CHATID, "#UNMUTE\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {unmot.chat.title}(`{unmot.chat_id}`)")


@bot.on(admin_cmd(pattern=f"unmute(?: |$)(.*)", allow_sudo=True))
async def unmoot(unmot):
    """ For .unmute command, unmute the replied/tagged person """
    # Admin or creator check
    chat = await unmot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await unmot.reply(NO_ADMIN)
        return

    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.spam_mute_sql import unmute
    except AttributeError:
        await unmot.reply(NO_SQL)
        return

    # If admin or creator, inform the user and start unmuting
    await unmot.reply(f"`{JAVES_NNAME}`**unmuting user........**")
    user = await get_user_from_event(unmot)
    user = user[0]
    if user:
        pass
    else:
        return

    if unmute(unmot.chat_id, user.id) is False:
        return await unmot.reply(f"`{JAVES_NNAME}: `**Error! User probably already unmuted.**")
    else:

        try:
            await unmot.client(
                EditBannedRequest(unmot.chat_id, user.id, UNBAN_RIGHTS))
            await unmot.reply(f"`{JAVES_NNAME}: `**{user.first_name} was unmuted in {unmot.chat.title}**")
        except UserIdInvalidError:
            await unmot.reply("`{JAVES_NNAME}: `**Uh oh my unmute logic broke!**")
            return

        if BOTLOG:
            await unmot.client.send_message(
                BOTLOG_CHATID, "#UNMUTE\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {unmot.chat.title}(`{unmot.chat_id}`)")






@javes05(outgoing=True, disable_errors=True, pattern="^!ungban(?: |$)(.*)")
async def ungmoot(un_gmute):
    """ For .ungmute command, ungmutes the target in the userbot """
    # Admin or creator check
    chat = await un_gmute.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    me = await un_gmute.client.get_me()
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    my_username = f"@{me.username}" if me.username else my_mention

    # If not admin and not creator, return
    if not admin and not creator:
        await un_gmute.edit(NO_ADMIN)
        return

    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.gmute_sql import ungmute
    except AttributeError:
        await un_gmute.edit(NO_SQL)
        return

    user = await get_user_from_event(un_gmute)
    user = user[0]
    if user:
        pass
    else:
        return

    # If pass, inform and start ungmuting
    await un_gmute.edit(f"`{JAVES_NNAME}:` **UnGbaning User !! **")

    if ungmute(user.id) is False:
        await un_gmute.edit(f"`{JAVES_NNAME}:` **Error! User probably not gbanned.**")
    else:    	
        try:
            await un_gmute.client(
                EditBannedRequest(un_gmute.chat_id, user.id, UNBAN_RIGHTS))
        # Inform about success
            await un_gmute.edit(f"`{JAVES_NNAME}:` **Admin {my_username} UnGbanned [{user.first_name}](tg://user?id={user.id})**")
        except UserIdInvalidError:
            return await un_gmute.edit(f"`{JAVES_NNAME}:` ** unGban failed!! ** ")


            if BOTLOG:
              await un_gmute.client.send_message(
                BOTLOG_CHATID, "#UNGBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {un_gmute.chat.title}(`{un_gmute.chat_id}`)")
        

@bot.on(admin_cmd(pattern=f"ungban(?: |$)(.*)", allow_sudo=True))
async def ungmoot(un_gmute):
    """ For .ungmute command, ungmutes the target in the userbot """
    # Admin or creator check
    chat = await un_gmute.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    me = await un_gmute.client.get_me()
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    my_username = f"@{me.username}" if me.username else my_mention

    # If not admin and not creator, return
    if not admin and not creator:
        await un_gmute.reply(NO_ADMIN)
        return

    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.gmute_sql import ungmute
    except AttributeError:
        await un_gmute.reply(NO_SQL)
        return

    user = await get_user_from_event(un_gmute)
    user = user[0]
    if user:
        pass
    else:
        return

    # If pass, inform and start ungmuting
    await un_gmute.reply(f"`{JAVES_NNAME}:` **UnGbaning User !! **")

    if ungmute(user.id) is False:
        await un_gmute.reply(f"`{JAVES_NNAME}:` **Error! User probably not gbanned.**")
    else:    	
        try:
            await un_gmute.client(
                EditBannedRequest(un_gmute.chat_id, user.id, UNBAN_RIGHTS))
        # Inform about success
            await un_gmute.reply(f"`{JAVES_NNAME}:` **Admin {my_username} UnGbanned [{user.first_name}](tg://user?id={user.id})**")
        except UserIdInvalidError:
            return await un_gmute.reply(f"`{JAVES_NNAME}:` ** unGban failed!! ** ")


            if BOTLOG:
              await un_gmute.client.send_message(
                BOTLOG_CHATID, "#UNGBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {un_gmute.chat.title}(`{un_gmute.chat_id}`)")
        



       
@javes05(outgoing=True, disable_errors=True, pattern="^!gban(?: |$)(.*)")
async def gspider(gspdr):
    """ For .gmute command, globally mutes the replied/tagged person """
    # Admin or creator check
    chat = await gspdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    
    # If not admin and not creator, return
    if not admin and not creator:
        await gspdr.edit(NO_ADMIN)
        return

    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.gmute_sql import gmute
    except AttributeError:
        await gspdr.edit(NO_SQL)
        return

    user, reason = await get_user_from_event(gspdr)
    if user:
        pass
    else:
        return

    # If pass, inform and start gmuting
    await gspdr.edit(f"`{JAVES_NNAME}:` **Gbaning User !! **")
    if gmute(user.id) is False:
        await gspdr.edit(
            f"`{JAVES_NNAME}:`**Error! User probably already gmuted.**")
    else:    	
        try:
            await gspdr.client(
                EditBannedRequest(gspdr.chat_id, user.id, BANNED_RIGHTS))
            me = await gspdr.client.get_me()
            my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
            my_username = f"@{me.username}" if me.username else my_mention
            if reason:
               await gspdr.edit(
                     f"`{JAVES_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                     f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `{reason}`")
                     
            else:
                  await gspdr.edit(
                     f"`{JAVES_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                     f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `Private!`")
            if BOTLOG:
                  await gspdr.client.send_message(
                     BOTLOG_CHATID, "#GBAN\n"
                        f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                        f"CHAT: {gspdr.chat.title}(`{gspdr.chat_id}`)")
        except UserIdInvalidError:
            return await gspdr.edit(f"`{JAVES_NNAME}:` ** Gban failed!! ** ")

@bot.on(admin_cmd(pattern=f"gban(?: |$)(.*)", allow_sudo=True))
async def gspider(gspdr):
    """ For .gmute command, globally mutes the replied/tagged person """
    # Admin or creator check
    chat = await gspdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    
    # If not admin and not creator, return
    if not admin and not creator:
        await gspdr.reply(NO_ADMIN)
        return

    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.gmute_sql import gmute
    except AttributeError:
        await gspdr.reply(NO_SQL)
        return

    user, reason = await get_user_from_event(gspdr)
    if user:
        pass
    else:
        return

    # If pass, inform and start gmuting
    await gspdr.reply(f"`{JAVES_NNAME}:` **Gbaning User !! **")
    if gmute(user.id) is False:
        await gspdr.reply(
            f"`{JAVES_NNAME}:`**Error! User probably already gmuted.**")
    else:    	
        try:
            await gspdr.client(
                EditBannedRequest(gspdr.chat_id, user.id, BANNED_RIGHTS))
            me = await gspdr.client.get_me()
            my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
            my_username = f"@{me.username}" if me.username else my_mention
            if reason:
               await gspdr.reply(
                     f"`{JAVES_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                     f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `{reason}`")
                     
            else:
                  await gspdr.reply(
                     f"`{JAVES_NNAME}:` **New Gban !! ** \n" 
                     f"`GbanAdmin`: **{my_username}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"                     
                     f"**Chat** :  `{gspdr.chat.title}`\n"
                     f"**Reason**  : `Private!`")
            if BOTLOG:
                  await gspdr.client.send_message(
                     BOTLOG_CHATID, "#GBAN\n"
                        f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                        f"CHAT: {gspdr.chat.title}(`{gspdr.chat_id}`)")
        except UserIdInvalidError:
            return await gspdr.reply(f"`{JAVES_NNAME}:` ** Gban failed!! ** ")





@javes05(outgoing=True, disable_errors=True, pattern="^\!delusers(?: |$)(.*)", groups_only=True)
async def rm_deletedacc(show):
    """ For .delusers command, list all the ghost/deleted accounts in a chat. """
    if not show.is_group:
        await show.edit(f"`{JAVES_NNAME}:` ** This is not a group.**")
        return
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = f"`{JAVES_NNAME}:` **No deleted accounts found**"

    if con != "clean":
        await show.edit(f"`{JAVES_NNAME}:` ** Searching for deleted accounts...**")
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = f"`{JAVES_NNAME}:` Found **{del_u}** deleted account(s) in this group,\
            \nclean them by using `!delusers clean`"

        await show.edit(del_status)
        return

    # Here laying the sanity check
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await show.edit(f"`{JAVES_NNAME}:` **Sorry,  I can't able to get admin rights here**")
        return

    await show.edit(f"`{JAVES_NNAME}:` ** Removing deleted accounts...**")
    del_u = 0
    del_a = 0

    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS))
            except ChatAdminRequiredError:
                await show.edit(f"`{JAVES_NNAME}:` **Sorry, I don't have ban rights in this group")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(
                EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        del_status = f"`{JAVES_NNAME}`: Cleaned **{del_u}** deleted account(s)"

    if del_a > 0:
        del_status = f"`{JAVES_NNAME}`: Cleaned **{del_u}** deleted account(s) \
        \n**{del_a}** deleted admin accounts are not removed"

    await show.edit(del_status)
    await sleep(2)
    await show.delete()

    if BOTLOG:
        await show.client.send_message(
            BOTLOG_CHATID, "#CLEANUP\n"
            f"Cleaned **{del_u}** deleted account(s) !!\
            \nCHAT: {show.chat.title}(`{show.chat_id}`)")


@bot.on(admin_cmd(pattern=f"delusers(?: |$)(.*)", allow_sudo=True))
async def rm_deletedacc(show):
    """ For .delusers command, list all the ghost/deleted accounts in a chat. """
    if not show.is_group:
        await show.reply(f"`{JAVES_NNAME}:` ** This is not a group.**")
        return
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = f"`{JAVES_NNAME}:` **No deleted accounts found**"

    if con != "clean":
        await show.reply(f"`{JAVES_NNAME}:` ** Searching for deleted accounts...**")
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = f"`{JAVES_NNAME}:` Found **{del_u}** deleted account(s) in this group,\
            \nclean them by using `!delusers clean`"

        await show.reply(del_status)
        return

    # Here laying the sanity check
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await show.reply(f"`{JAVES_NNAME}:` **Sorry,  I can't able to get admin rights here**")
        return

    await show.reply(f"`{JAVES_NNAME}:` ** Removing deleted accounts...**")
    del_u = 0
    del_a = 0

    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS))
            except ChatAdminRequiredError:
                await show.reply(f"`{JAVES_NNAME}:` **Sorry, I don't have ban rights in this group")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(
                EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        del_status = f"`{JAVES_NNAME}`: Cleaned **{del_u}** deleted account(s)"

    if del_a > 0:
        del_status = f"`{JAVES_NNAME}`: Cleaned **{del_u}** deleted account(s) \
        \n**{del_a}** deleted admin accounts are not removed"

    await show.reply(del_status)
    await sleep(2)
    await show.delete()

    if BOTLOG:
        await show.client.send_message(
            BOTLOG_CHATID, "#CLEANUP\n"
            f"Cleaned **{del_u}** deleted account(s) !!\
            \nCHAT: {show.chat.title}(`{show.chat_id}`)")

   

    

@javes05(outgoing=True, disable_errors=True, pattern="^\!admins$", groups_only=True)
async def get_admin(show):
    """ For .admins command, list all of the admins of the chat. """
    info = await show.client.get_entity(show.chat_id)
    title = info.title if info.title else "this chat"
    mentions = f'<b>Admins in {title}:</b> \n'
    try:
        async for user in show.client.iter_participants(
                show.chat_id, filter=ChannelParticipantsAdmins):
            if not user.deleted:
                link = f"<a href=\"tg://user?id={user.id}\">{user.first_name}</a>"
                userid = f"<code>{user.id}</code>"
                mentions += f"\n{link} {userid}"
            else:
                mentions += f"\nDeleted Account <code>{user.id}</code>"
    except ChatAdminRequiredError as err:
        mentions += " " + str(err) + "\n"
    try:
        await show.edit(mentions, parse_mode="html")
    except MessageTooLongError:
        await show.edit(
            f"`{JAVES_NNAME}`: **Too many admins here. Uploading admin list as file**")
        file = open("adminlist.txt", "w+")
        file.write(mentions)
        file.close()
        await show.client.send_file(
            show.chat_id,
            "adminlist.txt",
            caption='Admins in {}'.format(title),
            reply_to=show.id,
        )
        remove("adminlist.txt")


@bot.on(admin_cmd(pattern=f"admins$", allow_sudo=True))
async def get_admin(show):
    """ For .admins command, list all of the admins of the chat. """
    info = await show.client.get_entity(show.chat_id)
    title = info.title if info.title else "this chat"
    mentions = f'<b>Admins in {title}:</b> \n'
    try:
        async for user in show.client.iter_participants(
                show.chat_id, filter=ChannelParticipantsAdmins):
            if not user.deleted:
                link = f"<a href=\"tg://user?id={user.id}\">{user.first_name}</a>"
                userid = f"<code>{user.id}</code>"
                mentions += f"\n{link} {userid}"
            else:
                mentions += f"\nDeleted Account <code>{user.id}</code>"
    except ChatAdminRequiredError as err:
        mentions += " " + str(err) + "\n"
    try:
        await show.reply(mentions, parse_mode="html")
    except MessageTooLongError:
        await show.reply(
            f"`{JAVES_NNAME}`: **Too many admins here. Uploading admin list as file**")
        file = open("adminlist.txt", "w+")
        file.write(mentions)
        file.close()
        await show.client.send_file(
            show.chat_id,
            "adminlist.txt",
            caption='Admins in {}'.format(title),
            reply_to=show.id,
        )
        remove("adminlist.txt")




@javes05(outgoing=True, disable_errors=True, pattern="^\!bots$", groups_only=True)
async def get_bots(show):
    """ For .bots command, list all of the bots of the chat. """
    info = await show.client.get_entity(show.chat_id)
    title = info.title if info.title else "this chat"
    mentions = f'<b>Bots in {title}:</b>\n'
    try:
        if isinstance(show.to_id, PeerChat):
            await show.edit("`I heard that only Supergroups can have bots.`")
            return
        else:
            async for user in show.client.iter_participants(
                    show.chat_id, filter=ChannelParticipantsBots):
                if not user.deleted:
                    link = f"<a href=\"tg://user?id={user.id}\">{user.first_name}</a>"
                    userid = f"<code>{user.id}</code>"
                    mentions += f"\n{link} {userid}"
                else:
                    mentions += f"\nDeleted Bot <code>{user.id}</code>"
    except ChatAdminRequiredError as err:
        mentions += " " + str(err) + "\n"
    try:
        await show.edit(mentions, parse_mode="html")
    except MessageTooLongError:
        await show.edit(
            f"`{JAVES_NNAME}`: ** Too many bots here. Uploading bots list as file.**")
        file = open("botlist.txt", "w+")
        file.write(mentions)
        file.close()
        await show.client.send_file(
            show.chat_id,
            "botlist.txt",
            caption='Bots in {}'.format(title),
            reply_to=show.id,
        )
        remove("botlist.txt")

@bot.on(admin_cmd(pattern=f"bots$", allow_sudo=True))
async def get_bots(show):
    """ For .bots command, list all of the bots of the chat. """
    info = await show.client.get_entity(show.chat_id)
    title = info.title if info.title else "this chat"
    mentions = f'<b>Bots in {title}:</b>\n'
    try:
        if isinstance(show.to_id, PeerChat):
            await show.reply("`I heard that only Supergroups can have bots.`")
            return
        else:
            async for user in show.client.iter_participants(
                    show.chat_id, filter=ChannelParticipantsBots):
                if not user.deleted:
                    link = f"<a href=\"tg://user?id={user.id}\">{user.first_name}</a>"
                    userid = f"<code>{user.id}</code>"
                    mentions += f"\n{link} {userid}"
                else:
                    mentions += f"\nDeleted Bot <code>{user.id}</code>"
    except ChatAdminRequiredError as err:
        mentions += " " + str(err) + "\n"
    try:
        await show.reply(mentions, parse_mode="html")
    except MessageTooLongError:
        await show.reply(
            f"`{JAVES_NNAME}`: ** Too many bots here. Uploading bots list as file.**")
        file = open("botlist.txt", "w+")
        file.write(mentions)
        file.close()
        await show.client.send_file(
            show.chat_id,
            "botlist.txt",
            caption='Bots in {}'.format(title),
            reply_to=show.id,
        )
        remove("botlist.txt")




@javes05(outgoing=True, disable_errors=True, pattern="^\!pin(?: |$)(.*)", groups_only=True)
async def pin(msg):
    """ For .pin command, pins the replied/tagged message on the top the chat. """
    # Admin or creator check
    chat = await msg.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await msg.edit(NO_ADMIN)
        return

    to_pin = msg.reply_to_msg_id

    if not to_pin:
        await msg.edit(f"`{JAVES_NNAME}`: ** Reply to a message to pin it.**")
        return

    options = msg.pattern_match.group(1)

    is_silent = True

    if options.lower() == "loud":
        is_silent = False

    try:
        await msg.client(
            UpdatePinnedMessageRequest(msg.to_id, to_pin, is_silent))
    except BadRequestError:
        await msg.edit(NO_PERM)
        return

    await msg.edit(f"`{JAVES_NNAME}`: ** Pinned Successfully in {msg.chat.title}!**")

    user = await get_user_from_id(msg.from_id, msg)

    if BOTLOG:
        await msg.client.send_message(
            BOTLOG_CHATID, "#PIN\n"
            f"ADMIN: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {msg.chat.title}(`{msg.chat_id}`)\n"
            f"LOUD: {not is_silent}")


@bot.on(admin_cmd(pattern=f"pin(?: |$)(.*)", allow_sudo=True))
async def pin(msg):
    """ For .pin command, pins the replied/tagged message on the top the chat. """
    # Admin or creator check
    chat = await msg.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await msg.reply(NO_ADMIN)
        return

    to_pin = msg.reply_to_msg_id

    if not to_pin:
        await msg.reply(f"`{JAVES_NNAME}`: ** Reply to a message to pin it.**")
        return

    options = msg.pattern_match.group(1)

    is_silent = True

    if options.lower() == "loud":
        is_silent = False

    try:
        await msg.client(
            UpdatePinnedMessageRequest(msg.to_id, to_pin, is_silent))
    except BadRequestError:
        await msg.reply(NO_PERM)
        return

    await msg.reply(f"`{JAVES_NNAME}`: ** Pinned Successfully in {msg.chat.title}!**")

    user = await get_user_from_id(msg.from_id, msg)

    if BOTLOG:
        await msg.client.send_message(
            BOTLOG_CHATID, "#PIN\n"
            f"ADMIN: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {msg.chat.title}(`{msg.chat_id}`)\n"
            f"LOUD: {not is_silent}")





@javes05(outgoing=True, disable_errors=True, pattern="^\!kick(?: |$)(.*)", groups_only=True)
async def kick(usr):
    """ For .kick command, kicks the replied/tagged person from the group. """
    # Admin or creator check
    chat = await usr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await usr.edit(NO_ADMIN)
        return

    user, reason = await get_user_from_event(usr)
    if not user:
        await usr.edit(f"`{JAVES_NNAME}`: ** Couldn't fetch user.**")
        return

    await usr.edit(f"`{JAVES_NNAME}`: ** Kicking User**")

    try:
        await usr.client.kick_participant(usr.chat_id, user.id)
        await sleep(.5)
    except Exception as e:
        await usr.edit(NO_PERM)
        return

    if reason:
        await usr.edit(
            f"`{JAVES_NNAME}`: Kicked [{user.first_name}](tg://user?id={user.id})!\nReason: {reason}"
        )
    else:
        await usr.edit(
            f"`{JAVES_NNAME}`: Kicked [{user.first_name}](tg://user?id={user.id})!")

    if BOTLOG:
        await usr.client.send_message(
            BOTLOG_CHATID, "#KICK\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {usr.chat.title}(`{usr.chat_id}`)\n")


@bot.on(admin_cmd(pattern=f"kick(?: |$)(.*)", allow_sudo=True))
async def kick(usr):
    """ For .kick command, kicks the replied/tagged person from the group. """
    # Admin or creator check
    chat = await usr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await usr.reply(NO_ADMIN)
        return

    user, reason = await get_user_from_event(usr)
    if not user:
        await usr.reply(f"`{JAVES_NNAME}`: ** Couldn't fetch user.**")
        return

    await usr.reply(f"`{JAVES_NNAME}`: ** Kicking User**")

    try:
        await usr.client.kick_participant(usr.chat_id, user.id)
        await sleep(.5)
    except Exception as e:
        await usr.reply(NO_PERM)
        return

    if reason:
        await usr.reply(
            f"`{JAVES_NNAME}`: Kicked [{user.first_name}](tg://user?id={user.id})!\nReason: {reason}"
        )
    else:
        await usr.reply(
            f"`{JAVES_NNAME}`: Kicked [{user.first_name}](tg://user?id={user.id})!")

    if BOTLOG:
        await usr.client.send_message(
            BOTLOG_CHATID, "#KICK\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {usr.chat.title}(`{usr.chat_id}`)\n")






@javes05(outgoing=True, disable_errors=True, pattern="^\!users ?(.*)", groups_only=True)
async def get_users(show):
    """ For .users command, list all of the users in a chat. """
    info = await show.client.get_entity(show.chat_id)
    title = info.title if info.title else "this chat"
    mentions = 'Users in {}: \n'.format(title)
    try:
        if not show.pattern_match.group(1):
            async for user in show.client.iter_participants(show.chat_id):
                if not user.deleted:
                    mentions += f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
                else:
                    mentions += f"\nDeleted Account `{user.id}`"
        else:
            searchq = show.pattern_match.group(1)
            async for user in show.client.iter_participants(
                    show.chat_id, search=f'{searchq}'):
                if not user.deleted:
                    mentions += f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
                else:
                    mentions += f"\nDeleted Account `{user.id}`"
    except ChatAdminRequiredError as err:
        mentions += " " + str(err) + "\n"
    try:
        await show.edit(mentions)
    except MessageTooLongError:
        await show.edit(
            f"`{JAVES_NNAME}`: ** This is a huge group. Uploading users lists as file.")
        file = open("userslist.txt", "w+")
        file.write(mentions)
        file.close()
        await show.client.send_file(
            show.chat_id,
            "userslist.txt",
            caption='Users in {}'.format(title),
            reply_to=show.id,
        )
        remove("userslist.txt")


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]

        if user.isnumeric():
            user = int(user)

        if not user:
            await event.edit(f"`{JAVES_NNAME}`: ** Pass the user's username, id or reply!**")
            return

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj


@bot.on(admin_cmd(pattern=f"users ?(.*)", allow_sudo=True))
async def get_users(show):
    """ For .users command, list all of the users in a chat. """
    info = await show.client.get_entity(show.chat_id)
    title = info.title if info.title else "this chat"
    mentions = 'Users in {}: \n'.format(title)
    try:
        if not show.pattern_match.group(1):
            async for user in show.client.iter_participants(show.chat_id):
                if not user.deleted:
                    mentions += f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
                else:
                    mentions += f"\nDeleted Account `{user.id}`"
        else:
            searchq = show.pattern_match.group(1)
            async for user in show.client.iter_participants(
                    show.chat_id, search=f'{searchq}'):
                if not user.deleted:
                    mentions += f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
                else:
                    mentions += f"\nDeleted Account `{user.id}`"
    except ChatAdminRequiredError as err:
        mentions += " " + str(err) + "\n"
    try:
        await show.reply(mentions)
    except MessageTooLongError:
        await show.reply(
            f"`{JAVES_NNAME}`: ** This is a huge group. Uploading users lists as file.")
        file = open("userslist.txt", "w+")
        file.write(mentions)
        file.close()
        await show.client.send_file(
            show.chat_id,
            "userslist.txt",
            caption='Users in {}'.format(title),
            reply_to=show.id,
        )
        remove("userslist.txt")


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]

        if user.isnumeric():
            user = int(user)

        if not user:
            await event.reply(f"`{JAVES_NNAME}`: ** Pass the user's username, id or reply!**")
            return

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.reply(str(err))
            return None

    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.reply(str(err))
        return None

    return user_obj







@javes05(outgoing=True, disable_errors=True, pattern="^\!savefilter2 (\w*)")
async def add_new_filter(new_handler):
    """ For .filter command, allows adding new filters in a chat """
    try:
        from userbot.modules.sql_helper.filter_sql import add_filter
    except AttributeError:
        await new_handler.edit("`Running on Non-SQL mode!`")
        return
    keyword = new_handler.pattern_match.group(1)
    string = new_handler.text.partition(keyword)[2]
    msg = await new_handler.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await new_handler.client.send_message(
                BOTLOG_CHATID, f"#FILTER\
            \nCHAT ID: {new_handler.chat_id}\
            \nTRIGGER: {keyword}\
            \n\nThe following message is saved as the filter's reply data for the chat, please do NOT delete it !!"
            )
            msg_o = await new_handler.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=new_handler.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            await new_handler.edit(
                f"`{JAVES_NNAME}`: ** Saving media as reply to the filter requires the BOTLOG_CHATID to be set.**"
            )
            return
    elif new_handler.reply_to_msg_id and not string:
        rep_msg = await new_handler.get_reply_message()
        string = rep_msg.text
    success = " `Filter` **{}** `{} successfully`"
    if add_filter(str(new_handler.chat_id), keyword, string, msg_id) is True:
        await new_handler.edit(success.format(keyword, 'added'))
    else:
        await new_handler.edit(success.format(keyword, 'updated'))



@bot.on(admin_cmd(pattern=f"savefilter2 (\w*)", allow_sudo=True))
async def add_new_filter(new_handler):
    """ For .filter command, allows adding new filters in a chat """
    try:
        from userbot.modules.sql_helper.filter_sql import add_filter
    except AttributeError:
        await new_handler.reply("`Running on Non-SQL mode!`")
        return
    keyword = new_handler.pattern_match.group(1)
    string = new_handler.text.partition(keyword)[2]
    msg = await new_handler.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await new_handler.client.send_message(
                BOTLOG_CHATID, f"#FILTER\
            \nCHAT ID: {new_handler.chat_id}\
            \nTRIGGER: {keyword}\
            \n\nThe following message is saved as the filter's reply data for the chat, please do NOT delete it !!"
            )
            msg_o = await new_handler.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=new_handler.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            await new_handler.reply(
                f"`{JAVES_NNAME}`: ** Saving media as reply to the filter requires the BOTLOG_CHATID to be set.**"
            )
            return
    elif new_handler.reply_to_msg_id and not string:
        rep_msg = await new_handler.get_reply_message()
        string = rep_msg.text
    success = " `Filter` **{}** `{} successfully`"
    if add_filter(str(new_handler.chat_id), keyword, string, msg_id) is True:
        await new_handler.reply(success.format(keyword, 'added'))
    else:
        await new_handler.reply(success.format(keyword, 'updated'))







@javes05(outgoing=True, disable_errors=True, pattern="^\!clearfilter2 (\w*)")
async def remove_a_filter(r_handler):
    """ For .stop command, allows you to remove a filter from a chat. """
    try:
        from userbot.modules.sql_helper.filter_sql import remove_filter
    except AttributeError:
        await r_handler.edit("`Running on Non-SQL mode!`")
        return
    filt = r_handler.pattern_match.group(1)
    if not remove_filter(r_handler.chat_id, filt):
        await r_handler.edit("`Filter` **{}** `doesn't exist.`".format(filt))
    else:
        await r_handler.edit(
            "`Filter` **{}** `was deleted successfully`".format(filt))


@bot.on(admin_cmd(pattern=f"clearfilter2 ?(.*)", allow_sudo=True))
async def remove_a_filter(r_handler):
    """ For .stop command, allows you to remove a filter from a chat. """
    try:
        from userbot.modules.sql_helper.filter_sql import remove_filter
    except AttributeError:
        await r_handler.reply("`Running on Non-SQL mode!`")
        return
    filt = r_handler.pattern_match.group(1)
    if not remove_filter(r_handler.chat_id, filt):
        await r_handler.reply("`Filter` **{}** `doesn't exist.`".format(filt))
    else:
        await r_handler.reply(
            "`Filter` **{}** `was deleted successfully`".format(filt))



@javes05(outgoing=True, disable_errors=True, pattern="^\!checkfilter2$")
async def filters_active(event):
    """ For .filters command, lists all of the active filters in a chat. """
    try:
        from userbot.modules.sql_helper.filter_sql import get_filters
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    transact = f"`{JAVES_NNAME}`: ** There are no filters in this chat.**"
    filters = get_filters(event.chat_id)
    for filt in filters:
        if transact == "`There are no filters in this chat.`":
            transact = "Active filters in this chat:\n"
            transact += "`{}`\n".format(filt.keyword)
        else:
            transact += "`{}`\n".format(filt.keyword)

    await event.edit(transact)


@bot.on(admin_cmd(pattern=f"checkfilter2$", allow_sudo=True))
async def filters_active(event):
    """ For .filters command, lists all of the active filters in a chat. """
    try:
        from userbot.modules.sql_helper.filter_sql import get_filters
    except AttributeError:
        await event.reply("`Running on Non-SQL mode!`")
        return
    transact = f"`{JAVES_NNAME}`: ** There are no filters in this chat.**"
    filters = get_filters(event.chat_id)
    for filt in filters:
        if transact == "`There are no filters in this chat.`":
            transact = "Active filters in this chat:\n"
            transact += "`{}`\n".format(filt.keyword)
        else:
            transact += "`{}`\n".format(filt.keyword)

    await event.reply(transact)






@javes05(pattern="!chatinfo(?: |$)(.*)", outgoing=True)
async def info(event):
    await event.edit("`Analysing the chat...`")
    chat = await get_chatinfo(event)
    caption = await fetch_info(chat, event)
    try:
        await event.edit(caption, parse_mode="html")
    except Exception as e:
        print("Exception:", e)
        await event.edit("`An unexpected error has occurred.`")
    return


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.edit("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.edit("`This is a private channel/group or I am banned from there`")
            return None
        except ChannelPublicGroupNaError:
            await event.edit("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return chat_info


async def fetch_info(chat, event):
    # chat.chats is a list so we use get_entity() to avoid IndexError
    chat_obj_info = await event.client.get_entity(chat.full_chat.id)
    broadcast = chat_obj_info.broadcast if hasattr(chat_obj_info, "broadcast") else False
    chat_type = "Channel" if broadcast else "Group"
    chat_title = chat_obj_info.title
    warn_emoji = emojize(":warning:")
    try:
        msg_info = await event.client(GetHistoryRequest(peer=chat_obj_info.id, offset_id=0, offset_date=datetime(2010, 1, 1), 
                                                        add_offset=-1, limit=1, max_id=0, min_id=0, hash=0))
    except Exception as e:
        msg_info = None
        print("Exception:", e)
    # No chance for IndexError as it checks for msg_info.messages first
    first_msg_valid = True if msg_info and msg_info.messages and msg_info.messages[0].id == 1 else False
    # Same for msg_info.users
    creator_valid = True if first_msg_valid and msg_info.users else False
    creator_id = msg_info.users[0].id if creator_valid else None
    creator_firstname = msg_info.users[0].first_name if creator_valid and msg_info.users[0].first_name is not None else "Deleted Account"
    creator_username = msg_info.users[0].username if creator_valid and msg_info.users[0].username is not None else None
    created = msg_info.messages[0].date if first_msg_valid else None
    former_title = msg_info.messages[0].action.title if first_msg_valid and type(msg_info.messages[0].action) is MessageActionChannelMigrateFrom and msg_info.messages[0].action.title != chat_title else None
    try:
        dc_id, location = get_input_location(chat.full_chat.chat_photo)
    except Exception as e:
        dc_id = "Unknown"
        location = str(e)
    
    #this is some spaghetti I need to change
    description = chat.full_chat.about
    members = chat.full_chat.participants_count if hasattr(chat.full_chat, "participants_count") else chat_obj_info.participants_count
    admins = chat.full_chat.admins_count if hasattr(chat.full_chat, "admins_count") else None
    banned_users = chat.full_chat.kicked_count if hasattr(chat.full_chat, "kicked_count") else None
    restrcited_users = chat.full_chat.banned_count if hasattr(chat.full_chat, "banned_count") else None
    members_online = chat.full_chat.online_count if hasattr(chat.full_chat, "online_count") else 0
    group_stickers = chat.full_chat.stickerset.title if hasattr(chat.full_chat, "stickerset") and chat.full_chat.stickerset else None
    messages_viewable = msg_info.count if msg_info else None
    messages_sent = chat.full_chat.read_inbox_max_id if hasattr(chat.full_chat, "read_inbox_max_id") else None
    messages_sent_alt = chat.full_chat.read_outbox_max_id if hasattr(chat.full_chat, "read_outbox_max_id") else None
    exp_count = chat.full_chat.pts if hasattr(chat.full_chat, "pts") else None
    username = chat_obj_info.username if hasattr(chat_obj_info, "username") else None
    bots_list = chat.full_chat.bot_info  # this is a list
    bots = 0
    supergroup = "<b>Yes</b>" if hasattr(chat_obj_info, "megagroup") and chat_obj_info.megagroup else "No"
    slowmode = "<b>Yes</b>" if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled else "No"
    slowmode_time = chat.full_chat.slowmode_seconds if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled else None
    restricted = "<b>Yes</b>" if hasattr(chat_obj_info, "restricted") and chat_obj_info.restricted else "No"
    verified = "<b>Yes</b>" if hasattr(chat_obj_info, "verified") and chat_obj_info.verified else "No"
    username = "@{}".format(username) if username else None
    creator_username = "@{}".format(creator_username) if creator_username else None
    #end of spaghetti block
    
    if admins is None:
        # use this alternative way if chat.full_chat.admins_count is None, works even without being an admin
        try:
            participants_admins = await event.client(GetParticipantsRequest(channel=chat.full_chat.id, filter=ChannelParticipantsAdmins(),
                                                                            offset=0, limit=0, hash=0))
            admins = participants_admins.count if participants_admins else None
        except Exception as e:
            print("Exception:", e)
    if bots_list:
        for bot in bots_list:
            bots += 1

    caption = "<b>CHAT INFO:</b>\n"
    caption += f"ID: <code>{chat_obj_info.id}</code>\n"
    if chat_title is not None:
        caption += f"{chat_type} name: {chat_title}\n"
    if former_title is not None:  # Meant is the very first title
        caption += f"Former name: {former_title}\n"
    if username is not None:
        caption += f"{chat_type} type: Public\n"
        caption += f"Link: {username}\n"
    else:
        caption += f"{chat_type} type: Private\n"
    if creator_username is not None:
        caption += f"Creator: {creator_username}\n"
    elif creator_valid:
        caption += f"Creator: <a href=\"tg://user?id={creator_id}\">{creator_firstname}</a>\n"
    if created is not None:
        caption += f"Created: <code>{created.date().strftime('%b %d, %Y')} - {created.time()}</code>\n"
    else:
        caption += f"Created: <code>{chat_obj_info.date.date().strftime('%b %d, %Y')} - {chat_obj_info.date.time()}</code> {warn_emoji}\n"
    caption += f"Data Centre ID: {dc_id}\n"
    if exp_count is not None:
        chat_level = int((1+sqrt(1+7*exp_count/14))/2)
        caption += f"{chat_type} level: <code>{chat_level}</code>\n"
    if messages_viewable is not None:
        caption += f"Viewable messages: <code>{messages_viewable}</code>\n"
    if messages_sent:
        caption += f"Messages sent: <code>{messages_sent}</code>\n"
    elif messages_sent_alt:
        caption += f"Messages sent: <code>{messages_sent_alt}</code> {warn_emoji}\n"
    if members is not None:
        caption += f"Members: <code>{members}</code>\n"
    if admins is not None:
        caption += f"Administrators: <code>{admins}</code>\n"
    if bots_list:
        caption += f"Bots: <code>{bots}</code>\n"
    if members_online:
        caption += f"Currently online: <code>{members_online}</code>\n"
    if restrcited_users is not None:
        caption += f"Restricted users: <code>{restrcited_users}</code>\n"
    if banned_users is not None:
        caption += f"Banned users: <code>{banned_users}</code>\n"
    if group_stickers is not None:
        caption += f"{chat_type} stickers: <a href=\"t.me/addstickers/{chat.full_chat.stickerset.short_name}\">{group_stickers}</a>\n"
    caption += "\n"
    if not broadcast:
        caption += f"Slow mode: {slowmode}"
        if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled:
            caption += f", <code>{slowmode_time}s</code>\n\n"
        else:
            caption += "\n\n"
    if not broadcast:
        caption += f"Supergroup: {supergroup}\n\n"
    if hasattr(chat_obj_info, "restricted"):
        caption += f"Restricted: {restricted}\n"
        if chat_obj_info.restricted:
            caption += f"> Platform: {chat_obj_info.restriction_reason[0].platform}\n"
            caption += f"> Reason: {chat_obj_info.restriction_reason[0].reason}\n"
            caption += f"> Text: {chat_obj_info.restriction_reason[0].text}\n\n"
        else:
            caption += "\n"
    if hasattr(chat_obj_info, "scam") and chat_obj_info.scam:
    	caption += "Scam: <b>Yes</b>\n\n"
    if hasattr(chat_obj_info, "verified"):
        caption += f"Verified by Telegram: {verified}\n\n"
    if description:
        caption += f"Description: \n<code>{description}</code>\n"
    return caption




@bot.on(admin_cmd(pattern=f"chatinfo(?: |$)(.*)", allow_sudo=True))
async def info(event):
    await event.reply("`Analysing the chat...`")
    chat = await get_chatinfo(event)
    caption = await fetch_info(chat, event)
    try:
        await event.reply(caption, parse_mode="html")
    except Exception as e:
        print("Exception:", e)
        await event.reply("`An unexpected error has occurred.`")
    return


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply("`This is a private channel/group or I am banned from there`")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError) as err:
            await event.reply(str(err))
            return None
    return chat_info


async def fetch_info(chat, event):
    # chat.chats is a list so we use get_entity() to avoid IndexError
    chat_obj_info = await event.client.get_entity(chat.full_chat.id)
    broadcast = chat_obj_info.broadcast if hasattr(chat_obj_info, "broadcast") else False
    chat_type = "Channel" if broadcast else "Group"
    chat_title = chat_obj_info.title
    warn_emoji = emojize(":warning:")
    try:
        msg_info = await event.client(GetHistoryRequest(peer=chat_obj_info.id, offset_id=0, offset_date=datetime(2010, 1, 1), 
                                                        add_offset=-1, limit=1, max_id=0, min_id=0, hash=0))
    except Exception as e:
        msg_info = None
        print("Exception:", e)
    # No chance for IndexError as it checks for msg_info.messages first
    first_msg_valid = True if msg_info and msg_info.messages and msg_info.messages[0].id == 1 else False
    # Same for msg_info.users
    creator_valid = True if first_msg_valid and msg_info.users else False
    creator_id = msg_info.users[0].id if creator_valid else None
    creator_firstname = msg_info.users[0].first_name if creator_valid and msg_info.users[0].first_name is not None else "Deleted Account"
    creator_username = msg_info.users[0].username if creator_valid and msg_info.users[0].username is not None else None
    created = msg_info.messages[0].date if first_msg_valid else None
    former_title = msg_info.messages[0].action.title if first_msg_valid and type(msg_info.messages[0].action) is MessageActionChannelMigrateFrom and msg_info.messages[0].action.title != chat_title else None
    try:
        dc_id, location = get_input_location(chat.full_chat.chat_photo)
    except Exception as e:
        dc_id = "Unknown"
        location = str(e)
    
    #this is some spaghetti I need to change
    description = chat.full_chat.about
    members = chat.full_chat.participants_count if hasattr(chat.full_chat, "participants_count") else chat_obj_info.participants_count
    admins = chat.full_chat.admins_count if hasattr(chat.full_chat, "admins_count") else None
    banned_users = chat.full_chat.kicked_count if hasattr(chat.full_chat, "kicked_count") else None
    restrcited_users = chat.full_chat.banned_count if hasattr(chat.full_chat, "banned_count") else None
    members_online = chat.full_chat.online_count if hasattr(chat.full_chat, "online_count") else 0
    group_stickers = chat.full_chat.stickerset.title if hasattr(chat.full_chat, "stickerset") and chat.full_chat.stickerset else None
    messages_viewable = msg_info.count if msg_info else None
    messages_sent = chat.full_chat.read_inbox_max_id if hasattr(chat.full_chat, "read_inbox_max_id") else None
    messages_sent_alt = chat.full_chat.read_outbox_max_id if hasattr(chat.full_chat, "read_outbox_max_id") else None
    exp_count = chat.full_chat.pts if hasattr(chat.full_chat, "pts") else None
    username = chat_obj_info.username if hasattr(chat_obj_info, "username") else None
    bots_list = chat.full_chat.bot_info  # this is a list
    bots = 0
    supergroup = "<b>Yes</b>" if hasattr(chat_obj_info, "megagroup") and chat_obj_info.megagroup else "No"
    slowmode = "<b>Yes</b>" if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled else "No"
    slowmode_time = chat.full_chat.slowmode_seconds if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled else None
    restricted = "<b>Yes</b>" if hasattr(chat_obj_info, "restricted") and chat_obj_info.restricted else "No"
    verified = "<b>Yes</b>" if hasattr(chat_obj_info, "verified") and chat_obj_info.verified else "No"
    username = "@{}".format(username) if username else None
    creator_username = "@{}".format(creator_username) if creator_username else None
    #end of spaghetti block
    
    if admins is None:
        # use this alternative way if chat.full_chat.admins_count is None, works even without being an admin
        try:
            participants_admins = await event.client(GetParticipantsRequest(channel=chat.full_chat.id, filter=ChannelParticipantsAdmins(),
                                                                            offset=0, limit=0, hash=0))
            admins = participants_admins.count if participants_admins else None
        except Exception as e:
            print("Exception:", e)
    if bots_list:
        for bot in bots_list:
            bots += 1

    caption = "<b>CHAT INFO:</b>\n"
    caption += f"ID: <code>{chat_obj_info.id}</code>\n"
    if chat_title is not None:
        caption += f"{chat_type} name: {chat_title}\n"
    if former_title is not None:  # Meant is the very first title
        caption += f"Former name: {former_title}\n"
    if username is not None:
        caption += f"{chat_type} type: Public\n"
        caption += f"Link: {username}\n"
    else:
        caption += f"{chat_type} type: Private\n"
    if creator_username is not None:
        caption += f"Creator: {creator_username}\n"
    elif creator_valid:
        caption += f"Creator: <a href=\"tg://user?id={creator_id}\">{creator_firstname}</a>\n"
    if created is not None:
        caption += f"Created: <code>{created.date().strftime('%b %d, %Y')} - {created.time()}</code>\n"
    else:
        caption += f"Created: <code>{chat_obj_info.date.date().strftime('%b %d, %Y')} - {chat_obj_info.date.time()}</code> {warn_emoji}\n"
    caption += f"Data Centre ID: {dc_id}\n"
    if exp_count is not None:
        chat_level = int((1+sqrt(1+7*exp_count/14))/2)
        caption += f"{chat_type} level: <code>{chat_level}</code>\n"
    if messages_viewable is not None:
        caption += f"Viewable messages: <code>{messages_viewable}</code>\n"
    if messages_sent:
        caption += f"Messages sent: <code>{messages_sent}</code>\n"
    elif messages_sent_alt:
        caption += f"Messages sent: <code>{messages_sent_alt}</code> {warn_emoji}\n"
    if members is not None:
        caption += f"Members: <code>{members}</code>\n"
    if admins is not None:
        caption += f"Administrators: <code>{admins}</code>\n"
    if bots_list:
        caption += f"Bots: <code>{bots}</code>\n"
    if members_online:
        caption += f"Currently online: <code>{members_online}</code>\n"
    if restrcited_users is not None:
        caption += f"Restricted users: <code>{restrcited_users}</code>\n"
    if banned_users is not None:
        caption += f"Banned users: <code>{banned_users}</code>\n"
    if group_stickers is not None:
        caption += f"{chat_type} stickers: <a href=\"t.me/addstickers/{chat.full_chat.stickerset.short_name}\">{group_stickers}</a>\n"
    caption += "\n"
    if not broadcast:
        caption += f"Slow mode: {slowmode}"
        if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled:
            caption += f", <code>{slowmode_time}s</code>\n\n"
        else:
            caption += "\n\n"
    if not broadcast:
        caption += f"Supergroup: {supergroup}\n\n"
    if hasattr(chat_obj_info, "restricted"):
        caption += f"Restricted: {restricted}\n"
        if chat_obj_info.restricted:
            caption += f"> Platform: {chat_obj_info.restriction_reason[0].platform}\n"
            caption += f"> Reason: {chat_obj_info.restriction_reason[0].reason}\n"
            caption += f"> Text: {chat_obj_info.restriction_reason[0].text}\n\n"
        else:
            caption += "\n"
    if hasattr(chat_obj_info, "scam") and chat_obj_info.scam:
    	caption += "Scam: <b>Yes</b>\n\n"
    if hasattr(chat_obj_info, "verified"):
        caption += f"Verified by Telegram: {verified}\n\n"
    if description:
        caption += f"Description: \n<code>{description}</code>\n"
    return caption

import userbot.modules.sql_helper.warns_sql as sql







@javes05(outgoing=True, disable_errors=True, pattern="^!warn(?: |$)(.*)")
async def _(event):
 reply_message = await event.get_reply_message()
 idd = reply_message.from_id
 if idd == 710844948:
   await reply_message.reply(f"`{JAVES_NNAME}:` ** He is my master, I can't ** ")
 else:
    if event.fwd_from:
        return
    warn_reason = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    limit, soft_warn = sql.get_warn_setting(event.chat_id)
    num_warns, reasons = sql.warn_user(reply_message.from_id, event.chat_id, warn_reason)
    if num_warns >= limit:
        sql.reset_warns(reply_message.from_id, event.chat_id)
        if soft_warn:
            logger.info("kick user")
            reply = "{} warnings, <u><a href='tg://user?id={}'>user</a></u> has been kicked!".format(limit, reply_message.from_id)
        else:
            logger.info("ban user")
            reply = "{} warnings, <u><a href='tg://user?id={}'>user</a></u> has been banned!".format(limit, reply_message.from_id)
    else:
        reply = "<u><a href='tg://user?id={}'>user</a></u> has {}/{} warnings... watch out!".format(reply_message.from_id, num_warns, limit)
        if warn_reason:
            reply += "\nReason for last warn:\n{}".format(html.escape(warn_reason))
    #
    await event.edit(reply, parse_mode="html")


@bot.on(admin_cmd(pattern=f"warn(?: |$)(.*)", allow_sudo=True))
async def _(event):
 reply_message = await event.get_reply_message()
 idd = reply_message.from_id
 if idd == 710844948:
   await reply_message.reply(f"`{JAVES_NNAME}:` ** He is my master, I can't ** ")
 else:
    if event.fwd_from:
        return
    warn_reason = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    limit, soft_warn = sql.get_warn_setting(event.chat_id)
    num_warns, reasons = sql.warn_user(reply_message.from_id, event.chat_id, warn_reason)
    if num_warns >= limit:
        sql.reset_warns(reply_message.from_id, event.chat_id)
        if soft_warn:
            logger.info("kick user")
            reply = "{} warnings, <u><a href='tg://user?id={}'>user</a></u> has been kicked!".format(limit, reply_message.from_id)
        else:
            logger.info("ban user")
            reply = "{} warnings, <u><a href='tg://user?id={}'>user</a></u> has been banned!".format(limit, reply_message.from_id)
    else:
        reply = "<u><a href='tg://user?id={}'>user</a></u> has {}/{} warnings... watch out!".format(reply_message.from_id, num_warns, limit)
        if warn_reason:
            reply += "\nReason for last warn:\n{}".format(html.escape(warn_reason))
    #
    await event.reply(reply, parse_mode="html")


@javes05(outgoing=True, disable_errors=True, pattern="^!warns(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    result = sql.get_warns(reply_message.from_id, event.chat_id)
    if result and result[0] != 0:
        num_warns, reasons = result
        limit, soft_warn = sql.get_warn_setting(event.chat_id)
        if reasons:
            text = "This user has {}/{} warnings, for the following reasons:".format(num_warns, limit)
            text += "\r\n"
            text += reasons
            await event.edit(text)
        else:
            await event.edit("this user has {} / {} warning, but no reasons for any of them.".format(num_warns, limit))
    else:
        await event.edit("this user hasn't got any warnings!")

@bot.on(admin_cmd(pattern=f"warns(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    result = sql.get_warns(reply_message.from_id, event.chat_id)
    if result and result[0] != 0:
        num_warns, reasons = result
        limit, soft_warn = sql.get_warn_setting(event.chat_id)
        if reasons:
            text = "This user has {}/{} warnings, for the following reasons:".format(num_warns, limit)
            text += "\r\n"
            text += reasons
            await event.edit(text)
        else:
            await event.reply("this user has {} / {} warning, but no reasons for any of them.".format(num_warns, limit))
    else:
        await event.reply("this user hasn't got any warnings!")


@javes05(outgoing=True, disable_errors=True, pattern="^!resetwarns(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    sql.reset_warns(reply_message.from_id, event.chat_id)
    await event.edit("Warnings have been reset!")


@bot.on(admin_cmd(pattern=f"resetwarns(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    sql.reset_warns(reply_message.from_id, event.chat_id)
    await event.reply("Warnings have been reset!")







@javes05(outgoing=True, disable_errors=True, pattern="^!invite(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await event.edit(f"**{JAVES_NNAME}:** invite  users to a chat, not to a Private Message")
    else:
        if not event.is_channel and event.is_group:
            # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
            for user_id in to_add_users.split(" "):
                try:
                    await event.client(functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id,
                        user_id=user_id,
                        fwd_limit=1000000
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.edit(f"**{JAVES_NNAME}:** Invited Successfully")
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split(" "):
                try:
                    await event.client(functions.channels.InviteToChannelRequest(
                        channel=event.chat_id,
                        users=[user_id]
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.edit(f"**{JAVES_NNAME}:** Invited Successfully")

@bot.on(admin_cmd(pattern=f"invite(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await event.reply(f"**{JAVES_NNAME}:** invite  users to a chat, not to a Private Message")
    else:
        if not event.is_channel and event.is_group:
            # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
            for user_id in to_add_users.split(" "):
                try:
                    await event.client(functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id,
                        user_id=user_id,
                        fwd_limit=1000000
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.reply(f"**{JAVES_NNAME}:** Invite request sent telethon Successfully")
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split(" "):
                try:
                    await event.client(functions.channels.InviteToChannelRequest(
                        channel=event.chat_id,
                        users=[user_id]
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.reply(f"**{JAVES_NNAME}:** Invite request sent telethon Successfully")




@javes05(outgoing=True, disable_errors=True, pattern="^!savefilter ?(.*)")
async def on_snip_save(event):
    name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if msg:
        snip = {'type': TYPE_TEXT, 'text': msg.message or ''}
        if msg.media:
            media = None
            if isinstance(msg.media, types.MessageMediaPhoto):
                media = utils.get_input_photo(msg.media.photo)
                snip['type'] = TYPE_PHOTO
            elif isinstance(msg.media, types.MessageMediaDocument):
                media = utils.get_input_document(msg.media.document)
                snip['type'] = TYPE_DOCUMENT
            if media:
                snip['id'] = media.id
                snip['hash'] = media.access_hash
                snip['fr'] = media.file_reference
        add_filter(event.chat_id, name, snip['text'], snip['type'], snip.get('id'), snip.get('hash'), snip.get('fr'))
        await event.edit(f"`{JAVES_NNAME}`: filter {name} saved successfully. Get it with {name}")
    else:
        await event.edit(f"`{JAVES_NNAME}`: **Reply to a message with `!savefilter keyword` to save the filter**")


@bot.on(admin_cmd(pattern=f"savefilter (.*)", allow_sudo=True))
async def on_snip_save(event):
    name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if msg:
        snip = {'type': TYPE_TEXT, 'text': msg.message or ''}
        if msg.media:
            media = None
            if isinstance(msg.media, types.MessageMediaPhoto):
                media = utils.get_input_photo(msg.media.photo)
                snip['type'] = TYPE_PHOTO
            elif isinstance(msg.media, types.MessageMediaDocument):
                media = utils.get_input_document(msg.media.document)
                snip['type'] = TYPE_DOCUMENT
            if media:
                snip['id'] = media.id
                snip['hash'] = media.access_hash
                snip['fr'] = media.file_reference
        add_filter(event.chat_id, name, snip['text'], snip['type'], snip.get('id'), snip.get('hash'), snip.get('fr'))
        await event.reply(f"`{JAVES_NNAME}`: filter {name} saved successfully. Get it with {name}")
    else:
        await event.reply(f"`{JAVES_NNAME}`: **Reply to a message with `.savefilter keyword` to save the filter**")


@javes05(outgoing=True, disable_errors=True, pattern="^\!checkfilter$")
async def on_snip_list(event):
    all_snips = get_all_rkfilters(event.chat_id)
    OUT_STR = f"`{JAVES_NNAME}`: Available filters in the Current Chat:\n"
    if len(all_snips) > 0:
        for a_snip in all_snips:
            OUT_STR += f"~> {a_snip.keyword} \n"
    else:
        OUT_STR = f"`{JAVES_NNAME}`: No filters. Start Saving using `!savefilter`"
    if len(OUT_STR) > 4096:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "filters.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=f"`{JAVES_NNAME}`: **Available filters in the Current Chat**",
                reply_to=event
            )
            await event.delete()
    else:
        await event.edit(OUT_STR)

@bot.on(admin_cmd(pattern=f"checkfilter$", allow_sudo=True))
async def on_snip_list(event):
    all_snips = get_all_rkfilters(event.chat_id)
    OUT_STR = f"`{JAVES_NNAME}`: Available filters in the Current Chat:\n"
    if len(all_snips) > 0:
        for a_snip in all_snips:
            OUT_STR += f"~> {a_snip.keyword} \n"
    else:
        OUT_STR = f"`{JAVES_NNAME}`: No filters. Start Saving using `.savefilter`"
    if len(OUT_STR) > 4096:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "filters.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=f"`{JAVES_NNAME}`: **Available filters in the Current Chat**",
                reply_to=event
            )
            await event.delete()
    else:
        await event.reply(OUT_STR)


@javes05(outgoing=True, disable_errors=True, pattern="^\!clearfilter (\w*)")
async def on_snip_delete(event):
    name = event.pattern_match.group(1)
    remove_filter(event.chat_id, name)
    await event.edit(f"`{JAVES_NNAME}`: filter {name} deleted successfully")

@bot.on(admin_cmd(pattern=f"clearfilter (.*)", allow_sudo=True))
async def on_snip_delete(event):
    name = event.pattern_match.group(1)
    remove_filter(event.chat_id, name)
    await event.edit(f"`{JAVES_NNAME}`: filter {name} deleted successfully")




@javes05(outgoing=True, disable_errors=True, pattern="^\!clearallfilter$")
async def on_all_snip_delete(event):
    remove_all_rkfilters(event.chat_id)
    await event.edit(f"`{JAVES_NNAME}`: filters **in current chat** deleted successfully")




@bot.on(admin_cmd(pattern=f"clearallfilter$", allow_sudo=True))
async def on_all_snip_delete(event):
    remove_all_rkfilters(event.chat_id)
    await event.reply(f"`{JAVES_NNAME}`: filters **in current chat** deleted successfully")

import asyncio
import re
import userbot.modules.sql_helper.blacklist_sql as sql
from telethon import events, utils
from telethon.tl import types, functions



@bot.on(events.NewMessage(incoming=True))
async def on_new_message(event):
    # TODO: exempt admins from locks
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    for snip in snips:
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception as e:
                await event.reply("I do not have DELETE permission in this chat")
                sql.rm_from_blacklist(event.chat_id, snip.lower())
            break


@javes05(outgoing=True, pattern="^!addblacklist ((.|\n)*)")       
async def on_add_black_list(event):
    text = event.pattern_match.group(1)
    to_blacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
    for trigger in to_blacklist:
        sql.add_to_blacklist(event.chat_id, trigger.lower())
    await event.edit("Added {} triggers to the blacklist in the current chat".format(len(to_blacklist)))



@bot.on(admin_cmd(pattern=f"saveblacklist ((.|\n)*)", allow_sudo=True))
async def on_add_black_list(event):
    text = event.pattern_match.group(1)
    to_blacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
    for trigger in to_blacklist:
        sql.add_to_blacklist(event.chat_id, trigger.lower())
    await event.reply("Added {} triggers to the blacklist in the current chat".format(len(to_blacklist)))

@javes05(outgoing=True, pattern="^!checkblacklist(?: |$)(.*)")
async def on_view_blacklist(listbl):
    all_blacklisted = sql.get_chat_blacklist(listbl.chat_id)
    OUT_STR = "Blacklists in the Current Chat:\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"`{trigger}`\n"
    else:
        OUT_STR = "`There are no blacklist in current chat.`"
    if len(OUT_STR) > 4096:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "blacklist.text"
            await listbl.client.send_file(
                listbl.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="BlackLists in the Current Chat",
                reply_to=listbl
            )
            await listbl.delete()
    else:
        await listbl.edit(OUT_STR)
        
        
        
        
        
@bot.on(admin_cmd(pattern=f"checkblacklist$", allow_sudo=True))
async def on_view_blacklist(listbl):
    all_blacklisted = sql.get_chat_blacklist(listbl.chat_id)
    OUT_STR = "Blacklists in the Current Chat:\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"`{trigger}`\n"
    else:
        OUT_STR = "`There are no blacklist in current chat.`"
    if len(OUT_STR) > 4096:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "blacklist.text"
            await listbl.client.send_file(
                listbl.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="BlackLists in the Current Chat",
                reply_to=listbl
            )
            await listbl.delete()
    else:
        await listbl.reply(OUT_STR)
           
        
        
        
@javes05(outgoing=True, pattern="^!clearblacklist ((.|\n)*)")       
async def on_delete_blacklist(event):
    text = event.pattern_match.group(1)
    to_unblacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
    successful = 0
    for trigger in to_unblacklist:
        if sql.rm_from_blacklist(event.chat_id, trigger.lower()):
            successful += 1
    await event.edit(f"Removed {successful} / {len(to_unblacklist)} from the blacklist")
        

@bot.on(admin_cmd(pattern=f"clearblacklist ((.|\n)*)", allow_sudo=True))
async def on_delete_blacklist(event):
    text = event.pattern_match.group(1)
    to_unblacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
    successful = 0
    for trigger in to_unblacklist:
        if sql.rm_from_blacklist(event.chat_id, trigger.lower()):
            successful += 1
    await event.edit(f"Removed {successful} / {len(to_unblacklist)} from the blacklist")




@javes05(outgoing=True, pattern="^!unbanall ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str:
        logger.info(f"`{JAVES_NNAME}: `**proccessing**")
    else:
        if event.is_private:
            return False
        await event.edit(f"`{JAVES_NNAME}:`**Searching Participant Lists**")
        p = 0
        async for i in bot.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
            rights = ChatBannedRights(
                until_date=0,
                view_messages=False
            )
            try:
                await bot(functions.channels.EditBannedRequest(event.chat_id, i, rights))
            except FloodWaitError as ex:
                logger.warn("sleeping for {} seconds".format(ex.seconds))
                sleep(ex.seconds)
            except Exception as ex:
                await event.edit(str(ex))
            else:
                p += 1
        await event.edit("{}: {} unbanned".format(event.chat_id, p))



@bot.on(admin_cmd(pattern=f"unbanall ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str:
        logger.info(f"`{JAVES_NNAME}: `**proccessing**")
    else:
        if event.is_private:
            return False
        await event.reply(f"`{JAVES_NNAME}:`**Searching Participant Lists**")
        p = 0
        async for i in bot.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
            rights = ChatBannedRights(
                until_date=0,
                view_messages=False
            )
            try:
                await bot(functions.channels.replyBannedRequest(event.chat_id, i, rights))
            except FloodWaitError as ex:
                logger.warn("sleeping for {} seconds".format(ex.seconds))
                sleep(ex.seconds)
            except Exception as ex:
                await event.reply(str(ex))
            else:
                p += 1
        await event.reply("{}: {} unbanned".format(event.chat_id, p))









@javes05(outgoing=True, pattern="^!akick ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_private:
        return False
    input_str = event.pattern_match.group(1)
    if input_str:
        chat = await event.get_chat()
        if not (chat.admin_rights or chat.creator):
            await event.edit(f"`{JAVES_NNAME}: `**Sorry i cant get admin permission**")
            return False
    p = 0
    b = 0
    c = 0
    d = 0
    e = []
    m = 0
    n = 0
    y = 0
    w = 0
    o = 0
    q = 0
    r = 0
    await event.edit("Searching Participant Lists.")
    async for i in bot.iter_participants(event.chat_id):
        p = p + 1
        #
        # Note that it's "reversed". You must set to ``True`` the permissions
        # you want to REMOVE, and leave as ``None`` those you want to KEEP.
        rights = ChatBannedRights(
            until_date=None,
            view_messages=True
        )
        if isinstance(i.status, UserStatusEmpty):
            y = y + 1
            if "y" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusLastMonth):
            m = m + 1
            if "m" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusLastWeek):
            w = w + 1
            if "w" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusOffline):
            o = o + 1
            if "o" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusOnline):
            q = q + 1
            if "q" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusRecently):
            r = r + 1
            if "r" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if i.bot:
            b = b + 1
            if "b" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        elif i.deleted:
            d = d + 1
            if "d" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.edit(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                else:
                    c = c + 1
        elif i.status is None:
            n = n + 1
    if input_str:
        required_string = """Kicked {} / {} users
Deleted Accounts: {}
UserStatusEmpty: {}
UserStatusLastMonth: {}
UserStatusLastWeek: {}
UserStatusOffline: {}
UserStatusOnline: {}
UserStatusRecently: {}
Bots: {}
None: {}"""
        await event.edit(required_string.format(c, p, d, y, m, w, o, q, r, b, n))
        await asyncio.sleep(5)
    await event.edit("""Total= {} users
Number Of Deleted Accounts= {}
Status: Empty= {}
      : Last Month= {}
      : Last Week= {}
      : Offline= {}
      : Online= {}
      : Recently= {}
Number Of Bots= {}
Unidentified= {}""".format(p, d, y, m, w, o, q, r, b, n))


async def ban_user(chat_id, i, rights):
    try:
        await bot(functions.channels.EditBannedRequest(chat_id, i, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)



@bot.on(admin_cmd(pattern=f"akick ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if event.is_private:
        return False
    input_str = event.pattern_match.group(1)
    if input_str:
        chat = await event.get_chat()
        if not (chat.admin_rights or chat.creator):
            await event.reply(f"`{JAVES_NNAME}: `**Sorry i cant get admin permission**")
            return False
    p = 0
    b = 0
    c = 0
    d = 0
    e = []
    m = 0
    n = 0
    y = 0
    w = 0
    o = 0
    q = 0
    r = 0
    await event.reply("Searching Participant Lists.")
    async for i in bot.iter_participants(event.chat_id):
        p = p + 1
        #
        # Note that it's "reversed". You must set to ``True`` the permissions
        # you want to REMOVE, and leave as ``None`` those you want to KEEP.
        rights = ChatBannedRights(
            until_date=None,
            view_messages=True
        )
        if isinstance(i.status, UserStatusEmpty):
            y = y + 1
            if "y" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.reply(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusLastMonth):
            m = m + 1
            if "m" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.reply(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusLastWeek):
            w = w + 1
            if "w" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.reply(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusOffline):
            o = o + 1
            if "o" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.reply(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusOnline):
            q = q + 1
            if "q" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.reply(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusRecently):
            r = r + 1
            if "r" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.reply(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if i.bot:
            b = b + 1
            if "b" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.reply(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        elif i.deleted:
            d = d + 1
            if "d" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await event.reply(f"`{JAVES_NNAME}: ` **I need admin priveleges to perform this action!**")
                    e.append(str(e))
                else:
                    c = c + 1
        elif i.status is None:
            n = n + 1
    if input_str:
        required_string = """Kicked {} / {} users
Deleted Accounts: {}
UserStatusEmpty: {}
UserStatusLastMonth: {}
UserStatusLastWeek: {}
UserStatusOffline: {}
UserStatusOnline: {}
UserStatusRecently: {}
Bots: {}
None: {}"""
        await event.reply(required_string.format(c, p, d, y, m, w, o, q, r, b, n))
        await asyncio.sleep(5)
    await event.reply("""Total= {} users
Number Of Deleted Accounts= {}
Status: Empty= {}
      : Last Month= {}
      : Last Week= {}
      : Offline= {}
      : Online= {}
      : Recently= {}
Number Of Bots= {}
Unidentified= {}""".format(p, d, y, m, w, o, q, r, b, n))


async def ban_user(chat_id, i, rights):
    try:
        await bot(functions.channels.replyBannedRequest(chat_id, i, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)      