
import urllib.request
opener = urllib.request.build_opener()
response = opener.open("https://httpbin.org/get")
print(response.read())
print("")




import requests

response = requests.get("https://coinmarketcap.com/")
print(response.text)
