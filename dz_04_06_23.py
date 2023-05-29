#1

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.example.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.content , "html.parser")
    h2 = soup.find_all("h2").text
    print(h2)
else:
    print("No connection or no h2")

#2

import requests
from bs4 import BeautifulSoup

response = requests.get("https://uk.wikipedia.org/")
if response.status_code == 200:
    soup = BeautifulSoup(response.content , "html.parser")
    tablee = soup.find_all("table")
    for i in tablee:
        print(i)

#3

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.example.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.content , "html.parser")
    elements = soup.find_all({"class": "example-class"})
    if elements:
        elements_name = elements.text.strip()
        print(elements_name)
    else:
        print("Таких елементів немає на сторінці")

#4


import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.example.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.content , "html.parser")
    h1 = soup.find_all("h1").text
    print(h1)
else:
    print("No connection or no h1")
