import asyncio
import pyfiglet
import asyncio
import io
from datetime import datetime as dt
from pytz import country_names as c_n
from pytz import country_timezones as c_tz
from pytz import timezone as tz
from userbot import CMD_HELP, COUNTRY, TZ_NUMBER
from userbot.events import register
import asyncio
from asyncio import wait, sleep
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import register
import traceback
from re import match
from selenium import webdriver
from asyncio import sleep
from selenium.webdriver.chrome.options import Options
from userbot.events import register
from userbot import GOOGLE_CHROME_BIN, CHROME_DRIVER, CMD_HELP
import io
import os
import urllib
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
from telethon.tl.types import MessageMediaPhoto
from PIL import Image
from asyncio import sleep
from pylast import User, WSError
from re import sub
from urllib import parse
from os import environ
from sys import setrecursionlimit
import os
import asyncio
import qrcode
import barcode
from barcode.writer import ImageWriter
from bs4 import BeautifulSoup
from telethon.errors import AboutTooLongError
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import User as Userbot
from telethon.errors.rpcerrorlist import FloodWaitError
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID, DEFAULT_BIO, BIO_PREFIX, lastfm, LASTFM_USERNAME, bot
from userbot.events import register
from subprocess import PIPE
from subprocess import run as runapp
import pybase64
from userbot import CMD_HELP
from userbot.events import register 
from getpass import getuser
from os import remove
from sys import executable
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID
from userbot.events import register
from telethon import events, functions
from userbot import CMD_HELP
from userbot.events import register
import sys
from requests import get, post, exceptions
import asyncio
import os
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, LOGS, TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register
from os import popen
import re
import urllib.parse
import json
from random import choice
import requests
from bs4 import BeautifulSoup
from humanize import naturalsize
import re
from requests import get
from bs4 import BeautifulSoup
from userbot import CMD_HELP
from userbot.events import register
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import register
from userbot import bot, CMD_HELP

@register(outgoing=True, pattern="^!figlet(?: |$)(.*)")
async def figlet(event):
    if event.fwd_from:
        return
    CMD_FIG = {"slant": "slant", "3D": "3-d", "5line": "5lineoblique", "alpha": "alphabet", "banner": "banner3-D", "doh": "doh", "iso": "isometric1", "letter": "letters", "allig": "alligator", "dotm": "dotmatrix", "bubble": "bubble", "bulb": "bulbhead", "digi": "digital"}
    input_str = event.pattern_match.group(1)
    if "|" in input_str:
        text, cmd = input_str.split("|", maxsplit=1)
    elif input_str is not None:
        cmd = None
        text = input_str
    else:
        await event.edit("Please add some text to figlet")
        return
    if cmd is not None:
        try:
            font = CMD_FIG[cmd]
        except KeyError:
            await event.edit("Invalid selected font.")
            return
        result = pyfiglet.figlet_format(text, font=font)
    else:
        result = pyfiglet.figlet_format(text)
    await event.respond("‌‌‎`{}`".format(result))
    await event.delete()
    
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

GITHUB = 'https://github.com'
DEVICES_DATA = 'https://raw.githubusercontent.com/androidtrackers/' \
               'certified-android-devices/master/devices.json'


@register(outgoing=True, pattern="^\!magisk$")
async def magisk(request):
    """ magisk latest releases """
    magisk_dict = {
        "Stable":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/master/stable.json",
        "Beta":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/master/beta.json",
        "Canary (Release)":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/canary/release.json",
        "Canary (Debug)":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/canary/debug.json"
    }
    releases = 'Latest Magisk Releases:\n'
    for name, release_url in magisk_dict.items():
        data = get(release_url).json()
        releases += f'{name}: [ZIP v{data["magisk"]["version"]}]({data["magisk"]["link"]}) | ' \
                    f'[APK v{data["app"]["version"]}]({data["app"]["link"]}) | ' \
                    f'[Uninstaller]({data["uninstaller"]["link"]})\n'
    await request.edit(releases)


@register(outgoing=True, pattern=r"^\!device(?: |$)(\S*)")
async def device_info(request):
    """ get android device basic info from its codename """
    textx = await request.get_reply_message()
    device = request.pattern_match.group(1)
    if device:
        pass
    elif textx:
        device = textx.text
    else:
        await request.edit("`Usage: .device <codename> / <model>`")
        return
    found = [
        i for i in get(DEVICES_DATA).json()
        if i["device"] == device or i["model"] == device
    ]
    if found:
        reply = f'Search results for {device}:\n\n'
        for item in found:
            brand = item['brand']
            name = item['name']
            codename = item['device']
            model = item['model']
            reply += f'{brand} {name}\n' \
                f'**Codename**: `{codename}`\n' \
                f'**Model**: {model}\n\n'
    else:
        reply = f"`Couldn't find info about {device}!`\n"
    await request.edit(reply)


@register(outgoing=True, pattern=r"^\!codename(?: |)([\S]*)(?: |)([\s\S]*)")
async def codename_info(request):
    """ search for android codename """
    textx = await request.get_reply_message()
    brand = request.pattern_match.group(1).lower()
    device = request.pattern_match.group(2).lower()
    if brand and device:
        pass
    elif textx:
        brand = textx.text.split(' ')[0]
        device = ' '.join(textx.text.split(' ')[1:])
    else:
        await request.edit("`Usage: .codename <brand> <device>`")
        return
    found = [
        i for i in get(DEVICES_DATA).json()
        if i["brand"].lower() == brand and device in i["name"].lower()
    ]
    if len(found) > 8:
        found = found[:8]
    if found:
        reply = f'Search results for {brand.capitalize()} {device.capitalize()}:\n\n'
        for item in found:
            brand = item['brand']
            name = item['name']
            codename = item['device']
            model = item['model']
            reply += f'{brand} {name}\n' \
                f'**Codename**: `{codename}`\n' \
                f'**Model**: {model}\n\n'
    else:
        reply = f"`Couldn't find {device} codename!`\n"
    await request.edit(reply)


