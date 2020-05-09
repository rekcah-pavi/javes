import os
import io
import json
from requests import get
from datetime import datetime
from userbot import bot as javes
from userbot.events import rekcah05
from pytz import country_timezones as c_tz
from pytz import timezone as tz
from pytz import country_names as c_n
from userbot import CMD_HELP, WEATHER_DEFCITY
from userbot import OPEN_WEATHER_MAP_APPID as OWM_API
import requests
from telethon.tl.types import MessageMediaPhoto
from userbot import CMD_HELP, REM_BG_API_KEY, TEMP_DOWNLOAD_DIRECTORY
import time
from telethon import events
import os
import requests
import logging
from userbot import bot, OCR_SPACE_API_KEY, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
import asyncio
import shutil
from bs4 import BeautifulSoup
import re
from time import sleep
from html import unescape
from userbot.events import javes05
from re import findall
from selenium import webdriver
from urllib.parse import quote_plus
from telethon import events
import os
import requests
import logging
from userbot import bot, OCR_SPACE_API_KEY, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from urllib.error import HTTPError
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from wikipedia import summary
from wikipedia.exceptions import DisambiguationError, PageError
import asyncurban
from coffeehouse.lydia import LydiaAI
from coffeehouse.api import API
import asyncio
from userbot import LYDIA_API_KEY
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import javes05
from telethon import events
from requests import get
from search_engine_parser import GoogleSearch
from google_images_download import google_images_download
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googletrans import LANGUAGES, Translator
from gtts import gTTS
from gtts.lang import tts_langs
from emoji import get_emoji_regexp
from youtube_dl import YoutubeDL
from youtube_dl.utils import (DownloadError, ContentTooShortError,ExtractorError, GeoRestrictedError,MaxDownloadsReached, PostProcessingError,UnavailableVideoError, XAttrMetadataError)
from asyncio import sleep
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID, YOUTUBE_API_KEY, CHROME_DRIVER, GOOGLE_CHROME_BIN
from telethon.tl.types import DocumentAttributeAudio
from userbot.modules.system import progress, humanbytes, time_formatter
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
ACC_LYDIA = {}

if LYDIA_API_KEY:
    api_key = LYDIA_API_KEY
    api_client = API(api_key)
    lydia = LydiaAI(api_client)




