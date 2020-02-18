#!/usr/bin/env python3
#scraping develop basic sample

import requests
from bs4 import BeautifulSoup

def GetData(url):
    siteURL = requests.get(url)
    soup = BeautifulSoup(siteURL.content,"lxml")
    texts = soup.find('title').get_text()
    print(texts)


urls = [
    "https://yukai-r.jp",
    "https://www.ooedoonsen.jp",
    "https://www.hoshinoresorts.com/",
]
for url in urls:
    GetData(url)
