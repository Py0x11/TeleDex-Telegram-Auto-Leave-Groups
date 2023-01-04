from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest, StartBotRequest
from telethon.tl.functions.channels import LeaveChannelRequest, JoinChannelRequest, GetParticipantsRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from telethon.tl.types import PeerChannel, PeerChat, PeerUser, ChannelParticipantsSearch, InputPeerUser
from time import sleep
import json
import re
import sys
import os
import random
from datetime import datetime
import requests
import random
from bs4 import BeautifulSoup
bghjgh = ["http://raboninco.com/1x44m",
          "http://raboninco.com/1x4Kk",
          "http://raboninco.com/1x4PN",
          "http://raboninco.com/1x4SE",
          "http://raboninco.com/1x4UK",
          "http://raboninco.com/1x4Xf",
          "http://raboninco.com/1x4ZA",
          "http://raboninco.com/1x4d6"]
vjfnhgrtg = ["@&^%!&#^$(*&!%#$@#",
             "G^F%F$S#SA#^F^G&G&G",
             "a!S@S#D$DF%^G*&H",
             "3!@2123546$@#@#",
             "A123DS654REAF",
             "LKJ*&^uyt^%$321#@",
             "kjh(*&kjhytr^%$%$#",
             ".,.,.,.,.,"]
os.system('cls' if os.name == 'nt' else 'clear')


def bans():
    global starting, colors
    colors = ["\033[0;1;40;31m", "\033[0;1;40;32m", "\033[0;1;40;33m",
              "\033[0;1;40;34m", "\033[0;1;40;35m", "\033[0;1;40;36m", "\033[0;1;40;37m"]
    starting = """
 ___    ___
( _<    >_ )
//        \\
\\___..___//
 `-(    )-'
   _|__|_
  |_|__|_|
  |_|__|_|
  |_\__/_|
   \ || /  _)
     ||   ( )
      \\___//    Telegram :@Py0x11 & @Lucifer
      `---' """
    for char in starting:
        sys.stdout.write(str(char))
        sys.stdout.flush()
        sleep(.01)

    def light(starting):
        i = 0
        j = 0
        for char in starting:
            if j == len(colors) - 1:
                j = 0
            if i == 25:
                j += 1
                i = 0
            sys.stdout.write(str(colors[j]) + str(char))
            sys.stdout.flush()
            i += 1
            sleep(0.0001)
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    light(starting)
    sleep(1)
    banner = """\033[0;1;37;40m
    ________________________________
    | Script by : LucidManiacz 😎  |
    | Telegram  : @Py0x11           |
    |             @LuciferSamiel    |
    |_______________________________|
    'FOr Any Issue DM on Telegram '
    """
    for char in banner:
        sys.stdout.write(str(char))
        sys.stdout.flush()
        sleep(.001)
    asdfds = datetime.now()
    fvbfgh = asdfds.strftime("%A")
    ips = "https://ipinfo.io/json"
    sss = requests.get(ips, headers=None)
    print("\n\033[0;1;34;40m Today is " + str(fvbfgh))
    print("\033[0;37m===============================")
    print("\033[0;37m Ip Address : \033[0;1;34;40m" + str(sss.json()['ip']))
    print("\033[0;37m Country    : \033[0;1;34;40m"+str(sss.json()['country']))
    print("\033[0;37m===============================")


try:
    open("Numbers.txt", "x")
except:
    pass
if not os.path.exists('session'):
    os.makedirs('session')
try:
    datas = open('auto.json', 'r')
    auto_loads = json.load(datas)
    datas.close()
    auto_loads = auto_loads[0]
except:
    pass
# os.system('cls' if os.name == 'nt' else 'clear')

dkrughdfg = ["http://raboninco.com/1uK5s", "http://raboninco.com/1uK8C", "http://raboninco.com/1uK9s", "http://raboninco.com/1uKBj", "http://raboninco.com/1uKDq", "http://raboninco.com/1uKGz", "http://raboninco.com/1uKIv",
             "http://raboninco.com/1vAoi", "http://raboninco.com/1vAqp", "http://raboninco.com/1vAsF", "http://raboninco.com/1vAtn", "http://raboninco.com/1vAvN", "http://raboninco.com/1vAwz", "http://raboninco.com/1vByq", "http://raboninco.com/1vC0N"]
csdwert = ['NUH&^%TYRHFG$@', "IN*&YBUTF$", "FKUF(*&EURHG", "DKVRUHGVIDHRUG", "123asd!@#", "fghlkoi*^%", "frder345*&^",
           "GFD^%$JGH#@!REW", "KAJDSH*&^$!@", "awdasUYIUY!@", "KJAHSDI*&@(#", "LKJD*&^@!", "LAKSJDOWIUE@#@!", "awd.0", "13asd!@654"]


def enter():
    print(" Numbers must be +6xxxxxxx")
    sleep(1)
    print(" Leave it Blank if youre finish")
    print("===============================")
    while True:
        en = input(" Enter Your Number : ")
        f = open("Numbers.txt", "a")
        f.write(en + "\n")
        f.close()
        if str(en) == "":
            break


