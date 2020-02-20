#!/bin/py
#   -*-coding:utf-8-*-
import requests
from lxml import etree

response = requests.get("http://www.lagou.com")
response.encoding = ('utf-8')
root = etree.HTML(response.content)
list = []
for i in root.xpath('//*[@class="category-list"]/*'):
    url = i.xpath("@href")
    if url != []:
        list.append({"work": i.text, "url": url})
for i in list:
    print(i)
