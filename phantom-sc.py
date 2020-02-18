#!/usr/bin/env python3
#scraping develop inc phantomJS Cloud & BeautifulSoup

import json
import urllib.parse
import requests
from bs4 import BeautifulSoup

URL =  'https://www.jalan.net/uw/uwp3200/uww3201init.do?yadNo=357202&planCd=02420090&roomTypeCd=0392936'

payload = {'url':URL,'renderType':'HTML','outputAsJson':'true'}
payload = json.dumps(payload) #JSONパース
payload = urllib.parse.quote(payload,safe = '') #URIエンコード

key = '**-*****-*****-*****-*****-*****'
url = "https://phantomjscloud.com/api/browser/v2/"+ key+"/?request=" + payload

response = requests.get(url) #GETリクエスト

responseDict = response.json()
html = responseDict["content"]["data"];
soup = BeautifulSoup(html, "lxml")
title_text = soup.find('title').get_text()
print(title_text)