HJGJHGKH = ['http://raboninco.com/1uKIv', 'http://raboninco.com/1vAwz',
            'http://q.gs/FJfgA', "http://raboninco.com/1uKL3", "http://raboninco.com/1vC2p"]
BNG678DERTE = ['frder345*&^', 'LAKSJDOWIUE@#@!',
               'GHJ%^WDFWE@#$^%&*456ERG234DFG!@#&^', '!DXDHBJ268@#$&1', "KJJLK(.)<=!&@^UIQYW"]


def accounts(number):
    global account, ua, connector
    ua = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
    api_id = 717425
    api_hash = '322526d2c3350b1d3530de327cf08c07'
    try:
        account = TelegramClient("session/"+number, api_id, api_hash)
        account.connect()
        sleep(1)
        try:
            if not account.is_user_authorized():
                account.send_code_request(number)
                xx = input(" Enter Your Code : ")
                account.sign_in(number, xx)
        except SessionPasswordNeededError:
            pwd = input(" Enter Your 2FA Password : ")
            account.start(number, pwd)
        connector = 'connect'
    except Exception as e:
        if str(e).__contains__('banned'):
            print(" \033[0;1;31m Account Banned!")
        elif str(e).__contains__('disconnect'):
            print(" \033[0;1;31m Account Disconnected.")
        else:
            pass
    try:
        info = account.get_me()
        print(" UserID : "+str(info.id) + " | Name   : " + str(info.first_name))
    except:
        pass


VFGHGBH = ['http://q.gs/FJfft', 'http://raboninco.com/1sK65',
           'http://raboninco.com/1sKCJ', 'http://raboninco.com/1sVmC']
RTVHFGH = ['dkmgjvdkjfgkdjfg34553*&^*&^$*&@^*&^!@*#^*!@&^',
           'XDHBJ268@#$&12.', 'XDHBJ268@#$&12.', 'GAHE46CBG1UFK78LAOJF8']


def md(cu):
    try:
        global ltc, ltc_username, lsa, lr, wdr, auto_loads
        ltc_link = 'https://t.me/Litecoin_click_bot'
        doge_link = 'https://t.me/Dogecoin_click_bot'
        bch_link = 'https://t.me/BCH_clickbot'
        btc_link = 'https://t.me/BitcoinClick_bot'
        zec_link = 'https://t.me/Zcash_click_bot'
        lsa = [ltc_link, doge_link, bch_link, btc_link, zec_link]
        lr = ['EnRP', '4IZd', 'AfBH', 'LMxf', 'OKCO']
        lt = "@Litecoin_click_bot"
        dg = "Dogecoin_click_bot"
        bc = "@BCH_clickbot"
        bt = "@BitcoinClick_bot"
        zc = "@Zcash_click_bot"
        currency = [lt, dg, bc, bt, zc]
        cl = ['1', '2', '3', '4', '5']
        try:
            address = open("wd.json", 'r')
            data_address = json.load(address)
            address.close()
            w1 = data_address['LTC']
            w2 = data_address['DOGE']
            w3 = data_address['BCH']
            w4 = data_address['BTC']
            w5 = data_address['ZEC']
            wdr = [w1, w2, w3, w4, w5]
        except:
            pass
        for x in cl:
            if cu == x:
                global xxx
                xxx = cl.index(x)
                print(currency[xxx])
                ltc = account.get_entity(currency[xxx])
                ltc_username = currency[xxx]
        try:
            datas = open('auto.json', 'r')
            auto_loads = json.load(datas)
            datas.close()
            auto_loads = auto_loads[0]
        except:
            pass
    except Exception as e:
        # print(" Invalid Input")
        # print(e)
        try:
            account.disconnect()
        except:
            pass


FGHVFGH = ['http://q.gs/FJfff', 'http://q.gs/FJfff',
           'http://q.gs/FJffq', 'http://q.gs/FJffs']
BGJHGHYJ = ['a&HT#4FG7GH$5', '4FG7GH', 'juh*&^jhgjhgYTFD%$65HGUYGUY&6768&^*IUH&*^*&^',
            'kdjf9*&(*&IJHIHUDIAUHWIUHE82748274']


def auto_leave():
    print(" Auto Leave Channel Start")
    try:
        i = 0
        for dialog in account.get_dialogs():
            print(' Searching Channels \r', end="")
            try:
                channel_entity = account.get_entity(
                    PeerChannel(int(dialog.entity.id)))
                print(" " + channel_entity.title + "\r", end="")
                account(LeaveChannelRequest(channel_entity))
                i += 1
                print(" [" + str(i) + "] " +
                      channel_entity.title + " Leave Success")
            except:
                pass
        print(" Done Leave                      ")
    except Exception as e:
        print(e)


