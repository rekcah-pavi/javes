
from userbot import CMD_HELP
from userbot.events import javes05


@javes05(outgoing=True, pattern="^!help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("Please specify a valid module name.")
    else:
        await event.edit("Usage: !help <module name>\
            \n Example - !help admin")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`, "
        await event.reply(string)
        
        
CMD_HELP.update({
    "admin":
    "!promote <username/reply/userid> <custom name>\
\nUsage: Provides admin rights to the person in the chat.\
\n\n!demote <username/reply/userid>\
\nUsage: Revokes the person's admin permissions in the chat.\
\n\n!ban <reply> <reason (optional)>\
\nUsage: Bans the person off your chat.\
\n\n!unban <username/reply/userid>\
\nUsage: Removes the ban from the person in the chat.\
\n\n!mute <username/reply/userid> <reason (optional)>\
\nUsage: Mutes the person in the chat, works on admins too.\
\n\n!warn <reply to a message > <reason (optional)>\
\nUsage: warn the person\
\n\n!resetwarns <reply to a user > \
\nUsage: reset the target person's warns\
\n\n!warns <reply to a user > \
\nUsage: get warnings of the targeted person\
\n\n!unmute <username/reply/userid>\
\nUsage: Removes the person from the muted list.\
\n\n!gban <username/reply/userid> <reason (optional)>\
\nUsage: Ban the person in all groups you have in common with them. and mute user in your pm too!\
\n\n!unban <username/reply/userid>\
\nUsage: Reply someone's message with !ungban to remove them from the gban list.\
\n\n!delusers\
\nUsage: Searches for deleted accounts in a group. Use !delusers clean to remove deleted accounts from the group.\
\n\n!admins\
\nUsage: Retrieves a list of admins in the chat.\
\n\n!bots\
\nUsage: Retrieves a list of bots in the chat.\
\n\n!users  <Retrieves a list of members in the chat.>\
\nUsage: Retrieves all (or queried) users in the chat.\
\n\n!pin <reply to message>\
\nUsage: Changes the group's display picture.\
\n\n!setgpic <reply to image>\
\nUsage: Changes the group's display picture."
})


CMD_HELP.update({
    "notes":
    "\
#<notename>\
\nUsage: Gets the specified note.\
\n\n!savenote <notename> <notedata> or reply to a message with !savenote <notename>\
\nUsage: Saves the replied message as a note with the notename. (Works with pics, docs, and stickers too!)\
\n\n!checknote\
\nUsage: Gets all saved notes in a chat.\
\n\n!clearnote <notename>\
\nUsage: Deletes the specified note."
})


CMD_HELP.update({
    "welcome":
    "\
!savewelcome <welcome message> or reply to a message with !savewelcome\
\nUsage: Saves the message as a welcome note in the chat.\
\n\nAvailable variables for formatting welcome messages :\
\n`{mention}, {title}, {count}, {first}, {last}, {fullname}, {userid}, {username}, {my_first}, {my_fullname}, {my_last}, {my_mention}, {my_username}`\
\n\n!checkwelcome\
\nUsage: Check whether you have a welcome note in the chat.\
\n\n!clearwelcome\
\nUsage: Deletes the welcome note for the current chat.\
\n\n!savewelcome2,!checkwelcome2,!clearwelcome2\
\nUsage: same like welcome \
"
})

CMD_HELP.update({
    "locks":
    "!lock <all (or) type(s)> or !unlock <all (or) type(s)>\
\nUsage: Allows you to lock/unlock some common message types in the chat.\
[NOTE: Requires proper admin rights in the chat !!]\
\n\nAvailable message types to lock/unlock are: \
\n`all, msg, media, sticker, gif, game, inline, poll, invite, pin, info`"
})


CMD_HELP.update({
    "chat":
    "!chatid\
\nUsage: Fetches the current chat's ID\
\n\n!userid\
\nUsage: Fetches the ID of the user in reply, if its a forwarded message, finds the ID for the source.\
\n\n!chatinfo\
\nUsage: Fetches the group's info\
\n\n!log\
\nUsage: Forwards the message you've replied to in your bot logs group.\
\n\n!invite\
\nUsage: !invite <username> invite the user to the group.\
\n\n!kickme\
\nUsage: Leave from a targeted group.\
\n\n!link <username/userid> : <optional text> (or) reply to someone's message with !link <optional text>\
\nUsage: Generate a permanent link to the user's profile with optional custom text."
})

CMD_HELP.update({
    "filter":
    "!checkfilter\
    \nUsage: Lists all active userbot filters in a chat.\
    \n\n!savefilter <keyword> <reply text> or reply to a message with !savefilter <keyword>\
    \nUsage: Saves the replied message as a reply to the 'keyword'.\
    \nThe bot will reply to the message whenever 'keyword' is mentioned.\
    \nWorks with everything from files to stickers.\
    \n\n!clearfilter <filter>\
    \nUsage: Stops the specified filter. \
    \n\n!clearallfilter <filter>\
    \nUsage: Stops all filters.\
    \n\n!savefilter2 , !checkfilter2, clearfilter2 <filter>\
    \nUsage: same like filter "
})


CMD_HELP.update({
    "blacklist":
    "!checkblacklist\
    \nUsage: Lists all active userbot blacklists in a chat.\
    \n\n!saveblacklist <keyword> <reply text> or reply to a message with !saveblacklist <keyword>\
    \nUsage: Delete then non admins blacklisted wards.\
    \n\n!clearblacklist <ward>\
    \nUsage: Stops the specified blacklist ward. "
})




CMD_HELP.update({
    "others":
    "!comming soon!\
    \n check Channel @javes05 for now"
})

