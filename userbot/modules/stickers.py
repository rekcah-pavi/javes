import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import javes05
from userbot import bot, CMD_HELP
from userbot import bot, CMD_HELP
import io
import math
import urllib.request
from os import remove
from userbot.events import javes05
import io
import os
import random
import textwrap
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument
from PIL import Image
import random
from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto
from userbot import bot, CMD_HELP
import io
import os
import random
import textwrap
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID
from telethon.tl.types import DocumentAttributeSticker
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
PACK_FULL = "Whoa! That's probably enough stickers for one pack, give it a break. \
A pack can't have more than 120 stickers at the moment."

KANGING_STR = [
    
    "Kanging this sticker...",
    "Hey that's a nice sticker!\
    \nMind if I kang?!..",
    
    "Kanging this sticker ... ",
]


@javes05(outgoing=True, pattern="^\!kang")
async def kang(args):
    """ For .kang command, kangs stickers or creates new ones. """
    kang_meme = random.choice(KANGING_STR)
    user = await bot.get_me()
    if not user.username:
        user.username = user.first_name
    message = await args.get_reply_message()
    photo = None
    emojibypass = False
    is_anim = False
    emoji = None

    if message and message.media:
        if isinstance(message.media, MessageMediaPhoto):
            await args.edit(f"`{kang_meme}`")
            photo = io.BytesIO()
            photo = await bot.download_media(message.photo, photo)
        elif "image" in message.media.document.mime_type.split('/'):
            await args.edit(f"`{kang_meme}`")
            photo = io.BytesIO()
            await bot.download_file(message.media.document, photo)
            if (DocumentAttributeFilename(file_name='sticker.webp') in
                    message.media.document.attributes):
                emoji = message.media.document.attributes[1].alt
                emojibypass = True
        elif "tgsticker" in message.media.document.mime_type:
            await args.edit(f"`{kang_meme}`")
            await bot.download_file(message.media.document,
                                    'AnimatedSticker.tgs')

            attributes = message.media.document.attributes
            for attribute in attributes:
                if isinstance(attribute, DocumentAttributeSticker):
                    emoji = attribute.alt

            emojibypass = True
            is_anim = True
            photo = 1
        else:
            await args.edit("`Unsupported File!`")
            return
    else:
        await args.edit("`I can't kang that...`")
        return

    if photo:
        splat = args.text.split()
        if not emojibypass:
            emoji = "🤔"
        pack = 1
        if len(splat) == 3:
            pack = splat[2]  # User sent both
            emoji = splat[1]
        elif len(splat) == 2:
            if splat[1].isnumeric():
                # User wants to push into different pack, but is okay with
                # thonk as emote.
                pack = int(splat[1])
            else:
                # User sent just custom emote, wants to push to default
                # pack
                emoji = splat[1]

        packname = f"a{user.id}_by_{user.username}_{pack}"
        packnick = f"@{user.username}'s pack Vol.{pack}"
        cmd = '/newpack'
        file = io.BytesIO()

        if not is_anim:
            image = await resize_photo(photo)
            file.name = "sticker.png"
            image.save(file, "PNG")
        else:
            packname += "_anim"
            packnick += " (Animated)"
            cmd = '/newanimated'

        response = urllib.request.urlopen(
            urllib.request.Request(f'http://t.me/addstickers/{packname}'))
        htmlstr = response.read().decode("utf8").split('\n')

        if "  A <strong>Telegram</strong> user has created the <strong>Sticker&nbsp;Set</strong>." not in htmlstr:
            async with bot.conversation('Stickers') as conv:
                await conv.send_message('/addsticker')
                await conv.get_response()
                # Ensure user doesn't get spamming notifications
                await bot.send_read_acknowledge(conv.chat_id)
                await conv.send_message(packname)
                x = await conv.get_response()
                while x.text == PACK_FULL:
                    pack += 1
                    packname = f"a{user.id}_by_{user.username}_{pack}"
                    packnick = f"@{user.username}'s pack Vol.{pack}"
                    await args.edit(f"`{kang_meme}\
                    \nMoving on to Vol.{str(pack)}..`")
                    await conv.send_message(packname)
                    x = await conv.get_response()
                    if x.text == "Invalid pack selected.":
                        await conv.send_message(cmd)
                        await conv.get_response()
                        # Ensure user doesn't get spamming notifications
                        await bot.send_read_acknowledge(conv.chat_id)
                        await conv.send_message(packnick)
                        await conv.get_response()
                        # Ensure user doesn't get spamming notifications
                        await bot.send_read_acknowledge(conv.chat_id)
                        if is_anim:
                            await conv.send_file('AnimatedSticker.tgs')
                            remove('AnimatedSticker.tgs')
                        else:
                            file.seek(0)
                            await conv.send_file(file, force_document=True)
                        await conv.get_response()
                        await conv.send_message(emoji)
                        # Ensure user doesn't get spamming notifications
                        await bot.send_read_acknowledge(conv.chat_id)
                        await conv.get_response()
                        await conv.send_message("/publish")
                        if is_anim:
                            await conv.get_response()
                            await conv.send_message(f"<{packnick}>")
                        # Ensure user doesn't get spamming notifications
                        await conv.get_response()
                        await bot.send_read_acknowledge(conv.chat_id)
                        await conv.send_message("/skip")
                        # Ensure user doesn't get spamming notifications
                        await bot.send_read_acknowledge(conv.chat_id)
                        await conv.get_response()
                        await conv.send_message(packname)
                        # Ensure user doesn't get spamming notifications
                        await bot.send_read_acknowledge(conv.chat_id)
                        await conv.get_response()
                        # Ensure user doesn't get spamming notifications
                        await bot.send_read_acknowledge(conv.chat_id)
                        await args.edit(f"`Haha, yes. New kang pack unlocked!\
                            \nPack can be found [here](t.me/addstickers/{packname})",
                                        parse_mode='md')
                        return
                if is_anim:
                    await conv.send_file('AnimatedSticker.tgs')
                    remove('AnimatedSticker.tgs')
                else:
                    file.seek(0)
                    await conv.send_file(file, force_document=True)
                rsp = await conv.get_response()
                if "Sorry, the file type is invalid." in rsp.text:
                    await args.edit(
                        "`Failed to add sticker, use` @Stickers `bot to add the sticker manually.`"
                    )
                    return
                await conv.send_message(emoji)
                # Ensure user doesn't get spamming notifications
                await bot.send_read_acknowledge(conv.chat_id)
                await conv.get_response()
                await conv.send_message('/done')
                await conv.get_response()
                # Ensure user doesn't get spamming notifications
                await bot.send_read_acknowledge(conv.chat_id)
        else:
            await args.edit(f"`{JAVES_NNAME}`: **Brewing a new Pack...**")
            async with bot.conversation('Stickers') as conv:
                await conv.send_message(cmd)
                await conv.get_response()
                # Ensure user doesn't get spamming notifications
                await bot.send_read_acknowledge(conv.chat_id)
                await conv.send_message(packnick)
                await conv.get_response()
                # Ensure user doesn't get spamming notifications
                await bot.send_read_acknowledge(conv.chat_id)
                if is_anim:
                    await conv.send_file('AnimatedSticker.tgs')
                    remove('AnimatedSticker.tgs')
                else:
                    file.seek(0)
                    await conv.send_file(file, force_document=True)
                rsp = await conv.get_response()
                if "Sorry, the file type is invalid." in rsp.text:
                    await args.edit(
                        "`Failed to add sticker, use` @Stickers `bot to add the sticker manually.`"
                    )
                    return
                await conv.send_message(emoji)
                # Ensure user doesn't get spamming notifications
                await bot.send_read_acknowledge(conv.chat_id)
                await conv.get_response()
                await conv.send_message("/publish")
                if is_anim:
                    await conv.get_response()
                    await conv.send_message(f"<{packnick}>")
                # Ensure user doesn't get spamming notifications
                await conv.get_response()
                await bot.send_read_acknowledge(conv.chat_id)
                await conv.send_message("/skip")
                # Ensure user doesn't get spamming notifications
                await bot.send_read_acknowledge(conv.chat_id)
                await conv.get_response()
                await conv.send_message(packname)
                # Ensure user doesn't get spamming notifications
                await bot.send_read_acknowledge(conv.chat_id)
                await conv.get_response()
                # Ensure user doesn't get spamming notifications
                await bot.send_read_acknowledge(conv.chat_id)

        await args.edit(f"`{JAVES_NNAME}`: **Sticker kanged successfully!**\
            \nPack can be found [here](t.me/addstickers/{packname})",
                        parse_mode='md')


