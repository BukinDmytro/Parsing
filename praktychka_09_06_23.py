import requests
from bs4 import BeautifulSoup
import random
import telebot
from telebot import types
bot = telebot.TeleBot("6272305334:AAGd6szstDkWa3795wh8fdaCwI6a5yNSCSE")
response = requests.get("https://minfin.com.ua/ua/currency/nbu/")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    usdeurpln = soup.find_all('div', {"class": "sc-1x32wa2-9 fevpFL"})
    elem1 = usdeurpln[2]
    print(elem1.text)
    elem2 = usdeurpln[3]
    print(elem2.text)
    elem3 = usdeurpln[4]
    print(elem3.text)

@bot.message_handler(commands = ['start'])
def start(m , res = False):
    #adding three buttons

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Долари")
    item2 = types.KeyboardButton("Євро")
    item3 = types.KeyboardButton("Злоті")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(m.chat.id , "Натисни одну із кнопок" , reply_markup = markup)

@bot.message_handler(content_types = ["text"])
def handler_text(message):
    if message.text.strip() == 'Долари':
        answer = elem1
    elif message.text.strip() == 'Євро':
        answer = elem2
    elif message.text.strip() == 'Злоті':
        answer = elem3
    bot.send_message(message.chat.id , answer)
bot.polling()