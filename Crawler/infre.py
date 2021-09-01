from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://infre.kr/")
bsObj = BeautifulSoup(html, "html.parser")
titles = bsObj.findAll("title")
for title in titles:
    print(title)