async def ocr_space_file(filename,
                         overlay=False,
                         api_key=OCR_SPACE_API_KEY,
                         language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {
        'isOverlayRequired': overlay,
        'apikey': api_key,
        'language': language,
    }
    with open(filename, 'rb') as f:
        r = requests.post(
            'https://api.ocr.space/parse/image',
            files={filename: f},
            data=payload,
        )
    return r.json()



@javes05(pattern="^!read(?: |$)(.*)", outgoing=True)
async def ocr(event):
 if OCR_SPACE_API_KEY is None:
	 await event.edit(f"`{JAVES_NNAME}:` **ocr api key missing please add it before use**")
 else:
    await event.edit(f"`{JAVES_NNAME}:` **Reading...**")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    lang_code = event.pattern_match.group(1)
    downloaded_file_name = await bot.download_media(
        await event.get_reply_message(), TEMP_DOWNLOAD_DIRECTORY)
    test_file = await ocr_space_file(filename=downloaded_file_name,
                                     language=lang_code)
    try:
        ParsedText = test_file["ParsedResults"][0]["ParsedText"]
    except BaseException:
        await event.edit(f"`{JAVES_NNAME}:` **Couldn't read it.`\n`Is api key entered correct?**")
    else:
        await event.edit(f"`{JAVES_NNAME}:` **Here's what I could read from it:**\n\n{ParsedText}"
                         )
    os.remove(downloaded_file_name)

@javes05(outgoing=True, pattern="^!stop$")
async def iqless(e):
    await e.edit(f"`{JAVES_NNAME}`: **comand !stop changed to !offauto**")      

   

@javes05(outgoing=True, pattern="^!lydia$")
async def repcf(event):
 if LYDIA_API_KEY is None:
	  await event.edit(f"`{JAVES_NNAME}:` **lydia api key missing please add it before use**")
 else:
    if event.fwd_from:
        return
    await event.edit(f"`{JAVES_NNAME}:` **connecting lydia apikey.......**")
    try:
        session = lydia.create_session()
        session_id = session.id
        reply = await event.get_reply_message()
        msg = reply.text
        text_rep = session.think_thought(msg)
        await event.edit("**Lydia says**: {0}".format(text_rep))
    except Exception as e:
        await event.edit(str(e))

@javes05(outgoing=True, disable_errors=True, pattern="^!auto$")
async def addcf(event):
 if LYDIA_API_KEY is None:
	 await event.edit(f"`{JAVES_NNAME}:` **lydia api key missing please add it before use**")
 else:  
      if event.fwd_from:
          return
      await event.edit(f"`{JAVES_NNAME}:` **Running...**")
      await asyncio.sleep(4)
      await event.edit(f"`{JAVES_NNAME}:` **Connecting api key.......**")
      reply_msg = await event.get_reply_message()
      if reply_msg:
          session = lydia.create_session()
          session_id = session.id
          if reply_msg.from_id is None:
              return await event.edit(f"`{JAVES_NNAME}:` **Invalid user type.**")
          ACC_LYDIA.update({(event.chat_id & reply_msg.from_id): session})
          await event.edit("Auto reply activated this  user: {} in chat: {}".format(str(reply_msg.from_id), str(event.chat_id)))
      else:
          await event.edit(f"`{JAVES_NNAME}:` **Tag any user's message to activate on them**")

@javes05(outgoing=True, disable_errors=True, pattern="^!offauto$")
async def remcf(event):
    if event.fwd_from:
        return
    await event.edit(f"`{JAVES_NNAME}:` **Running..**")
    await asyncio.sleep(4)
    await event.edit(f"`{JAVES_NNAME}:` **Processing...**")
    reply_msg = await event.get_reply_message()
    try:
        del ACC_LYDIA[event.chat_id & reply_msg.from_id]
        await event.edit(" Auto reply disabled for user: {} in chat: {}".format(str(reply_msg.from_id), str(event.chat_id)))
    except Exception:
        await event.edit(f"`{JAVES_NNAME}:` **This person does not have activated auto reply on him/her.**")

@javes05(incoming=True, disable_errors=True, disable_edited=True)
async def user(event):
    user_text = event.text    
    try:
        session = ACC_LYDIA[event.chat_id & event.from_id]
        msg = event.text
        async with event.client.action(event.chat_id, "typing"):
            text_rep = session.think_thought(msg)
            wait_time = 0
            for i in range(len(text_rep)):
                wait_time = wait_time + 0.1
            await asyncio.sleep(wait_time)
            await event.reply(text_rep)
    except (KeyError, TypeError):
        return


@javes05(outgoing=True, pattern="^\!rbg(?: |$)(.*)")
async def kbg(remob):
    """ For .rbg command, Remove Image Background. """
    if REM_BG_API_KEY is None:
        await remob.edit(
            f"`{JAVES_NNAME}:` **Error: Remove.BG API key missing! Add it to environment vars or config.env.**"
        )
        return
    input_str = remob.pattern_match.group(1)
    message_id = remob.message.id
    if remob.reply_to_msg_id:
        message_id = remob.reply_to_msg_id
        reply_message = await remob.get_reply_message()
        await remob.edit(f"`{JAVES_NNAME}:` **Connecting api key......**")
        try:
            if isinstance(
                    reply_message.media, MessageMediaPhoto
            ) or "image" in reply_message.media.document.mime_type.split('/'):
                downloaded_file_name = await remob.client.download_media(
                    reply_message, TEMP_DOWNLOAD_DIRECTORY)
                await remob.edit(f"`{JAVES_NNAME}:` **Removing background from this image..**")
                output_file_name = await ReTrieveFile(downloaded_file_name)
                os.remove(downloaded_file_name)
            else:
                await remob.edit(f"`{JAVES_NNAME}:` **Error**"
                                 )
        except Exception as e:
            await remob.edit(str(e))
            return
    elif input_str:
        await remob.edit(
            f"`Removing background from online image hosted at`\n{input_str}")
        output_file_name = await ReTrieveURL(input_str)
    else:
        await remob.edit(f"`{JAVES_NNAME}:` **I need something to remove the background from.**")
        return
    contentType = output_file_name.headers.get("content-type")
    if "image" in contentType:
        with io.BytesIO(output_file_name.content) as remove_bg_image:
            remove_bg_image.name = "removed_bg.png"
            await remob.client.send_file(
                remob.chat_id,
                remove_bg_image,
                caption="Background removed ",
                force_document=True,
                reply_to=message_id)
            await remob.delete()
    else:
        await remob.edit("**Error (Invalid API key, I guess ?)**\n`{}`".format(
            output_file_name.content.decode("UTF-8")))


# this method will call the API, and return in the appropriate format
# with the name provided.
async def ReTrieveFile(input_file_name):
    headers = {
        "X-API-Key": REM_BG_API_KEY,
    }
    files = {
        "image_file": (input_file_name, open(input_file_name, "rb")),
    }
    r = requests.post("https://api.remove.bg/v1.0/removebg",
                      headers=headers,
                      files=files,
                      allow_redirects=True,
                      stream=True)
    return r


async def ReTrieveURL(input_url):
    headers = {
        "X-API-Key": REM_BG_API_KEY,
    }
    data = {"image_url": input_url}
    r = requests.post("https://api.remove.bg/v1.0/removebg",
                      headers=headers,
                      data=data,
                      allow_redirects=True,
                      stream=True)
    return r


# ===== CONSTANT =====
if WEATHER_DEFCITY:
    DEFCITY = WEATHER_DEFCITY
else:
    DEFCITY = None
# ====================


async def get_tz(con):
    """ Get time zone of the given country. """
    """ Credits: @aragon12 and @zakaryan2004. """
    for c_code in c_n:
        if con == c_n[c_code]:
            return tz(c_tz[c_code][0])
    try:
        if c_n[con]:
            return tz(c_tz[con][0])
    except KeyError:
        return


@javes05(outgoing=True, pattern="^!weather(?: |$)(.*)")
async def get_weather(weather):
    """ For .weather command, gets the current weather of a city. """

    if not OWM_API:
        await weather.edit(
            f"`{JAVES_NNAME}:` **Get an API key from** https://openweathermap.org/ `first.`")
        return

    APPID = OWM_API

    if not weather.pattern_match.group(1):
        CITY = DEFCITY
        if not CITY:
            await weather.edit(
                f"`{JAVES_NNAME}:` **Please specify a city or set one as default using the WEATHER_DEFCITY config variable.**"
            )
            return
    else:
        CITY = weather.pattern_match.group(1)

    timezone_countries = {
        timezone: country
        for country, timezones in c_tz.items() for timezone in timezones
    }

    if "," in CITY:
        newcity = CITY.split(",")
        if len(newcity[1]) == 2:
            CITY = newcity[0].strip() + "," + newcity[1].strip()
        else:
            country = await get_tz((newcity[1].strip()).title())
            try:
                countrycode = timezone_countries[f'{country}']
            except KeyError:
                await weather.edit("`Invalid country.`")
                return
            CITY = newcity[0].strip() + "," + countrycode.strip()

    url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={APPID}'
    request = get(url)
    result = json.loads(request.text)

    if request.status_code != 200:
        await weather.edit(f"`Invalid country.`")
        return

    cityname = result['name']
    curtemp = result['main']['temp']
    humidity = result['main']['humidity']
    min_temp = result['main']['temp_min']
    max_temp = result['main']['temp_max']
    desc = result['weather'][0]
    desc = desc['main']
    country = result['sys']['country']
    sunrise = result['sys']['sunrise']
    sunset = result['sys']['sunset']
    wind = result['wind']['speed']
    winddir = result['wind']['deg']

    ctimezone = tz(c_tz[country][0])
    time = datetime.now(ctimezone).strftime("%A, %I:%M %p")
    fullc_n = c_n[f"{country}"]

    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

    div = (360 / len(dirs))
    funmath = int((winddir + (div / 2)) / div)
    findir = dirs[funmath % len(dirs)]
    kmph = str(wind * 3.6).split(".")
    mph = str(wind * 2.237).split(".")

    def fahrenheit(f):
        temp = str(((f - 273.15) * 9 / 5 + 32)).split(".")
        return temp[0]

    def celsius(c):
        temp = str((c - 273.15)).split(".")
        return temp[0]

    def sun(unix):
        xx = datetime.fromtimestamp(unix, tz=ctimezone).strftime("%I:%M %p")
        return xx

    await weather.edit(
        f"**Temperature:** `{celsius(curtemp)}Â°C | {fahrenheit(curtemp)}Â°F`\n"
        +
        f"**Min. Temp.:** `{celsius(min_temp)}Â°C | {fahrenheit(min_temp)}Â°F`\n"
        +
        f"**Max. Temp.:** `{celsius(max_temp)}Â°C | {fahrenheit(max_temp)}Â°F`\n"
        + f"**Humidity:** `{humidity}%`\n" +
        f"**Wind:** `{kmph[0]} kmh | {mph[0]} mph, {findir}`\n" +
        f"**Sunrise:** `{sun(sunrise)}`\n" +
        f"**Sunset:** `{sun(sunset)}`\n\n" + f"**{desc}**\n" +
        f"`{cityname}, {fullc_n}`\n" + f"`{time}`")




@javes05(outgoing=True, pattern="^\!youtube (.*)")
async def yt_search(video_q):
    
    query = video_q.pattern_match.group(1)
    result = ''

    if not YOUTUBE_API_KEY:
        await video_q.edit(
            f"`{JAVES_NNAME}:` **Error: YouTube API key missing! Add it to environment vars or config.env.**"
        )
        return

    await video_q.edit(f"`{JAVES_NNAME}:` **Connecting api key.....**")

    full_response = await youtube_search(query)
    videos_json = full_response[1]

    for video in videos_json:
        title = f"{unescape(video['snippet']['title'])}"
        link = f"https://youtu.be/{video['id']['videoId']}"
        result += f"{title}\n{link}\n\n"

    reply_text = f"**Search Query:**\n`{query}`\n\n**Results:**\n\n{result}"

    await video_q.edit(reply_text)


async def youtube_search(query,
                         order="relevance",
                         token=None,
                         location=None,
                         location_radius=None):
    """ Do a YouTube search. """
    youtube = build('youtube',
                    'v3',
                    developerKey=YOUTUBE_API_KEY,
                    cache_discovery=False)
    search_response = youtube.search().list(
        q=query,
        type="video",
        pageToken=token,
        order=order,
        part="id,snippet",
        maxResults=10,
        location=location,
        locationRadius=location_radius).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result)
    try:
        nexttok = search_response["nextPageToken"]
        return (nexttok, videos)
    except HttpError:
        nexttok = "last_page"
        return (nexttok, videos)
    except KeyError:
        nexttok = "KeyError, try again."
        return (nexttok, videos)

