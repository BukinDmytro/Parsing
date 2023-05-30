import random
import telebot
from telebot import types #for buttons

f = open("facts.txt" , "r" , encoding = "UTF-8")
facts = f.read().split('\n')
f.close()
f = open("thinks.txt" , "r" , encoding = "UTF-8")
thinks = f.read().split('\n')
f.close()
bot = telebot.TeleBot("5676024972:AAGT6X02rO8UcZLrD_hYDu8-SUgswx2ET4A")
@bot.message_handler(commands = ['start'])

def start(m , res = False):
    #adding two buttons

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Факт")
    item2 = types.KeyboardButton("Приказка")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id , "Натисни одну із кнопок" , reply_markup = markup)

@bot.message_handler(content_types = ["text"])
def handler_text(message):
    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
    elif message.text.strip() == 'Приказка':
        answer = random.choice(thinks)
    bot.send_message(message.chat.id , answer)
bot.polling()