@register(outgoing=True, pattern=r"^\!specs(?: |)([\S]*)(?: |)([\s\S]*)")
async def devices_specifications(request):
    """ Mobile devices specifications """
    textx = await request.get_reply_message()
    brand = request.pattern_match.group(1).lower()
    device = request.pattern_match.group(2).lower()
    if brand and device:
        pass
    elif textx:
        brand = textx.text.split(' ')[0]
        device = ' '.join(textx.text.split(' ')[1:])
    else:
        await request.edit("`Usage: .specs <brand> <device>`")
        return
    all_brands = BeautifulSoup(
        get('https://www.devicespecifications.com/en/brand-more').content,
        'lxml').find('div', {
            'class': 'brand-listing-container-news'
        }).findAll('a')
    brand_page_url = None
    try:
        brand_page_url = [
            i['href'] for i in all_brands if brand == i.text.strip().lower()
        ][0]
    except IndexError:
        await request.edit(f'`{brand} is unknown brand!`')
    devices = BeautifulSoup(get(brand_page_url).content, 'lxml') \
        .findAll('div', {'class': 'model-listing-container-80'})
    device_page_url = None
    try:
        device_page_url = [
            i.a['href']
            for i in BeautifulSoup(str(devices), 'lxml').findAll('h3')
            if device in i.text.strip().lower()
        ]
    except IndexError:
        await request.edit(f"`can't find {device}!`")
    if len(device_page_url) > 2:
        device_page_url = device_page_url[:2]
    reply = ''
    for url in device_page_url:
        info = BeautifulSoup(get(url).content, 'lxml')
        reply = '\n**' + info.title.text.split('-')[0].strip() + '**\n\n'
        info = info.find('div', {'id': 'model-brief-specifications'})
        specifications = re.findall(r'<b>.*?<br/>', str(info))
        for item in specifications:
            title = re.findall(r'<b>(.*?)</b>', item)[0].strip()
            data = re.findall(r'</b>: (.*?)<br/>', item)[0]\
                .replace('<b>', '').replace('</b>', '').strip()
            reply += f'**{title}**: {data}\n'
    await request.edit(reply)


@register(outgoing=True, pattern=r"^\!twrp(?: |$)(\S*)")
async def twrp(request):
    """ get android device twrp """
    textx = await request.get_reply_message()
    device = request.pattern_match.group(1)
    if device:
        pass
    elif textx:
        device = textx.text.split(' ')[0]
    else:
        await request.edit("`Usage: .twrp <codename>`")
        return
    url = get(f'https://dl.twrp.me/{device}/')
    if url.status_code == 404:
        reply = f"`Couldn't find twrp downloads for {device}!`\n"
        await request.edit(reply)
        return
    page = BeautifulSoup(url.content, 'lxml')
    download = page.find('table').find('tr').find('a')
    dl_link = f"https://dl.twrp.me{download['href']}"
    dl_file = download.text
    size = page.find("span", {"class": "filesize"}).text
    date = page.find("em").text.strip()
    reply = f'**Latest TWRP for {device}:**\n' \
        f'[{dl_file}]({dl_link}) - __{size}__\n' \
        f'**Updated:** __{date}__\n'
    await request.edit(reply)

@register(outgoing=True, pattern=r"^\!direct(?: |$)([\s\S]*)")
async def direct_link_generator(request):
    """ direct links generator """
    await request.edit("`Processing...`")
    textx = await request.get_reply_message()
    message = request.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await request.edit("`Usage: .direct <url>`")
        return
    reply = ''
    links = re.findall(r'\bhttps?://.*\.\S+', message)
    if not links:
        reply = "`No links found!`"
        await request.edit(reply)
    for link in links:
        if 'drive.google.com' in link:
            reply += gdrive(link)
        elif 'zippyshare.com' in link:
            reply += zippy_share(link)
        elif 'mega.' in link:
            reply += mega_dl(link)
        elif 'yadi.sk' in link:
            reply += yandex_disk(link)
        elif 'cloud.mail.ru' in link:
            reply += cm_ru(link)
        elif 'mediafire.com' in link:
            reply += mediafire(link)
        elif 'sourceforge.net' in link:
            reply += sourceforge(link)
        elif 'osdn.net' in link:
            reply += osdn(link)
        elif 'github.com' in link:
            reply += github(link)
        elif 'androidfilehost.com' in link:
            reply += androidfilehost(link)
        else:
            reply += re.findall(r"\bhttps?://(.*?[^/]+)",
                                link)[0] + 'is not supported'
    await request.edit(reply)


