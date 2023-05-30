import requests
from bs4 import BeautifulSoup
import random
import telebot
from telebot import types

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