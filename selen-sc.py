#!/usr/bin/env python3
#scraping develop inc Selenium & BeautifulSoup
#指定URLに遷移し、そこからページ間移動しないTips.

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary  # webdriverパスを通すためのコード
import time
import csv
import os #csvの出力先path設定で使用

# ブラウザのオプションを格納する変数設定
options = Options()

# Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


def GetData(url):
    driver.get(url)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find('title').get_text()
    reserved = soup.select_one('.jlnpc-yado__notify--inn-reserved').get_text()
    print(title + '\n' + reserved)

    #csv export
    body = [title, reserved]
    output_dir=os.path.dirname(os.path.abspath(__file__))
    file_name = "out.csv"
    output_file = os.path.join(output_dir, file_name)
    with open(output_file, mode='a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(body)

urls = [
    'https://www.jalan.net/uw/uwp3200/uww3201init.do?yadNo=357202&planCd=02420090&roomTypeCd=0392936',
    'https://www.jalan.net/uw/uwp3200/uww3201init.do?yadNo=322203&planCd=00115329&roomTypeCd=0024643'
]
for url in urls:
    GetData(url)