@javes.on(rekcah05(pattern=f"read(?: |$)(.*)", allow_sudo=True))
async def ocr(event):
 if OCR_SPACE_API_KEY is None:
	 await event.reply(f"`{JAVES_NNAME}:` **ocr api key missing please add it before use**")
 else:
    await event.reply(f"`{JAVES_NNAME}:` **Reading...**")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    lang_code = event.pattern_match.group(1)
    downloaded_file_name = await bot.download_media(
        await event.get_reply_message(), TEMP_DOWNLOAD_DIRECTORY)
    test_file = await ocr_space_file(filename=downloaded_file_name,
                                     language=lang_code)
    try:
        ParsedText = test_file["ParsedResults"][0]["ParsedText"]
    except BaseException:
        await event.reply(f"`{JAVES_NNAME}:` **Couldn't read it.`\n`Is api key entered correct?**")
    else:
        await event.reply(f"`{JAVES_NNAME}:` **Here's what I could read from it:**\n\n{ParsedText}"
                         )
    os.remove(downloaded_file_name)

@javes05(outgoing=True, pattern="^!stop$")
async def iqless(e):
    await e.reply(f"`{JAVES_NNAME}`: **comand !stop changed to !offauto**")      

   
@javes.on(rekcah05(pattern=f"lydia$", allow_sudo=True))
async def repcf(event):
 if LYDIA_API_KEY is None:
	  await event.reply(f"`{JAVES_NNAME}:` **lydia api key missing please add it before use**")
 else:
    if event.fwd_from:
        return
    #await event.reply(f"`{JAVES_NNAME}:` **connecting lydia apikey.......**")
    try:
        session = lydia.create_session()
        session_id = session.id
        reply = await event.get_reply_message()
        msg = reply.text
        text_rep = session.think_thought(msg)
        await event.reply("**Lydia says**: {0}".format(text_rep))
    except Exception as e:
        await event.reply(str(e))