def gdrive(url: str) -> str:
    """ GDrive direct links generator """
    drive = 'https://drive.google.com'
    try:
        link = re.findall(r'\bhttps?://drive\.google\.com\S+', url)[0]
    except IndexError:
        reply = "`No Google drive links found`\n"
        return reply
    file_id = ''
    reply = ''
    if link.find("view") != -1:
        file_id = link.split('/')[-2]
    elif link.find("open?id=") != -1:
        file_id = link.split("open?id=")[1].strip()
    elif link.find("uc?id=") != -1:
        file_id = link.split("uc?id=")[1].strip()
    url = f'{drive}/uc?export=download&id={file_id}'
    download = requests.get(url, stream=True, allow_redirects=False)
    cookies = download.cookies
    try:
        # In case of small file size, Google downloads directly
        dl_url = download.headers["location"]
        if 'accounts.google.com' in dl_url:  # non-public file
            reply += '`Link is not public!`\n'
            return reply
        name = 'Direct Download Link'
    except KeyError:
        # In case of download warning page
        page = BeautifulSoup(download.content, 'lxml')
        export = drive + page.find('a', {'id': 'uc-download-link'}).get('href')
        name = page.find('span', {'class': 'uc-name-size'}).text
        response = requests.get(export,
                                stream=True,
                                allow_redirects=False,
                                cookies=cookies)
        dl_url = response.headers['location']
        if 'accounts.google.com' in dl_url:
            reply += 'Link is not public!'
            return reply
    reply += f'[{name}]({dl_url})\n'
    return reply


def zippy_share(url: str) -> str:
    """ ZippyShare direct links generator
    Based on https://github.com/LameLemon/ziggy"""
    reply = ''
    dl_url = ''
    try:
        link = re.findall(r'\bhttps?://.*zippyshare\.com\S+', url)[0]
    except IndexError:
        reply = "`No ZippyShare links found`\n"
        return reply
    session = requests.Session()
    base_url = re.search('http.+.com', link).group()
    response = session.get(link)
    page_soup = BeautifulSoup(response.content, "lxml")
    scripts = page_soup.find_all("script", {"type": "text/javascript"})
    for script in scripts:
        if "getElementById('dlbutton')" in script.text:
            url_raw = re.search(r'= (?P<url>\".+\" \+ (?P<math>\(.+\)) .+);',
                                script.text).group('url')
            math = re.search(r'= (?P<url>\".+\" \+ (?P<math>\(.+\)) .+);',
                             script.text).group('math')
            dl_url = url_raw.replace(math, '"' + str(eval(math)) + '"')
            break
    dl_url = base_url + eval(dl_url)
    name = urllib.parse.unquote(dl_url.split('/')[-1])
    reply += f'[{name}]({dl_url})\n'
    return reply


def yandex_disk(url: str) -> str:
    """ Yandex.Disk direct links generator
    Based on https://github.com/wldhx/yadisk-direct"""
    reply = ''
    try:
        link = re.findall(r'\bhttps?://.*yadi\.sk\S+', url)[0]
    except IndexError:
        reply = "`No Yandex.Disk links found`\n"
        return reply
    api = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}'
    try:
        dl_url = requests.get(api.format(link)).json()['href']
        name = dl_url.split('filename=')[1].split('&disposition')[0]
        reply += f'[{name}]({dl_url})\n'
    except KeyError:
        reply += '`Error: File not found / Download limit reached`\n'
        return reply
    return reply


def mega_dl(url: str) -> str:
    """ MEGA.nz direct links generator
    Using https://github.com/tonikelope/megadown"""
    reply = ''
    try:
        link = re.findall(r'\bhttps?://.*mega.*\.nz\S+', url)[0]
    except IndexError:
        reply = "`No MEGA.nz links found`\n"
        return reply
    command = f'bin/megadown -q -m {link}'
    result = popen(command).read()
    try:
        data = json.loads(result)
        print(data)
    except json.JSONDecodeError:
        reply += "`Error: Can't extract the link`\n"
        return reply
    dl_url = data['url']
    name = data['file_name']
    size = naturalsize(int(data['file_size']))
    reply += f'[{name} ({size})]({dl_url})\n'
    return reply


def cm_ru(url: str) -> str:
    """ cloud.mail.ru direct links generator
    Using https://github.com/JrMasterModelBuilder/cmrudl.py"""
    reply = ''
    try:
        link = re.findall(r'\bhttps?://.*cloud\.mail\.ru\S+', url)[0]
    except IndexError:
        reply = "`No cloud.mail.ru links found`\n"
        return reply
    command = f'bin/cmrudl -s {link}'
    result = popen(command).read()
    result = result.splitlines()[-1]
    try:
        data = json.loads(result)
    except json.decoder.JSONDecodeError:
        reply += "`Error: Can't extract the link`\n"
        return reply
    dl_url = data['download']
    name = data['file_name']
    size = naturalsize(int(data['file_size']))
    reply += f'[{name} ({size})]({dl_url})\n'
    return reply


def mediafire(url: str) -> str:
    """ MediaFire direct links generator """
    try:
        link = re.findall(r'\bhttps?://.*mediafire\.com\S+', url)[0]
    except IndexError:
        reply = "`No MediaFire links found`\n"
        return reply
    reply = ''
    page = BeautifulSoup(requests.get(link).content, 'lxml')
    info = page.find('a', {'aria-label': 'Download file'})
    dl_url = info.get('href')
    size = re.findall(r'\(.*\)', info.text)[0]
    name = page.find('div', {'class': 'filename'}).text
    reply += f'[{name} {size}]({dl_url})\n'
    return reply


def sourceforge(url: str) -> str:
    """ SourceForge direct links generator """
    try:
        link = re.findall(r'\bhttps?://.*sourceforge\.net\S+', url)[0]
    except IndexError:
        reply = "`No SourceForge links found`\n"
        return reply
    file_path = re.findall(r'files(.*)/download', link)[0]
    reply = f"Mirrors for __{file_path.split('/')[-1]}__\n"
    project = re.findall(r'projects?/(.*?)/files', link)[0]
    mirrors = f'https://sourceforge.net/settings/mirror_choices?' \
        f'projectname={project}&filename={file_path}'
    page = BeautifulSoup(requests.get(mirrors).content, 'html.parser')
    info = page.find('ul', {'id': 'mirrorList'}).findAll('li')
    for mirror in info[1:]:
        name = re.findall(r'\((.*)\)', mirror.text.strip())[0]
        dl_url = f'https://{mirror["id"]}.dl.sourceforge.net/project/{project}/{file_path}'
        reply += f'[{name}]({dl_url}) '
    return reply


