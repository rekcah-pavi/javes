import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import register
from userbot import bot, CMD_HELP


@register(outgoing=True, pattern="^!name(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("`javes: Can't scan bot meaage`")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```javes: reply to a media message```")
       return
    chat = "@SangMataInfo_bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("`Reply to actual users message.`")
       return
    await event.edit("`javes: Hacking........`")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("`Please unblock @sangmatainfo_bot and try again`")
              return
          if response.text.startswith("Forward"):
             await event.edit("`javes: This user have forward privacy`")
          else: 
             await event.edit(f"javes: Userdetails\n {response.message.message}")





@register(outgoing=True, disable_errors=True, pattern="^!scan(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```javes: Can't scan bot meaage```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("```javes: reply to a media message```")
       return
    chat = "@DrWebBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```javes: Reply to actual users message.```")
       return
    await event.edit(" `javes: Scanning......`")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=161163358))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @sangmatainfo_bot and try again```")
              return
          if response.text.startswith("Forward"):
             await event.edit("```javes: This user have forward privacy```")
          else:
          	if response.text.startswith("Select"):
          		await event.edit("`javes: Please go to` @DrWebBot `and select your language.`") 
          	else: 
          			await event.edit(f"javes: Antivirus scan was completed. \n {response.message.message}")


@register(outgoing=True, pattern="^!ss(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```Reply to text message```")
       return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```javes: Can't scan bot meaage```")
       return
    await event.edit("```Making a Quote```")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @QuotLyBot and try again```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```javes: This user have forward privacy```")
          else: 
             await event.delete()   
             await bot.forward_messages(event.chat_id, response.message)