@javes.on(rekcah05(pattern=f"auto$", allow_sudo=True))
async def addcf(event):
 if LYDIA_API_KEY is None:
	 await event.reply(f"`{JAVES_NNAME}:` **lydia api key missing please add it before use**")
 else:  
      if event.fwd_from:
          return
      #await event.reply(f"`{JAVES_NNAME}:` **Running...**")
      await asyncio.sleep(4)
      await event.reply(f"`{JAVES_NNAME}:` **Connecting api key.......**")
      reply_msg = await event.get_reply_message()
      if reply_msg:
          session = lydia.create_session()
          session_id = session.id
          if reply_msg.from_id is None:
              return await event.reply(f"`{JAVES_NNAME}:` **Invalid user type.**")
          ACC_LYDIA.update({(event.chat_id & reply_msg.from_id): session})
          await event.reply("Auto reply activated this  user: {} in chat: {}".format(str(reply_msg.from_id), str(event.chat_id)))
      else:
          await event.reply(f"`{JAVES_NNAME}:` **Tag any user's message to activate on them**")


@javes.on(rekcah05(pattern=f"offauto$", allow_sudo=True))
async def remcf(event):
    if event.fwd_from:
        return
    #await event.reply(f"`{JAVES_NNAME}:` **Running..**")
    await asyncio.sleep(4)
    await event.reply(f"`{JAVES_NNAME}:` **Processing...**")
    reply_msg = await event.get_reply_message()
    try:
        del ACC_LYDIA[event.chat_id & reply_msg.from_id]
        await event.reply(" Auto reply disabled for user: {} in chat: {}".format(str(reply_msg.from_id), str(event.chat_id)))
    except Exception:
        await event.reply(f"`{JAVES_NNAME}:` **This person does not have activated auto reply on him/her.**")