def osdn(url: str) -> str:
    """ OSDN direct links generator """
    osdn_link = 'https://osdn.net'
    try:
        link = re.findall(r'\bhttps?://.*osdn\.net\S+', url)[0]
    except IndexError:
        reply = "`No OSDN links found`\n"
        return reply
    page = BeautifulSoup(
        requests.get(link, allow_redirects=True).content, 'lxml')
    info = page.find('a', {'class': 'mirror_link'})
    link = urllib.parse.unquote(osdn_link + info['href'])
    reply = f"Mirrors for __{link.split('/')[-1]}__\n"
    mirrors = page.find('form', {'id': 'mirror-select-form'}).findAll('tr')
    for data in mirrors[1:]:
        mirror = data.find('input')['value']
        name = re.findall(r'\((.*)\)', data.findAll('td')[-1].text.strip())[0]
        dl_url = re.sub(r'm=(.*)&f', f'm={mirror}&f', link)
        reply += f'[{name}]({dl_url}) '
    return reply


def github(url: str) -> str:
    """ GitHub direct links generator """
    try:
        link = re.findall(r'\bhttps?://.*github\.com.*releases\S+', url)[0]
    except IndexError:
        reply = "`No GitHub Releases links found`\n"
        return reply
    reply = ''
    dl_url = ''
    download = requests.get(url, stream=True, allow_redirects=False)
    try:
        dl_url = download.headers["location"]
    except KeyError:
        reply += "`Error: Can't extract the link`\n"
    name = link.split('/')[-1]
    reply += f'[{name}]({dl_url}) '
    return reply


def androidfilehost(url: str) -> str:
    """ AFH direct links generator """
    try:
        link = re.findall(r'\bhttps?://.*androidfilehost.*fid.*\S+', url)[0]
    except IndexError:
        reply = "`No AFH links found`\n"
        return reply
    fid = re.findall(r'\?fid=(.*)', link)[0]
    session = requests.Session()
    user_agent = useragent()
    headers = {'user-agent': user_agent}
    res = session.get(link, headers=headers, allow_redirects=True)
    headers = {
        'origin': 'https://androidfilehost.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': user_agent,
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-mod-sbb-ctype': 'xhr',
        'accept': '*/*',
        'referer': f'https://androidfilehost.com/?fid={fid}',
        'authority': 'androidfilehost.com',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'submit': 'submit',
        'action': 'getdownloadmirrors',
        'fid': f'{fid}'
    }
    mirrors = None
    reply = ''
    error = "`Error: Can't find Mirrors for the link`\n"
    try:
        req = session.post(
            'https://androidfilehost.com/libs/otf/mirrors.otf.php',
            headers=headers,
            data=data,
            cookies=res.cookies)
        mirrors = req.json()['MIRRORS']
    except (json.decoder.JSONDecodeError, TypeError):
        reply += error
    if not mirrors:
        reply += error
        return reply
    for item in mirrors:
        name = item['name']
        dl_url = item['url']
        reply += f'[{name}]({dl_url}) '
    return reply


def useragent():
    """
    useragent random setter
    """
    useragents = BeautifulSoup(
        requests.get(
            'https://developers.whatismybrowser.com/'
            'useragents/explore/operating_system_name/android/').content,
        'lxml').findAll('td', {'class': 'useragent'})
    user_agent = choice(useragents)
    return user_agent.text
    
    
    
    DOGBIN_URL = "https://del.dog/"


