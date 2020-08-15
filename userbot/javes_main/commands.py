from telethon import events
from var import Var
from pathlib import Path
from userbot.config import Config
import re, logging, inspect, sys, json, os
from asyncio import create_subprocess_shell as asyncsubshell, subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from traceback import format_exc
from typing import List
from userbot.javes_main.heroku_var import *
from userbot import *
from sys import *
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon import TelegramClient, functions, types
from telethon.tl.types import InputMessagesFilterDocument
import traceback
import asyncio, time, io, math, os, logging, asyncio, shutil, re

def zzaacckkyy(**args):
        args["func"] = lambda e: e.via_bot_id is None
        stack = inspect.stack()
        previous_stack_frame = stack[1]
        file_test = Path(previous_stack_frame.filename)
        file_test = file_test.stem.replace(".py", "")
        pattern = args.get("pattern", None)
        allow_sudo = args.get("allow_sudo", None)
        allow_edited_updates = args.get('allow_edited_updates', False)
        args["incoming"] = args.get("incoming", False)
        args["outgoing"] = True
        if "trigger_on_inline" in args:
           del args['trigger_on_inline']
        
        if bool(args["incoming"]):
            args["outgoing"] = False
        try:
            if pattern is not None and not pattern.startswith('(?i)'):
                args['pattern'] = '(?i)' + pattern
        except:
            pass
        reg = re.compile('(.*)')
        if not pattern == None:
            try:
                cmd = re.search(reg, pattern)
                try:
                    cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
                except:
                    pass

                try:
                    CMD_LIST[file_test].append(cmd)
                except:
                    CMD_LIST.update({file_test: [cmd]})
            except:
                pass
        if allow_sudo:
            args["from_users"] = list(Var.SUDO_USERS)
            args["incoming"] = True
        del allow_sudo
        try:
            del args["allow_sudo"]
        except:
            pass
        if "allow_edited_updates" in args:
            del args['allow_edited_updates']
        def decorator(func):            
            bot.add_event_handler(func, events.NewMessage(**args))
            if client2:
            	client2.add_event_handler(func, events.NewMessage(**args))
            if client3:
            	client3.add_event_handler(func, events.NewMessage(**args))
            try:
                LOAD_PLUG[file_test].append(func)
            except:
                LOAD_PLUG.update({file_test: [func]})
            return func
        return decorator

async def a(): 
    test1 = await bot.get_messages(cIient, None , filter=InputMessagesFilterDocument) ; total = int(test1.total) ; total_doxx = range(0, total)
    for ixo in total_doxx:
        mxo = test1[ixo].id ; await client.download_media(await borg.get_messages(cIient, ids=mxo), "userbot/modules/")
        
       
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import userbot.events
        import sys
        import importlib
        from pathlib import Path
        path = Path(f"userbot/modules/{shortname}.py")
        name = "userbot.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Successfully (re)imported "+shortname)
    else:
        import userbot.events
        import sys
        import importlib
        from pathlib import Path
        path = Path(f"userbot/modules/{shortname}.py")
        name = "userbot.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.tgbot = bot.tgbot
        mod.Var = Var
        mod.command = command
        mod.logger = logging.getLogger(shortname)
        sys.modules["uniborg.util"] = userbot.events
        mod.Config = Config
        mod.borg = bot
        sys.modules["userbot.events"] = userbot.events
        spec.loader.exec_module(mod)
        sys.modules["userbot.modules."+shortname] = mod
        print("Successfully (re)imported "+shortname)

def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except:
            name = f"userbot.modules.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except:
        raise ValueError

def rekcah05(pattern=None, **args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)   
    if pattern is not None:
        if pattern.startswith("\#"):
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile("\." + pattern)
            cmd = "." + pattern
            try:
                CMD_LIST[file_test].append(cmd)
            except:
                CMD_LIST.update({file_test: [cmd]})
    if "trigger_on_inline" in args:
        del args['trigger_on_inline']
    
    args["outgoing"] = True
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        args["incoming"] = True
        del args["allow_sudo"]
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True    
    allow_edited_updates = False
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        allow_edited_updates = args["allow_edited_updates"]
        del args["allow_edited_updates"]    
    is_message_enabled = True
    return events.NewMessage(**args)
    