@javes.on(rekcah05(pattern=f"rbg(?: |$)(.*)", allow_sudo=True))
async def kbg(remob):
    """ For .rbg command, Remove Image Background. """
    if REM_BG_API_KEY is None:
        await remob.reply(
            f"`{JAVES_NNAME}:` **Error: Remove.BG API key missing! Add it to environment vars or config.env.**"
        )
        return
    input_str = remob.pattern_match.group(1)
    message_id = remob.message.id
    if remob.reply_to_msg_id:
        message_id = remob.reply_to_msg_id
        reply_message = await remob.get_reply_message()
        await remob.reply(f"`{JAVES_NNAME}:` **Connecting api key......**")
        try:
            if isinstance(
                    reply_message.media, MessageMediaPhoto
            ) or "image" in reply_message.media.document.mime_type.split('/'):
                downloaded_file_name = await remob.client.download_media(
                    reply_message, TEMP_DOWNLOAD_DIRECTORY)
                await remob.reply(f"`{JAVES_NNAME}:` **Removing background from this image..**")
                output_file_name = await ReTrieveFile(downloaded_file_name)
                os.remove(downloaded_file_name)
            else:
                await remob.reply(f"`{JAVES_NNAME}:` **Error**"
                                 )
        except Exception as e:
            await remob.reply(str(e))
            return
    elif input_str:
        await remob.reply(
            f"`Removing background from online image hosted at`\n{input_str}")
        output_file_name = await ReTrieveURL(input_str)
    else:
        await remob.reply(f"`{JAVES_NNAME}:` **I need something to remove the background from.**")
        return
    contentType = output_file_name.headers.get("content-type")
    if "image" in contentType:
        with io.BytesIO(output_file_name.content) as remove_bg_image:
            remove_bg_image.name = "removed_bg.png"
            await remob.client.send_file(
                remob.chat_id,
                remove_bg_image,
                caption="Background removed ",
                force_document=True,
                reply_to=message_id)
            await remob.delete()
    else:
        await remob.reply("**Error (Invalid API key, I guess ?)**\n`{}`".format(
            output_file_name.content.decode("UTF-8")))