async def resize_photo(photo):
    """ Resize the given photo to 512x512 """
    image = Image.open(photo)
    maxsize = (512, 512)
    if (image.width and image.height) < 512:
        size1 = image.width
        size2 = image.height
        if image.width > image.height:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        image = image.resize(sizenew)
    else:
        image.thumbnail(maxsize)

    return image


@javes05(outgoing=True, disable_errors=True, pattern="^!ss2(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit(f"`{JAVES_NNAME}`: **Reply to a Photo**")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit(f"`{JAVES_NNAME}`: **Reply to a photo**")
       return
    chat = "@BuildStickerBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit(f"`{JAVES_NNAME}`: **Reply to actual users message.**")
       return
    await event.edit(f"`{JAVES_NNAME}`: **processing Img to Sticker.......**")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=164977173))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @BuildStickerBot and try again```")
              return
          if response.text.startswith("Forward"):
             await event.edit(f"`{JAVES_NNAME}`: **privacy error**")
          else:
          	if response.text.startswith("Select"):
          		await event.edit("`Please go to` @DrWebBot `and select your language.`") 
          	else: 
          			await bot.send_file(event.chat_id, response.message.media)



@javes05(outgoing=True, pattern="^\!stickerinfo$")
async def get_pack_info(event):
    if not event.is_reply:
        await event.edit(f"`{JAVES_NNAME}`: **Reply to a sticker to get the pack details*")
        return

    rep_msg = await event.get_reply_message()
    if not rep_msg.document:
        await event.edit(f"`{JAVES_NNAME}`: **Reply to a sticker to get the pack details**")
        return

    try:
        stickerset_attr = rep_msg.document.attributes[1]
        await event.edit(
            "`Fetching details of the sticker pack, please wait..`")
    except BaseException:
        await event.edit("`This is not a sticker. Reply to a sticker.`")
        return

    if not isinstance(stickerset_attr, DocumentAttributeSticker):
        await event.edit(f"`{JAVES_NNAME}`: **This is not a sticker. Reply to a sticker.**")
        return

    get_stickerset = await bot(
        GetStickerSetRequest(
            InputStickerSetID(
                id=stickerset_attr.stickerset.id,
                access_hash=stickerset_attr.stickerset.access_hash)))
    pack_emojis = []
    for document_sticker in get_stickerset.packs:
        if document_sticker.emoticon not in pack_emojis:
            pack_emojis.append(document_sticker.emoticon)

    OUTPUT = f"**Sticker Title:** `{get_stickerset.set.title}\n`" \
        f"**Sticker Short Name:** `{get_stickerset.set.short_name}`\n" \
        f"**Official:** `{get_stickerset.set.official}`\n" \
        f"**Archived:** `{get_stickerset.set.archived}`\n" \
        f"**Stickers In Pack:** `{len(get_stickerset.packs)}`\n" \
        f"**Emojis In Pack:**\n{' '.join(pack_emojis)}"

    await event.edit(OUTPUT)

@javes05 (outgoing=True, pattern="^!ss(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit(f"`{JAVES_NNAME}`: **Reply to any user message.**")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit(f"`{JAVES_NNAME}`: **Reply to text message**")
       return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit(f"`{JAVES_NNAME}`: **Can't scan bot meaage**")
       return
    await event.edit(f"`{JAVES_NNAME}`: ** Processing Text to Sticker **")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply(f"`{JAVES_NNAME}`: **Please unblock @QuotLyBot and try again**")
              return
          if response.text.startswith("Hi!"):
             await event.edit(f"`{JAVES_NNAME}`: **PrivacyError**")
          else: 
             await event.delete()   
             await bot.forward_messages(event.chat_id, response.message)


@javes05 (outgoing=True, pattern="^!text(?: |$)(.*)")
async def sticklet(event):
    R = random.randint(0,256)
    G = random.randint(0,256)
    B = random.randint(0,256)

    # get the input text
    # the text on which we would like to do the magic on
    sticktext = event.pattern_match.group(1)

    # delete the userbot command,
    # i don't know why this is required
    await event.delete()

    # https://docs.python.org/3/library/textwrap.html#textwrap.wrap
    sticktext = textwrap.wrap(sticktext, width=10)
    # converts back the list to a string
    sticktext = '\n'.join(sticktext)

    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230

    FONT_FILE = await get_font_file(event.client, "@FontRes")

    font = ImageFont.truetype(FONT_FILE, size=fontsize)

    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype(FONT_FILE, size=fontsize)

    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(((512-width)/2,(512-height)/2), sticktext, font=font, fill=(R, G, B))

    image_stream = io.BytesIO()
    image_stream.name = "Javes.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)

    # finally, reply the sticker
    #await event.reply( file=image_stream, reply_to=event.message.reply_to_msg_id)
    #replacing upper line with this to get reply tags

    await event.client.send_file(event.chat_id, image_stream, reply_to=event.message.reply_to_msg_id)
    # cleanup
    try:
        os.remove(FONT_FILE)
    except:
        pass


async def get_font_file(client, channel_id):
    # first get the font messages
    font_file_message_s = await client.get_messages(
        entity=channel_id,
        filter=InputMessagesFilterDocument,
        # this might cause FLOOD WAIT,
        # if used too many times
        limit=None
    )
    # get a random font from the list of fonts
    # https://docs.python.org/3/library/random.html#random.choice
    font_file_message = random.choice(font_file_message_s)
    # download and return the file path
    return await client.download_media(font_file_message)


 






@bot.on(events.NewMessage(outgoing=True, pattern="!text2 ?(?:(.*?) \| )?(.*)"))
@bot.on(events.MessageEdited(outgoing=True, pattern="!text2 ?(?:(.*?) \| )?(.*)"))

async def sticklet(event):

    R = random.randint(0,256)

    G = random.randint(0,256)

    B = random.randint(0,256)



    reply_message = event.message

    # get the input text

    # the text on which we would like to do the magic on

    font_file_name = event.pattern_match.group(1)

    if not font_file_name:

        font_file_name = ""



    sticktext = event.pattern_match.group(2)

    if not sticktext and event.reply_to_msg_id:

        reply_message = await event.get_reply_message()

        sticktext = reply_message.message

    elif not sticktext:

        await event.edit(f"`{JAVES_NNAME}`: **need something **")

        return



    if event.reply_to_msg_id:

        reply_message = await event.get_reply_message()

    # delete the userbot command,

    # i don't know why this is required

    await event.delete()



    # https://docs.python.org/3/library/textwrap.html#textwrap.wrap

    sticktext = textwrap.wrap(sticktext, width=10)

    # converts back the list to a string

    sticktext = '\n'.join(sticktext)



    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))

    draw = ImageDraw.Draw(image)

    fontsize = 230



    FONT_FILE = await get_font_file(event.client, "@FontRes", font_file_name)



    font = ImageFont.truetype(FONT_FILE, size=fontsize)



    while draw.multiline_textsize(sticktext, font=font) > (512, 512):

        fontsize -= 3

        font = ImageFont.truetype(FONT_FILE, size=fontsize)



    width, height = draw.multiline_textsize(sticktext, font=font)

    draw.multiline_text(((512-width)/2,(512-height)/2), sticktext, font=font, fill=(R, G, B))



    image_stream = io.BytesIO()

    image_stream.name = "javes.webp"

    image.save(image_stream, "WebP")

    image_stream.seek(0)



    # finally, reply the sticker

    await event.client.send_file(event.chat_id, image_stream, caption="Sticklet", reply_to=event.message.reply_to_msg_id)



    # cleanup

    try:

        os.remove(FONT_FILE)

    except:

        pass





async def get_font_file(client, channel_id, search_kw=""):

    # first get the font messages

    font_file_message_s = await client.get_messages(

        entity=channel_id,

        filter=InputMessagesFilterDocument,

        # this might cause FLOOD WAIT,

        # if used too many times

        limit=None,

        search=search_kw

    )

    # get a random font from the list of fonts

    # https://docs.python.org/3/library/random.html#random.choice

    font_file_message = random.choice(font_file_message_s)

    # download and return the file path

    return await client.download_media(font_file_message)