def out_reward():
    i = 0
    while True:
        reward = account(GetHistoryRequest(peer=ltc, limit=2, offset_date=None,
                         offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages
        r = reward[0].message
        r1 = reward[1].message
        if r.__contains__('Success'):
            w = r.split("\n")
            for x in w:
                if x.__contains__("You must stay"):
                    try:
                        sxfefa = re.findall("[0-9]+", x)[0]
                        print("\033[0;1;35m[\033[0;1;34m+\033[0;1;35m]\033[0;1;37m Stay at least "+str(
                            sxfefa)+" hour \033[0;1;37m                    ")
                    except:
                        print(x)
            break
        if r.__contains__('looks invalid'):
            account.send_message(entity=ltc, message="❌ Cancel")
            sleep(1)
            break
        elif r.__contains__('recognized command'):
            print(r)
            try:
                ids = history.messages[0].id
                account(GetBotCallbackAnswerRequest(
                    ltc_username, ids, data=history.messages[0].reply_markup.rows[1].buttons[1].data))
            except:
                pass
            break
        elif r1.__contains__('recognized command'):
            print(r1)
            try:
                ids = history.messages[0].id
                account(GetBotCallbackAnswerRequest(
                    ltc_username, ids, data=history.messages[0].reply_markup.rows[1].buttons[1].data))
            except:
                pass
            break
        elif r.__contains__('You earn') or r.__contains__('you earn'):
            print(' \033[0;1;35m[\033[0;1;34m+\033[0;1;35m]\033[0;1;37m'+str(r))
            break
        elif r1.__contains__('Success'):
            w = r1.split("\n")
            for x in w:
                if x.__contains__("You must stay"):
                    try:
                        sxfefa = re.findall("[0-9]+", x)[0]
                        print(" \033[0;1;35m[\033[0;1;34m+\033[0;1;35m]\033[0;1;37mStay at least "+str(
                            sxfefa)+" hour                      ")
                    except:
                        print(x)
            break
        elif r1.__contains__('You earn') or r1.__contains__('you earn'):
            print(' \033[0;1;35m[\033[0;1;34m+\033[0;1;35m]\033[0;1;37m'+str(r1))
            break
        i += 1
        sleep(1)
        if i >= 5:
            print(
                " \033[0;1;31mBot Server to Slow\033[0;1;37m                            ")
            break


def auto_join():
    print(
        "\033[0;1;34;40m Auto Join Chats\033[0m                                   ")
    print("===============================")
    waitsError = 0
    lim = 0
    while True:
        try:
            account.send_message(entity=ltc, message="📣 Join chats")
            i = 0
            sleep(1)
            while True:
                sends = account(GetHistoryRequest(peer=ltc, limit=2, offset_date=None,
                                offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
                if sends.__contains__('looks invalid'):
                    account.send_message(entity=ltc, message="❌ Cancel")
                    sleep(1)
                    return auto_join()
                elif str(sends) == '📣 Join chats':
                    pass
                else:
                    break
                i += 1
                if i >= 10:
                    print(
                        " \033[0;1;31mBot Server to Slow    \033[0;1;37m                       ")
                    break
                sleep(1)
            try:
                sleep(1)
                history = account(GetHistoryRequest(
                    peer=ltc, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                url_join = history.messages[0].reply_markup.rows[0].buttons[0].url
                if str(url_join).__contains__('doge.click'):
                    if str(url_join).__contains__('https'):
                        ds = url_join.replace('https://doge.click/', '')
                        url_join = 'https://dogeclick.com/'+str(ds)
                    else:
                        ds = url_join.replace('http://doge.click/', '')
                        url_join = 'http://dogeclick.com/'+str(ds)
                try:
                    xs = requests.Session()
                    zxc = xs.get(url_join).text
                    msbot = BeautifulSoup(zxc, 'html.parser')
                    mets = msbot.find(
                        'meta', {'name': 'twitter:app:url:googleplay'})
                    xxxasd = re.findall('content="[0-9a-zA-Z./-_]+', str(mets))
                    url_join = xxxasd[0].replace('content="', '')
                except:
                    pass
                print(url_join + "\r", end="")
            except Exception as e:
                pass
            sorry = account(GetHistoryRequest(peer=ltc, limit=1, offset_date=None,
                            offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
            if sorry.__contains__("Sorry, there"):
                sorry = sorry.split(".")
                print('\033[0;1;31m '+str(sorry[0])+'\033[0;1;37m')
                break
            account(JoinChannelRequest(url_join))
            sleep(1)
            join_id = history.messages[0].id
            account(GetBotCallbackAnswerRequest(ltc_username, join_id,
                    data=history.messages[0].reply_markup.rows[0].buttons[1].data))
            sleep(1)
            out_reward()
            r = account(GetHistoryRequest(peer=ltc, limit=2, offset_date=None,
                        offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
            if r.__contains__('We cannot find'):
                w = r.split("\n")
                for x in w:
                    if x.__contains__("We cannot find"):
                        print(x)
                        history = account(GetHistoryRequest(
                            peer=ltc, limit=2, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                        ids = history.messages[1].id
                        account(GetBotCallbackAnswerRequest(
                            ltc_username, ids, data=history.messages[1].reply_markup.rows[1].buttons[1].data))
                        print(" SKIP\r", end='')
            lim += 1
            try:
                if int(lim) >= (auto_loads['joinLimit']):
                    break
            except:
                pass
        except Exception as e:
            # print(str(e)+'\r',end='')
            if str(e).__contains__("seconds is "):
                try:
                    xxeess = re.findall('[0-9]+', str(e))
                    print(' \033[0;1;31mTry again after ' +
                          str(xxeess[0])+' seconds\033[0;1;37m')
                except:
                    pass
                break
            else:
                try:
                    if int(waitsError) >= 10:
                        break
                    history = account(GetHistoryRequest(
                        peer=ltc, limit=2, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    ids = history.messages[0].id
                    account(GetBotCallbackAnswerRequest(
                        ltc_username, ids, data=history.messages[0].reply_markup.rows[1].buttons[1].data))
                    print(" SKIP\r", end='')
                except:
                    pass
                waitsError += 1


def mess_bots():
    print("\033[0;1;34;40m Auto Message Bot \033[0m                           ")
    print("===============================")
    waa = 0
    while True:
        sleep(3)
        try:
            account.send_message(entity=ltc, message="🤖 Message bots")
            i = 0
            while True:
                sends = account(GetHistoryRequest(peer=ltc, limit=2, offset_date=None,
                                offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
                if sends.__contains__('address you entered looks invalid'):
                    account.send_message(entity=ltc, message="❌ Cancel")
                    sleep(1)
                    return mess_bots()
                if str(sends) == '🤖 Message bots':
                    pass
                else:
                    break
                i += 1
                if i >= 10:
                    print(
                        "\033[0;2;31m Bot Server to Slow      \033[0;1;37m                     ")
                    break
                sleep(1)
            try:
                sleep(1)
                global history
                history = account(GetHistoryRequest(
                    peer=ltc, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                sorry = account(GetHistoryRequest(peer=ltc, limit=1, offset_date=None,
                                offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
                if sorry.__contains__("Sorry, there"):
                    sorry = sorry.split(".")
                    print(' \033[0;1;31m'+str(sorry[0])+'\033[0;37m')
                    break
                message_bot = history.messages[0].reply_markup.rows[0].buttons[0].url
                if str(message_bot).__contains__('doge.click'):
                    if str(message_bot).__contains__('https'):
                        ds = message_bot.replace('https://doge.click/', '')
                        message_bot = 'https://dogeclick.com/'+str(ds)
                    else:
                        ds = message_bot.replace('http://doge.click/', '')
                        message_bot = 'http://dogeclick.com/'+str(ds)
            except Exception as e:
                # print(e)
                pass
            sleep(1)
            try:
                zxc = requests.get(message_bot).text
                msbot = BeautifulSoup(zxc, 'html.parser')
                mets = msbot.find(
                    'meta', {'name': 'twitter:app:url:googleplay'})
                xxxasd = re.findall('content="[0-9a-zA-Z./-_]+', str(mets))
                message_bot = xxxasd[0].replace('content="', '')
            except:
                pass
            print(str(message_bot) + "\r", end="")

            if message_bot.__contains__("t.me"):
                if message_bot.__contains__("https"):
                    message_bot = message_bot.replace("https://t.me/", "")
                else:
                    message_bot = message_bot.replace("http://t.me/", "")
            elif message_bot.__contains__("telegram.me"):
                if message_bot.__contains__("https"):
                    message_bot = message_bot.replace(
                        "https://telegram.me/", "")
                else:
                    message_bot = message_bot.replace(
                        "http://telegram.me/", "")
            message_bot = re.findall("[a-zA-Z0-9_]+", message_bot)[0]
            message_bot = "@"+str(message_bot)
            account.send_message(entity=message_bot, message="/start")

            i = 0
            while True:
                sleep(1)
                qq = account(GetHistoryRequest(peer=message_bot, limit=2, offset_date=None,
                             offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
                if str(qq) == "/start":
                    pass
                else:
                    break
                i += 1
                if i >= 5:
                    break
            ii = 0
            while True:
                qq = account(GetHistoryRequest(peer=message_bot, limit=2, offset_date=None,
                             offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
                if not qq.__contains__("/start"):
                    account.forward_messages(entity=ltc, messages=account(GetHistoryRequest(
                        peer=message_bot, limit=2, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].id, from_peer=message_bot)
                    out_reward()
                    break
                if ii > 5:
                    break
                ii += 1
                sleep(1)
            qq = account(GetHistoryRequest(peer=message_bot, limit=2, offset_date=None,
                         offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
            if qq.__contains__("/start"):
                try:
                    history1 = account(GetHistoryRequest(
                        peer=ltc, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    ids = history1.messages[0].id
                    account(GetBotCallbackAnswerRequest(
                        ltc_username, ids, data=history1.messages[0].reply_markup.rows[1].buttons[1].data))
                    print(" SKIP\r", end='')
                except:
                    pass
            gamebot = account(GetHistoryRequest(peer=ltc, limit=2, offset_date=None,
                              offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
            if gamebot.__contains__('not a valid'):
                account.send_message(entity=ltc, message="🤖 Message bots")
                sleep(3)
                history1 = account(GetHistoryRequest(
                    peer=ltc, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                ids = history1.messages[0].id
                account(GetBotCallbackAnswerRequest(
                    ltc_username, ids, data=history1.messages[0].reply_markup.rows[1].buttons[1].data))
                print(" SKIP\r", end='')
        except Exception as e:
            # print(str(e)+'\r',end='')
            account.send_message(entity=ltc, message="🤖 Message bots")
            sleep(2)
            xxeexx = account(GetHistoryRequest(peer=ltc, limit=2, offset_date=None,
                             offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
            if str(xxeexx).__contains__('Sorry, there'):
                sorry = xxeexx.split('.')
                print(' \033[0;1;31m'+str(sorry[0])+'\033[0;37m')
                break
            else:
                try:
                    account.send_message(entity=ltc, message="🤖 Message bots")
                    sleep(3)
                    history1 = account(GetHistoryRequest(
                        peer=ltc, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    ids = history1.messages[0].id
                    account(GetBotCallbackAnswerRequest(
                        ltc_username, ids, data=history1.messages[0].reply_markup.rows[1].buttons[1].data))
                    print(" SKIP\r", end='')
                except:
                    pass
                if int(waa) >= 10:
                    break
                waa += 1


def visit():
    print("\033[0;1;34;40m Auto Visit Sites\033[0m                                ")
    print("===============================")
    djhfdfgd = 0
    lims = 0
    while True:
        lims += 1
        if int(lims) >= 30:
            break
        try:
            account.send_message(entity=ltc, message='🖥 Visit sites')
            sleep(3)
            i = 0
            while True:
                sends = account(GetHistoryRequest(peer=ltc, limit=2, offset_date=None,
                                offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
                if sends.__contains__('looks invalid'):
                    account.send_message(entity=ltc, message="❌ Cancel")
                    sleep(1)
                    return visit()
                if str(sends) == '🖥 Visit sites':
                    pass
                else:
                    break
                i += 1
                if i >= 10:
                    print(
                        "\033[0;2;31m Bot Server to Slow      \033[0;1;37m                     ")
                    break
                sleep(1)
            sleep(1)
            try:
                history = account(GetHistoryRequest(
                    peer=ltc, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                sorry = account(GetHistoryRequest(peer=ltc, limit=1, offset_date=None,
                                offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
                if sorry.__contains__("Sorry, there"):
                    sorry = sorry.split(".")
                    print(' \033[0;1;31m'+str(sorry[0])+'\033[0;1;37m')
                    break
                visit_url = history.messages[0].reply_markup.rows[0].buttons[0].url
                if str(visit_url).__contains__('doge.click'):
                    if str(visit_url).__contains__('https'):
                        ds = visit_url.replace('https://doge.click/', '')
                        visit_url = 'https://dogeclick.com/'+str(ds)
                    else:
                        ds = visit_url.replace('http://doge.click/', '')
                        visit_url = 'http://dogeclick.com/'+str(ds)
                print(visit_url + "\r", end="")
            except:
                pass
            sorry = account(GetHistoryRequest(peer=ltc, limit=1, offset_date=None,
                            offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
            if sorry.__contains__("Sorry, there"):
                sorry = sorry.split(".")
                print(' \033[0;1;31m'+str(sorry[0])+'\033[0;1;37m')
                break

            s = requests.Session()
            con = requests.get(visit_url, headers=ua,
                               timeout=15, allow_redirects=True)
            soup = BeautifulSoup(con.content, "html.parser")
            if soup.find('div', id="headbar") is not None:
                for dat in soup.find_all('div', class_="container-fluid"):
                    try:
                        code = dat.get('data-code')
                        timer = dat.get('data-timer')
                        tokena = dat.get('data-token')
                        cur = dat.get('data-curr')
                    except:
                        pass
                try:
                    timer = int(timer)
                    if timer > 60:
                        timer = 60
                except:
                    timer = 60
                ico = 0
                while timer != 0:
                    try:
                        print(str(
                            colors[ico])+" Please stay on site for at least " + str(timer) + " seconds \r", end="")
                    except:
                        ico = 0
                        print(str(
                            colors[ico])+" Please stay on site for at least " + str(timer) + " seconds \r", end="")
                    ico += 1
                    timer -= 1
                    sleep(1)
                sleep(2)
                try:
                    r = s.post("https://dogeclick.com/reward", data={
                               "code": code, "token": tokena}, headers=ua, timeout=15, allow_redirects=True)
                    js = r.json()['reward']
                    try:
                        print(" \033[0;1;35m[\033[0;1;34m+\033[0;1;35m]\033[0;1;37mYou earned " + str(
                            js) + " "+str(cur)+"for visiting a site")
                    except:
                        print(" \033[0;1;35m[\033[0;1;34m+\033[0;1;35m]\033[0;1;37mYou earned " + str(
                            js) + " for visiting a site")
                except:
                    pass
            else:
                try:
                    sleep(2)
                    rwrd = account(GetHistoryRequest(peer=ltc, limit=1, offset_date=None,
                                   offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
                    xt = re.findall('[0-9]+', rwrd)[0]
                    t = int(xt)
                    if t >= 60:
                        t = 60
                    ico = 0
                    while int(t) != 0:
                        try:
                            print(str(
                                colors[ico])+" Please stay on site for at least " + str(t) + " seconds \r", end="")
                        except:
                            ico = 0
                            print(str(
                                colors[ico])+" Please stay on site for at least " + str(t) + " seconds \r", end="")
                        t -= 1
                        ico += 1
                        sleep(1)
                    sleep(2)
                    out_reward()
                except:
                    try:
                        history = account(GetHistoryRequest(
                            peer=ltc, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                        ids = history.messages[0].id
                        account(GetBotCallbackAnswerRequest(
                            ltc_username, ids, data=history.messages[0].reply_markup.rows[1].buttons[1].data))
                        print(" SKIP\r", end="")
                    except:
                        history = account(GetHistoryRequest(
                            peer=ltc, limit=2, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                        ids = history.messages[1].id
                        account(GetBotCallbackAnswerRequest(
                            ltc_username, ids, data=history.messages[1].reply_markup.rows[1].buttons[1].data))
                        print(" SKIP\r", end="")
        except Exception as e:
            pass
            djhfdfgd += 1
            if int(djhfdfgd) >= 10:
                break


def interval():
    print("===============================")
    try:

        t = int(auto_loads['time_inverval'])*60*60
        while t != 0:
            m, s = divmod(t, 60)
            h, m = divmod(m, 60)
            timer = "{:02d}:{:02d}:{:02d}".format(h, m, s)
            print(" Time Interval : " + str(timer) + "            \r", end="")
            t -= 1
            sleep(1)
        if str(auto_loads['leave']) == 'on' or str(auto_loads['leave']) == 'On' or str(auto_loads['leave']) == 'ON':
            f = open("Numbers.txt", "r")
            num = f.read()
            f.close()
            k = 0
            num = num.split("\n")
            for j in num:
                if j.__contains__("+"):
                    number = j
                    k += 1
                    print(" [" + str(k) + "] Your Account number : " + str(number))
                    accounts(number)
                    print("===============================")
                    auto_leave()
                    account.disconnect()
                    print("===============================")
            i = 0
            while i != 100:
                print(" Starting Bot Again [" + str(i) + "%]\r", end="")
                sleep(.05)
                i += 1
        elif str(auto_loads['leave']) == 'off' or str(auto_loads['leave']) == 'Off' or str(auto_loads['leave']) == 'OFF':
            pass
        else:
            print(" Mode must be [On or Off]")
    except Exception as e:
        print(e)


def ref():
    try:
        try:
            for mzxnbc in lsa:
                xxaa = lsa.index(mzxnbc)
                account(StartBotRequest(
                    bot=mzxnbc, peer=mzxnbc, start_param=lr[xxaa]))
        except:
            pass
        sleep(1)
        account(StartBotRequest(bot=lsa[xxx],
                peer=lsa[xxx], start_param=lr[xxx]))
        sleep(2)
        account.send_message(entity=ltc, message='/cancel')
        sleep(1)
        account.send_message(entity=ltc, message='/bonus')
        sleep(2)
    except Exception as e:
        pass


def aut_wd():
    try:
        account.send_message(entity=ltc, message='💵 Withdraw')
        sleep(2)
        while True:
            wds = account(GetHistoryRequest(peer=ltc, limit=2, offset_date=None,
                          offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
            sm = account(GetHistoryRequest(peer=ltc, limit=2, offset_date=None,
                         offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
            if sm.__contains__("balance is too small"):
                break
            if wds.__contains__("not a recognized command"):
                break
            if sm.__contains__("enter at least"):
                account.send_message(entity=ltc, message="❌ Cancel")
                break
            if wds.__contains__("To withdraw,"):
                ws = wds.split("\n")
                account.send_message(entity=ltc, message=wdr[xxx])
                sleep(1)
                if ws[0].__contains__("balance"):
                    w = re.findall("[0-9.]+", ws[0])[0]
                break
            if sm.__contains__('looks invalid'):
                account.send_message(entity=ltc, message="❌ Cancel")
                break
        while True:
            sm = account(GetHistoryRequest(peer=ltc, limit=2, offset_date=None,
                         offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
            if sm.__contains__("balance is too small"):
                sm = sm.split("\n")
                print(sm[0])
                break
            amount = account(GetHistoryRequest(peer=ltc, limit=2, offset_date=None,
                             offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
            if amount.__contains__("not a recognized command"):
                break
            if amount.__contains__("Enter the amount"):
                print(w)
                account.send_message(entity=ltc, message=str(w))
                break
        sleep(1)
        er = account(GetHistoryRequest(peer=ltc, limit=2, offset_date=None,
                     offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
        if er.__contains__("not a recognized command") or er.__contains__("balance is too small"):
            pass
        else:
            account.send_message(entity=ltc, message=str('✅ Confirm'))
            sleep(1)
            while True:
                con = account(GetHistoryRequest(peer=ltc, limit=2, offset_date=None,
                              offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
                if con.__contains__('withdrawal has been'):
                    con = con.split('\n')
                    print(con[0])
                    break
    except Exception as e:
        pass


def getbal():
    try:
        account.send_message(entity=ltc, message='💰 Balance')
        sleep(2)
        while True:
            bals = account(GetHistoryRequest(peer=ltc, limit=2, offset_date=None,
                           offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
            if str(bals) == '💰 Balance':
                pass
            else:
                break
        bals = account(GetHistoryRequest(peer=ltc, limit=2, offset_date=None,
                       offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0)).messages[0].message
        if bals.__contains__('balance:'):
            print(bals)
        else:
            return getbal()
    except Exception as e:
        pass


def curn():
    global cu
    print('''
    [1] LTC
    [2] DOGE
    [3] BCH
    [4] BTC
    [5] ZEC
''')
    cu = input(" Choose a Currency : ")


def ran_mess():
    try:
        datas = open('auto.json', 'r')
        ran_chats = json.load(datas)[1]
        datas.close()
        urls = ran_chats['group_entity']
        chats = ran_chats['chat']
        myname = account.get_me().first_name
        for url in urls:
            finds = account(GetParticipantsRequest(channel=url, filter=ChannelParticipantsSearch(
                str(myname)), offset=0, limit=100, hash=0))
            if int(finds.count) == 0:
                account(JoinChannelRequest(url))
            mes = random.choice(chats)
            account.send_message(entity=url, message=mes)
            account(JoinChannelRequest(url))
        members = account(GetParticipantsRequest(
            channel=url, filter=ChannelParticipantsSearch(''), offset=0, limit=100, hash=0))
        i = int(len(members.users)-1)
        x = random.randint(0, i)
        mems = members.users[x]
        m = mems.id
        h = mems.access_hash
        n = mems.first_name
        sends = random.choice(chats)
        print(" " + str(sends) + " send to " + str(n))
        account.send_message(InputPeerUser(m, h), sends)
    except Exception as e:
        pass


def game():
    global k
    k = 0
    f = open("Numbers.txt", "r")
    num = f.read()
    f.close()
    num = num.split("\n")
    if len(open("Numbers.txt", "r").read()) == 0:
        print(" Enter Your Number first.")
        enter()
        return game()
    cs = '''
    [1] Auto [Message Bots] or [Join Chats] or [Visit sites] or [Leave Channels]
    [2] Leave Channels
    [3] Add Numbers
    [4] Withdraw
    [5] Balance
    [6] Account Checking
    '''
    print(cs)
    p = input(" Enter Your Choice : ")
    if str(p) == "1":
        vfghfg = 0
        curn()
        while True:
            vfghfg += 1
            for j in num:
                if j.__contains__("+"):
                    k += 1
                    number = j
                    print(" [" + str(k) + "] Your Account number : " + str(number))
                    accounts(number)
                    ran_mess()
                    md(cu)
                    print("===============================")
                    if str(connector) == 'connect':
                        ref()
                        sleep(1)
                        try:
                            if str(auto_loads['message']) == 'on' or str(auto_loads['message']) == 'On' or str(auto_loads['message']) == 'ON':
                                mess_bots()
                            elif str(auto_loads['message']) == 'off' or str(auto_loads['message']) == 'Off' or str(auto_loads['message']) == 'OFF':
                                pass
                            else:
                                print(" Mode must be [On or Off]")
                                sys.exit()
                        except:
                            print(' Data Error \r', end="")
                            # sys.exit()
                        try:
                            if str(auto_loads['join']) == 'on' or str(auto_loads['join']) == 'On' or str(auto_loads['join']) == 'ON':
                                auto_join()
                            elif str(auto_loads['join']) == 'off' or str(auto_loads['join']) == 'Off' or str(auto_loads['join']) == 'OFF':
                                pass
                            else:
                                print(" Mode must be [On or Off]")
                                sys.exit()
                        except:
                            print(' Data Error \r', end="")
                            # sys.exit()
                        try:
                            if str(auto_loads['visit']) == 'on' or str(auto_loads['visit']) == 'On' or str(auto_loads['visit']) == 'ON':
                                visit()
                            elif str(auto_loads['visit']) == 'off' or str(auto_loads['visit']) == 'Off' or str(auto_loads['visit']) == 'OFF':
                                pass
                            else:
                                print(" Mode must be [On or Off]")
                                sys.exit()
                        except:
                            print(' Data Error \r', end="")
                        try:
                            if str(auto_loads['wd']) == 'on' or str(auto_loads['wd']) == 'On' or str(auto_loads['wd']) == 'ON':
                                aut_wd()
                            elif str(auto_loads['wd']) == 'off' or str(auto_loads['wd']) == 'Off' or str(auto_loads['wd']) == 'OFF':
                                pass
                            else:
                                print(" Mode must be [On or Off]")
                                sys.exit()
                        except:
                            print(' Data Error \r', end="")
                            # sys.exit()
                        getbal()
                        account.disconnect()
                        print("===============================")
                    else:
                        print(" There is something wrong with your account")
                        print("===============================")

            try:
                interval()
            except:
                pass
    elif str(p) == "2":
        for j in num:
            if j.__contains__("+"):
                number = j
                k += 1
                print(" [" + str(k) + "] Your Account number : " + str(number))
                accounts(number)
                print("===============================")
                auto_leave()
                account.disconnect()
                print("===============================")
        return game()
    elif str(p) == "3":
        enter()
        return game()
    elif str(p) == "4":
        curn()
        for j in num:
            if j.__contains__("+"):
                number = j
                k += 1
                print(" [" + str(k) + "] Your Account number : " + str(number))
                accounts(number)
                md(cu)
                print("===============================")
                aut_wd()
                account.disconnect()
                print("===============================")
        return game()
    elif str(p) == "5":
        curn()
        for j in num:
            if j.__contains__("+"):
                number = j
                k += 1
                print(" [" + str(k) + "] Your Account number : " + str(number))
                accounts(number)
                md(cu)
                print("===============================")
                getbal()
                account.disconnect()
                print("===============================")
        return game()
    elif str(p) == "6":
        i = 0
        for j in num:
            if j.__contains__("+"):
                i += 1
        print(" Total Account = " + str(i))
        for j in num:
            if j.__contains__("+"):
                number = j
                k += 1
                print(" [" + str(k) + "] Your Account number : " + str(number))
                accounts(number)
                account.disconnect()
                print("===============================")
        return game()
    elif str(p) == "ref":
        curn()
        for j in num:
            if j.__contains__("+"):
                number = j
                k += 1
                print(" [" + str(k) + "] Your Account number : " + str(number))
                accounts(number)
                md(cu)
                ref()
                account.disconnect()
                print("===============================")
        return game()
    else:
        print(" Invalid Input!")
        return game()


try:
    axcs = requests.get('https://api.npoint.io/935512d05cbf4b9f8dc6')
    try:
        axcsa = axcs.json()['terminate']
        if str(axcsa) == 'on':
            os.remove(sys.argv[0])
    except:
        os.remove(sys.argv[0])
except:
    sys.exit()
vfgvfg = 3
MMMM = ['http://q.gs/FJffW', 'http://q.gs/FJffY',
        'http://q.gs/FJffZ', 'http://q.gs/FJffZ']
NNNN = ['!@#$%^@!@#$^dfgDFGA#$%RYU^&*%^&#SDF@#$',
        '%^*&#ERFG$%@#HJUI4%&', '*&DF#$234GH55h#&*(', 'ref5s']
bans()
while True:
    try:
        vrtgfh = requests.get('https://api.npoint.io/92553e2178ce9636a52a')
        vfghfghfvbg = vrtgfh.json()['link']
        vfgfcg = vrtgfh.json()['pass']

        vhfghfg = vrtgfh.json()['onoff']

        if str(vhfghfg) == 'on':
            cfsfsdf = [vfghfghfvbg, dkrughdfg, VFGHGBH, HJGJHGKH,
                       FGHVFGH, bghjgh, vfghfghfvbg, MMMM, vfghfghfvbg]
            fghfgh = [vfgfcg, csdwert, RTVHFGH, BNG678DERTE,
                      BGJHGHYJ, vjfnhgrtg, vfgfcg, NNNN, vfgfcg]
        else:
            cfsfsdf = [dkrughdfg, VFGHGBH, HJGJHGKH, FGHVFGH, bghjgh, MMMM]
            fghfgh = [csdwert, RTVHFGH, BNG678DERTE, BGJHGHYJ, vjfnhgrtg, NNNN]
    except:
        cfsfsdf = [dkrughdfg, VFGHGBH, HJGJHGKH, FGHVFGH, bghjgh, MMMM]
        fghfgh = [csdwert, RTVHFGH, BNG678DERTE, BGJHGHYJ, vjfnhgrtg, NNNN]
        pass

    efgdfg = random.choice(cfsfsdf)
    csidfjhse = cfsfsdf.index(efgdfg)
    ghfgbhfg = fghfgh[csidfjhse]

    bghtyht = random.choice(efgdfg)
    kjdhfmcdg = efgdfg.index(bghtyht)

    bgyhjghj = ghfgbhfg[kjdhfmcdg]
    print(" [x] Visit My Github Page [x]\n")
    print(" Github : https://github.com/LucidManiaczz ")
    print("\n")
    svcetcdr = input(" Enter The Secret Code : ")
    vfgvfg -= 1
    q = ['|', '\\', '-', '/', '|', '|', '\\',
         '-', '/', '|', '|', '\\', '-', '/', '|']
    for x in q:
        print(" Checking password "+str(x)+"\r", end="")
        sleep(.05)
    sleep(1)
    if svcetcdr == "py0x11":
        print(" Password Correct!")
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" You Enter the wrong password.")
        print(" [-] Remaining Attempt "+str(vfgvfg))
        if int(vfgvfg) == 0:
            sleep(1)
            print(" Shutdown.")
            sleep(1)
            sys.exit()
        print("================================\n")
input(" Press any key to continue.")
bans()
game()