# this method will call the API, and return in the appropriate format
# with the name provided.
async def ReTrieveFile(input_file_name):
    headers = {
        "X-API-Key": REM_BG_API_KEY,
    }
    files = {
        "image_file": (input_file_name, open(input_file_name, "rb")),
    }
    r = requests.post("https://api.remove.bg/v1.0/removebg",
                      headers=headers,
                      files=files,
                      allow_redirects=True,
                      stream=True)
    return r


async def ReTrieveURL(input_url):
    headers = {
        "X-API-Key": REM_BG_API_KEY,
    }
    data = {"image_url": input_url}
    r = requests.post("https://api.remove.bg/v1.0/removebg",
                      headers=headers,
                      data=data,
                      allow_redirects=True,
                      stream=True)
    return r


# ===== CONSTANT =====
if WEATHER_DEFCITY:
    DEFCITY = WEATHER_DEFCITY
else:
    DEFCITY = None
# ====================


async def get_tz(con):
    """ Get time zone of the given country. """
    """ Credits: @aragon12 and @zakaryan2004. """
    for c_code in c_n:
        if con == c_n[c_code]:
            return tz(c_tz[c_code][0])
    try:
        if c_n[con]:
            return tz(c_tz[con][0])
    except KeyError:
        return

@javes.on(rekcah05(pattern=f"weather(?: |$)(.*)", allow_sudo=True))
async def get_weather(weather):
    """ For .weather command, gets the current weather of a city. """

    if not OWM_API:
        await weather.reply(
            f"`{JAVES_NNAME}:` **Get an API key from** https://openweathermap.org/ `first.`")
        return

    APPID = OWM_API

    if not weather.pattern_match.group(1):
        CITY = DEFCITY
        if not CITY:
            await weather.reply(
                f"`{JAVES_NNAME}:` **Please specify a city or set one as default using the WEATHER_DEFCITY config variable.**"
            )
            return
    else:
        CITY = weather.pattern_match.group(1)

    timezone_countries = {
        timezone: country
        for country, timezones in c_tz.items() for timezone in timezones
    }

    if "," in CITY:
        newcity = CITY.split(",")
        if len(newcity[1]) == 2:
            CITY = newcity[0].strip() + "," + newcity[1].strip()
        else:
            country = await get_tz((newcity[1].strip()).title())
            try:
                countrycode = timezone_countries[f'{country}']
            except KeyError:
                await weather.reply("`Invalid country.`")
                return
            CITY = newcity[0].strip() + "," + countrycode.strip()

    url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={APPID}'
    request = get(url)
    result = json.loads(request.text)

    if request.status_code != 200:
        await weather.reply(f"`Invalid country.`")
        return

    cityname = result['name']
    curtemp = result['main']['temp']
    humidity = result['main']['humidity']
    min_temp = result['main']['temp_min']
    max_temp = result['main']['temp_max']
    desc = result['weather'][0]
    desc = desc['main']
    country = result['sys']['country']
    sunrise = result['sys']['sunrise']
    sunset = result['sys']['sunset']
    wind = result['wind']['speed']
    winddir = result['wind']['deg']

    ctimezone = tz(c_tz[country][0])
    time = datetime.now(ctimezone).strftime("%A, %I:%M %p")
    fullc_n = c_n[f"{country}"]

    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

    div = (360 / len(dirs))
    funmath = int((winddir + (div / 2)) / div)
    findir = dirs[funmath % len(dirs)]
    kmph = str(wind * 3.6).split(".")
    mph = str(wind * 2.237).split(".")

    def fahrenheit(f):
        temp = str(((f - 273.15) * 9 / 5 + 32)).split(".")
        return temp[0]

    def celsius(c):
        temp = str((c - 273.15)).split(".")
        return temp[0]

    def sun(unix):
        xx = datetime.fromtimestamp(unix, tz=ctimezone).strftime("%I:%M %p")
        return xx

    await weather.reply(
        f"**Temperature:** `{celsius(curtemp)}Â°C | {fahrenheit(curtemp)}Â°F`\n"
        +
        f"**Min. Temp.:** `{celsius(min_temp)}Â°C | {fahrenheit(min_temp)}Â°F`\n"
        +
        f"**Max. Temp.:** `{celsius(max_temp)}Â°C | {fahrenheit(max_temp)}Â°F`\n"
        + f"**Humidity:** `{humidity}%`\n" +
        f"**Wind:** `{kmph[0]} kmh | {mph[0]} mph, {findir}`\n" +
        f"**Sunrise:** `{sun(sunrise)}`\n" +
        f"**Sunset:** `{sun(sunset)}`\n\n" + f"**{desc}**\n" +
        f"`{cityname}, {fullc_n}`\n" + f"`{time}`")



