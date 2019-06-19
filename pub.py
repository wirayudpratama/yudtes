# -*- coding: utf-8 -*-

#import Yud
from LineAPI.linepy import *
from LineAPI.akad.ttypes import *
#from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
#from bs4 import BeautifulSoup
from googletrans import Translator
from multiprocessing import Pool, Process
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pytz, traceback, atexit#, pafy
try:
    with open('token.txt','r') as lg:
        tkn = lg.read()
        client = LINE(tkn)
except:
    client = LINE()
    with open('token.txt','w') as lg:
        lg.write(client.authToken)
#===================================open codec===========================================#

plates = codecs.open("template.json","r","utf-8")
plate = json.load(plates)

#client = LINE()
#client = LINE("Token")
#client.log("Auth Token : " + str(client.authToken))
#channelToken = client.getChannelResult()
#client.log("Channel Token : " + str(channelToken))

clientMid = client.profile.mid 
nadyaProfile = client.getProfile() 
lineSettings = client.getSettings()
oepoll = OEPoll(client)
botStart = time.time()
#=============[ DATA STREAM ]=====================================================================================
with open('settings.json','r') as stg:settings = json.load(stg)
client={"changepicture":False}
def setback():                                                                                                   
    with open('settings.json','w') as sb:json.dump(settings, sb, sort_keys=True, indent=4, ensure_ascii=False)
try:                                                                                                             
    with open("Log_data.json","r",encoding="utf_8_sig") as f:                                                    
        msg_dict = json.loads(f.read())                                                                          
except:                                                                                                          
    print("Couldn't Read Log Data")             
#==================================================
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []
msg_dict={}

helpmess = """╭──[─┅═✥[ʏᴜᴅʜᴀ-ʙᴏᴛ]✥═┅─]"\n│ @!
│───────────
│【ʏᴜᴅ】 Welcome「On/Off」
│【ʏᴜᴅ】 Help token
│【ʏᴜᴅ】 Help special
│【ʏᴜᴅ】 Help group
│【ʏᴜᴅ】 Translate
│【ʏᴜᴅ】 TaxtToSpeech
│【ʏᴜᴅ】 Runtime
│【ʏᴜᴅ】 Speed
│【ʏᴜᴅ】 About 
│【ʏᴜᴅ】 Creator
│【ʏᴜᴅ】 Pesan to creator: 「Text」
│【ʏᴜᴅ】 @yudbye
╰──────────"""

tokenmess = """╭──[─┅═✥[ʏᴜᴅʜᴀ-ʙᴏᴛ]✥═┅─]"\n│ @!
│───────────
│【ʏᴜᴅ】 Token chromeos
│【ʏᴜᴅ】 Token iosipad
│【ʏᴜᴅ】 Token win10
│【ʏᴜᴅ】 Token desktopmac
│【ʏᴜᴅ】 Token desktopwin
│───────────
│【ʏᴜᴅ】 Token2 chromeos
│【ʏᴜᴅ】 Token2 iosipad
│【ʏᴜᴅ】 Token2 win10
│【ʏᴜᴅ】 Token2 desktopmac
│【ʏᴜᴅ】 Token2 desktopwin
╰──────────"""

specialmess = """╭──[─┅═✥[ʏᴜᴅʜᴀ-ʙᴏᴛ]✥═┅─]"\n│ @!
│───────────
│【ʏᴜᴅ】 Get-mp3 「Query」
│【ʏᴜᴅ】 Get-video 「Query」
│【ʏᴜᴅ】 Get-audio 「Query」
│【ʏᴜᴅ】 Get-lirik 「Query」
│【ʏᴜᴅ】 Get-bintang 「Query」
│【ʏᴜᴅ】 Get-fs 「Query」
│【ʏᴜᴅ】 Get-gif 「Query」
│【ʏᴜᴅ】 Get-line 「ID Line」
│【ʏᴜᴅ】 Get-anime 「Query」
│【ʏᴜᴅ】 Get-mimpi 「Query」
│【ʏᴜᴅ】 Get-telepon 「Number」
│【ʏᴜᴅ】 Get-sms 「Number」
│【ʏᴜᴅ】 Get-meme 「Query」
│【ʏᴜᴅ】 Listmeme
│【ʏᴜᴅ】 Get-xxx 「Query」
│───────────
│【ʏᴜᴅ】 Top kaskus
│【ʏᴜᴅ】 Nekopoi
│【ʏᴜᴅ】 Quote
│【ʏᴜᴅ】 Creepypasta
│【ʏᴜᴅ】 Wikipedia 「Query」
│【ʏᴜᴅ】 Zodiac 「zodiac」
│【ʏᴜᴅ】 Meme「Text1」「Text2」
│【ʏᴜᴅ】 Retro「Text1」「Text2」
│【ʏᴜᴅ】 Pcid|id_line|text
│【ʏᴜᴅ】 Neon「Text」
│【ʏᴜᴅ】 Jadwal 「Channel TV」」
│【ʏᴜᴅ】 CheckDate 「Date」 
│【ʏᴜᴅ】 CheckWebsite 「url」
│【ʏᴜᴅ】 CheckPraytime 「Location」
│【ʏᴜᴅ】 CheckWeather 「Location」
│【ʏᴜᴅ】 CheckLocation 「Location」
│【ʏᴜᴅ】 Schedulepray 「Location」
│【ʏᴜᴅ】 SearchImage 「Search」
│【ʏᴜᴅ】 SearchMusic 「Search」 
│【ʏᴜᴅ】 SearchLyric 「Search」
│【ʏᴜᴅ】 SearchYoutube 「Search」 
│【ʏᴜᴅ】 Instapost「Nomor」 
│【ʏᴜᴅ】 Instastory 「Username」「Nomor」  
╰──────────"""

groupmess = """╭──[─┅═✥[ʏᴜᴅʜᴀ-ʙᴏᴛ]✥═┅─]"\n│ @!
│───────────
│【ʏᴜᴅ】 Apakah 「Question」
│【ʏᴜᴅ】 Dosa 「Mention」
│【ʏᴜᴅ】 Pahala 「Mention」
│【ʏᴜᴅ】 Info saya
│───────────
│【ʏᴜᴅ】 StealContact「Mention」
│【ʏᴜᴅ】 StealMid「Mention」
│【ʏᴜᴅ】 StealName「Mention」
│【ʏᴜᴅ】 StealBio「Mention」
│【ʏᴜᴅ】 StealPicture「Mention」
│【ʏᴜᴅ】 StealVideoProfile「Mention」
│【ʏᴜᴅ】 StealCover「Mention」
│【ʏᴜᴅ】 Mentionall
│───────────
│【ʏᴜᴅ】 Spam: 「On/Off」「Jumlah 1-20」「Text」
│【ʏᴜᴅ】 GroupCreator
│【ʏᴜᴅ】 GroupId
│【ʏᴜᴅ】 GroupName
│【ʏᴜᴅ】 GroupPicture
│【ʏᴜᴅ】 GroupTicket
│【ʏᴜᴅ】 GroupTicket「On/Off」
│【ʏᴜᴅ】 GroupList
│【ʏᴜᴅ】 GroupMemberList
│【ʏᴜᴅ】 GroupInfo
│【ʏᴜᴅ】 ChangeGroupName「Name」
│【ʏᴜᴅ】 ChangeGroupPicture
╰──────────"""