@register(outgoing=True, pattern=r"^\!paste(?: |$)([\s\S]*)")
async def paste(pstl):
    """ For .paste command, pastes the text directly to dogbin. """
    dogbin_final_url = ""
    match = pstl.pattern_match.group(1).strip()
    reply_id = pstl.reply_to_msg_id

    if not match and not reply_id:
        await pstl.edit("`Elon Musk said I cannot paste void.`")
        return

    if match:
        message = match
    elif reply_id:
        message = (await pstl.get_reply_message())
        if message.media:
            downloaded_file_name = await pstl.client.download_media(
                message,
                TEMP_DOWNLOAD_DIRECTORY,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8") + "\r"
            os.remove(downloaded_file_name)
        else:
            message = message.message

    # Dogbin
    await pstl.edit("`Pasting text . . .`")
    resp = post(DOGBIN_URL + "documents", data=message.encode('utf-8'))

    if resp.status_code == 200:
        response = resp.json()
        key = response['key']
        dogbin_final_url = DOGBIN_URL + key

        if response['isUrl']:
            reply_text = ("`Pasted successfully!`\n\n"
                          f"`Shortened URL:` {dogbin_final_url}\n\n"
                          "`Original(non-shortened) URLs`\n"
                          f"`Dogbin URL`: {DOGBIN_URL}v/{key}\n")
        else:
            reply_text = ("`Pasted successfully!`\n\n"
                          f"`Dogbin URL`: {dogbin_final_url}")
    else:
        reply_text = ("`Failed to reach Dogbin`")

    await pstl.edit(reply_text)
    if BOTLOG:
        await pstl.client.send_message(
            BOTLOG_CHATID,
            f"Paste query was executed successfully",
        )


@register(outgoing=True, pattern="^\!getpaste(?: |$)(.*)")
async def get_dogbin_content(dog_url):
    """ For .getpaste command, fetches the content of a dogbin URL. """
    textx = await dog_url.get_reply_message()
    message = dog_url.pattern_match.group(1)
    await dog_url.edit("`Getting dogbin content...`")

    if textx:
        message = str(textx.message)

    format_normal = f'{DOGBIN_URL}'
    format_view = f'{DOGBIN_URL}v/'

    if message.startswith(format_view):
        message = message[len(format_view):]
    elif message.startswith(format_normal):
        message = message[len(format_normal):]
    elif message.startswith("del.dog/"):
        message = message[len("del.dog/"):]
    else:
        await dog_url.edit("`Is that even a dogbin url?`")
        return

    resp = get(f'{DOGBIN_URL}raw/{message}')

    try:
        resp.raise_for_status()
    except exceptions.HTTPError as HTTPErr:
        await dog_url.edit(
            "Request returned an unsuccessful status code.\n\n" + str(HTTPErr))
        return
    except exceptions.Timeout as TimeoutErr:
        await dog_url.edit("Request timed out." + str(TimeoutErr))
        return
    except exceptions.TooManyRedirects as RedirectsErr:
        await dog_url.edit(
            "Request exceeded the configured number of maximum redirections." +
            str(RedirectsErr))
        return

    reply_text = "`Fetched dogbin URL content successfully!`\n\n`Content:` " + resp.text

    await dog_url.edit(reply_text)
    if BOTLOG:
        await dog_url.client.send_message(
            BOTLOG_CHATID,
            "Get dogbin content query was executed successfully",
        )

    
    @register(outgoing=True, pattern="^\!eval(?: |$)(.*)")
async def evaluate(query):
    """ For .eval command, evaluates the given Python expression. """
    if query.is_channel and not query.is_group:
        await query.edit("`Eval isn't permitted on channels`")
        return

    if query.pattern_match.group(1):
        expression = query.pattern_match.group(1)
    else:
        await query.edit("``` Give an expression to evaluate. ```")
        return

    if expression in ("userbot.session", "config.env"):
        await query.edit("`That's a dangerous operation! Not Permitted!`")
        return

    try:
        evaluation = str(eval(expression))
        if evaluation:
            if isinstance(evaluation, str):
                if len(evaluation) >= 4096:
                    file = open("output.txt", "w+")
                    file.write(evaluation)
                    file.close()
                    await query.client.send_file(
                        query.chat_id,
                        "output.txt",
                        reply_to=query.id,
                        caption="`Output too large, sending as file`",
                    )
                    remove("output.txt")
                    return
                await query.edit("**Query: **\n`"
                                 f"{expression}"
                                 "`\n**Result: **\n`"
                                 f"{evaluation}"
                                 "`")
        else:
            await query.edit("**Query: **\n`"
                             f"{expression}"
                             "`\n**Result: **\n`No Result Returned/False`")
    except Exception as err:
        await query.edit("**Query: **\n`"
                         f"{expression}"
                         "`\n**Exception: **\n"
                         f"`{err}`")

    if BOTLOG:
        await query.client.send_message(
            BOTLOG_CHATID,
            f"Eval query {expression} was executed successfully")


@register(outgoing=True, pattern=r"^\!exec(?: |$)([\s\S]*)")
async def run(run_q):
    """ For .exec command, which executes the dynamically created program """
    code = run_q.pattern_match.group(1)

    if run_q.is_channel and not run_q.is_group:
        await run_q.edit("`Exec isn't permitted on channels!`")
        return

    if not code:
        await run_q.edit("``` At least a variable is required to \
execute. Use .help exec for an example.```")
        return

    if code in ("userbot.session", "config.env"):
        await run_q.edit("`That's a dangerous operation! Not Permitted!`")
        return

    if len(code.splitlines()) <= 5:
        codepre = code
    else:
        clines = code.splitlines()
        codepre = clines[0] + "\n" + clines[1] + "\n" + clines[2] + \
            "\n" + clines[3] + "..."

    command = "".join(f"\n {l}" for l in code.split("\n.strip()"))
    process = await asyncio.create_subprocess_exec(
        executable,
        '-c',
        command.strip(),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) \
        + str(stderr.decode().strip())

    if result:
        if len(result) > 4096:
            file = open("output.txt", "w+")
            file.write(result)
            file.close()
            await run_q.client.send_file(
                run_q.chat_id,
                "output.txt",
                reply_to=run_q.id,
                caption="`Output too large, sending as file`",
            )
            remove("output.txt")
            return
        await run_q.edit("**Query: **\n`"
                         f"{codepre}"
                         "`\n**Result: **\n`"
                         f"{result}"
                         "`")
    else:
        await run_q.edit("**Query: **\n`"
                         f"{codepre}"
                         "`\n**Result: **\n`No Result Returned/False`")

    if BOTLOG:
        await run_q.client.send_message(
            BOTLOG_CHATID,
            "Exec query " + codepre + " was executed successfully")


@register(outgoing=True, pattern="^\!term(?: |$)(.*)")
async def terminal_runner(term):
    """ For .term command, runs bash commands and scripts on your server. """
    curruser = getuser()
    command = term.pattern_match.group(1)
    try:
        from os import geteuid
        uid = geteuid()
    except ImportError:
        uid = "This ain't it chief!"

    if term.is_channel and not term.is_group:
        await term.edit("`Term commands aren't permitted on channels!`")
        return

    if not command:
        await term.edit("``` Give a command or use .help term for \
            an example.```")
        return

    if command in ("userbot.session", "config.env"):
        await term.edit("`That's a dangerous operation! Not Permitted!`")
        return

    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) \
        + str(stderr.decode().strip())

    if len(result) > 4096:
        output = open("output.txt", "w+")
        output.write(result)
        output.close()
        await term.client.send_file(
            term.chat_id,
            "output.txt",
            reply_to=term.id,
            caption="`Output too large, sending as file`",
        )
        remove("output.txt")
        return

    if uid == 0:
        await term.edit("`" f"{curruser}:~# {command}" f"\n{result}" "`")
    else:
        await term.edit("`" f"{curruser}:~$ {command}" f"\n{result}" "`")

    if BOTLOG:
        await term.client.send_message(
            BOTLOG_CHATID,
            "Terminal Command " + command + " was executed sucessfully",
        )

