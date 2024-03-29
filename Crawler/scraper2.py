from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import re

pages = set()


def getLinks(pageUrl):
    global pages
    try:
        html = urlopen("http://en.wikipedia.org" + pageUrl)
    except HTTPError as e:
        return None
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", {"href": re.compile("^(/wiki/)((?!:).)*$")}):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")