limit = {
    'batas': "5",
    'user':{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    
   
hasil = {
    "result":False,
    "posts":False,
    "postInfo":False,
    "liked":{}
    }
    
wordban = {
    "kontol":{},
    "kontl":{},
    "kntl":{},
    "memek":{},
    "anjing":{},
    "njing":{},
    "anjeng":{}
}

setTime = {}
setTime = wait2['setTime']

#if settings["restartPoint"] != None:
#    client.sendMessage(settings["restartPoint"], "Bot kembali aktif")

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}   

list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {    
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

#Bots=[mid]
#boty = ["u1869dc950cf9211164a150d91aa150db","u9ed37b221ed5b78a46d6209d93159bef","u3a354e28238fabd00ebfdbcac12e5973"]
admin=["u5239141f57b2d32c8b6933b88e02a93f","udf569e6eec420982af5898a94bb2fc45","u81a15ce8e621e30cb0f627aafc4e8b57"]
owner=["u5239141f57b2d32c8b6933b88e02a93f","udf569e6eec420982af5898a94bb2fc45","u81a15ce8e621e30cb0f627aafc4e8b57"]
yudha = ["u908c069ac42da884590db98cbe095253"]
settings["myProfile"]["displayName"] = nadyaProfile.displayName
settings["myProfile"]["statusMessage"] = nadyaProfile.statusMessage
settings["myProfile"]["pictureStatus"] = nadyaProfile.pictureStatus
coverId = client.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

def autoRestart():
    if time.time() - botStart > int(settings["timeRestart"]):
        backupData()
        time.sleep(5)
        restartBot()
	
def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    client.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                client.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "? Tukang {} Sider ?\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Auto Welcome 」\nHallo ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = client.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["welcome"]+" Di "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Respon Leave 」\nBaper Ya Kak ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = client.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["leave"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User?{}?\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n+--[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n+--[ Success ]"
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def download_page(url):
    try:
        headers = {}
        headers['User-Agent'] = random.choice(settings["userAgent"])
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        respData = str(resp.read())
        return respData
    except Exception as e:
        logError(e)
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+70)
        end_content = s.find(',"ow"',start_content-70)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            page = page[end_content:]
    return items

def backupData():
    try:
        backup = settings
        f = codecs.open('yudha.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def helptexttospeech():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTextToSpeech =  "╭──[ ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ ]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "af : Afrikaans" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "sq : Albanian" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "ar : Arabic" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "hy : Armenian" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "bn : Bengali" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "ca : Catalan" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "zh : Chinese" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "zhcn : Chinese (Mandarin/China)" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "zhtw : Chinese (Mandarin/Taiwan)" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "zhyue : Chinese (Cantonese)" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "hr : Croatian" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "cs : Czech" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "da : Danish" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "nl : Dutch" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "en : English" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "enau : English (Australia)" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "enuk : English (United Kingdom)" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "enus : English (United States)" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "eo : Esperanto" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "fi : Finnish" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "fr : French" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "de : German" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "el : Greek" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "hi : Hindi" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "hu : Hungarian" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "is : Icelandic" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "id : Indonesian" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "it : Italian" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "ja : Japanese" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "km : Khmer (Cambodian)" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "ko : Korean" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "la : Latin" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "lv : Latvian" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "mk : Macedonian" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "no : Norwegian" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "pl : Polish" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "pt : Portuguese" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "ro : Romanian" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "ru : Russian" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "sr : Serbian" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "si : Sinhala" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "sk : Slovak" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "es : Spanish" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "eses : Spanish (Spain)" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "esus : Spanish (United States)" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "sw : Swahili" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "sv : Swedish" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "ta : Tamil" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "th : Thai" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "tr : Turkish" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "uk : Ukrainian" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "vi : Vietnamese" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "cy : Welsh" + "\n" + \
                        "╰──────────" + "\n" + "\n" + \
                        "Contoh : " + key + "say-id Yudha Ganteng"
    return helpTextToSpeech

def helptranslate():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTranslate = "╭──[ ᴛʀᴀɴsʟᴀᴛᴇ ]" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "af : afrikaans" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "sq : albanian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "am : amharic" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ar : arabic" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "hy : armenian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "az : azerbaijani" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "eu : basque" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "be : belarusian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "bn : bengali" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "bs : bosnian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "bg : bulgarian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ca : catalan" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ceb : cebuano" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ny : chichewa" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "zhcn : chinese (simplified)" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "zhtw : chinese (traditional)" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "co : corsican" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "hr : croatian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "cs : czech" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "da : danish" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "nl : dutch" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "en : english" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "eo : esperanto" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "et : estonian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "tl : filipino" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "fi : finnish" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "fr : french" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "fy : frisian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "gl : galician" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ka : georgian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "de : german" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "el : greek" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "gu : gujarati" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ht : haitian creole" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ha : hausa" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "haw : hawaiian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "iw : hebrew" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "hi : hindi" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "hmn : hmong" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "hu : hungarian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "is : icelandic" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ig : igbo" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "id : indonesian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ga : irish" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "it : italian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ja : japanese" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "jw : javanese" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "kn : kannada" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "kk : kazakh" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "km : khmer" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ko : korean" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ku : kurdish (kurmanji)" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ky : kyrgyz" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "lo : lao" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "la : latin" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "lv : latvian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "lt : lithuanian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "lb : luxembourgish" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "mk : macedonian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "mg : malagasy" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ms : malay" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ml : malayalam" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "mt : maltese" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "mi : maori" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "mr : marathi" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "mn : mongolian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "my : myanmar (burmese)" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ne : nepali" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "no : norwegian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ps : pashto" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "fa : persian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "pl : polish" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "pt : portuguese" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "pa : punjabi" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ro : romanian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ru : russian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "sm : samoan" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "gd : scots gaelic" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "sr : serbian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "st : sesotho" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "sn : shona" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "sd : sindhi" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "si : sinhala" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "sk : slovak" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "sl : slovenian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "so : somali" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "es : spanish" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "su : sundanese" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "sw : swahili" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "sv : swedish" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "tg : tajik" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ta : tamil" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "te : telugu" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "th : thai" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "tr : turkish" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "uk : ukrainian" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ur : urdu" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "uz : uzbek" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "vi : vietnamese" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "cy : welsh" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "xh : xhosa" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "yi : yiddish" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "yo : yoruba" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "zu : zulu" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "fil : Filipino" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "he : Hebrew" + "\n" + \
                    "╰──────────" + "\n" + "\n" + \
                    "Contoh : " + key + "tr-id Yudha Ganteng"
    return helpTranslate

def clientBot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            #print ("[ 0 ] END OF OPERATION")
            return
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in admin:
                    settings["blacklist"][op.param2] = True
                    client.kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in admin:
                    try:
                        group = client.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            client.cancelGroupInvitation(op.param1,[_mid])
                            client.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if client.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in admin:
                            client.reissueGroupTicket(op.param1)
                            X = client.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            Ticket = client.reissueGroupTicket(op.param1)
                            client.kickoutFromGroup(op.param1,[op.param2])
                            client.updateGroup(X)
                except:
                    pass
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in admin:
                    settings["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in settings["blacklist"]:
                        	client.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in admin:
                    settings["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in settings["blacklist"]:
                            client.kickoutFromGroup(op.param1,[op.param2])
                    except:
                    	pass
        if op.type == 5:
            if settings["autoAdd"] == True:
                sendMention(op.param1, settings["autoAddMessage"],[op.param1])

        #if op.type == 17:
            #if settings["welcomemsg"] == True:
                #ginfo = client.getGroup(op.param1)
                #gid = client.getGroup(op.param1)
                #contact = client.getContact(op.param2)
                #client.sendContact(op.param1, contact.mid)
                #client.sendMessage(op.param1,"Selamat datang dan selamat berbelanja di " + gid.name)
        if op.type == 17 and settings["welcomemsg"]==True:
            client.acceptGroupInvitation(op.param1)
            pesannya = {
                "type": "template",
                "altText": "{} Mengirim Sticker".format(str(client.getContact(clientMid).displayName)),
                "baseSize": {
                    "height": 1040,
                    "width": 1040
                },
                "template": {
                    "type": "image_carousel",
                    "columns": [{
                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/177796075/IOS/sticker.png",
                        "action": {
                            "type": "uri",
                            "uri": "line://shop/detail/7384106",
                            "area": {
                                "x": 520,
                                "y": 0,
                                "width": 520,
                                "height": 1040
                            }
                        }
                    }]
                }
            }
            client.sendFlex(op.param1,pesannya)
            print ("Kam Showed")
        if op.type == 15 and settings["welcomemsg"]==True or op.type == 19 and settings["welcomemsg"]==True:
            client.acceptGroupInvitation(op.param1)
            pesannya = {
                "type": "template",
                "altText": "{} Mengirim Sticker".format(str(client.getContact(clientMid).displayName)),
                "baseSize": {
                    "height": 1040,
                    "width": 1040
                },
                "template": {
                    "type": "image_carousel",
                    "columns": [{
                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/177796076/IOS/sticker.png",
                        "action": {
                            "type": "uri",
                            "uri": "line.me/ti/p/%40175qduzr",
                            "area": {
                                "x": 520,
                                "y": 0,
                                "width": 520,
                                "height": 1040
                            }
                        }
                    }]
                }
            }
            client.sendFlex(op.param1,pesannya)
        #if op.type == 17:
            #if op.param1 in welcome:
                #ginfo = client.getGroup(op.param1)
                #contact = client.getContact(op.param2).picturePath
                #image = 'http://dl.profile.line.naver.jp'+contact
                #welcomeMembers(op.param1, [op.param2])
                #client.sendImageWithURL(op.param1, image)
        #if op.type == 15:
            #if op.param1 in welcome:
                #ginfo = client.getGroup(op.param1)
                #leaveMembers(op.param1, [op.param2])

        #if op.type == 15:
            #print ("[ 15 ] NOTIFIED LEAVE")
            #if settings["Leavemsg"] == True:
                #client.sendContact(op.param1, op.param2)
                #client.sendMessage(op.param1, "Terimakasih telah berkunjung")
                                
        if op.type == 13:
            if clientMid in op.param3:
                G = client.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            client.acceptGroupInvitation(op.param1)
                            Oa = 'u908c069ac42da884590db98cbe095253'
                            sendMention(op.param1,"Maaf member kurang dari 10 silahkan hubungi creator", [op.param2])
                            client.sendContact(op.param1, Oa)
                            client.leaveGroup(op.param1)
                        else:
                            client.acceptGroupInvitation(op.param1)
                            xname = client.getContact(op.param2).displayName
                            Oa = 'u908c069ac42da884590db98cbe095253'
                            sendMention(op.param1, "@! Thanks for invite me", [op.param2])
                            client.sendContact(op.param1, Oa)


        if op.type in [22, 24]:
            if settings["autoLeave"] == True:
                sendMention(op.param1, "@!, jangan invite saya")
                client.leaveRoom(op.param1)

        if op.type == 26:
            try:
                #print ("[ 26 ] SEND MESSAGE")
            #    msg_dict = msg._from
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if text.lower() == "help":
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                  sendMention(to, helpmess, [sender])
                                  Oa = 'u908c069ac42da884590db98cbe095253'
                                  client.sendContact(to, Oa)
                                  settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1

                            elif text.lower() == '/open':
                                del settings["limituser"][sender]
                                sendMention(to, "@! limit anda sudah terbuka", [sender])
				
                            elif text.lower() == 'limitlist':
                                if settings["limituser"] == {}:
                                    client.sendMessage(to, "Kosong")
                                else:
                                    mc = "Daftar Limit："
                                    for mi_d in settings["limituser"]:
                                        mc += "\n->" + client.getContact(mi_d).displayName
                                    client.sendMessage(to, mc)
				
                    #        elif wait["limit"][msg._from] >= 5:
                     #           sendMention(to, "@! anda terkena limit! ketik /open untuk membuka limit!", [msg._from])
					    
                            if text.lower() == "help special":
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                  sendMention(to, specialmess, [sender])
                                  Oa = 'u908c069ac42da884590db98cbe095253'
                                  client.sendContact(to, Oa)
                                  settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
				
                            if text.lower() == "help group":
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                  sendMention(to, groupmess, [sender])
                                  Oa = 'u908c069ac42da884590db98cbe095253'
                                  client.sendContact(to, Oa)
                                  settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
				
                            if text.lower() == "help token":
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                  sendMention(to, tokenmess, [sender])
                                  Oa = 'u908c069ac42da884590db98cbe095253'
                                  client.sendContact(to, Oa)
                                  settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    
                            if text.lower() == "tts":
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                    helpTextToSpeech = helptexttospeech()
                                    client.sendMessage(to, str(helpTextToSpeech))
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    
                                    
                            elif cmd == "translate":
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                    helpTranslate = helptranslate()
                                    client.sendMessage(to, str(helpTranslate))
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
				
                            elif cmd == "speed":
                                    start = time.time()
                                    client.sendMessage(to, "Progress...")
                                    elapsed_time = time.time() - start
                                    client.sendMessage(to, "[ Speed ]\nKecepatan mengirim pesan {} second".format(str(elapsed_time)))
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
				
                            elif cmd == "runtime":
                                    timeNow = time.time()
                                    runtime = timeNow - botStart
                                    runtime = format_timespan(runtime)
                                    client.sendMessage(to, "Bot sudah berjalan selama {}".format(str(runtime)))
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
				
                            elif cmd == "restart":
                              if msg._from in admin:
                                client.sendMessage(to, "Berhasil merestart Bot")
                                restartBot()
                                    
                            elif cmd == "oa": 
                              if msg._from in admin:
                                Oa = 'u908c069ac42da884590db98cbe095253'
                                client.sendContact(msg.to, Oa)

                            elif cmd == "creator":
                                Oa = 'u908c069ac42da884590db98cbe095253'
                                Own = 'u5239141f57b2d32c8b6933b88e02a93f'
                                client.sendContact(msg.to, Oa)
                                client.sendContact(msg.to, Own)
                                client.sendMessage(msg.to, "That is my creator")
                            elif "ayat:" in msg.text.lower():
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                   sep = msg.text.split(" ")
                                   ayat = msg.text.lower().replace(sep[0] + " ","")
                                   path = "http://islamcdn.com/quran/media/audio/ayah/ar.alafasy/" + ayat
                                   sendMention(msg.to, "@! ini ayat yang kamu cari", [sender])
                                   client.sendAudioWithURL(msg.to, path)
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
					
                            elif "jadwal " in msg.text.lower():
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                        txt = msg.text.split(" ")
                                        teks = msg.text.lower().replace("jadwal "+txt[1]+" ","")
                                        response = requests.get("https://farzain.xyz/api/premium/acaratv.php?apikey=kanekipubot&id="+txt[1]+"")
                                        data = response.json()
                                        pictig = str(data['status'])
                                        hasil = str(data['url'])
                                        text = "Status : "+pictig+"\n"+hasil+""
                                        client.sendMessage(msg.to, text)
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1

                            elif msg.text in ["Accept invite"]:
                                if msg._from in admin:
                                    gid = client.getGroupIdsInvited()
                                    _list = ""
                                    for i in gid:
                                        if i is not None:
                                            gids = client.getGroup(i)
                                            _list += gids.name
                                            client.acceptGroupInvitation(i)
                                        else:
                                            break
                                    if gid is not None:
                                        client.sendMessage(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                                    else:
                                        client.sendMessage(msg.to,"Tidak ada grup yang tertunda saat ini")
                            
                            elif msg.text in ["Result"]:
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                    mE = client.getProfile()
                                    gT = client.getGroupIdsJoined()
                                    fT = client.getAllContactIds()
                                    ginv = client.getGroupIdsInvited()
                                    client.sendMessage(msg.to,"「"+mE.displayName+"」 \n\nGroup total : " + str(len(gT))+ "\nFriend total: " +str(len(fT))+ "\nPending Group: " + str(len(ginv)))       
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
				
                            elif "Gbcont" in msg.text:
                                if msg._from in admin:
                                  n = client.getGroupIdsJoined()                
                                  Oa = 'u908c069ac42da884590db98cbe095253'
                                  for people in n:                	
                                  	client.sendContact(people, Oa)

                            elif "Gbcontbot" in msg.text:
                                if msg._from in admin:
                                  n = client.getGroupIdsJoined()                
                                  Oa = 'u908c069ac42da884590db98cbe095253'
                                  for people in n:                	
                                  	client.sendContact(people, Oa)

                            elif "Gbcontfams" in msg.text:
                                if msg._from in admin:
                                  n = client.getGroupIdsJoined()                
                                  Oa = 'uc99a2ab255130014a4ca4f3c3d9dad00'
                                  for people in n:                	
                                  	client.sendContact(people, Oa)
                            
                            
                            elif "Gbc " in msg.text:
                                if msg._from in admin:
                                  bctxt = msg.text.replace("Gbc ","")
                                  n = client.getGroupIdsJoined()                
                                  Oa = 'u908c069ac42da884590db98cbe095253'
                                  for people in n:                	
                                        client.sendMessage(people, bctxt)
                                        client.sendContact(people, Oa)
                    
                            elif "Sider on" in msg.text:
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                    try:
                                        del cctv['point'][msg.to]
                                        del cctv['sidermem'][msg.to]
                                        del cctv['cyduk'][msg.to]
                                    except:
                                        pass
                                    cctv['point'][msg.to] = msg.id
                                    cctv['sidermem'][msg.to] = ""
                                    cctv['cyduk'][msg.to]=True
                                    wait["Sider"] = True
                                    client.sendMessage(msg.to,"Siap On Cek Sider")
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                
                            elif "Sider off" in msg.text:
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                  if msg.to in cctv['point']:
                                      cctv['cyduk'][msg.to]=False
                                      wait["Sider"] = False
                                      client.sendMessage(msg.to, "Cek Sider Off")
                                      settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                  else:
                                      client.sendMessage(msg.to, "Heh Belom Di Set")
                    
                            elif text.lower() == 'about':
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                    try:
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                        arr = []
                                        owner = "u5239141f57b2d32c8b6933b88e02a93f"
                                        creator = client.getContact(owner)
                                        contact = client.getContact(owner)
                                        grouplist = client.getGroupIdsJoined()
                                        contactlist = client.getAllContactIds()
                                        blockedlist = client.getBlockedContactIds()
                                        ret_ = "╭──[ About YudhaPublicBot ]"
                                        ret_ += "\n│ Line : BotV1"
                                        ret_ += "\n│ Group : {}".format(str(len(grouplist)))
                                        ret_ += "\n│ Friend : {}".format(str(len(contactlist)))
                                        ret_ += "\n│ Blocked : {}".format(str(len(blockedlist)))
                                        ret_ += "\n│────────"
                                        ret_ += "\n│ Version : YudhaPublicBot V1"
                                        ret_ += "\n│ Creator : @!"
                                        ret_ += "\n╰──[ M.WiraYudhaP ]"
                                        sendMention(msg.to, str(ret_), yudha)
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))
                                        
                            elif msg.text.lower() in ["hi","hai","hy"]:
                                    sendMention(msg.to, "Hi too @!", [sender])
                            
                            elif msg.text.lower() in ["bah"]:
                                    client.sendMessage(msg.to, "Beh")
                                    client.sendMessage(msg.to, "Boh")
                                    client.sendMessage(msg.to, "Bih")
                                    client.sendMessage(msg.to, "Buh")

                            elif msg.text.lower() in ["tes","test"]:
                                    sendMention(msg.to, "Masuk by @!", [sender])
                            
                            elif msg.text.lower() in ["kam"]:
                                    client.sendMessage(msg.to, "preet")
                                    
                            elif "removeallchat" in msg.text.lower():
                                if msg._from in admin:
                                    try:
                                        client.removeAllMessages(op.param2)
                                        client.sendMessage(msg.to,"Done")
                                    except Exception as error:
                                        client.sendMessage(msg.to,"Error")
                            
                            elif cmd.startswith("zodiac "):
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    sep = msg.text.split(" ")
                                    query = text.replace(sep[0] + " ","")
                                    r = requests.post("https://aztro.herokuapp.com/?sign={}&day=today".format(urllib.parse.quote(query)))
                                    data = r.text
                                    data = json.loads(data)
                                    data1 = data["description"]
                                    data2 = data["color"]
                                    translator = Translator()
                                    hasil = translator.translate(data1, dest='id')
                                    hasil1 = translator.translate(data2, dest='id')
                                    A = hasil.text
                                    B = hasil1.text
                                    ret_ = "Ramalan zodiak {} hari ini \n".format(str(query))
                                    ret_ += str(A)
                                    ret_ += "\n\nTanggal : " +str(data["current_date"])
                                    ret_ += "\nRasi bintang : "+query
                                    ret_ += " ("+str(data["date_range"]+")")
                                    ret_ += "\nPasangan Zodiak : " +str(data["compatibility"])
                                    ret_ += "\nAngka keberuntungan : " +str(data["lucky_number"])
                                    ret_ += "\nWaktu keberuntungan : " +str(data["lucky_time"])
                                    ret_ += "\nWarna kesukaan : " +str(B)
                                    client.sendMessage(msg.to, str(ret_))

                            elif cmd.startswith("wikipedia "):
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                    try:
                                        sep = msg.text.split(" ")
                                        wiki = msg.text.replace(sep[0] + " ","")
                                        wikipedia.set_lang("id")
                                        pesan="?Title : "
                                        pesan+=wikipedia.page(wiki).title
                                        pesan+=" ?\n?Isi : "
                                        pesan+=wikipedia.summary(wiki, sentences=1)
                                        pesan+=" ?\n?Link : "+wikipedia.page(wiki).url
                                        pesan+=" ?\n"
                                        client.sendMessage(to, pesan)
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    except:
                                            try:
                                                pesan="Over Text Limit! Please Click link\n"
                                                pesan+=wikipedia.page(wiki).url
                                                client.sendMessage(to, pesan)
                                                settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                            except Exception as e:
                                                client.sendMessage(to, str(e))


                            elif cmd == "nekopoi" or cmd == "zzzzz":
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    r = requests.get("http://nekopoi.faith/")
                                    data = BeautifulSoup(r.content, 'html5lib')
                                    ret_= "Latest Update\n"
                                    for sam in data.findAll('div', attrs={'class':'eroinfo'}):
                                         ret_+="\n"+sam.find('h2').text+"\n"
                                         ret_+=sam.find('a')['href']+"\n"                                                                                       
                                    client.sendMessage(to,ret_)
                            elif cmd == 'square' or cmd == ' squares':
                                if msg._from in admin:
                                  a = client.getJoinedSquares()
                                  squares = a.squares
                                  txt2 = '? Squares ?\n'
                                  for s in range(len(squares)):
                                        txt2 += "\n"+str(s+1)+". "+str(squares[s].name)
                                  txt2 += "\n\nTotal {} Squares.".format(str(len(squares)))
                                  txt2 += "\n\nUsage : Square#num"
                                  client.sendMessage(to,str(txt2))
                            elif cmd == "quote" or cmd == " quote":
                                  if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                  if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                  else:
                                         settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                         r=requests.get("https://talaikis.com/api/quotes/random")
                                         data=r.text
                                         data=json.loads(data)
                                         hasil = "? Random Quote ?\n"
                                         hasil += "Category : " +str(data["cat"])
                                         hasil += "\n\n" +str(data["quote"])
                                         hasil += "\n\n * * * " +str(data["author"])+ " * * *"
                                         client.sendMessage(msg.to, str(hasil))

                            elif cmd == "creepypasta" or cmd == " creepypasta":
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    r=requests.get("http://hipsterjesus.com/api")
                                    data=r.text
                                    data=json.loads(data)
                                    hasil = "? Creepypasta ?\n" 
                                    hasil += str(data["text"])
                                    client.sendMessage(msg.to, str(hasil))

                            elif "Apakah " in msg.text:
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                    tanya = msg.text.replace("Apakah ","")
                                    jawab = ("Ya","Tidak","Bisa jadi")
                                    jawaban = random.choice(jawab)
                                    client.sendMessage(msg.to,jawaban)
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
            
#----------------------
                            elif "Dosa @" in msg.text:
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                   tanya = msg.text.replace("Dosa @","")
                                   jawab = ("60%","70%","80%","90%","100%","Tak terhingga")
                                   jawaban = random.choice(jawab)
                                   client.sendMessage(msg.to,"Dosanya " + tanya + "adalah " + jawaban + " Banyak banyak tobat Nak ")
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
#----------------------
                            elif "Pahala @" in msg.text:
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                   tanya = msg.text.replace("Pahala @","")
                                   jawab = ("0%","20%","40%","50%","60%","Tak ada")
                                   jawaban = random.choice(jawab)
                                   client.sendMessage(msg.to,"Pahalanya " + tanya + "adalah " + jawaban + "\nTobatlah nak")
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                
                            elif "Spam: " in msg.text:
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                     settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                     cond = msg.text.split(" ")
                                     value = int(cond[2])
                                     text = msg.text.replace("Spam: " + str(cond[1]) + " " + str(value) + " ","")
                                     ballon1 = value * (text + "\n")
                                     if cond[1] == "on":
                                         if value <= 20:
                                             for x in range(value):
                                                 client.sendMessage(msg.to, text)
                                         else:
                                             client.sendMessage(msg.to,"Jumlah spamming melebihi batas. Max 20")
                                     elif cond[1] == "off":
                                         if value <= 20:
                                             client.sendMessage(msg.to,ballon1)
                                         else:
                                             client.sendMessage(msg.to,"Jumlah spamming melebihi batas")
                                     else:
                                         client.sendMessage(msg.to,"Error condition")
                            
                            elif "@yudbye" in msg.text:
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                    if msg.toType == 2:
                                        ginfo = client.getGroup(msg.to)
                                        try:
                                            settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                            Oa= 'u908c069ac42da884590db98cbe095253'
                                            client.sendContact(msg.to, Oa)
                                            client.leaveGroup(msg.to)
                                        except:
                                            pass
                
                            elif "detectout" in msg.text:
                               if msg._from in admin:
                                groups = client.getGroupIdsJoined()
                                for group in groups:               	
                                    G = client.getGroup(group)
                                    if len(G.members) <= wait["autoCancel"]["members"]:
                                        Oa = 'u908c069ac42da884590db98cbe095253'
                                        owner = 'u5239141f57b2d32c8b6933b88e02a93f'
                                  #      sendMention(msg.to, "Halo @! detect group dibawah 10 members akan dimulai.", [sender])
                                        client.sendContact(group, Oa)
                                        client.sendContact(group, owner)
                                        client.sendMessage(group,"Member kurang dari 10 silahkan invite creator untuk menginvite saya")
                                        client.leaveGroup(group)
					
                            elif "meme " in msg.text.lower():
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                    try:
                                        txt = msg.text.split(" ")
                                        teks = msg.text.lower().replace("meme "+txt[1]+" ","")
                                        data = []
                                        r = requests.get("http://ofckaneki.dynu.net/bot.php")
                                        r = eval(r.text)
                                        for a in r:
                                            data.append(a)
                                        c = random.choice(data)
                                        foto = "https://memegen.link/"+c+"/"+txt[1]+"/"+teks+".jpg"
                                        client.sendImageWithURL(msg.to, foto)
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))
                                        
                            elif "retro " in msg.text.lower():
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                    try:
                                        txt = msg.text.split(" ")
                                        teks = msg.text.lower().replace("retro "+txt[1]+" ","")
                                        satu = ["1","2","3","4","5"]
                                        dua = ["1","2","3","4"]
                                        k = random.choice(satu)
                                        w = random.choice(dua)
                                        response = requests.get("http://leert.corrykalam.gq/retrowave.php?text1="+txt[1]+"&text2="+teks+"&text3=&btype="+k+"&ttype="+w+"")
                                        data = response.json()
                                        hasil = str(data['image'])
                                        download = str(data['image'])                      
                                        client.sendMessage(receiver, download)
                                        client.sendImageWithURL(receiver, hasil)
                                        Oa = 'u908c069ac42da884590db98cbe095253'
                                        client.sendContact(receiver, Oa)
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    except Exception as e:
                                        client.sendMessage(receiver, str(e))
			
                            elif text.lower().startswith("pcid"):
                               if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                  dan = text.split("|")
                                  x = client.findContactsByUserid(dan[1])
                                  a = client.getContact(sender)
                                  client.sendMessage(x.mid,"Anda mendapatkan pesan dari "+a.displayName+"\n\n"+dan[2])
                                  Oa = 'u908c069ac42da884590db98cbe095253'
                                  client.sendContact(x.mid, Oa)
                                  client.sendMessage(to,"Sukses mengirim pesan ke "+x.displayName+"\nDari: "+a.displayName+"\nPesan: "+dan[2])
                                  settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                   

                            elif "pesan to creator: " in msg.text.lower():
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                   txt = msg.text.split(" ")
                                   teks = msg.text.lower().replace("pesan to creator: ","")
                                   line = 'yud.xx'
                                   x = client.findContactsByUserid(line)
                                   a = client.getContact(msg._from)
                                   sendMention(x.mid,"Anda mendapatkan pesan dari @!\n\nSaran:\n"+teks+"", [a.mid])
                                   sendMention(msg.to,"Sukses mengirim saran ke "+x.displayName+"\nDari: @!\nSaran : "+teks+"", [a.mid])
                                   Oa = 'u908c069ac42da884590db98cbe095253'
                                   client.sendContact(msg.to, Oa)
                                   
                            elif "Gbcon: " in msg.text:
                              if msg._from in admin:
                                n = client.getGroupIdsJoined()   
                                y = msg.text.split(" ")
                                k = msg.text.replace("Gbcon: "+y[1]+" ","")
                                Oa = y[1]
                                for people in n:                	
                                	client.sendContact(people, Oa)

                            elif msg.text.lower() in ["groupcreator"]:
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                    msg.contentType = 13
                                    ginfo = client.getGroup(msg.to)
                                    gCreator = ginfo.creator.mid
                                    try:
                                        msg.contentMetadata = {'mid': gCreator}
                                        gCreator1 = ginfo.creator.displayName
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                        
                                    except:
                                        gCreator = "Error"
                                    client.sendMessage(msg.to, "Group Creator : " + gCreator1)
                                    client.sendContact(msg.to, gCreator)

                            elif "grouppicture " in msg.text.lower():
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                      googl = msg.text.lower().replace("groupimage ","")
                                      url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + googl
                                      raw_html = (download_page(url))
                                      items = []
                                      items = items + (_images_get_all_items(raw_html))
                                      path = random.choice(items)
                                      try:
                                          start = time.time()
                                          client.sendImageWithURL(msg.to,random.choice(items))
                                          client.sendImageWithURL(msg.to,random.choice(items))
                                          client.sendImageWithURL(msg.to,random.choice(items))
                                          client.sendMessage(msg.to,"Total Image Links ="+str(len(items)))
                                          settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                      except Exception as njer:
                                            client.sendMessage(msg.to, str(njer))
				
                            elif "info saya" in msg.text.lower():
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                  settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                  kelamin = ("Waria","Laki-laki","Perempuan","Tidak Diketahui","Bencong")
                                  wajah = ("Standar","Ganteng","Cantik","Beruk","Hancur")
                                  status = ("Menikah","Pacaran","Jones")
                                  k = random.choice(kelamin)
                                  w = random.choice(wajah)
                                  s = random.choice(status)
                                  sendMention(msg.to,"• Nama : @!\n• Kelamin : "+k+"\n• Wajah : "+w+"\n• Status Kehidupan : "+s, [sender])
# Pembatas Script #
                            elif "Surat:" in msg.text:
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                  try:
                                     settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                     sep = msg.text.split(" ")
                                     surah = int(text.replace(sep[0] + " ",""))
                                     if 0 < surah < 115:
                                         if surah not in [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 16, 17, 18, 20, 21, 23, 26, 37]:
                                             if len(str(surah)) == 1:
                                                 audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-00" + str(surah) + "-muslimcentral.com.mp3"
                                                 sendMention(msg.to, "@! ini surat yang kamu minta..", [msg._from])
                                                 client.sendAudioWithURL(msg.to, audionya)
                                             elif len(str(surah)) == 2:
                                                 audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-0" + str(surah) + "-muslimcentral.com.mp3"
                                                 sendMention(msg.to, "@! ini surat yang kamu minta..", [msg._from])
                                                 client.sendAudioWithURL(msg.to, audionya)
                                             else:
                                                 audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-" + str(surah) + "-muslimcentral.com.mp3"
                                                 sendMention(msg.to, "@! ini surat yang kamu minta..", [msg._from])
                                                 client.sendAudioWithURL(msg.to, audionya)
                                         else:
                                             sendMention(msg.to, "@! Surah yang kamu minta terlalu panjang", [msg._from])
                                     else:
                                         sendMention(msg.to, "@! Quran hanya 114 surah", [msg._from])
                                  except Exception as error:
                                      client.sendMessage(msg.to, "error\n"+str(error))
                              
                            elif "neon " in msg.text.lower():
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                    try:
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                        txt = msg.text.split(" ")
                                        teks = msg.text.lower().replace("neon ","")
                                        color = ["red","yellow","green","purple","violet","blue"]
                                        k = random.choice(color)
                                        foto = "https://ari-api.herokuapp.com/neon?text="+teks+"&color="+k+""
                                        sendMention(msg.to, "@!", [msg._from])
                                        client.sendImageWithURL(msg.to, foto)
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))
                            elif cmd == "autoadd on":
                              if msg._from in admin:
                                settings["autoAdd"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan auto add")
                            elif cmd == "autoadd off":
                              if msg._from in admin:
                                settings["autoAdd"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan auto add")
                            elif cmd == "autojoin on":
                              if msg._from in admin:
                                settings["autoJoin"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan auto join")
                            elif cmd == "autojoin off":
                              if msg._from in admin:
                                settings["autoJoin"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan auto join")
                            elif cmd == "autoleave on":
                              if msg._from in admin:
                                settings["autoLeave"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan auto leave")
                            elif cmd == "autoleave off":
                              if msg._from in admin:
                                settings["autoLeave"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan auto leave")
                            elif cmd == "autorespon on":
                              if msg._from in admin:
                                settings["autoRespon"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan auto respon")
                            elif cmd == "autorespon off":
                              if msg._from in admin:
                                settings["autoRespon"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan auto respon")
                            elif cmd == "autoread on":
                              if msg._from in admin:
                                settings["autoRead"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan auto read")
                            elif cmd == "autoread off":
                              if msg._from in admin:
                                settings["autoRead"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan auto read")
                            elif cmd == "autojointicket on":
                              if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan auto join by ticket")
                            elif cmd == "autojointicket off":
                              if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan auto join by ticket")
                            elif cmd == "checkcontact on":
                              if msg._from in admin:
                                settings["checkContact"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan check details contact")
                            elif cmd == "checkcontact off":
                              if msg._from in admin:
                                settings["checkContact"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan check details contact")
                            elif cmd == "checkpost on":
                              if msg._from in admin:
                                settings["checkPost"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan check details post")
                            elif cmd == "checkpost off":
                              if msg._from in admin:
                                settings["checkPost"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan check details post")
                            elif cmd == "checksticker on":
                              if msg._from in admin:
                                settings["checkSticker"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan check details sticker")
                            elif cmd == "checksticker off":
                              if msg._from in admin:
                                settings["checkSticker"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan check details sticker")
                            elif cmd == "unsendchat on":
                              if msg._from in admin:
                                settings["unsendMessage"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan unsend message")
                            elif cmd == "unsendchat off":
                              if msg._from in admin:
                                settings["unsendMessage"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan unsend message")
                            elif cmd == "autolike on":
                              if msg._from in admin:
                                settings["autoLike"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan autolike")
                            elif cmd == "autolike off":
                              if msg._from in admin:
                                settings["autoLike"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan autolike")
                            elif cmd == "welcome on":
                              if msg._from in admin:
                                settings["welcomemsg"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan unsend message")
                            elif cmd == "welcome off":
                              if msg._from in admin:
                                settings["welcomemsg"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan unsend message")
                            elif cmd == "status":
                              if msg._from in admin:
                                try:
                                    ret_ = "╭──[ Status ]"
                                    if settings["autoAdd"] == True: ret_ += "\n│ [ ON ] Auto Add"
                                    else: ret_ += "\n│ [ OFF ] Auto Add"
                                    if settings["autoJoin"] == True: ret_ += "\n│ [ ON ] Auto Join"
                                    else: ret_ += "\n│ [ OFF ] Auto Join"
                                    if settings["autoLeave"] == True: ret_ += "\n│ [ ON ] Auto Leave Room"
                                    else: ret_ += "\n│ [ OFF ] Auto Leave Room"
                                    if settings["autoJoinTicket"] == True: ret_ += "\n│ [ ON ] Auto Join Ticket"
                                    else: ret_ += "\n│ [ OFF ] Auto Join Ticket"
                                    if settings["autoRead"] == True: ret_ += "\n│ [ ON ] Auto Read"
                                    else: ret_ += "\n│ [ OFF ] Auto Read"
                                    if settings["autoRespon"] == True: ret_ += "\n│ [ ON ] Detect Mention"
                                    else: ret_ += "\n│ [ OFF ] Detect Mention"
                                    if settings["checkContact"] == True: ret_ += "\n│ [ ON ] Check Contact"
                                    else: ret_ += "\n│ [ OFF ] Check Contact"
                                    if settings["checkPost"] == True: ret_ += "\n│ [ ON ] Check Post"
                                    else: ret_ += "\n│ [ OFF ] Check Post"
                                    if settings["checkSticker"] == True: ret_ += "\n│ [ ON ] Check Sticker"
                                    else: ret_ += "\n│ [ OFF ] Check Sticker"
                                    if settings["setKey"] == True: ret_ += "\n│ [ ON ] Set Key"
                                    else: ret_ += "\n│ [ OFF ] Set Key"
                                    if settings["unsendMessage"] == True: ret_ += "\n│ [ ON ] Unsend Message"
                                    else: ret_ += "\n│ [ OFF ] Unsend Message"
                                    ret_ += "\n╰──[ Status ]"
                                    client.sendMessage(to, str(ret_))
                                except Exception as e:
                                    client.sendMessage(msg.to, str(e))
# Pembatas Script #
                            elif cmd == "crash":
                              if msg._from in admin:
                                client.sendContact(to, "u908c069ac42da884590db98cbe095253',")
                            elif cmd.startswith("changename:"):
                              if msg._from in admin:
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = client.getProfile()
                                    profile.displayName = string
                                    client.updateProfile(profile)
                                    client.sendMessage(to,"Berhasil mengganti display name menjadi{}".format(str(string)))
                            elif cmd.startswith("changebio:"):
                              if msg._from in admin:
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = client.getProfile()
                                    profile.statusMessage = string
                                    client.updateProfile(profile)
                                    client.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                            if cmd=='me':client.sendContact(to,sender);client.sendMessageMusic(to, title=client.getContact(sender).displayName, subText=str(client.getContact(sender).statusMessage), url='line.me/ti/p/%40175qduzr', iconurl="http://dl.profile.line-cdn.net/{}".format(client.getContact(sender).pictureStatus), contentMetadata={})
                            elif cmd == "mymid":
                                client.sendMessage(to, "[ MID ]\n{}".format(sender))
                            elif cmd == "myname":
                                contact = client.getContact(sender)
                                client.sendMessage(to, "[ Display Name ]\n{}".format(contact.displayName))
                            elif cmd == "mybio":
                                contact = client.getContact(sender)
                                client.sendMessage(to, "[ Status Message ]\n{}".format(contact.statusMessage))
                            elif cmd == "mypicture":
                                contact = client.getContact(sender)
                                client.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "myvideoprofile":
                                contact = client.getContact(sender)
                                client.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "mycover":
                                channel = client.getProfileCoverURL(sender)          
                                path = str(channel)
                                client.sendImageWithURL(to, path)
                            elif cmd.startswith("cloneprofile "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.cloneContactProfile(ls)
                                        client.sendMessage(to, "Berhasil mengclone profile {}".format(contact.displayName))
                            elif cmd == "restoreprofile":
                              if msg._from in admin:
                                try:
                                    clientProfile = client.getProfile()
                                    clientProfile.displayName = str(settings["myProfile"]["displayName"])
                                    clientProfile.statusMessage = str(settings["myProfile"]["statusMessage"])
                                    clientProfile.pictureStatus = str(settings["myProfile"]["pictureStatus"])
                                    client.updateProfileAttribute(8, clientProfile.pictureStatus)
                                    client.updateProfile(clientProfile)
                                    coverId = str(settings["myProfile"]["coverId"])
                                    client.updateProfileCoverById(coverId)
                                    client.sendMessage(to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                                except Exception as e:
                                    client.sendMessage(to, "Gagal restore profile")
                                    logError(error)
                            elif cmd == "backupprofile":
                              if msg._from in admin:
                                try:
                                    profile = client.getProfile()
                                    settings["myProfile"]["displayName"] = str(profile.displayName)
                                    settings["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                    settings["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
                                    coverId = client.getProfileDetail()["result"]["objectId"]
                                    settings["myProfile"]["coverId"] = str(coverId)
                                    client.sendMessage(to, "Berhasil backup profile")
                                except Exception as e:
                                    client.sendMessage(to, "Gagal backup profile")
                                    logError(error)
                            elif cmd.startswith("stealmid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                 if sender not in settings["limituser"]:
                                      settings["limituser"][sender] = {'count':0,'limit':5}
                                 if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                      sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                 else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}".format(str(ls))
                                    client.sendMessage(to, str(ret_))
                            elif cmd.startswith("stealname "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                 if sender not in settings["limituser"]:
                                      settings["limituser"][sender] = {'count':0,'limit':5}
                                 if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                      sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                 else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                            elif cmd.startswith("stealbio "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                 if sender not in settings["limituser"]:
                                      settings["limituser"][sender] = {'count':0,'limit':5}
                                 if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                      sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                 else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMessage(to, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                            elif cmd.startswith("stealpicture"):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                 if sender not in settings["limituser"]:
                                      settings["limituser"][sender] = {'count':0,'limit':5}
                                 if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                      sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                 else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        client.sendImageWithURL(to, str(path))
                            elif cmd.startswith("stealvideoprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                 if sender not in settings["limituser"]:
                                      settings["limituser"][sender] = {'count':0,'limit':5}
                                 if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                      sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                 else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        client.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("stealcover "):
                                if client != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                     if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                                     if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                     else:
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            channel = client.getProfileCoverURL(ls)
                                            path = str(channel)
                                            client.sendImageWithURL(to, str(path))
#===========================[ TOKEN EATER ]=====================================#
                            if text.lower() == 'token win10':
                             if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                req = requests.get(url = 'https://api.eater.tech/WIN10')
                                a = req.text
                                b = json.loads(a)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                tkn['{}'.format(msg._from)] = []
                                tkn['{}'.format(msg._from)].append({
                                    'qr': b['result'][0]['linkqr'],
                                    'tkn': b['result'][0]['linktkn']
                                    })
                                qrz = b['result'][0]['linkqr']
                                client.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                                with open('tkn.json', 'w') as outfile:
                                    json.dump(tkn, outfile)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                a = tkn['{}'.format(msg._from)][0]['tkn']
                                req = requests.get(url = '{}'.format(a))
                                b = req.text
                                sendMention(msg.to,  '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            
                            if text.lower() == 'token chromeos':
                             if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                req = requests.get(url = 'https://api.eater.tech/CHROMEOS')
                                a = req.text
                                b = json.loads(a)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                tkn['{}'.format(msg._from)] = []
                                tkn['{}'.format(msg._from)].append({
                                    'qr': b['result'][0]['linkqr'],
                                    'tkn': b['result'][0]['linktkn']
                                    })
                                qrz = b['result'][0]['linkqr']
                                client.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                                with open('tkn.json', 'w') as outfile:
                                    json.dump(tkn, outfile)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                a = tkn['{}'.format(msg._from)][0]['tkn']
                                req = requests.get(url = '{}'.format(a))
                                b = req.text
                                sendMention(msg.to,  '- TIPE TOKEN : CHROMEOS\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            
                            if text.lower() == 'token iosipad':
                             if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                req = requests.get(url = 'https://api.eater.tech/IOSIPAD')
                                a = req.text
                                b = json.loads(a)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                tkn['{}'.format(msg._from)] = []
                                tkn['{}'.format(msg._from)].append({
                                    'qr': b['result'][0]['linkqr'],
                                    'tkn': b['result'][0]['linktkn']
                                    })
                                qrz = b['result'][0]['linkqr']
                                client.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                                with open('tkn.json', 'w') as outfile:
                                    json.dump(tkn, outfile)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                a = tkn['{}'.format(msg._from)][0]['tkn']
                                req = requests.get(url = '{}'.format(a))
                                b = req.text
                                sendMention(msg.to,  '- TIPE TOKEN : IOSIPAD\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            
                            if text.lower() == 'token desktopmac':
                             if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                req = requests.get(url = 'https://api.eater.tech/DESKTOPMAC')
                                a = req.text
                                b = json.loads(a)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                tkn['{}'.format(msg._from)] = []
                                tkn['{}'.format(msg._from)].append({
                                    'qr': b['result'][0]['linkqr'],
                                    'tkn': b['result'][0]['linktkn']
                                    })
                                qrz = b['result'][0]['linkqr']
                                client.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                                with open('tkn.json', 'w') as outfile:
                                    json.dump(tkn, outfile)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                a = tkn['{}'.format(msg._from)][0]['tkn']
                                req = requests.get(url = '{}'.format(a))
                                b = req.text
                                sendMention(msg.to,  '- TIPE TOKEN : DESKTOPMAC\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            
                            if text.lower() == 'token desktopwin':
                             if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                req = requests.get(url = 'https://api.eater.tech/DESKTOPWIN')
                                a = req.text
                                b = json.loads(a)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                tkn['{}'.format(msg._from)] = []
                                tkn['{}'.format(msg._from)].append({
                                    'qr': b['result'][0]['linkqr'],
                                    'tkn': b['result'][0]['linktkn']
                                    })
                                qrz = b['result'][0]['linkqr']
                                client.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                                with open('tkn.json', 'w') as outfile:
                                    json.dump(tkn, outfile)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                a = tkn['{}'.format(msg._from)][0]['tkn']
                                req = requests.get(url = '{}'.format(a))
                                b = req.text
                                sendMention(msg.to,  '- TIPE TOKEN : DESKTOPWIN\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            if text.lower() == 'token2 win10':
                             if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                req = requests.get(url = 'https://api.eater.pw/WIN10')
                                a = req.text
                                b = json.loads(a)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                tkn['{}'.format(msg._from)] = []
                                tkn['{}'.format(msg._from)].append({
                                    'qr': b['result'][0]['linkqr'],
                                    'tkn': b['result'][0]['linktkn']
                                    })
                                qrz = b['result'][0]['linkqr']
                                client.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                                with open('tkn.json', 'w') as outfile:
                                    json.dump(tkn, outfile)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                a = tkn['{}'.format(msg._from)][0]['tkn']
                                req = requests.get(url = '{}'.format(a))
                                b = req.text
                                sendMention(msg.to,  '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            
                            if text.lower() == 'token2 chromeos':
                             if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                req = requests.get(url = 'https://api.eater.pw/CHROMEOS')
                                a = req.text
                                b = json.loads(a)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                tkn['{}'.format(msg._from)] = []
                                tkn['{}'.format(msg._from)].append({
                                    'qr': b['result'][0]['linkqr'],
                                    'tkn': b['result'][0]['linktkn']
                                    })
                                qrz = b['result'][0]['linkqr']
                                client.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                                with open('tkn.json', 'w') as outfile:
                                    json.dump(tkn, outfile)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                a = tkn['{}'.format(msg._from)][0]['tkn']
                                req = requests.get(url = '{}'.format(a))
                                b = req.text
                                sendMention(msg.to,  '- TIPE TOKEN : CHROMEOS\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            
                            if text.lower() == 'token2 iosipad':
                             if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                req = requests.get(url = 'https://api.eater.pw/IOSIPAD')
                                a = req.text
                                b = json.loads(a)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                tkn['{}'.format(msg._from)] = []
                                tkn['{}'.format(msg._from)].append({
                                    'qr': b['result'][0]['linkqr'],
                                    'tkn': b['result'][0]['linktkn']
                                    })
                                qrz = b['result'][0]['linkqr']
                                client.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                                with open('tkn.json', 'w') as outfile:
                                    json.dump(tkn, outfile)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                a = tkn['{}'.format(msg._from)][0]['tkn']
                                req = requests.get(url = '{}'.format(a))
                                b = req.text
                                sendMention(msg.to,  '- TIPE TOKEN : IOSIPAD\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            
                            if text.lower() == 'token2 desktopmac':
                             if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                req = requests.get(url = 'https://api.eater.pw/DESKTOPMAC')
                                a = req.text
                                b = json.loads(a)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                tkn['{}'.format(msg._from)] = []
                                tkn['{}'.format(msg._from)].append({
                                    'qr': b['result'][0]['linkqr'],
                                    'tkn': b['result'][0]['linktkn']
                                    })
                                qrz = b['result'][0]['linkqr']
                                client.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                                with open('tkn.json', 'w') as outfile:
                                    json.dump(tkn, outfile)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                a = tkn['{}'.format(msg._from)][0]['tkn']
                                req = requests.get(url = '{}'.format(a))
                                b = req.text
                                sendMention(msg.to,  '- TIPE TOKEN : DESKTOPMAC\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            
                            if text.lower() == 'token2 desktopwin':
                             if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                req = requests.get(url = 'https://api.eater.pw/DESKTOPWIN')
                                a = req.text
                                b = json.loads(a)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                tkn['{}'.format(msg._from)] = []
                                tkn['{}'.format(msg._from)].append({
                                    'qr': b['result'][0]['linkqr'],
                                    'tkn': b['result'][0]['linktkn']
                                    })
                                qrz = b['result'][0]['linkqr']
                                client.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                                with open('tkn.json', 'w') as outfile:
                                    json.dump(tkn, outfile)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                a = tkn['{}'.format(msg._from)][0]['tkn']
                                req = requests.get(url = '{}'.format(a))
                                b = req.text
                                sendMention(msg.to,  '- TIPE TOKEN : DESKTOPWIN\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
#===========================[ TOKEN EATER }=====================================#
                            elif cmd == 'groupid':
                                gid = client.getGroup(to)
                                client.sendMessage(to, "[ID Group : ]\n" + gid.id)
                            elif cmd == 'grouppicture':
                                group = client.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                client.sendImageWithURL(to, path)
                            elif cmd == 'groupname':
                                gid = client.getGroup(to)
                                client.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                            elif cmd == 'groupticket':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = client.reissueGroupTicket(to)
                                        client.sendMessage(to, "[ " + gid.name + " ]\nline://ti/g/{}".format(str(ticket)))
                                    else:
                                        client.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                            elif cmd == 'groupticket on':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        client.sendMessage(to, "Grup qr sudah terbuka")
                                    else:
                                        group.preventedJoinByTicket = False
                                        client.updateGroup(group)
                                        client.sendMessage(to, "Berhasil membuka grup qr")
                            elif cmd == 'groupticket off':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == True:
                                        client.sendMessage(to, "Grup qr sudah tertutup")
                                    else:
                                        group.preventedJoinByTicket = True
                                        client.updateGroup(group)
                                        client.sendMessage(to, "Berhasil menutup grup qr")
                            elif cmd == 'groupinfo':
                                group = client.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╭──[ ɢʀᴏᴜᴘ ɪɴғᴏ ]"
                                ret_ += "\n│ ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(str(group.name))
                                ret_ += "\n│ ɪᴅ ɢʀᴏᴜᴘ : {}".format(group.id)
                                ret_ += "\n│ ᴘᴇᴍʙᴜᴀᴛ : {}".format(str(gCreator))
                                ret_ += "\n│ ᴊᴜᴍʟᴀʜ ᴍᴇᴍʙᴇʀ : {}".format(str(len(group.members)))
                                ret_ += "\n│ ᴊᴜᴍʟᴀʜ ᴘᴇɴᴅɪɴɢ : {}".format(gPending)
                                ret_ += "\n│ ɢʀᴏᴜᴘ ǫʀ : {}".format(gQr)
                                ret_ += "\n│ ɢʀᴏᴜᴘ ᴛɪᴄᴋᴇᴛ : {}".format(gTicket)
                                ret_ += "\n╰──[ ғɪɴɪsʜ ]"
                                client.sendMessage(to, str(ret_))
                                client.sendImageWithURL(to, path)
                            elif cmd == 'groupmemberlist':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    ret_ = "╭──[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n│ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╰──[ Total {} ]".format(str(len(group.members)))
                                    client.sendMessage(to, str(ret_))
                            elif cmd == 'grouplist':
                              if msg._from in admin:
                                    groups = client.groups
                                    ret_ = "╭──[ Group List ]"
                                    no = 0 + 1
                                    for gid in groups:
                                        group = client.getGroup(gid)
                                        ret_ += "\n│ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n╰──[ Total {} Groups ]".format(str(len(groups)))
                                    client.sendMessage(to, str(ret_))
# Pembatas Script #
                            elif text.lower() == 'top kaskus':
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    r = requests.get("https://api.bayyu.net/kaskus-hotthread/?apikey=c28c944199384f191335f1f8924414fa839350d&page=2")
                                    data=r.text
                                    data=json.loads(data)                                                                                                      
                                    if data["hot_threads"] != []:
                                        no = 0
                                        hasil = "「 Kaskus Search 」\n"
                                        for news in data["hot_threads"]:
                                             no += 1                  
                                             hasil += "\n" + str(no) + ". Judul : " + str(news["title"]) + "\n • Deskripsi : " + str(news["detail"]) + "\n• Link: " + str(news["link"]) + "\n"
                                             hasil += "\n"
                                        client.sendMessage(msg.to, str(hasil))


                            elif cmd.startswith("get-telpon "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    sep = msg.text.split(" ")
                                    nomor = text.replace(sep[0] + " ","")
                                    r = requests.get("http://apisora2.herokuapp.com/prank/call/?no={}".format(urllib.parse.quote(nomor)))
                                    data = r.text
                                    data = json.loads(data)
                                    ret_ = "「 Prangked Telpon 」"
                                    ret_ += "\n• Status : {}".format(str(data["status"]))
                                    ret_ += "\n• Tujuan "+str(data["result"])
                                    client.sendMessage(msg.to, str(ret_))

                            elif cmd.startswith("get-sms "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    sep = msg.text.split(" ")
                                    nomor = text.replace(sep[0] + " ","")
                                    r = requests.get("http://apisora2.herokuapp.com/prank/sms/?no={}".format(urllib.parse.quote(nomor)))
                                    data = r.text
                                    data = json.loads(data)
                                    ret_ = "「 Prangked Sms 」"
                                    ret_ += "\n• Status : {}".format(str(data["status"]))
                                    ret_ += "\n• Tujuan "+str(data["result"])
                                    client.sendMessage(msg.to, str(ret_))

                            elif cmd.startswith("get-mimpi "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    sep = msg.text.split(" ")
                                    mimpi = msg.text.replace(sep[0] + " ","")  
                                    with requests.session() as s:
                                        s.headers['user-agent'] = 'Mozilla/5.0'
                                        r = s.get("http://primbon.com/tafsir_mimpi.php?mimpi={}&submit=+Submit+".format(urllib.parse.quote(mimpi)))
                                        soup = BeautifulSoup(r.content, 'html5lib')
                                        for anu in soup.find_all('i'):
                                            ret_ = anu.get_text()
                                            client.sendMessage(msg.to,ret_)

                            elif cmd.startswith("get-video "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    sep = msg.text.split(" ")
                                    search = msg.text.replace(sep[0] + " ","")
                                    with requests.session() as web:
                                          web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                          url = web.get("http://rahandiapi.herokuapp.com/youtubeapi/search?key=betakey&q={}".format(urllib.parse.quote(search)))
                                          data = url.text
                                          data = json.loads(data)
                                          if data["result"] != []:
                                              video = random.choice(data["result"]["videolist"])
                                              vid = video["url"]
                                              start = timeit.timeit()
                                              ret = "「 Informasi Video 」\n"
                                              ret += "• Judul : {}".format(str(data["result"]["title"]))
                                              ret += "\n• Author : {}".format(str(data["result"]["author"]))
                                              ret += "\n• Durasi : {}".format(str(data["result"]["duration"]))
                                              ret += "\n• Like nya : {}".format(str(data["result"]["likes"]))
                                              ret += "\n• Rating : {}".format(str(data["result"]["rating"]))
                                              ret += "\n• TimeTaken : {}".format(str(start))
                                              ret += "\n• Deskripsi : {}\n「 Waiting Encoding 」".format(str(data["result"]["description"]))
                                              client.sendMessage(msg.to, str(ret))
                                              client.sendVideoWithURL(msg.to, str(vid))

                            elif cmd.startswith("get-mp3 "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    sep = msg.text.split(" ")
                                    search = msg.text.replace(sep[0] + " ","")
                                    with requests.session() as web:
                                          web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                          url = web.get("http://rahandiapi.herokuapp.com/youtubeapi/search?key=betakey&q={}".format(urllib.parse.quote(search)))
                                          data = url.text
                                          data = json.loads(data)
                                          if data["result"] != []:
                                              audio = random.choice(data["result"]["audiolist"])
                                              aud = audio["url"]
                                              start = timeit.timeit()
                                              ret = "「 Informasi Mp3 」\n"
                                              ret += "• Judul : {}".format(str(data["result"]["title"]))
                                              ret += "\n• Author : {}".format(str(data["result"]["author"]))
                                              ret += "\n• Durasi : {}".format(str(data["result"]["duration"]))
                                              ret += "\n• Like nya : {}".format(str(data["result"]["likes"]))
                                              ret += "\n• Rating : {}".format(str(data["result"]["rating"]))
                                              ret += "\n• TimeTaken : {}".format(str(start))
                                              ret += "\n• Deskripsi : {}\n「 Waiting Encoding 」".format(str(data["result"]["description"]))
                                              client.sendMessage(msg.to, str(ret))
                                              client.sendAudioWithURL(msg.to, str(aud))

                            elif cmd.startswith("get-lirik "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    sep = msg.text.split(" ")
                                    search = msg.text.replace(sep[0] + " ","")
                                    params = {'songname': search}
                                    with requests.session() as web:
                                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                        url = "http://rahandiapi.herokuapp.com/lyricapi?key=betakey&q={}".format(urllib.parse.quote(search))
                                        link = web.get(url)
                                        data = link.text
                                        data = json.loads(data)
                                        start = timeit.timeit()
                                        ret_ = "「 Lirik Search 」"
                                        ret_ += "\n���✭」 Judul : {}".format(str(data["title"]))
                                        ret_ += "\n「✭」 Time Taken : {}".format(str(start))
                                        ret_ += "\n\n{}".format(str(data["lyric"]))
                                        client.sendMessage(msg.to, str(ret_))


                            elif cmd.startswith("get-instagram "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    try:
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                        sep = msg.text.split(" ")
                                        instagram = msg.text.replace(sep[0] + " ","")
                                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                        data = response.json()
                                        namaIG = str(data['graphql']['user']['full_name'])
                                        bioIG = str(data['graphql']['user']['biography'])
                                        mediaIG = str(data['graphql']['user']['edge_owner_to_timeline_media']['count'])
                                        verifIG = str(data['graphql']['user']['is_verified'])
                                        usernameIG = str(data['graphql']['user']['username'])
                                        followerIG = str(data['graphql']['user']['edge_followed_by']['count'])
                                        profileIG = data['graphql']['user']['profile_pic_url_hd']
                                        privateIG = str(data['graphql']['user']['is_private'])
                                        followIG = str(data['graphql']['user']['edge_follow']['count'])
                                        link = "• Link : " + "https://www.instagram.com/" + instagram
                                        text = "「 Instagram User 」\n• Name : "+namaIG+"\n• Username : "+usernameIG+"\n• Follower : "+followerIG+"\n• Following : "+followIG+"\n• Total post : "+mediaIG+"\n• Verified : "+verifIG+"\n• Private : "+privateIG+"\n• Biography : "+bioIG+"" "\n" + link
                                        client.sendImageWithURL(msg.to, profileIG)
                                        client.sendMessage(msg.to, str(text))
                                    except Exception as e:
                                            client.sendMessage(msg.to, str(e))

                            elif cmd.startswith("get-anime "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    sep = msg.text.split(" ")
                                    anime = msg.text.replace(sep[0] + " ","%20")                
                                    with requests.session() as web:
                                        web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    r = web.get("https://kitsu.io/api/edge/anime?filter[text]={}".format(urllib.parse.quote(anime)))
                                    data = r.text
                                    data = json.loads(data)
                                    ret_ = ''
                                    if data["data"] != []:
                                        for a in data["data"]:
                                            if a["attributes"]["subtype"] == "TV":
                                                sin = a["attributes"]["synopsis"]
                                                translator = Translator()
                                                hasil = translator.translate(sin, dest='id')
                                                sinop = hasil.text
                                                ret_ += '「 Anime {} 」'.format(str(a["attributes"]["canonicalTitle"]))
                                                ret_ += '\n• Rilis : '+str(a["attributes"]["startDate"])
                                                ret_ += '\n• Rating : '+str(a["attributes"]["ratingRank"])
                                                ret_ += '\n• Type : '+str(a["attributes"]["subtype"])
                                                ret_ += '\n• Sinopsis :\n'+str(sinop)
                                                ret_ += '\n\n'
                                                client.sendImageWithURL(msg.to, str(a["attributes"]["posterImage"]["small"]))
                                    client.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("get-xxx "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    proses = text.split(" ")
                                    urutan = text.replace(proses[0] + " ","")
                                    count = urutan.split("|")
                                    search = str(count[0])
                                    r = requests.get("https://api.avgle.com/v1/search/{}/1?limit=10".format(str(search)))
                                    data = json.loads(r.text)
                                    if len(count) == 1:
                                        no = 0
                                        hasil = "「 Pencarian Video 18+ 」\n"
                                        for aa in data["response"]["videos"]:
                                            no += 1
                                            hasil += "\n"+str(no)+". "+str(aa["title"])+"\nDurasi : "+str(aa["duration"])
                                            ret_ = "\n\nSelanjutnya Get-xxx {} | angka\nuntuk melihat detail video".format(str(search))
                                        client.sendMessage(msg.to,hasil+ret_)
                                    elif len(count) == 2:
                                        try:
                                            num = int(count[1])
                                            b = data["response"]["videos"][num - 1]
                                            c = str(b["vid"])
                                            d = requests.get("https://api.avgle.com/v1/video/"+str(c))
                                            data1 = json.loads(d.text)
                                            hasil = "Judul "+str(data1["response"]["video"]["title"])
                                            hasil += "\n\nDurasi : "+str(data1["response"]["video"]["duration"])
                                            hasil += "\nKualitas HD : "+str(data1["response"]["video"]["hd"])
                                            hasil += "\nDitonton "+str(data1["response"]["video"]["viewnumber"])
                                            #e = requests.get("https://api-ssl.bitly.com/v3/shorten?access_token=c52a3ad85f0eeafbb55e680d0fb926a5c4cab823&longUrl="+str(data1["response"]["video"]["video_url"]))
                                            #data2 = json.loads(e.text)
                                            hasil += "\nLink video : "+str(data1["response"]["video"]["video_url"])
                                            hasil += "\nLink embed : "+str(data1["response"]["video"]["embedded_url"])
                                            hasil += "\n\nKalau tidak bisa jangan lupa pakai vpn kesayangan anda"
                                            client.sendMessage(msg.to,hasil)
                                            anuanu = str(data1["response"]["video"]["preview_url"])
                                            path = client.downloadFileURL(anuanu)
                                            client.sendImage(msg.to,path)
                                            client.sendVideoWithURL(msg.to, data["data"]["url"])
                                        except Exception as e:
                                            client.sendText(msg.to," "+str(e))

                            elif cmd.startswith("get-gif "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    proses = text.split(" ")
                                    urutan = text.replace(proses[0] + " ","")
                                    count = urutan.split("|")
                                    search = str(count[0])
                                    r = requests.get("https://api.tenor.com/v1/search?key=PVS5D2UHR0EV&limit=10&q="+str(search))
                                    data = json.loads(r.text)
                                    if len(count) == 1:
                                        no = 0
                                        hasil = "「 Pencarian Gif 」\n"
                                        for aa in data["results"]:
                                            no += 1
                                            hasil += "\n" + str(no) + ". " + str(aa["title"])
                                            ret_ = "\n\nSelanjutnya Get-gif {} | angka\nuntuk melihat detail video".format(str(search))
                                        client.sendMessage(msg.to,hasil+ret_)
                                    elif len(count) == 2:
                                        try:
                                            num = int(count[1])
                                            b = data["results"][num - 1]
                                            c = str(b["id"])
                                            hasil = "Informasi gif ID "+str(c)
                                            hasil += "\n"
                                            client.sendMessage(msg.to,hasil)
                                            dl = str(b["media"][0]["loopedmp4"]["url"])
                                            client.sendVideoWithURL(msg.to,dl)
                                        except Exception as e:
                                            client.sendText(msg.to," "+str(e))  

                            elif cmd.startswith("listmeme"):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    proses = text.split(" ")
                                    keyword = text.replace(proses[0] + " ","")
                                    count = keyword.split("|")
                                    search = str(count[0])
                                    r = requests.get("http://api.imgflip.com/get_memes")
                                    data = json.loads(r.text)
                                    if len(count) == 1:
                                        no = 0
                                        hasil = "「 Daftar Meme Image 」\n"
                                        for aa in data["data"]["memes"]:
                                            no += 1
                                            hasil += "\n" + str(no) + ". "+ str(aa["name"])
                                        hasil += " "
                                        ret_ = "\n\nSelanjutnya ketik:\nListmeme | angka\nGet-meme text1 | text2 | angka"
                                        client.sendMessage(msg.to,hasil+ret_)
                                    if len(count) == 2:
                                        try:
                                            num = int(count[1])
                                            gambar = data["data"]["memes"][num - 1]
                                            hasil = "{}".format(str(gambar["name"]))
                                            sendMention(msg.to, msg._from,"「 Meme Image 」\nTunggu ","\nFoto sedang diproses...")
                                            client.sendMessage(msg.to,hasil)
                                            client.sendImageWithURL(msg.to,gambar["url"])
                                        except Exception as e:
                                            client.sendText(msg.to," "+str(e))

                            elif cmd.startswith("get-meme "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    proses = text.split(" ")
                                    keyword = text.replace(proses[0]+" ","")
                                    query = keyword.split("|")
                                    atas = query[0]
                                    bawah = query[1]
                                    r = requests.get("https://api.imgflip.com/get_memes")
                                    data = json.loads(r.text)
                                    try:
                                        num = int(query[2])
                                        namamem = data["data"]["memes"][num - 1]
                                        meme = int(namamem["id"])
                                        api = pyimgflip.Imgflip(username='andyihsan', password='ihsan848')
                                        result = api.caption_image(meme, atas,bawah)
                                        sendMention(msg.to, msg._from,"「 Meme Image 」\nTunggu ","\nFoto sedang diproses...")
                                        client.sendImageWithURL(msg.to,result["url"])
                                    except Exception as e:
                                        client.sendText(msg.to," "+str(e))

                            elif cmd.startswith("get-line "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    sep = text.split(" ")
                                    user = text.replace(sep[0] + " ","")
                                    conn = client.findContactsByUserid(user)
                                    try:
                                        anu = conn.mid
                                        dn = conn.displayName
                                        bio = conn.statusMessage
                                        sendMention(to, anu, "「 Contact Line ID 」\n• Nama : ", "\n• Nick : "+dn+"\n• Bio : "+bio+"\n• Contact link : http://line.me/ti/p/~"+user)
                                        client.sendContact(to, anu)
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))

                            elif cmd.startswith("get-fs "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    sep = msg.text.split(" ")
                                    anu = msg.text.replace(sep[0] + " "," ")                
                                    with requests.session() as web:
                                        web.headers["user-agent"] = random.choice(settings["userAgent"])
                                        r = web.get("https://farzain.xyz/api/premium/fs.php?apikey=apikey_saintsbot&id={}".format(urllib.parse.quote(anu)))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["status"] == "success":
                                            ret_ = data["url"]
                                            client.sendImageWithURL(msg.to,ret_)
                                        else:
                                            client.sendMessage(msg.to, "Error")

                            elif cmd.startswith("get-audio "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    sep = msg.text.split(" ")
                                    query = msg.text.replace(sep[0] + " "," ")
                                    cond = query.split("|")
                                    search = str(cond[0])
                                    with requests.session() as web:
                                        web.headers["User-Agent"] = "Mozilla/5.0"
                                        result = web.get("https://farzain.xyz/api/premium/yt_search.php?apikey=apikey_saintsbot&id={}".format(str(search)))
                                        data = result.text
                                        data = json.loads(data)
                                        if len(cond) == 1:
                                            if data["respons"] != []:
                                                num = 0
                                                ret_ = "「 Pencarian Audio 」\n"
                                                for res in data["respons"]:
                                                    num += 1
                                                    ret_ += "\n {}. {}".format(str(num), str(res['title']))
                                                ret_ += "\n\n Total {} Result".format(str(len(data["respons"])))
                                                client.sendMessage(msg.to, str(ret_))
                                                client.sendMessage(to, "Ketik Get-yt {} | angka\nuntuk melihat detail lagu".format(str(search)))
                                        if len(cond) == 2:
                                            num = int(cond[1])
                                            if num <= len(data["respons"]):
                                                res = data["respons"][num - 1]
                                                with requests.session() as web:
                                                    web.headers["User-Agent"] = "Mozilla/5.0"
                                                    result = web.get("http://rahandiapi.herokuapp.com/youtubeapi?key=betakey&q=https://www.youtube.com/watch?v={}".format(str(res['video_id'])))
                                                    data = result.text
                                                    data = json.loads(data)
                                                    ret_ = "「 Detail Lagu 」\nTitle : "+data['result']['title']
                                                    ret_ += "\nLikes : "+str(data['result']['likes'])
                                                    ret_ += "\nDislikes : "+str(data['result']['dislikes'])
                                                    ret_ += "\nDuration : "+str(data['result']['duration'])
                                                    ret_ += "\nRating : "+str(data['result']['rating'])
                                                    ret_ += "\nAuthor : "+str(data['result']['author'])+"\n"
                                                    cover = data['result']['thumbnail']
                                                    if data["result"]["audiolist"] != []:
                                                        for koplok in data["result"]["audiolist"]:
                                                            ret_ += "\nType : "+koplok['extension']
                                                            ret_ += "\nResolusi : "+koplok['resolution']
                                                            ret_ += "\nSize : "+koplok['size']
                                                            ret_ += "\nLink : "+koplok['url']
                                                            if koplok['resolution'] == '50k':
                                                                audio = koplok['url']
                                                    client.sendImageWithURL(msg.to,cover)
                                                    client.sendMessage(msg.to, str(ret_))
                                                    client.sendAudioWithURL(msg.to,audio)

                            elif cmd.startswith("get-bintang "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    sep = msg.text.split(" ")
                                    url = msg.text.replace(sep[0] + " ","")    
                                    with requests.session() as s:
                                        s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                        r = s.get("https://www.vemale.com/zodiak/{}".format(urllib.parse.quote(url)))
                                        soup = BeautifulSoup(r.content, 'html5lib')
                                        ret_ = ""
                                        for a in soup.select('div.vml-zodiak-detail'):
                                            ret_ += a.h1.string
                                            ret_ += "\n"+ a.h4.string
                                            ret_ += " : "+ a.span.string +""
                                        for b in soup.select('div.col-center'):
                                            ret_ += "\nTanggal : "+ b.string
                                        for d in soup.select('div.number-zodiak'):
                                            ret_ += "\nAngka keberuntungan : "+ d.string
                                        for c in soup.select('div.paragraph-left'):
                                            ta = c.text
                                            tab = ta.replace("    ", "")
                                            tabs = tab.replace(".", ".\n")
                                            ret_ += "\n"+ tabs
                                            #print (ret_)
                                        client.sendMessage(msg.to, str(ret_))
# Pembatas Script #
                            elif cmd == "changeprofilepicture":
                              if msg._from in admin:
                                settings["changePictureProfile"] = True
                                client.sendMessage(to, "Silahkan kirim gambarnya")
                            elif cmd == "changegrouppicture":
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                   if msg.toType == 2:
                                         if to not in settings["changeGroupPicture"]:
                                             settings["changeGroupPicture"].append(to)
                                         client.sendMessage(to, "Silahkan kirim gambarnya")
                                         settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                            elif cmd == 'mentionall' :
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    group = client.getGroup(msg.to)
                                    nama = [contact.mid for contact in group.members]
                                    k = len(nama)//20
                                    for a in range(k+1):
                                        txt = u''
                                        s=0
                                        b=[]
                                        for i in group.members[a*20 : (a+1)*20]:
                                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                            s += 7
                                            txt += u'@Zero \n'
                                        client.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                            elif cmd == "lurking on":
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                    hr = timeNow.strftime("%A")
                                    bln = timeNow.strftime("%m")
                                    for i in range(len(day)):
                                        if hr == day[i]: hasil = hari[i]
                                    for k in range(0, len(bulan)):
                                        if bln == str(k): bln = bulan[k-1]
                                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                    if receiver in read['readPoint']:
                                        try:
                                            del read['readPoint'][receiver]
                                            del read['readMember'][receiver]
                                            del read['readTime'][receiver]
                                        except:
                                            pass
                                        read['readPoint'][receiver] = msg_id
                                        read['readMember'][receiver] = ""
                                        read['readTime'][receiver] = readTime
                                        read['ROM'][receiver] = {}
                                        client.sendMessage(receiver,"Lurking telah diaktifkan")
                                    else:
                                        try:
                                            del read['readPoint'][receiver]
                                            del read['readMember'][receiver]
                                            del read['readTime'][receiver]
                                        except:
                                            pass
                                        read['readPoint'][receiver] = msg_id
                                        read['readMember'][receiver] = ""
                                        read['readTime'][receiver] = readTime
                                        read['ROM'][receiver] = {}
                                        client.sendMessage(receiver,"Set reading point : \n" + readTime)
                            elif cmd == "lurking off":
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                    hr = timeNow.strftime("%A")
                                    bln = timeNow.strftime("%m")
                                    for i in range(len(day)):
                                        if hr == day[i]: hasil = hari[i]
                                    for k in range(0, len(bulan)):
                                        if bln == str(k): bln = bulan[k-1]
                                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                    if receiver not in read['readPoint']:
                                        client.sendMessage(receiver,"Lurking telah dinonaktifkan")
                                    else:
                                        try:
                                            del read['readPoint'][receiver]
                                            del read['readMember'][receiver]
                                            del read['readTime'][receiver]
                                        except:
                                            pass
                                        client.sendMessage(receiver,"Delete reading point : \n" + readTime)
        
                            elif cmd == "lurking reset":
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                    hr = timeNow.strftime("%A")
                                    bln = timeNow.strftime("%m")
                                    for i in range(len(day)):
                                        if hr == day[i]: hasil = hari[i]
                                    for k in range(0, len(bulan)):
                                        if bln == str(k): bln = bulan[k-1]
                                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                    if msg.to in read["readPoint"]:
                                        try:
                                            del read["readPoint"][msg.to]
                                            del read["readMember"][msg.to]
                                            del read["readTime"][msg.to]
                                            del read["ROM"][msg.to]
                                        except:
                                            pass
                                        read['readPoint'][receiver] = msg_id
                                        read['readMember'][receiver] = ""
                                        read['readTime'][receiver] = readTime
                                        read['ROM'][receiver] = {}
                                        client.sendMessage(msg.to, "Reset reading point : \n" + readTime)
                                    else:
                                        client.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                                    
                            elif cmd == "lurking":
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        client.sendMessage(receiver,"Tidak Ada Sider")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = client.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '[R E A D E R ]\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n" + readTime
                                    try:
                                        client.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    client.sendMessage(receiver,"Lurking belum diaktifkan")
# Pembatas script #
                            elif 'Welcome ' in msg.text:
                                 spl = msg.text.replace('Welcome ','')
                                 if spl == 'on':
                                     if msg.to in welcome:
                                          msgs = "Welcome Msg sudah aktif"
                                     else:
                                          welcome.append(msg.to)
                                          ginfo = client.getGroup(msg.to)
                                          msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                     client.sendMessage(msg.to, "「 Status Welcome 」\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in welcome:
                                            welcome.remove(msg.to)
                                            ginfo = client.getGroup(msg.to)
                                            msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                       else:
                                            msgs = "Welcome Msg sudah tidak aktif"
                                       client.sendMessage(msg.to, "「 Status Welcome 」\n" + msgs)

                            elif 'Protecturl ' in msg.text:
                               if msg._from in admin:
                                  spl = msg.text.replace('Protecturl ','')
                                  if spl == 'on':
                                      if msg.to in protectqr:
                                           msgs = "Protect url sudah aktif"
                                      else:
                                           protectqr.append(msg.to)
                                           ginfo = client.getGroup(msg.to)
                                           msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      client.sendMessage(msg.to, "「 Status Protect Url 」\n" + msgs)
                                  elif spl == 'off':
                                        if msg.to in protectqr:
                                             protectqr.remove(msg.to)
                                             ginfo = cl.getGroup(msg.to)
                                             msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                        else:
                                             msgs = "Protect url sudah tidak aktif"
                                        client.sendMessage(msg.to, "「 Status Protect Url 」\n" + msgs)
                            elif 'Protectkick ' in msg.text:
                               if msg._from in admin:
                                  spl = msg.text.replace('Protectkick ','')
                                  if spl == 'on':
                                      if msg.to in protectkick:
                                           msgs = "Protect kick sudah aktif"
                                      else:
                                           protectkick.append(msg.to)
                                           ginfo = client.getGroup(msg.to)
                                           msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      client.sendMessage(msg.to, "「 Status Protect kick 」\n" + msgs)
                                  elif spl == 'off':
                                        if msg.to in protectkick:
                                             protectkick.remove(msg.to)
                                             ginfo = client.getGroup(msg.to)
                                             msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                        else:
                                             msgs = "Protect kick sudah tidak aktif"
                                        client.sendMessage(msg.to, "「 Status Protect kick 」\n" + msgs)

                            elif 'Protectjoin ' in msg.text:
                               if msg._from in admin:
                                  spl = msg.text.replace('Protectjoin ','')
                                  if spl == 'on':
                                      if msg.to in protectjoin:
                                           msgs = "Protect join sudah aktif"
                                      else:
                                           protectjoin.append(msg.to)
                                           ginfo = client.getGroup(msg.to)
                                           msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      client.sendMessage(msg.to, "「 Status Protect Join 」\n" + msgs)
                                  elif spl == 'off':
                                        if msg.to in protectjoin:
                                             protectjoin.remove(msg.to)
                                             ginfo = client.getGroup(msg.to)
                                             msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                        else:
                                             msgs = "Protect join sudah tidak aktif"
                                        client.sendMessage(msg.to, "「 Status Protect Join 」\n" + msgs)

                            elif 'Protectcancel ' in msg.text:
                               if msg._from in admin:
                                  spl = msg.text.replace('Protectcancel ','')
                                  if spl == 'on':
                                      if msg.to in protectcancel:
                                           msgs = "Protect cancel sudah aktif"
                                      else:
                                           protectcancel.append(msg.to)
                                           ginfo = client.getGroup(msg.to)
                                           msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      client.sendMessage(msg.to, "「 Status Protect Cancel 」\n" + msgs)
                                  elif spl == 'off':
                                        if msg.to in protectcancel:
                                             protectcancel.remove(msg.to)
                                             ginfo = client.getGroup(msg.to)
                                             msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                        else:
                                             msgs = "Protect cancel sudah tidak aktif"
                                        client.sendMessage(msg.to, "「 Status Protect Cancel 」\n" + msgs)

                            elif 'Protectinvite ' in msg.text:
                               if msg._from in admin:
                                  spl = msg.text.replace('Protectinvite ','')
                                  if spl == 'on':
                                      if msg.to in protectinvite:
                                           msgs = "Protect invite sudah aktif"
                                      else:
                                           protectinvite.append(msg.to)
                                           ginfo = client.getGroup(msg.to)
                                           msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      client.sendMessage(msg.to, "「 Status Protect Invite 」\n" + msgs)
                                  elif spl == 'off':
                                        if msg.to in protectinvite:
                                             protectinvite.remove(msg.to)
                                             ginfo = client.getGroup(msg.to)
                                             msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                        else:
                                             msgs = "Protect invite sudah tidak aktif"
                                        client.sendMessage(msg.to, "「 Status Protect Invite 」\n" + msgs)

                            elif 'Protectall ' in msg.text:
                               if msg._from in admin:
                                  spl = msg.text.replace('Protectall ','')
                                  if spl == 'on':
                                      if msg.to in protectqr:
                                          msgs = ""
                                      else:
                                          protectqr.append(msg.to)
                                      if msg.to in protectkick:
                                          msgs = ""
                                      else:
                                          protectkick.append(msg.to)
                                      if msg.to in protectinvite:
                                          msgs = ""
                                      else:
                                          protectinvite.append(msg.to)
                                      if msg.to in protectcancel:
                                          ginfo = cl.getGroup(msg.to)
                                          msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                          msgs += "\nSemua sudah diaktifkan"
                                      else:
                                          protectcancel.append(msg.to)
                                          ginfo = client.getGroup(msg.to)
                                          msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                          msgs += "\nSemua protection diaktifkan"
                                      client.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)
                                  elif spl == 'off':
                                        if msg.to in protectqr:
                                             protectqr.remove(msg.to)
                                        else:
                                             msgs = ""
                                        if msg.to in protectkick:
                                             protectkick.remove(msg.to)
                                        else:
                                             msgs = ""
                                        if msg.to in protectinvite:
                                             protectinvite.remove(msg.to)
                                        else:
                                             msgs = ""
                                        if msg.to in protectcancel:
                                             protectcancel.remove(msg.to)
                                             ginfo = client.getGroup(msg.to)
                                             msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                             msgs += "\nSemua protection dimatikan"
                                        else:
                                             ginfo = client.getGroup(msg.to)
                                             msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                             msgs += "\nSemua protection dimatikan"
                                        client.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)

                            elif cmd == "listprotect":
                                if msg._from in admin:
                                    ma = ""
                                    mb = ""
                                    mc = ""
                                    md = ""
                                    me = ""
                                    a = 0
                                    gid = protectqr
                                    for group in gid:
                                        a = a + 1
                                        end = '\n'
                                        ma += str(a) + ". " +client.getGroup(group).name + "\n"
                                    gid = protectkick
                                    for group in gid:
                                        a = a + 1
                                        end = '\n'
                                        mb += str(a) + ". " +client.getGroup(group).name + "\n"
                                    gid = protectjoin
                                    for group in gid:
                                        a = a + 1
                                        end = '\n'
                                        md += str(a) + ". " +client.getGroup(group).name + "\n"
                                    gid = protectcancel
                                    for group in gid:
                                        a = a + 1
                                        end = '\n'
                                        mc += str(a) + ". " +client.getGroup(group).name + "\n"
                                    gid = protectinvite
                                    for group in gid:
                                        a = a + 1
                                        end = '\n'
                                        me += str(a) + ". " +client.getGroup(group).name + "\n"
                                    client.sendMessage(msg.to,"「 Daftar Protection 」\n\n「✭」 PROTECT URL :\n"+ma+"\n「✭」 PROTECT KICK :\n"+mb+"\n「✭」 PROTECT JOIN :\n"+md+"\n「✭」 PROTECT CANCEL:\n"+mc+"\n「✭」 PROTECT INVITE:\n"+me+"\nTotal「%s」Grup diamankan" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))

                            elif 'Set welcome: ' in msg.text:
                               if msg._from in admin:
                                  spl = msg.text.replace('Set welcome: ','')
                                  if spl in [""," ","\n",None]:
                                      client.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                                  else:
                                      settings["welcome"] = spl
                                      client.sendMessage(msg.to, "「 Berhasil Diganti 」\nWelcome Msg diganti jadi :\n\n{}".format(str(spl)))

                            elif 'Set leave: ' in msg.text:
                               if msg._from in admin:
                                  spl = msg.text.replace('Set leave: ','')
                                  if spl in [""," ","\n",None]:
                                      client.sendMessage(msg.to, "Gagal mengganti Leave Msg")
                                  else:
                                      settings["leave"] = spl
                                      client.sendMessage(msg.to, "「 Berhasil Diganti 」\nLeave Msg diganti jadi :\n\n{}".format(str(spl)))

                            elif text.lower() == "cek welcome":
                               if msg._from in admin:
                                  client.sendMessage(msg.to, "「 Status Welcome 」\nWelcome Msg mu :\n\n" + str(wait["welcome"]))

                            elif text.lower() == "cek leave":
                               if msg._from in admin:
                                  client.sendMessage(msg.to, "「 Status Leave 」\nLeave Msg mu :\n\n" + str(wait["leave"]))
# Pembatas Script #   
                            elif text.lower() == 'kalender':
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                client.sendMessage(msg.to, readTime)
                            
                            elif cmd.startswith("checkwebsite"):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                   try:
                                       sep = text.split(" ")
                                       query = text.replace(sep[0] + " ","")
                                       r = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                       data = r.text
                                       data = json.loads(data)
                                       client.sendImageWithURL(to, data["result"])
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                   except Exception as error:
                                       logError(error)
                            elif cmd.startswith("checkdate"):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                   try:
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                       sep = msg.text.split(" ")
                                       tanggal = msg.text.replace(sep[0] + " ","")
                                       r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                       data=r.text
                                       data=json.loads(data)
                                       ret_ = "╭──[ D A T E ]"
                                       ret_ += "\n│ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                                       ret_ += "\n│ Age : {}".format(str(data["data"]["usia"]))
                                       ret_ += "\n│ Birthday : {}".format(str(data["data"]["ultah"]))
                                       ret_ += "\n│ Zodiak : {}".format(str(data["data"]["zodiak"]))
                                       ret_ += "\n╰──[ Success ]"
                                       client.sendMessage(to, str(ret_))
                                   except Exception as error:
                                       logError(error)
                            elif cmd.startswith("checkpraytime "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                   separate = msg.text.split(" ")
                                   location = msg.text.replace(separate[0] + " ","")
                                   r = requests.get("http://leert.corrykalam.gq/praytime.php?location={}".format(location))
                                   data = r.text
                                   data = json.loads(data)
                                   tz = pytz.timezone("Asia/Jakarta")
                                   timeNow = datetime.now(tz=tz)
                                   if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isya : ":
                                       ret_ = "╭──[ Jadwal Sholat Sekitar " + data[0] + " ]"
                                       ret_ += "\n│ Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                       ret_ += "\n│ Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                       ret_ += "\n│ " + data[1]
                                       ret_ += "\n│ " + data[2]
                                       ret_ += "\n│ " + data[3]
                                       ret_ += "\n│ " + data[4]
                                       ret_ += "\n│ " + data[5]
                                       ret_ += "\n╰──[ Success ]"
                                       client.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("checkweather "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                   try:
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                       sep = text.split(" ")
                                       location = text.replace(sep[0] + " ","")
                                       r = requests.get("https://farzain.com/api/cuaca.php?id={}".format(location))
                                       data = r.text
                                       data = json.loads(data)
                                       tz = pytz.timezone("Asia/Jakarta")
                                       timeNow = datetime.now(tz=tz)
                                       if "result" not in data:
                                           ret_ = "╭──[  Weather Status ]"
                                           ret_ += "\n│ Location : " + data[0].replace("Temperatur di kota ","")
                                           ret_ += "\n│ Suhu : " + data[1].replace("Suhu : ","") + "°C"
                                           ret_ += "\n│ Kelembaban : " + data[2].replace("Kelembaban : ","") + "%"
                                           ret_ += "\n│Tekanan udara : " + data[3].replace("Tekanan udara : ","") + "HPa"
                                           ret_ += "\n│ Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + "m/s"
                                           ret_ += "\n│──[ Time Status ]"
                                           ret_ += "\n│ Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                           ret_ += "\n│ Jam : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB"
                                           ret_ += "\n╰──[ Success ]"
                                           client.sendMessage(to, str(ret_))
                                   except Exception as error:
                                       logError(error)
                            elif cmd.startswith("checklocation "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                   try:
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                       sep = text.split(" ")
                                       location = text.replace(sep[0] + " ","")
                                       r = requests.get("http://leert.corrykalam.gq/location.php?location={}".format(location))
                                       data = r.text
                                       data = json.loads(data)
                                       if data[0] != "" and data[1] != "" and data[2] != "":
                                           link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                           ret_ = "╭──[ Location Status ]"
                                           ret_ += "\n│ Location : " + data[0]
                                           ret_ += "\n│ Google Maps : " + link
                                           ret_ += "\n╰──[ Success ]"
                                           client.sendMessage(to, str(ret_))
                                   except Exception as error:
                                       logError(error)
                            elif cmd.startswith("instainfo"):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                   try:
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                       sep = text.split(" ")
                                       search = text.replace(sep[0] + " ","")
                                       r = requests.get("https://www.instagram.com/{}/?__a=1".format(search))
                                       data = r.text
                                       data = json.loads(data)
                                       if data != []:
                                           ret_ = "╭──[ ᴘʀᴏғɪʟᴇ ɪɴsᴛᴀɢʀᴀᴍ ]"
                                           ret_ += "\n│ ɴᴀᴍᴀ : {}".format(str(data["graphql"]["user"]["full_name"]))
                                           ret_ += "\n│ ᴜsᴇʀɴᴀᴍᴇ : {}".format(str(data["graphql"]["user"]["username"]))
                                           ret_ += "\n│ ʙɪᴏ : {}".format(str(data["graphql"]["user"]["biography"]))
                                           ret_ += "\n│ ᴘᴇɴɢɪᴋᴜᴛ : {}".format(str(data["graphql"]["user"]["edge_followed_by"]["count"]))
                                           ret_ += "\n│ ᴅɪɪᴋᴜᴛɪ : {}".format(str(data["graphql"]["user"]["edge_follow"]["count"]))
                                           if data["graphql"]["user"]["is_verified"] == True:
                                               ret_ += "\n│ Verifikasi : Sudah"
                                           else:
                                               ret_ += "\n│ Verifikasi : Belum"
                                           if data["graphql"]["user"]["is_private"] == True:
                                               ret_ += "\n│ Akun Pribadi : Iya"
                                           else:
                                               ret_ += "\n│ Akun Pribadi : Tidak"
                                           ret_ += "\n│ ᴛᴏᴛᴀʟ ᴘᴏst : {}".format(str(data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]))
                                           ret_ += "\n╰──[ https://www.instagram.com/{} ]".format(search)
                                           path = data["graphql"]["user"]["profile_pic_url_hd"]
                                           client.sendImageWithURL(to, str(path))
                                           client.sendMessage(to, str(ret_))
                                   except Exception as error:
                                       logError(error)
                            elif cmd.startswith("instapost"):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                   try:
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                       sep = text.split(" ")
                                       text = text.replace(sep[0] + " ","")   
                                       cond = text.split("|")
                                       username = cond[0]
                                       no = cond[1] 
                                       r = requests.get("http://rahandiapi.herokuapp.com/instapost/{}/{}?key=betakey".format(str(username), str(no)))
                                       data = r.text
                                       data = json.loads(data)
                                       if data["find"] == True:
                                           if data["media"]["mediatype"] == 1:
                                               client.sendImageWithURL(msg.to, str(data["media"]["url"]))
                                           if data["media"]["mediatype"] == 2:
                                               client.sendVideoWithURL(msg.to, str(data["media"]["url"]))
                                           ret_ = "╭──[ Info Post ]"
                                           ret_ += "\n│ Jumlah Like : {}".format(str(data["media"]["like_count"]))
                                           ret_ += "\n│ Jumlah Comment : {}".format(str(data["media"]["comment_count"]))
                                           ret_ += "\n╰──[ Caption ]\n{}".format(str(data["media"]["caption"]))
                                           client.sendMessage(to, str(ret_))
                                   except Exception as error:
                                       logError(error)
                            elif cmd.startswith("instastory"):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                   try:
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                       sep = text.split(" ")
                                       text = text.replace(sep[0] + " ","")
                                       cond = text.split("|")
                                       search = str(cond[0])
                                       if len(cond) == 2:
                                           r = requests.get("http://rahandiapi.herokuapp.com/instastory/{}?key=betakey".format(search))
                                           data = r.text
                                           data = json.loads(data)
                                           if data["url"] != []:
                                               num = int(cond[1])
                                               if num <= len(data["url"]):
                                                   search = data["url"][num - 1]
                                                   if search["tipe"] == 1:
                                                       client.sendImageWithURL(to, str(search["link"]))
                                                   if search["tipe"] == 2:
                                                       client.sendVideoWithURL(to, str(search["link"]))
                                   except Exception as error:
                                       logError(error)
                                    
                            elif cmd.startswith("say-"):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                   sep = text.split("-")
                                   sep = sep[1].split(" ")
                                   lang = sep[0]
                                   say = text.replace("say-" + lang + " ","")
                                   if lang not in list_language["list_textToSpeech"]:
                                       return client.sendMessage(to, "Language not found")
                                   tts = gTTS(text=say, lang=lang)
                                   tts.save("hasil.mp3")
                                   client.sendAudio(to,"hasil.mp3")
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                
                            elif cmd.startswith("searchimage"):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                   try:
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                       separate = msg.text.split(" ")
                                       search = msg.text.replace(separate[0] + " ","")
                                       r = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(search))
                                       data = r.text
                                       data = json.loads(data)
                                       if data["result"] != []:
                                           items = data["result"]
                                           path = random.choice(items)
                                           a = items.index(path)
                                           b = len(items)
                                           client.sendImageWithURL(to, str(path))
                                   except Exception as error:
                                       logError(error)
                            elif cmd.startswith("searchmusic "):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                   sep = msg.text.split(" ")
                                   query = msg.text.replace(sep[0] + " ","")
                                   cond = query.split("|")
                                   search = str(cond[0])
                                   result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                   data = result.text
                                   data = json.loads(data)
                                   if len(cond) == 1:
                                       num = 0
                                       ret_ = "╭──[ Result  Musik ]"
                                       for music in data["result"]:
                                           num += 1
                                           ret_ += "\n│ {}. {}".format(str(num), str(music["single"]))
                                       ret_ += "\n╰──[ Total {} Musik ]".format(str(len(data["result"])))
                                       ret_ += "\n\nUntuk Melihat Details Music, silahkan gunakan command /music|「nomor」\nContoh: /music|1"
                                       client.sendMessage(to, str(ret_))
                                   elif len(cond) == 2:
                                       num = int(cond[1])
                                       if num <= len(data["result"]):
                                           music = data["result"][num - 1]
                                           result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                           data = result.text
                                           data = json.loads(data)
                                           if data["result"] != []:
                                               ret_ = "╭──[ Musik ]"
                                               ret_ += "\n│ Title : {}".format(str(data["result"]["song"]))
                                               ret_ += "\n│ Album : {}".format(str(data["result"]["album"]))
                                               ret_ += "\n│ Size : {}".format(str(data["result"]["size"]))
                                               ret_ += "\n│ Link : {}".format(str(data["result"]["mp3"][0]))
                                               ret_ += "\n╰──[ Finish ]"
                                               client.sendImageWithURL(to, str(data["result"]["img"]))
                                               client.sendMessage(to, str(ret_))
                                               client.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                            elif cmd.startswith("searchlirik"):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                   sep = msg.text.split(" ")
                                   query = msg.text.replace(sep[0] + " ","")
                                   cond = query.split("|")
                                   search = cond[0]
                                   api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                   data = api.text
                                   data = json.loads(data)
                                   if len(cond) == 1:
                                       num = 0
                                       ret_ = "╭──[ Result  Lirik ]"
                                       for lyric in data["results"]:
                                           num += 1
                                           ret_ += "\n│ {}. {}".format(str(num), str(lyric["single"]))
                                       ret_ += "\n╰──[ Total {}  Musik ]".format(str(len(data["results"])))
                                       ret_ += "\n\nUntuk Melihat Details Lyric, silahkan gunakan command {}SearchLyric {}|「number」".format(str(setKey), str(search))
                                       client.sendMessage(to, str(ret_))
                                   elif len(cond) == 2:
                                       num = int(cond[1])
                                       if num <= len(data["results"]):
                                           lyric = data["results"][num - 1]
                                           api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                           data = api.text
                                           data = json.loads(data)
                                           lyrics = data["results"]["lyric"]
                                           lyric = lyrics.replace('ti:','Title - ')
                                           lyric = lyric.replace('ar:','Artist - ')
                                           lyric = lyric.replace('al:','Album - ')
                                           removeString = "[1234567890.:]"
                                           for char in removeString:
                                               lyric = lyric.replace(char,'')
                                           client.sendMessage(msg.to, str(lyric))
                            elif cmd.startswith("searchyoutube"):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                   sep = text.split(" ")
                                   search = text.replace(sep[0] + " ","")
                                   params = {"search_query": search}
                                   r = requests.get("https://www.youtube.com/results", params = params)
                                   soup = BeautifulSoup(r.content, "html5lib")
                                   ret_ = "╭──[ Youtube Result ]"
                                   datas = []
                                   for data in soup.select(".yt-lockup-title > a[title]"):
                                       if "&lists" not in data["href"]:
                                           datas.append(data)
                                   for data in datas:
                                       ret_ += "\n│──[ {} ]".format(str(data["title"]))
                                       ret_ += "\n│ https://www.youtube.com{}".format(str(data["href"]))
                                   ret_ += "\n╰──[ Total {} ]".format(len(datas))
                                   client.sendMessage(to, str(ret_))
                            elif cmd.startswith("tr-"):
                               if sender not in settings["limituser"]:
                                          settings["limituser"][sender] = {'count':0,'limit':5}
                               if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                          sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                               else:
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                   sep = text.split("-")
                                   sep = sep[1].split(" ")
                                   lang = sep[0]
                                   say = text.replace("tr-" + lang + " ","")
                                   if lang not in list_language["list_translate"]:
                                       return client.sendMessage(to, "Language not found")
                                   translator = Translator()
                                   hasil = translator.translate(say, dest=lang)
                                   A = hasil.text
                                   client.sendMessage(to, str(A))
#================[ sticker ]===============
                        if cmd in ['hi','halo','hai','hy','hay','haii','helo','hello','hey']:  
                            pesannya = {
                                "type": "template",
                                "altText": "{} Mengirim Sticker".format(str(client.getContact(clientMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/52002768/IOS/sticker_animation@2x.png",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line.me/ti/p/%40175qduzr",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            client.sendFlex(msg.to,pesannya)
# Pembatas Script #
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = client.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            client.updateProfilePicture(path)
                            client.sendMessage(to, "Berhasil mengubah foto profile")
                        if msg.toType == 2:
                            if to in settings["changeGroupPicture"]:
                                path = client.downloadObjectMsg(msg_id)
                                settings["changeGroupPicture"].remove(to)
                                client.updateGroupPicture(to, path)
                                client.sendMessage(to, "Berhasil mengubah foto group")
                    elif msg.contentType == 7:
                        if settings["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "╭──[ sᴛɪᴄᴋᴇʀ ɪɴғᴏ ]"
                            ret_ += "\n│ sᴛɪᴄᴋᴇʀ ᴍɪᴅ : {}".format(stk_id)
                            ret_ += "\n│ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇs ɪᴅ : {}".format(pkg_id)
                            ret_ += "\n│ sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ : {}".format(stk_ver)
                            ret_ += "\n│ sᴛɪᴄᴋᴇʀ ᴜʀʟ : line://shop/detail/{}".format(pkg_id)
                            ret_ += "\n╰──[ Finish ]"
                            client.sendMessage(to, str(ret_))
                    elif msg.contentType == 13:
                        if settings["checkContact"] == True:
                            try:
                                contact = client.getContact(msg.contentMetadata["mid"])
                                if client != None:
                                    cover = client.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    client.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "╭──[ Details Contact ]"
                                ret_ += "\n│ Nama : {}".format(str(contact.displayName))
                                ret_ += "\n│ MID : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n│ Bio : {}".format(str(contact.statusMessage))
                                ret_ += "\n│ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n│ Gambar Cover : {}".format(str(cover))
                                ret_ += "\n╰──[ Finish ]"
                                client.sendMessage(to, str(ret_))
                            except:
                                client.sendMessage(to, "Kontak tidak valid")
                    elif msg.contentType == 16:
                        if settings["checkPost"] == True:
                            try:
                                ret_ = "╭──[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = client.getContact(sender)
                                    auth = "\n│ Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n│ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n│ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n│ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n│ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n│ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n│ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n│ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n│ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n│ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n│ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╰──[ Finish ]"
                                client.sendMessage(to, str(ret_))
                            except:
                                client.sendMessage(to, "Post tidak valid")
                backupData()		
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 26:
            try:
                #print ("[ 26 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if settings["autoRead"] == True:
                        client.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            client.sendMessage(msg.to,text)
                    if settings["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                client.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                client.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                         try:
                             if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                         n_links.append(l)
                                 for ticket_id in n_links:
                                     group = client.findGroupByTicket(ticket_id)
                                     if group.preventedJoinByTicket == False:
                                       if len(group.members) >= 10:
                                         if len(group.members) <= 498:
                                             client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                             client.sendMessage(to, client.profile.displayName + " berhasil masuk ke group %s" % str(group.name))
                                       else:
                                            client.sendMessage(to, client.profile.displayName + " tidak bisa bergabung ke group %s karena member dibawah 10" % str(group.name))
                                     else:
                                        client.sendMessage(to, client.profile.displayName + " tidak bisa bergabung karena QR Group %s tertutup" % str(group.name))
                         except:
                               pass
		
                    if msg.contentType == 0 and sender not in clientMid and msg.toType == 2:
                        if "MENTION" in msg.contentMetadata.keys() != None and settings["responMentionnya"]==True:
                            contact = ayam.getContact(msg._from)
                            cName = contact.displayName
                            text = msg.text
                            balas = ["gaush tag tag"]
                            ret_ = "" + random.choice(balas)
                            mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                            mentionees = mention["MENTIONEES"]
                            pesannya = {
                                    "type": "flex",
                                    "altText": "{} Mengirim Tanggapan Mention".format(str(ayam.getContact(ayamMid).displayName)),
                                    "contents": {
                                        "type": "bubble",
                                        "body": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/%40175qduzr"
                                            },
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "{}".format(str(text)),
                                                    "color": "#aaaaaa"
                                                }
                                            ]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "{}".format(str(ret_)),
                                                    "color": "#000000",
                                                    "align": "center",
                                                    "weight":"bold",
                                                    "wrap": True
                                                }
                                            ]
                                        },
                                        "styles": {
                                            "body": {
                                                "backgroundColor": "#ffda6b"
                                            },
                                            "footer": {
                                                "backgroundColor": "#f9bb00"
                                            }
                                        }
                                    }
                                }
                            for mention in mentionees:
                                if mention['M'] in ayamMid:
                                    client.sendFlex(msg.to,pesannya)
                                    break
                backupData()
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        
        if msg.contentType == 16:
            if settings["autolike"]==True:
                url_post = msg.contentMetadata['postEndUrl']
                pliter = url_post.replace('line://home/post?userMid=','')
                pliter = pliter.split('&postId=')
                client.likePost(mid=pliter[0],postId=pliter[1])
                client.createComment(mid=pliter[0],postId=pliter[1],text=settings["comment"])
                client.sendFlex(receiver, plate["likednya"])
                print ("Post Liked")
        
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            dan = client.getContact(op.param2)
                            tgb = client.getGroup(op.param1)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        sendMention(op.param1, "@! jomblo datang".format(str(tgb.name)),[op.param2])
                                    else:
                                        sendMention(op.param1, "@! sider mulu".format(str(tgb.name)),[op.param2])
                                else:
                                    sendMention(op.param1, "@! ngopi kuy".format(str(tgb.name)),[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass  
                
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = client.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n☀。" + Name
                        wait2['ROM'][op.param1][op.param2] = "☠。" + Name
                else:
                    client.sendMessage
            except:
                  pass
              
        if op.type == 26:
            msg = op.message
            msg.text = str(msg.text)
            text = msg.text
            try:
                if msg.contentType == 0:
                    try:
                        if msg.to in wait2['readPoint']:
                            if msg._from in wait2["ROM"][msg.to]:
                                del wait2["ROM"][msg.to][msg._from]
                        else:
                            pass
                    except:
                        pass
                else:
                    pass
            except KeyboardInterrupt:
                         sys.exit(0)
            except Exception as error:
                return
        if op.type == 55:
            #print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
        backupData()
    except Exception as error:
        logError(error)
	
while True:
    try:
        #autoRestart()
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clientBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e) 

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)

#while True:
 #   try:
      #  autoRestart()
  #      delete_log()
  #      ops = clientPoll.singleTrace(count=50)
   #     if ops is not None:
     #       for op in ops:
                #clientBot(op)
         #       clientPoll.setRevision(op.revision)
      #          thread1 = threading.Thread(target=clientBot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
              #  thread1.start()
      #          thread1.join()
 #   except Exception as error:
    #    logError(error)