@javes.on(rekcah05(pattern=f"youtube (.*)", allow_sudo=True))
async def yt_search(video_q):
    
    query = video_q.pattern_match.group(1)
    result = ''

    if not YOUTUBE_API_KEY:
        await video_q.reply(
            f"`{JAVES_NNAME}:` **Error: YouTube API key missing! Add it to environment vars or config.env.**"
        )
        return

    await video_q.reply(f"`{JAVES_NNAME}:` **Connecting api key.....**")

    full_response = await youtube_search(query)
    videos_json = full_response[1]

    for video in videos_json:
        title = f"{unescape(video['snippet']['title'])}"
        link = f"https://youtu.be/{video['id']['videoId']}"
        result += f"{title}\n{link}\n\n"

    reply_text = f"**Search Query:**\n`{query}`\n\n**Results:**\n\n{result}"

    await video_q.reply(reply_text)


async def youtube_search(query,
                         order="relevance",
                         token=None,
                         location=None,
                         location_radius=None):
    """ Do a YouTube search. """
    youtube = build('youtube',
                    'v3',
                    developerKey=YOUTUBE_API_KEY,
                    cache_discovery=False)
    search_response = youtube.search().list(
        q=query,
        type="video",
        pageToken=token,
        order=order,
        part="id,snippet",
        maxResults=10,
        location=location,
        locationRadius=location_radius).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result)
    try:
        nexttok = search_response["nextPageToken"]
        return (nexttok, videos)
    except HttpError:
        nexttok = "last_page"
        return (nexttok, videos)
    except KeyError:
        nexttok = "KeyError, try again."
        return (nexttok, videos)


@javes.on(rekcah05(pattern=f"read(?: |$)(.*)", allow_sudo=True))
async def ocr(event):
 if OCR_SPACE_API_KEY is None:
	 await event.reply(f"`{JAVES_NNAME}:` **ocr api key missing please add it before use**")
 else:
    await event.reply(f"`{JAVES_NNAME}:` **Reading...**")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    lang_code = event.pattern_match.group(1)
    downloaded_file_name = await bot.download_media(
        await event.get_reply_message(), TEMP_DOWNLOAD_DIRECTORY)
    test_file = await ocr_space_file(filename=downloaded_file_name,
                                     language=lang_code)
    try:
        ParsedText = test_file["ParsedResults"][0]["ParsedText"]
    except BaseException:
        await event.reply(f"`{JAVES_NNAME}:` **Couldn't read it.`\n`Is api key entered correct?**")
    else:
        await event.reply(f"`{JAVES_NNAME}:` **Here's what I could read from it:**\n\n{ParsedText}"
                         )
    os.remove(downloaded_file_name)


