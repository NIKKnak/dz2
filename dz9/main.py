
import requests
import telebot
from random import randint
from random import choice

bot = telebot.TeleBot("5844080573:AAHSieG0eid-fLZ8bylvMgUF0qJXFHaW-gE")
candys = dict()
enable_game = dict()
turn = dict()

# 
@bot.message_handler(commands=['usd'])
def send_welcome(message):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    for i in res.values():
    #     print(i)
        print(res['Valute']["USD"]['Name'], res['Valute']["USD"]['Value'])
    bot.reply_to(message, res['Valute']["USD"]['Name'])




@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Добро пожаловать в нашу игру!!\nБерите конфет сколько хотите, и не более 28\n"
                          "но помните, кто последний, тот и победил!!!")

def handle_game_proc(message):
    global enable_game
    try:
        if enable_game[message.chat.id] and 1 <= int(message.text) <= 28:
            return True\
                
        else:
            return False
    except KeyError:
        enable_game[message.chat.id] = False
        if enable_game[message.chat.id] and 1 <= int(message.text) <= 28:
            return True
        else:
            return False


@bot.message_handler(commands=['start'])
def send_welcome(message):
    global turn, candys, enable_game
    bot.reply_to(message, "Let's go")
    candys[message.chat.id] = 117
    turn[message.chat.id] = choice(['Bot', 'User'])
    bot.send_message(message.chat.id, f'Начинает {turn[message.chat.id]}')
    enable_game[message.chat.id] = True
    if turn[message.chat.id] == 'Bot':
        take = randint(1, candys[message.chat.id] % 29)
        candys[message.chat.id] -= take
        bot.send_message(message.chat.id, f'Бот взял {take}')
        bot.send_message(message.chat.id,
                         f'Осталось {candys[message.chat.id]}')
        turn[message.chat.id] = 'User'


@bot.message_handler(func=handle_game_proc)
def game_process(message):
    global candys, turn, enable_game
    if turn[message.chat.id] == 'User':
        if candys[message.chat.id] > 28:
            candys[message.chat.id] -= int(message.text)
            bot.send_message(message.chat.id,
                             f'Осталось {candys[message.chat.id]}')
            if candys[message.chat.id] > 28:
                take = randint(1, candys[message.chat.id] % 29)
                candys[message.chat.id] -= take
                bot.send_message(message.chat.id,
                                 f'Бот взял {take}')
                bot.send_message(message.chat.id,
                                 f'Осталось {candys[message.chat.id]}')
                if candys[message.chat.id] <= 28:
                    bot.send_message(message.chat.id, 'User Win')
                    enable_game[message.chat.id] = False
            else:
                bot.send_message(message.chat.id, 'Bot Win')
                enable_game[message.chat.id] = False
        else:
            bot.send_message(message.chat.id, 'Bot Win')
            enable_game[message.chat.id] = False


bot.infinity_polling()