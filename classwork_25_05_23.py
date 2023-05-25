'''
import urllib.request
opener = urllib.request.build_opener()
response = opener.open("https://httpbin.org/get")
print(response.read())
print("")
'''


import requests

response = requests.get("https://coinmarketcap.com/")
'''print(response.text)

response_parse = response.text.split('<span>')

for parse_elem in response_parse:
    if parse_elem.startswith("$"):
        print(parse_elem)
'''

from bs4 import BeautifulSoup
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features= "html.parser")
    soup_list = soup.find_all('a', {'href': "/currencies/bitcoin/markets/"})
    res = soup_list[0].find('span')
    print(res.text)