# -*- coding: utf-8 -*-
# -*- editing by WiraYudhaPratama-*-#

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
import requests
import json
import urllib.request
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit, subprocess
import time, requests

#client = LINE()
client = LINE("token")
squareChatMid='(sd88556581cadb14f8c645138d6a7da9b)' 
clientMid = client.profile.mid
clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientPoll = OEPoll(client)
botStart = time.time()
admin = ["u5d7d5d11183427aa3d043430075c7577"]#,"uecc57cb55f480ee2a45d81434a9b864d"]

temp_flood = {}
groupName = {}
groupImage = {}
delExpire = ()
msg_dict = {}
welcome = []
protectkick = []
protectinvite = []
protectqr = []
protectjoin = []
protectcancel = []

settings = {
    "userMentioned": {},
    "Welcome": False,
    "Leave": False,
    "autoAdd": False,
    "autoJoin": False,
    "autoLeave": False,
    "autoRead": False,
    "autoRespon": False,
    "autoResponGc": False,
    "autoJoinTicket": False,
    "autoJoinTicketSquare": False,
    "checkContact": False,
    "checkPost": False,
    "checkSticker": False,
    "changePictureProfile": False,
    "ChangeVideoProfile": False,
    "ChangeVideoProfilevid": False,
    "ChangeVideoProfilePicture": False,
    "changeCover": False,
    "changeProfileCover": {},
    "changeGroupPicture": [],
    "blacklist":{},
    "keyCommand": ".",
    "replyPesan": "Go back MDFK",
    "welcome": "Selamat datang",
    "leave": "Bye bye",
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "changeProfileVideo": {
          "status": False,
          "stage": {},
          "picture":{},
          "video":{}
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "setKey": False,
    "sider": False,
    "unsendMessage": False
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

message = {
    "replyPesan":"Don't tag me,It's annoying.",
}


read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
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

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
settings["myProfile"]["displayName"] = clientProfile.displayName
settings["myProfile"]["statusMessage"] = clientProfile.statusMessage
settings["myProfile"]["pictureStatus"] = clientProfile.pictureStatus
coverId = client.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

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

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        client.sendMessage(tmp, "Bot kembali aktif")
                    except Exception as error:
                        logError(error)

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

def userMentioned(to):
    try:
        mid = []
        for lu in settings["userMentioned"][to]:
            mid.append(lu)
        arrData = ""
        textx = "???[ List User ]\n".format(str(len(mid)))
        arr = []
        no = 0 + 1
        for i in mid:
            textx += "? {}. ".format(str(no))
            mention = "@x "
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            textx += "#{}x\n".format(str(settings["userMentioned"][to][i]))
            no += 1
        textx += "???[ Total {} User ]".format(str(len(mid)))
        settings["userMentioned"][to] = {}
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)

def sendMentionFooter(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Meka Finee "
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
    client.sendMessage(to, textx, {'AGENT_NAME':client.profile.displayName, 'AGENT_LINK': 'line://ti/p/~{}'.format(client.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + client.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
   
def ChangeVideoProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = client.genOBSParams({'oid': clientMid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'Hello_World.mp4'})
        data = {'params': obs_params}
        r_vp = client.server.postContent('{}/talk/vp/upload.nhn'.format(str(client.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        client.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))

def changeProfileVideo(to):
    if settings['changeProfileVideo']['picture'] == None:
        return client.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changeProfileVideo']['video'] == None:
        return client.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = client.genOBSParams({'oid': client.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = client.server.postContent('{}/talk/vp/upload.nhn'.format(str(client.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return client.sendMessage(to, "Gagal update profile")
        path_p = settings['changeProfileVideo']['picture']
        settings['changeProfileVideo']['status'] = False
        client.updateProfilePicture(path_p, 'vp')

def sendMessageFooter(to, text):
 client.reissueUserTicket()
 dap = client.getProfile()
 ticket = "http://line.me/ti/p/"+client.getUserTicket().id
 pict = "http://dl.profile.line-cdn.net/"+dap.pictureStatus
 name = dap.displayName
 dapi = {"AGENT_ICON": pict,
     "AGENT_NAME": name,
     "AGENT_LINK": ticket
 }
 client.sendMessage(to, text, contentMetadata=dapi)    
        
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
    
def helpmessage():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpMessage =   "╭──[─┅═✥[ʏᴜᴅʜᴀ-ʙᴏᴛ]✥═┅─]" + "\n" + \
                    "│• Gunakan[ " + key + " ]di depannya" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "yud" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "yud token" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "yud status" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "yud settings" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "yud self" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "yud group" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "yud special" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "yud media" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "Translate" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "TextToSpeech" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ErrorLog" + "\n" + \
                    "│【ʏᴜᴅ】 " + key + "ResetLogError" + "\n" + \
                    "│──────────" + "\n" + \
                    "│Creator: @!" + "\n" + \
                    "╰──────────"
    return helpMessage

def helptokenmessage():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTokenMessage =   "╭──[─┅═✥[ʏᴜᴅʜᴀ-ʙᴏᴛ]✥═┅─]" + "\n" + \
                         "│• Gunakan[ " + key + " ]di depannya" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token chrome" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token ios" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token win10" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token mac" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token desktop" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token done" + "\n" + \
                         "│──────────" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token2 chromeos" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token2 iosipad" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token2 win10" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token2 desktopmac" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token2 desktopwin" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token2 done" + "\n" + \
                         "│──────────" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token3 chromeos" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token3 iosipad" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token3 win10" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token3 desktopmac" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Token3 desktopwin" + "\n" + \
                    "│──────────" + "\n" + \
                    "│Creator: @!" + "\n" + \
                    "╰──────────"
    return helpTokenMessage


def statuscommand():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpStatusCommand =   "╭──[─┅═✥[ʏᴜᴅʜᴀ-ʙᴏᴛ]✥═┅─]" + "\n" + \
                          "│• Gunakan[ " + key + " ]di depannya" + "\n" + \
                          "│【ʏᴜᴅ】 " + key + "Restart" + "\n" + \
                          "│【ʏᴜᴅ】 " + key + "Runtime" + "\n" + \
                          "│【ʏᴜᴅ】 " + key + "Speed" + "\n" + \
                          "│【ʏᴜᴅ】 " + key + "Status" + "\n" + \
                          "│【ʏᴜᴅ】 MyKey" + "\n" + \
                          "│【ʏᴜᴅ】 SetKey[On/Off]" + "\n" + \
                          "│【ʏᴜᴅ】 Resetkey" + "\n" + \
                          "│【ʏᴜᴅ】 " + key + "ChangeKey:[Query]" + "\n" + \
                    "│──────────" + "\n" + \
                    "│Creator: @!" + "\n" + \
                    "╰──────────"
    return helpStatusCommand

def settingscommand():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSettingsCommand =  "╭──[─┅═✥[ʏᴜᴅʜᴀ-ʙᴏᴛ]✥═┅─]" + "\n" + \
                           "│• Gunakan[ " + key + " ]di depannya" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "AutoAdd[On/Off]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "AutoJoin[On/Off]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "AutoJoinTicket[On/Off]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "AutoJoinTicketSquare[On/Off]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "AutoLeave[On/Off]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "AutoRead[On/Off]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "AutoRespon[On/Off]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "CheckContact[On/Off]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "CheckPost[On/Off]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "CheckSticker[On/Off]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "UnsendChat[On/Off]" + "\n" + \
                    "│──────────" + "\n" + \
                    "│Creator: @!" + "\n" + \
                    "╰──────────"
    return helpSettingsCommand

def selfcommand():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSelfCommand =   "╭──[─┅═✥[ʏᴜᴅʜᴀ-ʙᴏᴛ]✥═┅─]" + "\n" + \
                        "│• Gunakan[ " + key + " ]di depannya" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "ChangeName:[Query]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "ChangeBio:[Query]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "Me" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "MyMid" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "MyName" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "MyBio" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "MyPicture" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "MyVideoProfile" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "MyCover" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "MyTicket" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "StealContact[Mention]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "StealMid[Mention]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "StealName[Mention]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "StealBio[Mention]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "StealPicture[Mention]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "StealVideoProfile[Mention]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "StealCover[Mention]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "CloneProfile[Mention]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "Removeallchat" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "RestoreProfile" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "BackupProfile" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "ChangePictureProfile" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "Changedual" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "CheckMention" + "\n" + \
                    "│──────────" + "\n" + \
                    "│Creator: @!" + "\n" + \
                    "╰──────────"
    return helpSelfCommand

def groupcommand():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpGroupCommand =   "╭──[─┅═✥[ʏᴜᴅʜᴀ-ʙᴏᴛ]✥═┅─]" + "\n" + \
                         "│• Gunakan[ " + key + " ]di depannya" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Leaveto [NamaGroup]" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Allbroadcast" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Gbroadcast" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "Fbroadcast" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "GroupCancel" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "GroupCreator" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "GroupId" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "GroupName" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "GroupPicture" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "GroupTicket" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "GroupTicket[On/Off]" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "GroupList" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "GroupMemberList" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "GroupInfo" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "ChangeGroupName[Name]" + "\n" + \
                         "│【ʏᴜᴅ】 " + key + "ChangeGroupPicture" + "\n" + \
                    "│──────────" + "\n" + \
                    "│Creator: @!" + "\n" + \
                    "╰──────────"
    return helpGroupCommand

def specialcommand():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSpecialCommand =   "╭──[─┅═✥[ʏᴜᴅʜᴀ-ʙᴏᴛ]✥═┅─]" + "\n" + \
                           "│• Gunakan[ " + key + " ]di depannya" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "Gitlabprofile [username]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "InviteGroupCall [Jumlah]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "Kalender" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "Mimic[On/Off]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "MimicList" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "MimicAdd[Mention]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "MimicDel[Mention]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "Mention" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "Murottal[Surah Ke]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "Lurking[On/Off/Reset]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "Lurking" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "Sider[On/Off]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "Rw text|text|text" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "Pcid|id_line|text" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "/call [Number]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "/sms [Number] [Text]" + "\n" + \
                           "│【ʏᴜᴅ】 " + key + "announce" + "\n" + \
                    "│──────────" + "\n" + \
                    "│Creator: @!" + "\n" + \
                    "╰──────────"
    return helpSpecialCommand

def mediacommand():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpMediaCommand =  "╭──[─┅═✥[ʏᴜᴅʜᴀ-ʙᴏᴛ]✥═┅─]" + "\n" + \
                        "│• Gunakan[ " + key + " ]di depannya" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "AnimeList" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "AnimeNew" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "Epplist [Number]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "Streamepp [Judul]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "Streameppz [Number]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "Meme-buzz [Search]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "CheckDate [Date]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "CheckWebsite [url]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "CheckPraytime [Location]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "CheckWeather [Location]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "CheckLocation [Location]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "InstaInfo [UserName]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "InstaPost [UserName]|[Number]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "InstaStory [UserName]|[Number]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "SearchYoutube [Search]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "SearchMusic [Search]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "SearchLyric [Search]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "SearchImage [Search]" + "\n" + \
                        "│【ʏᴜᴅ】 " + key + "Screenshotwebsite [Search]" + "\n" + \
                    "│──────────" + "\n" + \
                    "│Creator: @!" + "\n" + \
                    "╰──────────"
    return helpMediaCommand

def helptexttospeech():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTextToSpeech =  "╭──[─┅═✥[ʏᴜᴅʜᴀ-ʙᴏᴛ]✥═┅─]" + "\n" + \
                        "│• Gunakan[ " + key + " ]di depannya" + "\n" + \
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
                        "╰──────────"
    return helpTextToSpeech

def helptranslate():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTranslate = "╭──[─┅═✥[ʏᴜᴅʜᴀ-ʙᴏᴛ]✥═┅─]" + "\n" + \
                    "? -> Gunakan[ " + key + " ]di depannya" + "\n" + \
                    "?????? " + key + "af : afrikaans" + "\n" + \
                    "?????? " + key + "sq : albanian" + "\n" + \
                    "?????? " + key + "am : amharic" + "\n" + \
                    "?????? " + key + "ar : arabic" + "\n" + \
                    "?????? " + key + "hy : armenian" + "\n" + \
                    "?????? " + key + "az : azerbaijani" + "\n" + \
                    "?????? " + key + "eu : basque" + "\n" + \
                    "?????? " + key + "be : belarusian" + "\n" + \
                    "?????? " + key + "bn : bengali" + "\n" + \
                    "?????? " + key + "bs : bosnian" + "\n" + \
                    "?????? " + key + "bg : bulgarian" + "\n" + \
                    "?????? " + key + "ca : catalan" + "\n" + \
                    "?????? " + key + "ceb : cebuano" + "\n" + \
                    "?????? " + key + "zhcn : chinese (simplified)" + "\n" + \
                    "â”‚ï¿½ï¿½ï¿½á´›ï¿½ï¿½ã€‘ " + key + "zhtw : chinese (traditional)" + "\n" + \
                    "?????? " + key + "co : corsican" + "\n" + \
                    "?????? " + key + "hr : croatian" + "\n" + \
                    "?????? " + key + "cs : czech" + "\n" + \
                    "?????? " + key + "da : danish" + "\n" + \
                    "?????? " + key + "nl : dutch" + "\n" + \
                    "?????? " + key + "en : english" + "\n" + \
                    "?????? " + key + "eo : esperanto" + "\n" + \
                    "?????? " + key + "et : estonian" + "\n" + \
                    "?????? " + key + "tl : filipino" + "\n" + \
                    "?????? " + key + "fi : finnish" + "\n" + \
                    "?????? " + key + "fr : french" + "\n" + \
                    "?????? " + key + "fy : frisian" + "\n" + \
                    "?????? " + key + "gl : galician" + "\n" + \
                    "?????? " + key + "ka : georgian" + "\n" + \
                    "?????? " + key + "de : german" + "\n" + \
                    "?????? " + key + "el : greek" + "\n" + \
                    "?????? " + key + "gu : gujarati" + "\n" + \
                    "?????? " + key + "ht : haitian creole" + "\n" + \
                    "?????? " + key + "ha : hausa" + "\n" + \
                    "?????? " + key + "haw : hawaiian" + "\n" + \
                    "?????? " + key + "iw : hebrew" + "\n" + \
                    "?????? " + key + "hi : hindi" + "\n" + \
                    "?????? " + key + "hmn : hmong" + "\n" + \
                    "?????? " + key + "hu : hungarian" + "\n" + \
                    "?????? " + key + "is : icelandic" + "\n" + \
                    "?????? " + key + "ig : igbo" + "\n" + \
                    "?????? " + key + "id : indonesian" + "\n" + \
                    "?????? " + key + "ga : irish" + "\n" + \
                    "?????? " + key + "it : italian" + "\n" + \
                    "?????? " + key + "ja : japanese" + "\n" + \
                    "?????? " + key + "jw : javanese" + "\n" + \
                    "?????? " + key + "kn : kannada" + "\n" + \
                    "?????? " + key + "kk : kazakh" + "\n" + \
                    "?????? " + key + "km : khmer" + "\n" + \
                    "?????? " + key + "ku : kurdish (kurmanji)" + "\n" + \
                    "?????? " + key + "ky : kyrgyz" + "\n" + \
                    "?????? " + key + "lo : lao" + "\n" + \
                    "?????? " + key + "la : latin" + "\n" + \
                    "?????? " + key + "lv : latvian" + "\n" + \
                    "?????? " + key + "lt : lithuanian" + "\n" + \
                    "?????? " + key + "lb : luxembourgish" + "\n" + \
                    "?????? " + key + "mk : macedonian" + "\n" + \
                    "?????? " + key + "mg : malagasy" + "\n" + \
                    "?????? " + key + "ms : malay" + "\n" + \
                    "?????? " + key + "ml : malayalam" + "\n" + \
                    "?????? " + key + "mt : maltese" + "\n" + \
                    "?????? " + key + "mi : maori" + "\n" + \
                    "?????? " + key + "mr : marathi" + "\n" + \
                    "?????? " + key + "mn : mongolian" + "\n" + \
                    "?????? " + key + "my : myanmar (burmese)" + "\n" + \
                    "?????? " + key + "ne : nepali" + "\n" + \
                    "?????? " + key + "no : norwegian" + "\n" + \
                    "?????? " + key + "ps : pashto" + "\n" + \
                    "?????? " + key + "fa : persian" + "\n" + \
                    "?????? " + key + "pl : polish" + "\n" + \
                    "?????? " + key + "pt : portuguese" + "\n" + \
                    "?????? " + key + "pa : punjabi" + "\n" + \
                    "?????? " + key + "ro : romanian" + "\n" + \
                    "?????? " + key + "ru : russian" + "\n" + \
                    "?????? " + key + "sm : samoan" + "\n" + \
                    "?????? " + key + "gd : scots gaelic" + "\n" + \
                    "?????? " + key + "sr : serbian" + "\n" + \
                    "?????? " + key + "st : sesotho" + "\n" + \
                    "?????? " + key + "sn : shona" + "\n" + \
                    "?????? " + key + "sd : sindhi" + "\n" + \
                    "?????? " + key + "si : sinhala" + "\n" + \
                    "?????? " + key + "sk : slovak" + "\n" + \
                    "?????? " + key + "sl : slovenian" + "\n" + \
                    "?????? " + key + "so : somali" + "\n" + \
                    "?????? " + key + "es : spanish" + "\n" + \
                    "?????? " + key + "su : sundanese" + "\n" + \
                    "?????? " + key + "sw : swahili" + "\n" + \
                    "?????? " + key + "sv : swedish" + "\n" + \
                    "?????? " + key + "tg : tajik" + "\n" + \
                    "?????? " + key + "ta : tamil" + "\n" + \
                    "?????? " + key + "te : telugu" + "\n" + \
                    "?????? " + key + "th : thai" + "\n" + \
                    "?????? " + key + "tr : turkish" + "\n" + \
                    "?????? " + key + "uk : ukrainian" + "\n" + \
                    "?????? " + key + "ur : urdu" + "\n" + \
                    "?????? " + key + "uz : uzbek" + "\n" + \
                    "?????? " + key + "vi : vietnamese" + "\n" + \
                    "?????? " + key + "cy : welsh" + "\n" + \
                    "?????? " + key + "xh : xhosa" + "\n" + \
                    "?????? " + key + "yi : yiddish" + "\n" + \
                    "?????? " + key + "yo : yoruba" + "\n" + \
                    "?????? " + key + "zu : zulu" + "\n" + \
                    "?????? " + key + "fil : Filipino" + "\n" + \
                    "?????? " + key + "he : Hebrew" + "\n" + \
                    "╰──────────"

def clientBot(op):
    try:
        if op.type == 0:
            #print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
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
            #print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                sendMessageFooter(op.param1, "Halo {} Thanks For Add.".format(str(client.getContact(op.param1).displayName)))

        if op.type == 13:
            #print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            if settings["autoJoin"] == True:
                client.acceptGroupInvitation(op.param1)
                sendMessageFooter(op.param1, "Thanks For Invite")
                client.sendContact(op.param1, "u63bf99a61cca9f6dcc8d851c2c57a67b")

        if op.type == 17:
            #print ("[ 17 ] NOTIFIED WELCOME")
            if settings["Welcome"] == True:
               gid = client.getGroup(op.param1)
               yud = client.getContact(op.param2)
               cient.sendContact(op.param1, op.param2)
               sendMessageFooter(op.param1,"Selamat datang dan selamat berbelanja di " + gid.name)
               
        if op.type == 15:
            #print ("[ 15 ] NOTIFIED LEAVE")
            if settings["leave"] == True:
                client.sendContact(op.param1, op.param2)
                sendMessageFooter(op.param1, "Terimakasih telah berkunjung")
                
        if op.type in [22, 24]:
            #print ("[ 22 And 24 ] NOTIFIED INVITE INTO ROOM & NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                sendMessageFooter(op.param1, "Jangan invite gw!")
                client.sendContact(op.param1, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                client.leaveRoom(op.param1)
        if op.type in [25,26]:
            #print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if receiver in temp_flood:
                            if temp_flood[receiver]["expire"] == True:
                               if cmd == "open":
                                    temp_flood[receiver]["expire"] = False
                                    temp_flood[receiver]["time"] = time.time()
                                    client.sendMessage(to, "Bot kembali aktif")
                               return
                            elif time.time() - temp_flood[receiver]["time"] <= 5:
                                temp_flood[receiver]["flood"] += 1
                                if temp_flood[receiver]["flood"] >= 20:
                                    temp_flood[receiver]["flood"] = 0
                                    temp_flood[receiver]["expire"] = True
                                    
                                    client.sendMessage(to, "Flood detected, Bot will silent in 30 seconds in this room. Waiting for it or type Ran Open to activated.")
                            else:
                                 temp_flood[receiver]["flood"] = 0
                                 temp_flood[receiver]["time"] = time.time()
                        else:
                            temp_flood[receiver] = {
    	                        "time": time.time(),
    	                        "flood": 0,
    	                        "expire": False
                            }

        if op.type == 25:
            try:
                #print ("[ 25 ] SEND MESSAGE")
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
                            if cmd == "yud":
                                helpMessage = helpmessage()
                                sendMentionFooter(to, str(helpMessage), admin)
                                client.sendContact(to, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                            if cmd == "yud token":
                                helpTokenMessage = helptokenmessage()
                                sendMentionFooter(to, str(helpTokenMessage), admin)
                                client.sendContact(to, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                            if cmd == "yud status":
                                helpStatusCommand = statuscommand()
                                sendMentionFooter(to, str(helpStatusCommand), admin)
                                client.sendContact(to, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                            if cmd == "yud settings":
                                helpSettingsCommand = settingscommand()
                                sendMentionFooter(to, str(helpSettingsCommand), admin)
                                client.sendContact(to, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                            if cmd == "yud self":
                                helpSelfCommand = selfcommand()
                                sendMentionFooter(to, str(helpSelfCommand), admin)
                                client.sendContact(to, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                            if cmd == "yud group":
                                helpGroupCommand = groupcommand()
                                sendMentionFooter(to, str(helpGroupCommand), admin)
                                client.sendContact(to, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                            if cmd == "yud special":
                                helpSpecialCommand = specialcommand()
                                sendMentionFooter(to, str(helpSpecialCommand), admin)
                                client.sendContact(to, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                            if cmd == "yud media":
                                helpMediaCommand = mediacommand()
                                sendMentionFooter(to, str(helpMediaCommand), admin)
                                client.sendContact(to, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                            elif cmd == "TextToSpeech":
                                helpTextToSpeech = helptexttospeech()
                                sendMessageFooter(to, str(helpTextToSpeech))
                                client.sendContact(to, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                            elif cmd == "tts":
                                helpTextToSpeech = helptexttospeech()
                                sendMessageFooter(to, str(helpTextToSpeech))
                                client.sendContact(to, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                            elif cmd == "translate":
                                helpTranslate = helptranslate()
                                sendMessageFooter(to, str(helpTranslate))
                                client.sendContact(to, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                            elif cmd == "tr":
                                helpTranslate = helptranslate()
                                sendMessageFooter(to, str(helpTranslate))
                                client.sendContact(to, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                            elif cmd.startswith('/call '):
                                try:
                                    call = text.replace('/call ','')
                                    r = requests.get('https://farzain.xyz/api/prank().php?apikey=&id='+call+'&type=2')
                                    sendMentionFooter(receiver, "@! Sukses melakukan panggilan ke nomor  "+call,[sender])
                                except Exception as e:
                                    client.sendMessage(receiver, str(e))
                                    logError(e)
                            elif cmd.startswith('/sms '):
                                try:
                                    sms = text.replace('/sms ','')
                                    r = requests.get('https://farzain.xyz/api/prank().php?apikey=&id='+sms+'&type=1')
                                    sendMentionFooter(receiver, "@! Sukses mengirim pesan ke nomor  "+sms,[sender])
                                except Exception as e:
                                    client.sendMessage(receiver, str(e))
                                    logError(e)
                            elif cmd.startswith("changekey:"):
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                if " " in key:
                                    sendMessageFooter(to, "Key tidak bisa menggunakan spasi")
                                else:
                                    settings["keyCommand"] = str(key).lower()
                                    sendMessageFooter(to, "Berhasil mengubah key command menjadi [ {} ]".format(str(key).lower()))
                            elif cmd == "speed":
                                start = time.time()
                                sendMessageFooter(to, "Progress...")
                                elapsed_time = time.time() - start
                                sendMessageFooter(to, "[ Speed ]\nKecepatan mengirim pesan {} detik".format(str(elapsed_time)))
                            elif cmd == "gas":
                                start = time.time()
                                sendMessageFooter(to, "Progress...")
                                elapsed_time = time.time() - start
                                sendMessageFooter(to, "[ Speed ]\nKecepatan mengirim pesan {} detik".format(str(elapsed_time)))
                            elif cmd == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                sendMessageFooter(to, "Bot sudah berjalan selama {}".format(str(runtime)))
                            elif cmd == "rt":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                sendMessageFooter(to, "Bot sudah berjalan selama {}".format(str(runtime)))
                            elif cmd == "restart":
                                sendMessageFooter(to, "Berhasil merestart Bot")
                                restartBot()
                            elif cmd == "errorlog":
                                with open('errorLog.txt', 'r') as fp:
                                    isi = fp.read()
                                client.sendMessage(to, str(isi))
                            elif cmd == "resetlogerror":
                                with open("errorLog.txt","w") as fp:
                                    fp.write("")
                                sendMessageFooter(to,"Berhasil reset log error")
# Pembatas Script #
                            elif cmd == "welcome on":
                                settings["Welcome"] = True
                                sendMessageFooter(to, "Berhasil mengaktifkan welcome message")
                            elif cmd == "welcome off":
                                settings["Welcome"] = False
                                sendMessageFooter(to, "Berhasil menonaktifkan welcome message")
                            elif cmd == "leave on":
                                settings["Leave"] = True
                                sendMessageFooter(to, "Berhasil mengaktifkan Leave message")
                            elif cmd == "leave off":
                                settings["Leave"] = False
                                sendMessageFooter(to, "Berhasil menonaktifkan leave message")
                            elif cmd == "autoadd on":
                                settings["autoAdd"] = True
                                sendMessageFooter(to, "Berhasil mengaktifkan auto add")
                            elif cmd == "autoadd off":
                                settings["autoAdd"] = False
                                sendMessageFooter(to, "Berhasil menonaktifkan auto add")
                            elif cmd == "autojoin on":
                                settings["autoJoin"] = True
                                sendMessageFooter(to, "Berhasil mengaktifkan auto join")
                            elif cmd == "autojoin off":
                                settings["autoJoin"] = False
                                sendMessageFooter(to, "Berhasil menonaktifkan auto join")
                            elif cmd == "autoleave on":
                                settings["autoLeave"] = True
                                sendMessageFooter(to, "Berhasil mengaktifkan auto leave")
                            elif cmd == "autoleave off":
                                settings["autoLeave"] = False
                                sendMessageFooter(to, "Berhasil menonaktifkan auto leave")
                            elif cmd == "autorespon on":
                                settings["autoRespon"] = True
                                sendMessageFooter(to, "Berhasil mengaktifkan auto respon Pm")
                            elif cmd == "autorespon off":
                                settings["autoRespon"] = False
                                sendMessageFooter(to, "Berhasil menonaktifkan auto respon Pm")
                            elif cmd == "autoread on":
                                settings["autoRead"] = True
                                sendMessageFooter(to, "Berhasil mengaktifkan auto read")
                            elif cmd == "autoread off":
                                settings["autoRead"] = False
                                sendMessageFooter(to, "Berhasil menonaktifkan auto read")
                            elif cmd == "autojointicket on":
                                settings["autoJoinTicket"] = True
                                sendMessageFooter(to, "Berhasil mengaktifkan auto join by ticket")
                            elif cmd == "autojointicket off":
                                settings["autoJoinTicket"] = False
                                sendMessageFooter(to, "Berhasil menonaktifkan auto join by ticket")
                            elif cmd == "autoadd on":
                                settings["autoAdd"] = True
                                sendMessageFooter(to, "Berhasil mengaktifkan auto add")
                            elif cmd == "checkcontact on":
                                settings["checkContact"] = True
                                sendMessageFooter(to, "Berhasil mengaktifkan check details contact")
                            elif cmd == "checkcontact off":
                                settings["checkContact"] = False
                                sendMessageFooter(to, "Berhasil menonaktifkan check details contact")
                            elif cmd == "checkpost on":
                                settings["checkPost"] = True
                                sendMessageFooter(to, "Berhasil mengaktifkan check details post")
                            elif cmd == "checkpost off":
                                settings["checkPost"] = False
                                sendMessageFooter(to, "Berhasil menonaktifkan check details post")
                            elif cmd == "checksticker on":
                                settings["checkSticker"] = True
                                sendMessageFooter(to, "Berhasil mengaktifkan check details sticker")
                            elif cmd == "checksticker off":
                                settings["checkSticker"] = False
                                sendMessageFooter(to, "Berhasil menonaktifkan check details sticker")
                            elif cmd == "unsendchat on":
                                settings["unsendMessage"] = True
                                sendMessageFooter(to, "Berhasil mengaktifkan unsend message")
                            elif cmd == "unsendchat off":
                                settings["unsendMessage"] = False
                                sendMessageFooter(to, "Berhasil menonaktifkan unsend message")
                            elif cmd == "status":
                                try:
                                    ret_ = "???[ Status ]"
                                    if settings["autoAdd"] == True: ret_ += "\n? [ ON ] Auto Add"
                                    else: ret_ += "\n? [ OFF ] Auto Add"
                                    if settings["autoJoin"] == True: ret_ += "\n? [ ON ] Auto Join"
                                    else: ret_ += "\n? [ OFF ] Auto Join"
                                    if settings["autoLeave"] == True: ret_ += "\n? [ ON ] Auto Leave Room"
                                    else: ret_ += "\n? [ OFF ] Auto Leave Room"
                                    if settings["autoJoinTicket"] == True: ret_ += "\n? [ ON ] Auto Join Ticket"
                                    else: ret_ += "\n? [ OFF ] Auto Join Ticket"
                                    if settings["autoJoinTicketSquare"] == True: ret_ += "\n? [ ON ] Auto Join Ticket Square"
                                    else: ret_ += "\n? [ OFF ] Auto Join Ticket Square"
                                    if settings["autoRead"] == True: ret_ += "\n? [ ON ] Auto Read"
                                    else: ret_ += "\n? [ OFF ] Auto Read"
                                    if settings["autoRespon"] == True: ret_ += "\n? [ ON ] Detect Mention"
                                    else: ret_ += "\n? [ OFF ] Detect Mention"
                                    if settings["checkContact"] == True: ret_ += "\n? [ ON ] Check Contact"
                                    else: ret_ += "\n? [ OFF ] Check Contact"
                                    if settings["checkPost"] == True: ret_ += "\n? [ ON ] Check Post"
                                    else: ret_ += "\n? [ OFF ] Check Post"
                                    if settings["checkSticker"] == True: ret_ += "\n? [ ON ] Check Sticker"
                                    else: ret_ += "\n? [ OFF ] Check Sticker"
                                    if settings["setKey"] == True: ret_ += "\n? [ ON ] Set Key"
                                    else: ret_ += "\n? [ OFF ] Set Key"
                                    if settings["unsendMessage"] == True: ret_ += "\n? [ ON ] Unsend Message"
                                    else: ret_ += "\n? [ OFF ] Unsend Message"
                                    if settings["welcomemsg"] == True: ret_ += "\n? [ ON ] welcome Message"
                                    else: ret_ += "\n? [ OFF ] welcome Message"
                                    if settings["Leavemsg"] == True: ret_ += "\n? [ ON ] leave Message"
                                    else: ret_ += "\n? [ OFF ] leave Message"
                                    ret_ += "\n???[ Status ]"
                                    sendMessageFooter(to, str(ret_))
                                    client.sendContact(to, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                                except Exception as e:
                                    client.sendMessage(msg.to, str(e))
# Pembatas Script #
                            elif cmd == "crash":
                                client.sendContact(to, "u63bf99a61cca9f6dcc8d851c2c57a67b',")
                            elif cmd.startswith("changename:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = client.getProfile()
                                    profile.displayName = string
                                    client.updateProfile(profile)
                                    sendMessageFooter(to,"Berhasil mengganti display name menjadi{}".format(str(string)))
                            elif cmd.startswith("changebio:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = client.getProfile()
                                    profile.statusMessage = string
                                    client.updateProfile(profile)
                                    sendMessageFooter(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                            elif cmd == "me":
                                sendMentionFooter(to, "@!", [sender])
                                if msg.contentType == 19:
                                    client.sendContact(to, sender)
                            elif cmd == "mymid":
                                sendMessageFooter(to, "[ MID ]\n{}".format(sender))
                            elif cmd == "myname":
                                contact = client.getContact(sender)
                                sendMessageFooter(to, "[ Display Name ]\n{}".format(contact.displayName))
                            elif cmd == "mybio":
                                contact = client.getContact(sender)
                                sendMessageFooter(to, "[ Status Message ]\n{}".format(contact.statusMessage))
                            elif cmd == "mypicture":
                                contact = client.getContact(sender)
                                client.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "myvideoprofile":
                                contact = client.getContact(sender)
                                client.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "myticket":
                                  client.reissueUserTicket()
                                  arr = client.profile.displayName + " Ticket URL : http://line.me/ti/p/" + client.getUserTicket().id
                                  sendMessageFooter(to,arr)
                            elif cmd == "sticker":
                                try:
                                    query = msg.text.replace("sticker", "")
                                    query = int(query)
                                    if type(query) == int:
                                        client.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        client.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        client.sendText(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    client.sendText(receiver, str(e))     
                            elif cmd.startswith("cloneprofile "):
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
                                        sendMessageFooter(to, "Berhasil mengclone profile {}".format(contact.displayName))
                            elif cmd == "restoreprofile":
                                try:
                                    clientProfile = client.getProfile()
                                    clientProfile.displayName = str(settings["myProfile"]["displayName"])
                                    clientProfile.statusMessage = str(settings["myProfile"]["statusMessage"])
                                    clientProfile.pictureStatus = str(settings["myProfile"]["pictureStatus"])
                                    client.updateProfileAttribute(8, clientProfile.pictureStatus)
                                    client.updateProfile(clientProfile)
                                    coverId = str(settings["myProfile"]["coverId"])
                                    client.updateProfileCoverById(coverId)
                                    sendMessageFooter(to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                                except Exception as e:
                                    sendMessageFooter(to, "Gagal restore profile")
                                    logError(error)
                            elif cmd == "backupprofile":
                                try:
                                    profile = client.getProfile()
                                    settings["myProfile"]["displayName"] = str(profile.displayName)
                                    settings["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                    settings["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
                                    coverId = client.getProfileDetail()["result"]["objectId"]
                                    settings["myProfile"]["coverId"] = str(coverId)
                                    sendMessageFooter(to, "Berhasil backup profile")
                                except Exception as e:
                                    sendMessageFooter(to, "Gagal backup profile")
                                    logError(error)
                            elif cmd.startswith("autorespon: "):
                                text_ = removeCmd("autorespon:", text)
                                try:
                                    settings["replyPesan"] = text_
                                    client.sendMessage(to,"?AutoReply?Changed to : " + text_)
                                except:
                                    client.sendMessage(to,"?AutoReply?\nFailed to replace message")
                            elif cmd == "autorespon":
                                if settings["replyPesan"] is not None:
                                    client.sendMessage(to,"My Set AutoRespon : " + str(settings["replyPesan"])) 
                                else:
                                    client.sendMessage(to,"My Set AutoRespon : No messages are set")
                            elif cmd.startswith("stealmid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
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
                                    sendMessageFooter(to, str(ret_))
                            elif cmd.startswith("stealname "):
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
                                        sendMessageFooter(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                            elif cmd.startswith("stealbio "):
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
                                        sendMessageFooter(to, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                            elif cmd.startswith("stealpicture"):
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
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        client.sendImageWithURL(to, str(path))
                            elif cmd.startswith("stealvideoprofile "):
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
                                        path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        client.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("stealcover "):
                                if client != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
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
#================================================
                            elif 'kick' in text.lower():
                                   targets = []
                                   key = eval(msg.contentMetadata["MENTION"])
                                   key["MENTIONEES"] [0] ["M"]
                                   for x in key["MENTIONEES"]:
                                       targets.append(x["M"])
                                   for target in targets:
                                       try:
                                           client.kickoutFromGroup(msg.to,[target])                           
                                       except:
                                           sendMessageFooter(msg.to,"Error")
                            #if msg.text == "cancel":
                               #group = client.getGroup(msg.to)
                               #if group.invitee is None:
                                   #client.sendMessage(op.message.to, "Tidak ada orang yang diundang.")
                               #else:
                                   #gInviMids = [contact.mid for contact in group.invitee]
                                   #client.cancelGroupInvitation(msg.to, gInviMids)
                                   #sendMessageFooter(msg.to, str(len(group.invitee)) + " undangan dibatalkan.")
#================================================
                            elif text.lower() == 'announce':
                                gett = client.getChatRoomAnnouncements(receiver)
                                for a in gett:
                                    aa = client.getContact(a.creatorMid).displayName
                                    bb = a.contents
                                    cc = bb.link
                                    textt = bb.text
                                    sendMessageFooter(receiver, 'Link: ' + str(cc) + '\nText: ' + str(textt) + '\nMaker: ' + str(aa))
                            elif text.lower() == "kam":
                                sendMessageFooter(to, "Pret")
                            elif text.lower() == "@yudhabye":
                                client.leaveGroup(msg.to)
                            elif text.lower() == 'Gift':
                                client.sendGift(receiver, 'b828f799-14b1-4170-a60c-6d33a765cc9e', 'theme')
                            elif "Gift @" in msg.text:
                                _name = msg.text.replace("Gift @","")
                                _nametarget = _name.rstrip(' ')
                                gs = client.getGroup(msg.to)
                                for g in gs.members:
                                    if _nametarget == g.displayName:
                                        rangkum = ("[ "+g.displayName+" ]:"+g.mid) #Mid akan keluar pada Terminal
                                        client.log(rangkum) #Mencetak Mid
                                        client.sendGift(g.mid, 'b828f799-14b1-4170-a60c-6d33a765cc9e', 'theme')
                                        client.log(" [ Status ] : Done") #Mengirim Pesan
                                    else:
                                       pass #Melewatkan
                            elif text.lower() == 'animelist':
                                data = {
                                    'submit2': ''
                                    }
                                r = requests.post(url = 'https://boteater.com/anime/', data = data)
                                qr= r.text
                                os.system('rm {}.txt'.format(msg._from))
                                urllib.request.urlretrieve('http://149.28.137.54/animelist.json', '{}.txt'.format(msg._from))
                                links = []
                                juduls = []
                                if r.status_code == 404:
                                    sendMessageFooter(msg.to, 'FAIL!!!')
                                else:
                                    j = json.loads(qr)
                                    for p in j['result']:
                                        juduls.append(p['judul'])
                                        links.append(p['link'])
                                    h= ('>>ANIME LIST<<')
                                    number= 1
                                    try:
                                        for numx in range(1000):
                                            xx =juduls[numx]
                                            h+= ('\n{}. {}'.format(numx, xx))
                                            number += 1
                                    except:
                                        sendMessageFooter(msg.to, h)
                                        sendMessageFooter(msg.to, 'PLEASE TYPE = EPPLIST [NUMBER]')
                            if text.lower() == 'animenew':
                                data = {
                                    'submit1': ''
                                    }
                                r = requests.post(url = 'https://boteater.com/anime/', data = data)
                                qr= r.text
                                os.system('rm {}.txt'.format(msg._from))
                                urllib.request.urlretrieve('http://149.28.137.54/animebaru.json', '{}.txt'.format(msg._from))
                                links = []
                                juduls = []
                                if r.status_code == 404:
                                   sendMessageFooter(msg.to, 'FAIL!!!')
                                else:
                                    j = json.loads(qr)
                                    for p in j['result']:
                                        juduls.append(p['judul'])
                                        links.append(p['link'])
                                    h= ('>>ANIME LIST<<')
                                    number= 1
                                    try:
                                       for numx in range(1000):
                                           xx =juduls[numx]
                                           h+= ('\n{}. {}'.format(numx, xx))
                                           number += 1
                                    except:
                                        sendMessageFooter(msg.to, h)
                                        sendMessageFooter(msg.to, 'PLEASE TYPE = STREAMEPPZ [NUMBER]')
                            elif "epplist " in msg.text.lower():
                                separate = msg.text.split(" ")
                                numf = msg.text.replace(separate[0] + " ","")
                                numzz = int(numf)
                                numz = numzz
                                with open('{}.txt'.format(msg._from), 'r') as f:
                                    qr = f.read()
                                    j = json.loads(qr)
                                    juduls = []
                                    links = []
                                    for p in j['result']:
                                        juduls.append(p['judul'])
                                        links.append(p['link'])
                                    xx =links[numz]
                                    xxx =juduls[numz]
                                    data = {
                                        'link2': '{}'.format(xx),
                                        'submit4': ''
                                        }
                                    r = requests.post(url = 'https://boteater.com/anime/', data = data)
                                    qr= r.text
                                    f = open('{}.txt'.format(msg._from),'w')
                                    f.write(qr)
                                    f.close()
                                    links = []
                                    juduls = []
                                    if r.status_code == 404:
                                        sendMessageFooter(msg.to, 'FAIL!!! SELECT YOUR ANIME FIRST!!!')
                                    else:
                                        j = json.loads(qr)
                                        for p in j['result']:
                                            juduls.append(p['epp'])
                                            links.append(p['link'])
                                        h= ('>>EPISODE LIST LIST<< \n>>{}<<'.format(xxx))
                                        number= 1
                                        try:
                                           for numx in range(1000):
                                                zzz =juduls[numx]
                                                h+= ('\n{}. {}'.format(numx, zzz))
                                                number += 1
                                        except:
                                           sendMessageFooter(msg.to, h)
                                           sendMessageFooter(msg.to, 'PLEASE TYPE = STREAMEPP [NUMBER]')
                                           if juduls in ["", "\n", " ",  None]:
                                               client.sendMessage(msg.to, 'LINK ANIME IS DIED!!')
                            elif "streamepp " in msg.text.lower():
                                separate = msg.text.split(" ")
                                numf = msg.text.replace(separate[0] + " ","")
                                numzz = int(numf)
                                numz = numzz
                                with open('{}.txt'.format(msg._from), 'r') as f:
                                    qr = f.read()
                                    j = json.loads(qr)
                                    juduls = []
                                    links = []
                                    for p in j['result']:
                                        juduls.append(p['epp'])
                                        links.append(p['link'])
                                    xx =links[numz]
                                    xxx =juduls[numz]
                                    data = {
                                        'link1': '{}'.format(xx),
                                        'submit3': ''
                                        }
                                    r = requests.post(url = 'https://boteater.com/anime/', data = data)
                                    link= r.text
                                    sendMessageFooter(msg.to, ">> STREAM ANIME<< \n>> {} << \n{}".format(xxx, link))
                            elif "streameppz " in msg.text.lower():
                                separate = msg.text.split(" ")
                                numf = msg.text.replace(separate[0] + " ","")
                                numzz = int(numf)
                                numz = numzz
                                with open('{}.txt'.format(msg._from), 'r') as f:
                                    qr = f.read()
                                    j = json.loads(qr)
                                    juduls = []
                                    links = []
                                    for p in j['result']:
                                        juduls.append(p['judul'])
                                        links.append(p['link'])
                                    xx =links[numz]
                                    xxx =juduls[numz]
                                    data = {
                                        'link1': '{}'.format(xx),
                                        'submit3': ''
                                        }
                                    r = requests.post(url = 'https://boteater.com/anime/', data = data)
                                    link= r.text
                                    sendMessageFooter(msg.to, ">> STREAM ANIME<< \n>> {} << \n{}".format(xxx, link))
                            elif 'Rw ' in text:
                                try:
                                    txt = text.replace('rw ','').split('|')
                                    btype,ttype = random.choice([1,2,3,4,5]),random.choice([1,2,3,4])
                                    path = 'http://corrykalam.gq/retrowave.php?'
                                    if len(txt) == 1:
                                        params = {'text1': txt[0],'text2': '','text3': '','btype': str(btype),'ttype': str(ttype)}
                                    elif len(txt) == 2:
                                        params = {'text1': txt[0],'text2': txt[1],'text3': '','btype': str(btype),'ttype': str(ttype)}
                                    elif len(txt) == 3:
                                        params = {'text1': txt[0],'text2': txt[1],'text3': txt[2],'btype': str(btype),'ttype': str(ttype)}
                                    data = requests.get(path, params=params).json()
                                    client.sendImageWithURL(receiver, data['image'])
                                except Exception as e:
                                    client.sendMessage(receiver, str(e))
                            elif text.lower() == 'unsend me':
                                client.unsendMessage(msg_id)
                            elif text.lower() == 'getsq':
                                a = client.getJoinedSquares()
                                squares = a.squares
                                members = a.members
                                authorities = a.authorities
                                statuses = a.statuses
                                noteStatuses = a.noteStatuses
                                txt = str(squares)+'\n\n'+str(members)+'\n\n'+str(authorities)+'\n\n'+str(statuses)+'\n\n'+str(noteStatuses)+'\n\n'
                                txt2 = ''
                                for i in range(len(squares)):
                                    txt2 += str(i+1)+'. '+str(squares[i].invitationURL)+'\n'
                                client.sendText(receiver, txt2)
                            elif 'lc ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).mid
                                    s = client.getContact(u).displayName
                                    hasil = channel.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        channel.like(str(sender), str(result), likeType=random.choice(typel))
                                        channel.comment(str(sender), str(result), 'Auto Like by Yudha\n http://line.me/ti/p/~yud.xz')
                                    client.sendText(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif cmd.startswith ("meme-buzz "):
                                txt = msg.text.split(" ")       
                                image = "https://memegen.link/buzz/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+".jpg"
                                client.sendImageWithURL(msg.to, image)                     
                            elif cmd.startswith ('invitegroupcall '):
                               if msg.toType == 2:
                                sep = text.split(" ")
                                strnum = text.replace(sep[0] + " ","")
                                num = int(strnum)
                                sendMessageFooter(to, "Berhasil mengundang kedalam telponan group")
                                for var in range(0,num):
                                    group = client.getGroup(to)
                                    members = [mem.mid for mem in group.members]
                                    client.acquireGroupCallRoute(to)
                                    client.inviteIntoGroupCall(to, contactIds=members)
                            elif 'leaveto ' in text.lower():
                                gids = msg.text.replace('leaveto ',"")
                                gid = client.getGroup(gids)
                                try:
                                   client.leaveGroup(gids)
                                except:
                                   sendMessageFooter(to,"Succes leave to group " + gids.name)
                            elif cmd == "delannounce":
                                a = client.getChatRoomAnnouncements(to)
                                anu = []
                                for b in a:
                                    c = b.announcementSeq
                                    anu.append(c)
                                    client.removeChatRoomAnnouncement(to, c)
                                    sendMessageFooter(to, "Success deleted Announce") 
                            
#===========================[ TOKEN EATER ]=====================================#
                            if text.lower() == 'token desktopmac':
                               req = requests.get(url = 'https://api.eater.pw/DESKTOPMAC')
                               a = req.text
                               b = json.loads(a)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               tkn['{}'.format(msg._from)] = []
                               tkn['{}'.format(msg._from)].append({
                                   'qr': b['result'][0]['linkqr'],
                                   'tkn': b['result'][0]['linktkn']
                                   })
                               qrz = b['result'][0]['linkqr']
                               sendMessageFooter(to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                               with open('tkn.json', 'w') as outfile:
                                   json.dump(tkn, outfile)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               a = tkn['{}'.format(msg._from)][0]['tkn']
                               req = requests.get(url = '{}'.format(a))
                               b = req.text
                               sendMentionFooter(to, '- TIPE TOKEN : DESKTOPMAC\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            if text.lower() == 'token desktopwin':
                               req = requests.get(url = 'https://api.eater.pw/DESKTOPWIN')
                               a = req.text
                               b = json.loads(a)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               tkn['{}'.format(msg._from)] = []
                               tkn['{}'.format(msg._from)].append({
                                   'qr': b['result'][0]['linkqr'],
                                   'tkn': b['result'][0]['linktkn']
                                   })
                               qrz = b['result'][0]['linkqr']
                               sendMessageFooter(to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                               with open('tkn.json', 'w') as outfile:
                                   json.dump(tkn, outfile)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               a = tkn['{}'.format(msg._from)][0]['tkn']
                               req = requests.get(url = '{}'.format(a))
                               b = req.text
                               sendMentionFooter(to, '- TIPE TOKEN : DESKTOPWIN\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            if text.lower() == 'token chromeos':
                               req = requests.get(url = 'https://api.eater.pw/CHROMEOS')
                               a = req.text
                               b = json.loads(a)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               tkn['{}'.format(msg._from)] = []
                               tkn['{}'.format(msg._from)].append({
                                   'qr': b['result'][0]['linkqr'],
                                   'tkn': b['result'][0]['linktkn']
                                   })
                               qrz = b['result'][0]['linkqr']
                               sendMessageFooter(to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                               with open('tkn.json', 'w') as outfile:
                                   json.dump(tkn, outfile)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               a = tkn['{}'.format(msg._from)][0]['tkn']
                               req = requests.get(url = '{}'.format(a))
                               b = req.text
                               sendMentionFooter(to, '- TIPE TOKEN : CHROMEOS\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            if text.lower() == 'token iosipad':
                               req = requests.get(url = 'https://api.eater.pw/IOSIPAD')
                               a = req.text
                               b = json.loads(a)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               tkn['{}'.format(msg._from)] = []
                               tkn['{}'.format(msg._from)].append({
                                   'qr': b['result'][0]['linkqr'],
                                   'tkn': b['result'][0]['linktkn']
                                   })
                               qrz = b['result'][0]['linkqr']
                               sendMessageFooter(to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                               with open('tkn.json', 'w') as outfile:
                                   json.dump(tkn, outfile)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               a = tkn['{}'.format(msg._from)][0]['tkn']
                               req = requests.get(url = '{}'.format(a))
                               b = req.text
                               sendMentionFooter(to, '- TIPE TOKEN : IOSIPAD\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            if text.lower() == 'token win10':
                               req = requests.get(url = 'https://api.eater.pw/WIN10')
                               a = req.text
                               b = json.loads(a)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               tkn['{}'.format(msg._from)] = []
                               tkn['{}'.format(msg._from)].append({
                                   'qr': b['result'][0]['linkqr'],
                                   'tkn': b['result'][0]['linktkn']
                                   })
                               qrz = b['result'][0]['linkqr']
                               sendMessageFooter(to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                               with open('tkn.json', 'w') as outfile:
                                   json.dump(tkn, outfile)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               a = tkn['{}'.format(msg._from)][0]['tkn']
                               req = requests.get(url = '{}'.format(a))
                               b = req.text
                               sendMentionFooter(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
#===========================[ TOKEN EATER }=====================================#
                            if text.lower() == 'token2 win10':
                               req = requests.get(url = 'https://api.eater.tech/WIN10')
                               a = req.text
                               b = json.loads(a)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               tkn['{}'.format(msg._from)] = []
                               tkn['{}'.format(msg._from)].append({
                                   'qr': b['result'][0]['linkqr'],
                                   'tkn': b['result'][0]['linktkn']
                                   })
                               qrz = b['result'][0]['linkqr']
                               sendMessageFooter(to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                               with open('tkn.json', 'w') as outfile:
                                   json.dump(tkn, outfile)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               a = tkn['{}'.format(msg._from)][0]['tkn']
                               req = requests.get(url = '{}'.format(a))
                               b = req.text
                               sendMentionFooter(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                                
                            if text.lower() == 'token2 desktopwin':
                               req = requests.get(url = 'https://api.eater.tech/DESKTOPWIN')
                               a = req.text
                               b = json.loads(a)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               tkn['{}'.format(msg._from)] = []
                               tkn['{}'.format(msg._from)].append({
                                   'qr': b['result'][0]['linkqr'],
                                   'tkn': b['result'][0]['linktkn']
                                   })
                               qrz = b['result'][0]['linkqr']
                               sendMessageFooter(to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                               with open('tkn.json', 'w') as outfile:
                                   json.dump(tkn, outfile)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               a = tkn['{}'.format(msg._from)][0]['tkn']
                               req = requests.get(url = '{}'.format(a))
                               b = req.text
                               sendMentionFooter(to, '- TIPE TOKEN : DESKTOPWIN\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                            
                            if text.lower() == 'token2 desktopmac':
                               req = requests.get(url = 'https://api.eater.tech/DESKTOPMAC')
                               a = req.text
                               b = json.loads(a)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               tkn['{}'.format(msg._from)] = []
                               tkn['{}'.format(msg._from)].append({
                                   'qr': b['result'][0]['linkqr'],
                                   'tkn': b['result'][0]['linktkn']
                                   })
                               qrz = b['result'][0]['linkqr']
                               sendMessageFooter(to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                               with open('tkn.json', 'w') as outfile:
                                   json.dump(tkn, outfile)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               a = tkn['{}'.format(msg._from)][0]['tkn']
                               req = requests.get(url = '{}'.format(a))
                               b = req.text
                               sendMentionFooter(to, '- TIPE TOKEN : DESKTOPMAC\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                               
                            if text.lower() == 'token2 iosipad':
                               req = requests.get(url = 'https://api.eater.tech/IOSIPAD')
                               a = req.text
                               b = json.loads(a)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               tkn['{}'.format(msg._from)] = []
                               tkn['{}'.format(msg._from)].append({
                                   'qr': b['result'][0]['linkqr'],
                                   'tkn': b['result'][0]['linktkn']
                                   })
                               qrz = b['result'][0]['linkqr']
                               sendMessageFooter(to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                               with open('tkn.json', 'w') as outfile:
                                   json.dump(tkn, outfile)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               a = tkn['{}'.format(msg._from)][0]['tkn']
                               req = requests.get(url = '{}'.format(a))
                               b = req.text
                               sendMentionFooter(to, '- TIPE TOKEN : IOSIPAD\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                               
                            if text.lower() == 'token2 chromeos':
                               req = requests.get(url = 'https://api.eater.tech/CHROMEOS')
                               a = req.text
                               b = json.loads(a)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               tkn['{}'.format(msg._from)] = []
                               tkn['{}'.format(msg._from)].append({
                                   'qr': b['result'][0]['linkqr'],
                                   'tkn': b['result'][0]['linktkn']
                                   })
                               qrz = b['result'][0]['linkqr']
                               sendMessageFooter(to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                               with open('tkn.json', 'w') as outfile:
                                   json.dump(tkn, outfile)
                               tknop= codecs.open("tkn.json","r","utf-8")
                               tkn = json.load(tknop)
                               a = tkn['{}'.format(msg._from)][0]['tkn']
                               req = requests.get(url = '{}'.format(a))
                               b = req.text
                               sendMentionFooter(to, '- TIPE TOKEN : CHROMEOS\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
#==========================================
                            elif text.lower() == 'groupcancel':
                                gid = client.getGroupIdsInvited()
                                start = time.time()
                                for i in gid:
                                    client.rejectGroupInvitation(i)
                                elapsed_time = time.time() - start
                                sendMessageFooter(to, "Semua Undangan di batalkan ")
                                sendMessageFooter(to, "Pembatalan: %s Seconds" % (elapsed_time))
                            elif cmd == 'groupcreator':
                                group = client.getGroup(to)
                                GS = group.creator.mid
                                client.sendContact(to, GS)
                            elif cmd == 'groupid':
                                gid = client.getGroup(to)
                                sendMessageFooter(to, "[ID Group : ]\n" + gid.id)
                            elif cmd == 'grouppicture':
                                group = client.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                client.sendImageWithURL(to, path)
                            elif "Changegroupname " in msg.text:
                                if msg.toType == 2:
                                    X = client.getGroup(msg.to)
                                    X.name = msg.text.replace("Changegroupname ","")
                                    client.updateGroup(X)
                                else:
                                   sendMessageFooter(msg.to,"Hanya di group")
                            elif cmd == 'groupname':
                                gid = client.getGroup(to)
                                sendMessageFooter(to, "[Nama Group : ]\n" + gid.name)
                            elif cmd == 'groupticket':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    gid = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = client.reissueGroupTicket(to)
                                        sendMessageFooter(to, "[ " + gid.name + " ]\nline://ti/g/{}".format(str(ticket)))
                                    else:
                                        sendMessageFooter(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                            elif cmd == 'groupticket on':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        sendMessageFooter(to, "Grup qr sudah terbuka")
                                    else:
                                        group.preventedJoinByTicket = False
                                        client.updateGroup(group)
                                        sendMessageFooter(to, "Berhasil membuka grup qr")
                            elif cmd == 'groupticket off':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == True:
                                        sendMessageFooter(to, "Grup qr sudah tertutup")
                                    else:
                                        group.preventedJoinByTicket = True
                                        client.updateGroup(group)
                                        sendMessageFooter(to, "Berhasil menutup grup qr")
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
                                sendMessageFooter(to, str(ret_))
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
                                    sendMessageFooter(to, str(ret_))
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
                                    sendMessageFooter(to, str(ret_))
# Pembatas Script #
                            elif cmd == "checkmention":
                                  if to in settings["userMentioned"]:
                                       if settings["userMentioned"][to] != {}:
                                             #userMentioned(to)
                                       #else:
                                             #client.sendMessage(to, "Tidak ada yang ngetag")
                                        userMentioned(to)
                                  else:
                                        client.sendMessage(to, "Tidak ada yang ngetag.")
                            elif cmd == "changepictureprofile":
                                settings["changePictureProfile"] = True
                                sendMessageFooter(to, "Silahkan kirim gambarnya")
                            elif cmd == "changeprofilecover":
                                settings["changeCover"] = True
                                client.sendMessage(to, "Silahkan kirim gambarnya")
                            elif cmd == "Changeprofilevideo":
                                settings['changeProfileVideo']['status'] = True
                                settings['changeProfileVideo']['stage'] = 1
                                client.sendMessage(to, "[ Update Profile Video ]\n•", "\nSend video !")
                            elif cmd == "changegrouppicture":
                                if msg.toType == 2:
                                    if to not in settings["changeGroupPicture"]:
                                        settings["changeGroupPicture"].append(to)
                                    sendMessageFooter(to, "Silahkan kirim gambarnya")
                            elif cmd == "changevideoprofile":
                            	if msg.contentType == 0:
                                    settings["ChangeVideoProfilevid"] = True
                                    sendMentionFooter(to, "[ Notified ChangeDual ]\nChangeDual Started!\n\nSend 1 Video what u want\n@!", [sender])
                                    if msg.contentType == 2:
                                        path = client.downloadObjectMsg(msg_id,saveAs="tmp/vid.bin")
                                        settings["ChangeVideoProfilevid"] = False
                                        settings["ChangeVideoProfilePicture"] = True
                                        sendMentionFooter(to, "[ Notified ChangeDual ]\nChangeDual Started!\n\nSend 1 Picture what u want\n@!", [sender])
                                        if msg.contentType == 1:
                                            path = client.downloadObjectMsg(msg_id)
                                            settings["ChangeVideoProfilePicture"] = False
                                            client.updateProfileVideoPicture(path)
                                            sendMentionFooter(to, "[ Notified ChangeDual ]\nSuccessed Changedual\n @!", [sender])

                            elif cmd == 'changedual':
                            	pict = client.downloadFileURL("https://drive.google.com/uc?export=download&id=1wOgcSlzIZNWRaKl_j0eRPExcxhXhB-CM", saveAs="image.jpg")
                            	vids = client.downloadFileURL("https://drive.google.com/uc?export=download&id=1JA4fD4X1sy3SCFsMVjEtCShN1Mo7oGnc", saveAs="video.mp4")
                            	ChangeVideoProfile(pict, vids)
                            	sendMessageFooter(to, "Berhasil mengubah picture dan video profile")
                            elif cmd == 'mention':
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
                                    client.sendMessage(to, "Total {} Mention".format(str(len(nama)))) 
                            elif cmd == "sider on":
                            	try:
                            		del cctv['point'][msg.to]
                            		del cctv['sidermem'][msg.to]
                            		del cctv['cyduk'][msg.to]
                            	except:
                            		pass
                            	cctv['point'][msg.to] = msg.id
                            	cctv['sidermem'][msg.to] = ""
                            	cctv['cyduk'][msg.to]=True
                            	settings["Sider"] = True
                            	sendMessageFooter(msg.to,"Cek sider diaktifkan")
                            elif cmd == "sider off":
                            	if msg.to in cctv['point']:
                            		cctv['cyduk'][msg.to]=False
                            		settings["Sider"] = False
                            		sendMessageFooter(msg.to,"Cek sider dinonaktifkan")
                            	else:
                            		sendMessageFooter(msg.to,"sÉªá´…á´‡Ê€ É´á´á´› sá´‡á´›")
                            elif cmd == "lurking on":
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
                                    sendMessageFooter(receiver,"Lurking telah diaktifkan")
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
                                    sendMessageFooter(receiver,"Set reading point : \n" + readTime)
                            elif cmd == "lurking off":
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
                                if receiver not in read['readPoint']:
                                    sendMessageFooter(receiver,"Lurking telah dinonaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    sendMessageFooter(receiver,"Delete reading point : \n" + readTime)
        
                            elif cmd == "lurking reset":
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
                                    sendMessageFooter(msg.to, "Reset reading point : \n" + readTime)
                                else:
                                    sendMessageFooter(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                                    
                            elif cmd == "lurking":
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
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        sendMessageFooter(receiver,"Tidak Ada Sider")
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
                                    sendMessageFooter(receiver,"Lurking belum diaktifkan")
                            elif cmd.startswith("mimicadd"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        settings["mimic"]["target"][target] = True
                                        sendMessageFooter(msg.to,"Target ditambahkan!")
                                        break
                                    except:
                                        sendMessageFooter(msg.to,"Gagal menambahkan target")
                                        break
                            elif cmd.startswith("mimicdel"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        del settings["mimic"]["target"][target]
                                        sendMessageFooter(msg.to,"Target dihapuskan!")
                                        break
                                    except:
                                        sendMessageFooter(msg.to,"Gagal menghapus target")
                                        break
                                    
                            elif cmd == "mimiclist":
                                if settings["mimic"]["target"] == {}:
                                    sendMessageFooter(msg.to,"Tidak Ada Target")
                                else:
                                    mc = "â•­â”€â”€[ Mimic List ]"
                                    for mi_d in settings["mimic"]["target"]:
                                        mc += "\nâ”‚ "+client.getContact(mi_d).displayName
                                    mc += "\nâ•°â”€â”€[ Finish ]"
                                    sendMessageFooter(msg.to,mc)
                                
                            elif cmd.startswith("mimic"):
                                sep = text.split(" ")
                                mic = text.replace(sep[0] + " ","")
                                if mic == "on":
                                    if settings["mimic"]["status"] == False:
                                        settings["mimic"]["status"] = True
                                        sendMessageFooter(msg.to,"Reply Message on")
                                elif mic == "off":
                                    if settings["mimic"]["status"] == True:
                                        settings["mimic"]["status"] = False
                                        sendMessageFooter(msg.to,"Reply Message off")

                            elif text.lower().startswith("pcid"):
                            	dan = text.split("|")
                            	x = client.findContactsByUserid(dan[1])
                            	a = client.getContact(sender)
                            	sendMessageFooter(x.mid,"Anda mendapatkan pesan dari "+a.displayName+"\n\n"+dan[2])
                            	sendMessageFooter(to,"Sukses mengirim pesan ke "+x.displayName+"\nDari: "+a.displayName+"\nPesan: "+dan[2])

                            elif text.lower() == 'invgroupcall':    
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    members = [mem.mid for mem in group.members]
                                    call.acquireGroupCallRoute(to)
                                    call.inviteIntoGroupCall(to, contactIds=members)
                                    sendMessageFooter(to, "Berhasil mengundang kedalam telponan group")
                    
                            elif text.lower() == 'removechat':
                                client.removeAllMessages(op.param2)
                                sendMessageFooter(to, "Berhasil hapus semua chat")

                            elif msg.text.lower().startswith("gbroadcast "):   
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                groups = client.groups
                                for group in groups:
                                    sendMessageFooter(group, "[ Broadcast ]\n{}".format(str(txt)))
                                    #client.sendContact(group, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                                    sendMessageFooter(to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                    
                            elif cmd.startswith("fbroadcast "):
                                txt = removeCmd("fbroadcast", text)
                                friends = client.getAllContactIds()
                                for friend in friends:
                                    sendMessageFooter(friend, "[ Broadcast ]\n{}".format(str(txt)))
                                    time.sleep(1)
                                sendMessageFooter(to, "Berhasil broadcast ke {} teman".format(str(len(friends))))

                            elif msg.text.lower().startswith("allbroadcast "):   
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                friends = client.getAllContactIds
                                groups = client.groups
                                for group in groups:
                                    sendMessageFooter(group, "[ Broadcast ]\n{}".format(str(txt)))
                                    #client.sendContact(group, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                                    sendMessageFooter(to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                                for friend in friends:
                                    sendMessageFooter(friend, "[ Broadcast ]\n{}".format(str(txt)))
                                    #sclient.sendContact(friend, "u63bf99a61cca9f6dcc8d851c2c57a67b")
                                    sendMessageFooter(to, "Berhasil broadcast ke {} teman".format(str(len(friends))))
                            
                            elif text.lower().startswith("Gitlabprofile "):
                            	dan = "[ GitLab Profile ]\n\n"
                            	user = text.replace("gitlabprofile ","")
                            	data = requests.get("http://moeapi.panel.moe/api/gitlab/profile/?apikey=beta&username="+user).json()
                            	if "message" not in data:
                            		dan+="Name: "+str(data["result"]["name"])
                	            	dan+="\nUsername: "+str(data["result"]["username"])
                	            	dan+="\nBio: "+str(data["result"]["bio"])
                	            	dan+="\nSince: "+str(data["result"]["since"])
                            		dan+="\n\n[ Finish ]"
                	            	sendMessageFooter(to, str(yud))
                            elif cmd.startswith("murottal"):
                                try:
                                   sep = msg.text.split(" ")
                                   surah = int(text.replace(sep[0] + " ",""))
                                   if 0 < surah < 115:
                                       if surah not in [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 16, 17, 18, 20, 21, 23, 26, 37]:
                                           if len(str(surah)) == 1:
                                                audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-00" + str(surah) + "-muslimcentral.com.mp3"
                                                client.sendAudioWithURL(to, audionya)
                                           elif len(str(surah)) == 2:
                                               audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-0" + str(surah) + "-muslimcentral.com.mp3"
                                               client.sendAudioWithURL(to, audionya)
                                           else:
                                               audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-" + str(surah) + "-muslimcentral.com.mp3"
                                               client.sendAudioWithURL(to, audionya)
                                       else:
                                           sendMessageFooter(to, "Surah terlalu panjang")
                                   else:
                                       sendMessageFooter(to, "Qur'an hanya 114 surah")
                                except Exception as error:
                                    client.sendMessage(to, "error\n"+str(error))
                                    logError(error)
                            elif "clonegroup " in msg.text and msg.toType == 2:
                                gname = msg.text.replace("clonegroup ", "")
                                group = client.getGroup(msg.to)
                                members = [mem.mid for mem in group.members] + [pen.mid for pen in group.invitee] if group.invitee else [mem.mid for mem in group.members]
                                members.remove(client.profile.mid)
                                for mem in members:
                                    client.findAndAddContactsByMid(mem)
                                client.createGroup(gname, members)
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

                            elif '.Protectkick ' in msg.text:
                                   if msg._from in admin:
                                      spl = msg.text.replace('.Protectkick ','')
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
                            elif '.Protectinvite ' in msg.text:
                                   if msg._from in admin:
                                      spl = msg.text.replace('.Protectinvite ','')
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
                            elif cmd.startswith("protectqr|on "):
                                  if msg._from in admin:
                                    separate = msg.text.split(" ")
                                    number = msg.text.replace(separate[0] + " ","")
                                    groups = client.getGroupIdsJoined()
                                    ret_ = ""
                                    try:
                                        group = groups[int(number)-1]
                                        G = client.getGroup(group)
                                        try:
                                            protectqr[G] = True
                                            f=codecs.open('protectqr.json','w','utf-8')
                                            json.dump(protectqr, f, sort_keys=True, indent=4,ensure_ascii=False)
                                            gCreator = G.creator.mid
                                            dia = client.getContact(gCreator)
                                            zx = ""
                                            zxc = ""
                                            zx2 = []
                                            xpesan = '「 Protect Qr Diaktifkan 」\n• Creator :  '
                                            diaa = str(dia.displayName)
                                            pesan = ''
                                            pesan2 = pesan+"@a\n"
                                            xlen = str(len(zxc)+len(xpesan))
                                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                            zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                            zx2.append(zx)
                                            zxc += pesan2
                                        except:
                                            client.sendText(msg.to, "Grup itu tidak ada")
                                            gCreator = "Tidak ditemukan"
                                        if G.invitee is None:
                                            gPending = "0"
                                        else:
                                            gPending = str(len(G.invitee))
                                        timeCreated = []
                                        timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                        ret_ += xpesan+zxc
                                        ret_ += "• Nama grup : {}".format(G.name)
                                        ret_ += "\n• Pendingan : {}".format(gPending)
                                        ret_ += "\n• Jumlah Member : {}".format(str(len(G.members)))
                                        client.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as e:
                                        client.sendMessage(to, str(e))

                            elif '.Protecturl ' in msg.text:
                                   if msg._from in admin:
                                      spl = msg.text.replace('.Protecturl ','')
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
                                                 ginfo = client.getGroup(msg.to)
                                                 msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                            else:
                                                 msgs = "Protect url sudah tidak aktif"
                                            client.sendMessage(msg.to, "「 Status Protect Url 」\n" + msgs)

                            elif '.Protectjoin ' in msg.text:
                                if msg._from in admin:
                                   spl = msg.text.replace('.Protectjoin ','')
                                   if spl == 'on':
                                       if msg.to in protectjoin:
                                            msgs = "Protect join sudah aktif"
                                       else:
                                            protectjoin.append(msg.to)
                                            ginfo = client.getGroup(msg.to)
                                            msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                       client.sendMessage(msg.to, "? Status Protect Join ?\n" + msgs)
                                   elif spl == 'off':
                                         if msg.to in protectjoin:
                                              protectjoin.remove(msg.to)
                                              ginfo = client.getGroup(msg.to)
                                              msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         else:
                                              msgs = "Protect join sudah tidak aktif"
                                         client.sendMessage(msg.to, "? Status Protect Join ?\n" + msgs)

                            elif '.Protectcancel ' in msg.text:
                                if msg._from in admin:
                                   spl = msg.text.replace('.Protectcancel ','')
                                   if spl == 'on':
                                       if msg.to in protectcancel:
                                            msgs = "Protect cancel sudah aktif"
                                       else:
                                            protectcancel.append(msg.to)
                                            ginfo = client.getGroup(msg.to)
                                            msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                       client.sendMessage(msg.to, "? Status Protect Cancel ?\n" + msgs)
                                   elif spl == 'off':
                                         if msg.to in protectcancel:
                                              protectcancel.remove(msg.to)
                                              ginfo = client.getGroup(msg.to)
                                              msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         else:
                                              msgs = "Protect cancel sudah tidak aktif"
                                         client.sendMessage(msg.to, "? Status Protect Cancel ?\n" + msgs)

                            elif '.Protectall ' in msg.text:
                                   if msg._from in admin:
                                      spl = msg.text.replace('.Protectall ','')
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
                                              ginfo = client.getGroup(msg.to)
                                              msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                              msgs += "\nSemua sudah diaktifkan"
                                          else:
                                              protectcancel.append(msg.to)
                                              ginfo = client.getGroup(msg.to)
                                              msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                              msgs += "\nSemua protection diaktifkan"
                                          client.sendMessage(msg.to, "? Status Protection ?\n" + msgs)
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
                                            client.sendMessage(msg.to, "? Status Protection ?\n" + msgs)
                                      
# Pembatas Script #
                            elif text.lower() == "jadwaltv":
                                         result = requests.get("http://ari-api.herokuapp.com/jadwaltv").json()["result"];no=1;tv="   [ Jadwal TV ]   \n\n"
                                         for wildan in result:
                                          tv+="{}. {} - {} ({})\n".format(str(no), str(wildan["channelName"]), str(wildan["acara"]), str(wildan["jam"]))
                                          no+=1
                                         tv+="\n";sendMessageFooter(to, str(tv))
                            elif "screenshotwebsite" in msg.text.lower():
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                with requests.session() as web:
                                    r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                    data = r.text
                                    data = json.loads(data)
                                    client.sendImageWithURL(to, data["result"])
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
                                sendMessageFooter(msg.to, readTime)
                            elif cmd.startswith("checkwebsite"):
                                try:
                                    sep = text.split(" ")
                                    query = text.replace(sep[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                    data = r.text
                                    data = json.loads(data)
                                    client.sendImageWithURL(to, data["result"])
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkdate"):
                                try:
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
                                    sendMessageFooter(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkpraytime "):
                                separate = msg.text.split(" ")
                                location = msg.text.replace(separate[0] + " ","")
                                r = requests.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(location))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Makassar")
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
                                    sendMessageFooter(msg.to, str(ret_))
                            elif cmd.startswith("checkweather "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Makassar")
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
                                        sendMessageFooter(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checklocation "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "╭──[ Location Status ]"
                                        ret_ += "\n│ Location : " + data[0]
                                        ret_ += "\n│ Google Maps : " + link
                                        ret_ += "\n╰──[ Success ]"
                                        sendMessageFooter(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif text.lower().startswith("instainfo "):
                                try:
                                    search = text.lower().replace("instainfo ","")
                                    r = requests.get("http://api.dzin.tech/api/instaprofile/?apikey=beta&username={}".format(urllib.parse.quote(search)))
                                    data = r.text
                                    data = json.loads(data)
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
                                    url = data["result"]["url"]
                                    path = data["result"]["photo"]
                                    client.sendMessage(to, str(path))
                                    sendMessageFooter(to, str(ret_))
                                except:
                                    sendMessageFooter(to, "Username not found.")

                            elif cmd.startswith("instapost"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")   
                                    cond = text.split(" ")
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
                                        sendMessageFooter(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instastory"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")
                                    cond = text.split(" ")
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
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("say-" + lang + " ","")
                                if lang not in list_language["list_textToSpeech"]:
                                    return sendMessageFooter(to, "Language not found")
                                tts = gTTS(text=say, lang=lang)
                                tts.save("hasil.mp3")
                                client.sendAudio(to,"hasil.mp3")
                                
                            elif cmd.startswith("searchimage"):
                                try:
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
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(" ")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "???[ Result  Musik ]"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n? {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n???[ Total {} Musik ]".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Music, silahkan gunakan command {}SearchMusic {}|[number]".format(str(setKey), str(search))
                                    sendMessageFooter(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "???[ Musik ]"
                                            ret_ += "\n? Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n? Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n? Size : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n? Link : {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n???[ Finish ]"
                                            client.sendImageWithURL(to, str(data["result"]["img"]))
                                            sendMessageFooter(to, str(ret_))
                                            client.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                            elif text.lower().startswith("music2 "):
                                try:
                                    search = text.lower().replace("music2 ","")
                                    r = requests.get("https://farzain.xyz/api/joox.php?apikey=your_api_key&id={}".format(urllib.parse.quote(search))) #untuk api key bisa requests ke web http://www.farzain.xyz/requests.php
                                    data = r.text
                                    data = json.loads(data)
                                    info = data["info"]
                                    audio = data["audio"]
                                    hasil = " Hasil Musik \n"
                                    hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                    hasil += "\nJudul : {}".format(str(info["judul"]))
                                    hasil += "\nAlbum : {}".format(str(info["album"]))
                                    hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                    hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                    hasil += "\n\nLink : \n3. M4A : {}".format(str(audio["m4a"]))
                                    client.sendImageWithURL(msg.to, str(data["gambar"]))
                                    client.sendMessage(msg.to, "Downloading...")
                                    client.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                    client.sendVideoWithURL(msg.to, str(audio["m4a"]))
                                    client.sendMessage(msg.to, "Success Download...")
                                except Exception as error:
                                	client.sendMessage(msg.to, " Result Error \n" + str(error))


                            elif cmd.startswith("searchlyric"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(" ")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "???[ Result  Lirik ]"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n? {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n???[ Total {}  Musik ]".format(str(len(data["results"])))
                                    ret_ += "\n\nUntuk Melihat Details Lyric, silahkan gunakan command {}SearchLyric {}|[number]".format(str(setKey), str(search))
                                    sendMessageFooter(to, str(ret_))
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
                                        sendMessageFooter(msg.to, str(lyric))
                            elif cmd.startswith("searchyoutube"):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "???[ Youtube Result ]"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n???[ {} ]".format(str(data["title"]))
                                    ret_ += "\n? https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n???[ Total {} ]".format(len(datas))
                                sendMessageFooter(to, str(ret_))
                            elif cmd.startswith("tr-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("tr-" + lang + " ","")
                                if lang not in list_language["list_translate"]:
                                    return sendMessageFooter(to, "Language not found")
                                translator = Translator()
                                hasil = translator.translate(say, dest=lang)
                                A = hasil.text
                                client.sendMessage(to, str(A))
# Pembatas Script #
                        if text.lower() == "mykey":
                            sendMessageFooter(to, "KeyCommand Saat ini adalah [ {} ]".format(str(settings["keyCommand"])))
                        elif text.lower() == "setkey on":
                            settings["setKey"] = True
                            sendMessageFooter(to, "Berhasil mengaktifkan setkey")
                        elif text.lower() == "setkey off":
                            settings["setKey"] = False
                            sendMessageFooter(to, "Berhasil menonaktifkan setkey")
                        elif text.lower() == "resetkey":
                             settings["keyCommand"] = ""
                             sendMessageFooter(msg.to, "[Setkey]\nSetkey telah di reset")
# Pembatas Script #

# Pembatas Script #
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = client.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            client.updateProfilePicture(path)
                            sendMessageFooter(to, "Berhasil mengubah foto profile")
                        if settings["changeCover"] == True:
                            path = client.downloadObjectMsg(msg_id)
                            settings['changeProfileCover'] = path
                            settings["changeCover"] = False
                            cover = str(settings["changeProfileCover"])
                            client.updateProfileCoverById(cover)
                            client.sendMessage(to, "Berhasil mengubah foto cover")
                        if msg.toType == 2:
                            if to in settings["changeGroupPicture"]:
                                path = client.downloadObjectMsg(msg_id)
                                settings["changeGroupPicture"].remove(to)
                                client.updateGroupPicture(to, path)
                                sendMessageFooter(to, "Berhasil mengubah foto group")
                        elif msg.contentType == 2:
                            if settings['changeProfileVideo']['status'] == True:
                                path = client.downloadObjectMsg(msg_id)
                                if settings['changeProfileVideo']['stage'] == 1:
                                    settings['changeProfileVideo']['video'] = path
                                    client.sendMessage(to, "Send a pict to change change dual")
                                    settings['changeProfileVideo']['stage'] = 2
                                elif settings['changeProfileVideo']['stage'] == 2:
                                    settings['changeProfileVideo']['video'] = path
                                    changeProfileVideo(to)
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
                            sendMessageFooter(to, str(ret_))
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
                                sendMessageFooter(to, str(ret_))
                            except:
                                sendMessageFooter(to, "Kontak tidak valid")
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
                                sendMessageFooter(to, str(ret_))
                            except:
                                sendMessageFooter(to, "Post tidak valid")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        
        if op.type == 26:
            try:
                #print ("[ 26 ] RECIEVE MESS        msg = op.message
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
                                        if len(group.members) >= 200:
                                             client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                             sendMessageFooter(to, client.profile.displayName + " berhasil masuk ke group %s" % str(group.name))
                                        else:
                                            sendMessageFooter(to, client.profile.displayName + " tidak bisa bergabung ke group %s karena member dibawah 200" % str(group.name))
                                    else:
                                        sendMessageFooter(to, client.profile.displayName + " tidak bisa bergabung ke group %s karena QR group tertutup" % str(group.name))
                        if "/ti/g2/" in msg.text.lower():
                            if settings["autoJoinTicketSquare"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g2\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    square = client.findSquareByInvitationTicket(ticket_id)
                                    xx = square.squareStatus
                                    xx = xx.memberCount
                                    a = " [ Square Invitation Ticket ]"
                                    a += "\nName: " + square.square.name
                                    a += "\nDescription: " + square.square.desc
                                    a += "\nMember Count: " + str(xx)
                                    a += "\nInvitation URL: " + square.square.invitationURL
                                    a += "\nID: " + square.square.mid
                                    sendMessageFooter(to, str(a),contentMetadata = {'AGENT_ICON':'http://dl.profile.line-cdn.net/'+str(square.square.profileImageObsHash),'AGENT_NAME':'Click for view','AGENT_LINK':'http://dl.profile.line-cdn.net/'+str(square.square.profileImageObsHash)})
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = client.getGroup(at)
                                ryan = client.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                client.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                client.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = client.getGroup(at)
                                ryan = cient.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                client.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = client.getGroup(at)
                                ryan = client.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                client.sendMessage(at, str(ret_))
                                client.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
        #if op.type == 55:
        	#try:
        		#group_id = op.param1
        		#user_id=op.param2
        		#subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
        	#except Exception as e:
        		#print(e)
	      
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
                                cctv['sidermem'][op.param1] += "\nâ€¢ " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        sendMentionFooter(op.param1, "ᴡᴏʏ ☞ @!       ☜\nᴅɪ {} ᴋᴏᴋ ᴅɪᴇᴍ ᴅɪᴇᴍ ʙᴀᴇ...\nsɪɴɪ ɪᴋᴜᴛ ɴɢᴏᴘɪ".format(str(tgb.name)),[op.param2])
                                        client.sendContact(op.param1, op.param2)
                                        client.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                                    else:
                                        sendMentionFooter(op.param1, "ᴍʙʟᴏ ☞ @!       ☜\nɴɢɪɴᴛɪᴘ ᴅᴏᴀɴɢ ʟᴜ ᴅɪ {} \nsɪɴɪ ɢᴀʙᴜɴɢ ᴍᴀ ᴋɪᴛᴀ".format(str(tgb.name)),[op.param2])
                                        client.sendContact(op.param1, op.param2)
                                        client.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                                else:
                                    sendMentionFooter(op.param1, "ʜɪʟɪʜ ☞ @!       ☜\nɴɢᴀᴘᴀɪɴ ʟᴜ...\nɢᴀʙᴜɴɢ ᴄʜᴀᴛ sɪɴɪ ᴅɪ {} ".format(str(tgb.name)),[op.param2])
                                    client.sendContact(op.param1, op.param2)
                                    client.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
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

while True:
    try:
        delete_log()
        ops = clientPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clientBot(op)
                clientPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)



while True:
    try:
        eventsSquareChat=oepoll.singleFetchSquareChat(squareChatMid=squareChatMid)
        for e in eventsSquareChat:
            if e.createdTime is not 0:
                ts_old = int(e.createdTime) / 1000
                ts_now = int(time.time())
                client.log('[FETCH_TIME] ' + str(int(e.createdTime)))
                if ts_old >= ts_now:
                    '''
                        This is sample for implement BOT in LINE square
                        BOT will noticed who leave square chat
                        Command availabe :
                        > hi
                        > /author
                    '''
                    # Receive messages
                    if e.payload.receiveMessage != None:
                        payload=e.payload.receiveMessage
                        client.log('[RECEIVE_MESSAGE]')
                        msg=payload.squareMessage.message
                        msg_id=msg.id
                        receiver_id=msg._from
                        sender_id=msg.to
                        if msg.contentType == 0:
                            text=msg.text
                            if text.lower() == 'hi':
                                client.log('%s' % text)
                                client.sendSquareMessage(squareChatMid, 'Hi too! How are you?')
                            elif text.lower() == '/author':
                                client.log('%s' % text)
                                client.sendSquareMessage(squareChatMid, 'My author is linepy')
                    # Notified leave Square Chat
                    elif e.payload.notifiedLeaveSquareChat != None:
                        payload=e.payload.notifiedLeaveSquareChat
                        client.log('[NOTIFIED_LEAVE_SQUARE_CHAT]')
                        squareMemberMid=payload.squareChatMid
                        squareMemberMid=payload.squareMemberMid
                        squareMember=payload.squareMember
                        displayName=squareMember.displayName
                        client.sendSquareMessage(squareChatMid, 'Good bye! ' + str(displayName))
                    else:
                        pass

    except Exception as e:
        client.log("[FETCH_SQUARE] Fetch square chat error: " + str(e))

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)


while True:
    try:
        delExpire()
        delete_log()
        ops = clientPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clientBot(op)
                clientPoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
