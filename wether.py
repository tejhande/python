import requests
from bs4 import BeautifulSoup

search = "weather in jalna"
url=search
r = requests.get(url)

s = BeautifulSoup(r.text,"html.parser")

update = s.find("dl",class_="BNeawe")

print(update.text)