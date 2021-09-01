#! /Users/jaeseoklee/Documents/Programming/Scraping/scraping/bin/python3

from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
import re

html = urlopen("https://en.wikipedia.org/wiki/C_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", {"href":re.compile("^(/wiki/)(?!:)*$")}):
    if 'href' in link.attrs:
        print(link.attrs['href']);
