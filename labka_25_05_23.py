#1
'''
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.example.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.content , "html.parser")
    title = soup.find("title").text
    print(title)
else:
    print("No connection",response.status_code)
'''
#2

import requests
from bs4 import BeautifulSoup

response = requests.get("https://uk.wikipedia.org/")
if response.status_code == 200:
    soup = BeautifulSoup(response.content , "html.parser")
    img = soup.find_all("img") #словник
    for i in img:
        print("https://" + i["src"])

    with open("file.txt" , "w") as file:
        file.write(str(i))