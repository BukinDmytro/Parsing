import telebot
bot = telebot.TeleBot("5676024972:AAGT6X02rO8UcZLrD_hYDu8-SUgswx2ET4A")
@bot.message_handler(commands = ['start'])

def start_message(message):
    bot.send_message(message.chat.id,"Дароу кєнт 🤙")
@bot.message_handler(content_types = ["text"])
def handler_text(message):
    bot.send_message(message.chat.id , "Ти писав " + message.text + " ,але ти всеодно гей")
bot.polling()