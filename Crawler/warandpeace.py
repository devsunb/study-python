from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(), "html.parser")
# nameList = bsObj.findAll("span", {"class": "green"})
# nameList = bsObj.findAll("span", class_="green")
nameList = bsObj.findAll("span", {"class": "green", "class": "red"})

for name in nameList:
    print(name.get_text())