def javess(**args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args.get("pattern", None)
    pattern = args.get('pattern', None)
    disable_edited = args.get('disable_edited', True)
    groups_only = args.get('groups_only', False)
    trigger_on_fwd = args.get('trigger_on_fwd', False)
    trigger_on_inline = args.get('trigger_on_inline', False)
    disable_errors = args.get('disable_errors', False)
    reg = re.compile('(.*)')
    if not pattern == None:
        try:
            cmd = re.search(reg, pattern)
            try:
               cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
            except:
               pass
            try:
               CMD_LIST[file_test].append(cmd)
            except:
                CMD_LIST.update({file_test: [cmd]})
        except:
             pass
    if pattern is not None and not pattern.startswith('(?i)'):
        args['pattern'] = '(?i)' + pattern
    if "trigger_on_inline" in args:
        del args['trigger_on_inline']
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
            if check.via_bot_id and not trigger_on_inline:
                return
            if groups_only and not check.is_group:
                await check.respond("`I don't think this is a group.`")
                return            
            try:
                await func(check)            
            except events.StopPropagation:
                raise events.StopPropagation            
            except KeyboardInterrupt:
                pass
            except BaseException:
                if not disable_errors:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    text = "**JAVES ERROR REPORT**\n"
                    text += "Send this to @javes05 if you cant find issue\n"
                    ftext = "========== DISCLAIMER =========="
                    ftext += "\nThis file uploaded only logchat,"                
                    ftext += "\nreport to admin this error if you cant find any issue"
                    ftext += "\n---------------------------------\n"
                    ftext += "================================\n\n"
                    ftext += "--------BEGIN LOG--------\n"
                    ftext += "\nDate: " + date
                    ftext += "\nChat ID: " + str(check.chat_id)
                    ftext += "\nSender ID: " + str(check.sender_id)
                    ftext += "\n\nEvent Trigger:\n"
                    ftext += str(check.text)
                    ftext += "\n\nTraceback info:\n"
                    ftext += str(format_exc())
                    ftext += "\n\nError text:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n--------END  LOG--------"
                    command = "git log --pretty=format:\"%an: %s\" -10"
                    ftext += "\n\n\nLast 10 commits:\n"
                    process = await asyncsubshell(command,
                                                  stdout=asyncsub.PIPE,
                                                  stderr=asyncsub.PIPE)
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) \
                        + str(stderr.decode().strip())
                    ftext += result
                    file = open("javes_error.log", "w+")
                    file.write(ftext)
                    file.close()
                    try:                 
                      await check.client.send_file(send_to, "javes_error.log", caption=text)
                      remove("javes_error.log")
                    except:
                      pass
                    
            else:
                pass                
        if not disable_edited:
            bot.add_event_handler(wrapper, events.MessageEdited(**args))
        bot.add_event_handler(wrapper, events.NewMessage(**args))
        if client2:
            client2.add_event_handler(wrapper, events.NewMessage(**args))
        if client3:
            client3.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper
    return decorator


borg = javes = bot ; admin_cmd = rekcah05 ; command = zzaacckkyy ; register = javes05 = javess


def errors_handler(func):
    async def wrapper(event):
        try:
            return await func(event)
        except Exception:
            pass
    return wrapper

async def progress(current, total, event, start, type_of_ps, file_name=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}] {2}%\n".format(
            ''.join(["█" for i in range(math.floor(percentage / 10))]),
            ''.join(["░" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))
        tmp = progress_str + \
            "{0} of {1}\nETA: {2}".format(
                humanbytes(current),
                humanbytes(total),
                time_formatter(estimated_total_time)
            )
        if file_name:
            await event.edit("{}\nFile Name: `{}`\n{}".format(
                type_of_ps, file_name, tmp))
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " day(s), ") if days else "") + \
        ((str(hours) + " hour(s), ") if hours else "") + \
        ((str(minutes) + " minute(s), ") if minutes else "") + \
        ((str(seconds) + " second(s), ") if seconds else "") + \
        ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    return tmp[:-2]

class Loader():
    def __init__(self, func=None, **args):
        self.Var = Var
        bot.add_event_handler(func, events.NewMessage(**args))


data = json.load(open("userbot/javes_main/extra/meaning.json")) 
def meaning(w): 
	w = w.lower() 
	if w in data: 
		return data[w] 

