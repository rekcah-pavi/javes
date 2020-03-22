

import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from traceback import format_exc

from telethon import events

from userbot import bot, BOTLOG_CHATID, LOGSPAMMER


def javes05(**args):
    """ Register a new event. """
    pattern = args.get('pattern', None)
    disable_edited = args.get('disable_edited', False)
    groups_only = args.get('groups_only', False)
    trigger_on_fwd = args.get('trigger_on_fwd', False)
    disable_errors = args.get('disable_errors', False)

    if pattern is not None and not pattern.startswith('(?i)'):
        args['pattern'] = '(?i)' + pattern

    if "disable_edited" in args:
        del args['disable_edited']

    if "groups_only" in args:
        del args['groups_only']

    if "disable_errors" in args:
        del args['disable_errors']

    if "trigger_on_fwd" in args:
        del args['trigger_on_fwd']

    def decorator(func):
        async def wrapper(check):
            if LOGSPAMMER:
                send_to = BOTLOG_CHATID

            if not trigger_on_fwd and check.fwd_from:
                return

            if groups_only and not check.is_group:
                await check.respond("`I don't think this is a group.`")
                return

            try:
                await func(check)

            # Thanks to @kandnub for this HACK.
            # Raise StopPropagation to Raise StopPropagation
            # This needed for AFK to working properly

            except events.StopPropagation:
                raise events.StopPropagation
            # This is a gay exception and must be passed out. So that it doesnt spam chats
            except KeyboardInterrupt:
                pass
            except BaseException:

                # Check if we have to disable it.
                # If not silence the log spam on the console,
                # with a dumb except.

                if not disable_errors:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    text = "**JAVES ERROR REPORT**\n"
                    text += "Send this to @rekcah05 if you cant find issue\n"

                    ftext = "========== DISCLAIMER =========="
                    ftext += "\nThis file uploaded ONLY here,"                
                    ftext += "\nyou may not report this error if you've"
                    ftext += "\nany confidential data here, no one will see your data\n"
                    ftext += "================================\n\n"
                    ftext += "--------BEGIN USERBOT TRACEBACK LOG--------\n"
                    ftext += "\nDate: " + date
                    ftext += "\nChat ID: " + str(check.chat_id)
                    ftext += "\nSender ID: " + str(check.sender_id)
                    ftext += "\n\nEvent Trigger:\n"
                    ftext += str(check.text)
                    ftext += "\n\nTraceback info:\n"
                    ftext += str(format_exc())
                    ftext += "\n\nError text:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"

                    command = "git log --pretty=format:\"%an: %s\" -10"

                    ftext += "\n\n\nLast 10 commits:\n"

                    process = await asyncsubshell(command,
                                                  stdout=asyncsub.PIPE,
                                                  stderr=asyncsub.PIPE)
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) \
                        + str(stderr.decode().strip())

                    ftext += result

                    file = open("error.log", "w+")
                    file.write(ftext)
                    file.close()

                    if LOGSPAMMER:
                        await check.respond("`Error 4O4`")

                    await check.client.send_file(send_to,
                                                 "error.log",
                                                 caption=text)
                    remove("error.log")
            else:
                pass

        if not disable_edited:
            bot.add_event_handler(wrapper, events.MessageEdited(**args))
        bot.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper

    return decorator
    