@register(outgoing=True, pattern="^\!hash (.*)")
async def gethash(hash_q):
    """ For .hash command, find the md5, sha1, sha256, sha512 of the string. """
    hashtxt_ = hash_q.pattern_match.group(1)
    hashtxt = open("hashdis.txt", "w+")
    hashtxt.write(hashtxt_)
    hashtxt.close()
    md5 = runapp(["md5sum", "hashdis.txt"], stdout=PIPE)
    md5 = md5.stdout.decode()
    sha1 = runapp(["sha1sum", "hashdis.txt"], stdout=PIPE)
    sha1 = sha1.stdout.decode()
    sha256 = runapp(["sha256sum", "hashdis.txt"], stdout=PIPE)
    sha256 = sha256.stdout.decode()
    sha512 = runapp(["sha512sum", "hashdis.txt"], stdout=PIPE)
    runapp(["rm", "hashdis.txt"], stdout=PIPE)
    sha512 = sha512.stdout.decode()
    ans = ("Text: `" + hashtxt_ + "`\nMD5: `" + md5 + "`SHA1: `" + sha1 +
           "`SHA256: `" + sha256 + "`SHA512: `" + sha512[:-1] + "`")
    if len(ans) > 4096:
        hashfile = open("hashes.txt", "w+")
        hashfile.write(ans)
        hashfile.close()
        await hash_q.client.send_file(
            hash_q.chat_id,
            "hashes.txt",
            reply_to=hash_q.id,
            caption="`It's too big, sending a text file instead. `")
        runapp(["rm", "hashes.txt"], stdout=PIPE)
    else:
        await hash_q.reply(ans)


@register(outgoing=True, pattern="^\!base64 (en|de) (.*)")
async def endecrypt(query):
    """ For .base64 command, find the base64 encoding of the given string. """
    if query.pattern_match.group(1) == "en":
        lething = str(
            pybase64.b64encode(bytes(query.pattern_match.group(2),
                                     "utf-8")))[2:]
        await query.reply("Encoded: `" + lething[:-1] + "`")
    else:
        lething = str(
            pybase64.b64decode(bytes(query.pattern_match.group(2), "utf-8"),
                               validate=True))[2:]
        await query.reply("Decoded: `" + lething[:-1] + "`")

@register(pattern=r"^\!decode$", outgoing=True)
async def parseqr(qr_e):
    """ For .decode command, get QR Code/BarCode content from the replied photo. """
    downloaded_file_name = await qr_e.client.download_media(
        await qr_e.get_reply_message())
    # parse the Official ZXing webpage to decode the QRCode
    command_to_exec = [
        "curl", "-X", "POST", "-F", "f=@" + downloaded_file_name + "",
        "https://zxing.org/w/decode"
    ]
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    os.remove(downloaded_file_name)
    if not t_response:
        logger.info(e_response)
        logger.info(t_response)
        await qr_e.edit("Failed to decode.")
        return
    soup = BeautifulSoup(t_response, "html.parser")
    qr_contents = soup.find_all("pre")[0].text
    await qr_e.edit(qr_contents)


@register(pattern=r"^\!barcode(?: |$)([\s\S]*)", outgoing=True)
async def barcode(event):
    """ For .barcode command, genrate a barcode containing the given content. """
    await event.edit("`Processing..`")
    input_str = event.pattern_match.group(1)
    message = "SYNTAX: `.barcode <long text to include>`"
    reply_msg_id = event.message.id
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        reply_msg_id = previous_message.id
        if previous_message.media:
            downloaded_file_name = await event.client.download_media(
                previous_message)
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        event.edit("SYNTAX: `.barcode <long text to include>`")
        return

    bar_code_type = "code128"
    try:
        bar_code_mode_f = barcode.get(bar_code_type,
                                      message,
                                      writer=ImageWriter())
        filename = bar_code_mode_f.save(bar_code_type)
        await event.client.send_file(event.chat_id,
                                     filename,
                                     reply_to=reply_msg_id)
        os.remove(filename)
    except Exception as e:
        await event.edit(str(e))
        return
    await event.delete()


@register(pattern=r"^\!makeqr(?: |$)([\s\S]*)", outgoing=True)
async def make_qr(makeqr):
    """ For .makeqr command, make a QR Code containing the given content. """
    input_str = makeqr.pattern_match.group(1)
    message = "SYNTAX: `.makeqr <long text to include>`"
    reply_msg_id = None
    if input_str:
        message = input_str
    elif makeqr.reply_to_msg_id:
        previous_message = await makeqr.get_reply_message()
        reply_msg_id = previous_message.id
        if previous_message.media:
            downloaded_file_name = await makeqr.client.download_media(
                previous_message)
            m_list = None
            with open(downloaded_file_name, "rb") as file:
                m_list = file.readlines()
            message = ""
            for media in m_list:
                message += media.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(message)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("img_file.webp", "PNG")
    await makeqr.client.send_file(makeqr.chat_id,
                                  "img_file.webp",
                                  reply_to=reply_msg_id)
    os.remove("img_file.webp")
    await makeqr.delete()


    @register(outgoing=True, pattern=r"^\!reverse(?: |$)(\d*)")
