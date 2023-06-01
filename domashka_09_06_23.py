import requests
import wikipedia
from bs4 import BeautifulSoup
import random
import telebot
from telebot import types
bot = telebot.TeleBot("6003048631:AAHv61_F4QA8cN_oVTw2SRlvWNljQC2TXI4")


result = wikipedia.search(input("Введіть свій запит на англійській мові:"))

for search in result:
    print(search)
    print(wikipedia.page(search).summary)

if len(wikipedia.page(search).summary) < 1000:
    print("Була знайдена стаття на менш ніж 1000 символів або ж не була знайдена взагалі (")
else:
    print(wikipedia.page(search).summary)