async def okgoogle(img):
    """ For .reverse command, Google search images and stickers. """
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")

    message = await img.get_reply_message()
    if message and message.media:
        photo = io.BytesIO()
        await bot.download_media(message, photo)
    else:
        await img.edit("`Reply to photo or sticker nigger.`")
        return

    if photo:
        await img.edit("`Processing...`")
        try:
            image = Image.open(photo)
        except OSError:
            await img.edit('`Unsupported sexuality, most likely.`')
            return
        name = "okgoogle.png"
        image.save(name, "PNG")
        image.close()
        # https://stackoverflow.com/questions/23270175/google-reverse-image-search-using-post-request#28792943
        searchUrl = 'https://www.google.com/searchbyimage/upload'
        multipart = {
            'encoded_image': (name, open(name, 'rb')),
            'image_content': ''
        }
        response = requests.post(searchUrl,
                                 files=multipart,
                                 allow_redirects=False)
        fetchUrl = response.headers['Location']

        if response != 400:
            await img.edit("`Image successfully uploaded to Google. Maybe.`"
                           "\n`Parsing source now. Maybe.`")
        else:
            await img.edit("`Google told me to fuck off.`")
            return

        os.remove(name)
        match = await ParseSauce(fetchUrl +
                                 "&preferences?hl=en&fg=1#languages")
        guess = match['best_guess']
        imgspage = match['similar_images']

        if guess and imgspage:
            await img.edit(f"[{guess}]({fetchUrl})\n\n`Looking for images...`")
        else:
            await img.edit("`Couldn't find anything for your uglyass.`")
            return

        if img.pattern_match.group(1):
            lim = img.pattern_match.group(1)
        else:
            lim = 3
        images = await scam(match, lim)
        yeet = []
        for i in images:
            k = requests.get(i)
            yeet.append(k.content)
        try:
            await img.client.send_file(entity=await
                                       img.client.get_input_entity(img.chat_id
                                                                   ),
                                       file=yeet,
                                       reply_to=img)
        except TypeError:
            pass
        await img.edit(
            f"[{guess}]({fetchUrl})\n\n[Visually similar images]({imgspage})")


async def ParseSauce(googleurl):
    """Parse/Scrape the HTML code for the info we want."""

    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, 'html.parser')

    results = {'similar_images': '', 'best_guess': ''}

    try:
        for similar_image in soup.findAll('input', {'class': 'gLFyf'}):
            url = 'https://www.google.com/search?tbm=isch&q=' + \
                urllib.parse.quote_plus(similar_image.get('value'))
            results['similar_images'] = url
    except BaseException:
        pass

    for best_guess in soup.findAll('div', attrs={'class': 'r5a77d'}):
        results['best_guess'] = best_guess.get_text()

    return results


async def scam(results, lim):

    single = opener.open(results['similar_images']).read()
    decoded = single.decode('utf-8')

    imglinks = []
    counter = 0

    pattern = r'^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$'
    oboi = re.findall(pattern, decoded, re.I | re.M)

    for imglink in oboi:
        counter += 1
        if not counter >= int(lim):
            imglinks.append(imglink)
        else:
            break

    return imglinks

    @register(pattern=r"^\!goss (.*)", outgoing=True)
async def capture(url):
    """ For .ss command, capture a website's screenshot and send the photo. """
    await url.edit("`Processing ...`")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--test-type")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    input_str = url.pattern_match.group(1)
    link_match = match(r'\bhttps?://.*\.\S+', input_str)
    if link_match:
        link = link_match.group()
    else:
        await url.edit("`I need a valid link to take screenshots from.`")
        return
    driver.get(link)
    height = driver.execute_script(
        "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);"
    )
    width = driver.execute_script(
        "return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);"
    )
    driver.set_window_size(width + 125, height + 125)
    wait_for = height / 1000
    await url.edit(f"`Generating screenshot of the page...`\
    \n`Height of page = {height}px`\
    \n`Width of page = {width}px`\
    \n`Waiting ({int(wait_for)}s) for the page to load.`")
    await sleep(int(wait_for))
    im_png = driver.get_screenshot_as_png()
    # saves screenshot of entire page
    driver.close()
    message_id = url.message.id
    if url.reply_to_msg_id:
        message_id = url.reply_to_msg_id
    with io.BytesIO(im_png) as out_file:
        out_file.name = "screencapture.png"
        await url.edit("`Uploading screenshot as file..`")
        await url.client.send_file(url.chat_id,
                                   out_file,
                                   caption=input_str,
                                   force_document=True,
                                   reply_to=message_id)

@register(outgoing=True, pattern="^\!cspam (.*)")
async def tmeme(e):
    cspam = str(e.pattern_match.group(1))
    message = cspam.replace(" ", "")
    await e.delete()
    for letter in message:
        await e.respond(letter)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#CSPAM\n"
            "TSpam was executed successfully")


@register(outgoing=True, pattern="^\!wspam (.*)")
async def tmeme(e):
    wspam = str(e.pattern_match.group(1))
    message = wspam.split()
    await e.delete()
    for word in message:
        await e.respond(word)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#WSPAM\n"
            "WSpam was executed successfully")


@register(outgoing=True, pattern="^\!spam (.*)")
async def spammer(e):
    counter = int(e.pattern_match.group(1).split(' ', 1)[0])
    spam_message = str(e.pattern_match.group(1).split(' ', 1)[1])
    await e.delete()
    await asyncio.wait([e.respond(spam_message) for i in range(counter)])
    if BOTLOG:
        await e.client.send_message(BOTLOG_CHATID, "#SPAM\n"
                                    "Spam was executed successfully")


@register(outgoing=True, pattern="^\!picspam")
async def tiny_pic_spam(e):
    message = e.text
    text = message.split()
    counter = int(text[1])
    link = str(text[2])
    await e.delete()
    for i in range(1, counter):
        await e.client.send_file(e.chat_id, link)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#PICSPAM\n"
            "PicSpam was executed successfully")


@register(outgoing=True, pattern="^\!delayspam (.*)")
async def spammer(e):
    spamDelay = float(e.pattern_match.group(1).split(' ', 2)[0])
    counter = int(e.pattern_match.group(1).split(' ', 2)[1])
    spam_message = str(e.pattern_match.group(1).split(' ', 2)[2])
    await e.delete()
    for i in range(1, counter):
        await e.respond(spam_message)
        await sleep(spamDelay)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#DelaySPAM\n"
            "DelaySpam was executed successfully")

async def get_tz(con):
    """ Get time zone of the given country. """
    if "(Uk)" in con:
        con = con.replace("Uk", "UK")
    if "(Us)" in con:
        con = con.replace("Us", "US")
    if " Of " in con:
        con = con.replace(" Of ", " of ")
    if "(Western)" in con:
        con = con.replace("(Western)", "(western)")
    if "Minor Outlying Islands" in con:
        con = con.replace("Minor Outlying Islands", "minor outlying islands")
    if "Nl" in con:
        con = con.replace("Nl", "NL")

    for c_code in c_n:
        if con == c_n[c_code]:
            return c_tz[c_code]
    try:
        if c_n[con]:
            return c_tz[con]
    except KeyError:
        return


@register(outgoing=True,
          pattern="^\!time(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?")
async def time_func(tdata):
    """ For .time command, return the time of
        1. The country passed as an argument,
        2. The default userbot country(set it by using .settime),
        3. The server where the userbot runs.
    """
    con = tdata.pattern_match.group(1).title()
    tz_num = tdata.pattern_match.group(2)

    t_form = "%H:%M"
    c_name = None

    if len(con) > 4:
        try:
            c_name = c_n[con]
        except KeyError:
            c_name = con
        timezones = await get_tz(con)
    elif COUNTRY:
        c_name = COUNTRY
        tz_num = TZ_NUMBER
        timezones = await get_tz(COUNTRY)
    else:
        await tdata.edit(f"`It's`  **{dt.now().strftime(t_form)}**  `here.`")
        return

    if not timezones:
        await tdata.edit("`Invaild country.`")
        return

    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            tz_num = int(tz_num)
            time_zone = timezones[tz_num - 1]
        else:
            return_str = f"`{c_name} has multiple timezones:`\n\n"

            for i, item in enumerate(timezones):
                return_str += f"`{i+1}. {item}`\n"

            return_str += "\n`Choose one by typing the number "
            return_str += "in the command.`\n"
            return_str += f"`Example: .time {c_name} 2`"

            await tdata.edit(return_str)
            return

    dtnow = dt.now(tz(time_zone)).strftime(t_form)

    if c_name != COUNTRY:
        await tdata.edit(
            f"`It's`  **{dtnow}**  `in {c_name}({time_zone} timezone).`")
        return

    elif COUNTRY:
        await tdata.edit(f"`It's`  **{dtnow}**  `here, in {COUNTRY}"
                         f"({time_zone} timezone).`")
        return


@register(outgoing=True,
          pattern="^\!date(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?")
async def date_func(dat):
    """ For .date command, return the date of
        1. The country passed as an argument,
        2. The default userbot country(set it by using .settime),
        3. The server where the userbot runs.
    """
    con = dat.pattern_match.group(1).title()
    tz_num = dat.pattern_match.group(2)

    d_form = "%d/%m/%y - %A"
    c_name = ''

    if len(con) > 4:
        try:
            c_name = c_n[con]
        except KeyError:
            c_name = con
        timezones = await get_tz(con)
    elif COUNTRY:
        c_name = COUNTRY
        tz_num = TZ_NUMBER
        timezones = await get_tz(COUNTRY)
    else:
        await dat.edit(f"`It's`  **{dt.now().strftime(d_form)}**  `here.`")
        return

    if not timezones:
        await dat.edit("`Invaild country.`")
        return

    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            tz_num = int(tz_num)
            time_zone = timezones[tz_num - 1]
        else:
            return_str = f"`{c_name} has multiple timezones:`\n"

            for i, item in enumerate(timezones):
                return_str += f"`{i+1}. {item}`\n"

            return_str += "\n`Choose one by typing the number "
            return_str += "in the command.`\n"
            return_str += f"Example: .date {c_name} 2"

            await dat.edit(return_str)
            return

    dtnow = dt.now(tz(time_zone)).strftime(d_form)

    if c_name != COUNTRY:
        await dat.edit(
            f"`It's`  **{dtnow}**  `in {c_name}({time_zone} timezone).`")
        return

    elif COUNTRY:
        await dat.edit(f"`It's`  **{dtnow}**  `here, in {COUNTRY}"
                       f"({time_zone} timezone).`")
        return


