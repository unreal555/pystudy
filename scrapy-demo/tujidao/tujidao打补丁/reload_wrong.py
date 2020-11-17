#!/bin/py
#   -*-coding:utf-8-*-
import re, os
import mytools
import requests

basedir = r'e:\a\full'

headers = {}
headers['host'] = 'img.hywly.com'
headers['DNT'] = '1'
headers['Accept'] = 'text/html, application/xhtml+xml, */*'
headers['Accept-Language'] = 'zh-CN'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
headers['Accept-Encoding'] = 'gzip, deflate'
headers['Connection'] = 'Keep-Alive'
headers['Cache-Control'] = 'no-cache'

print(headers)
with open(r'e:\a\tujidao\wrong.txt', 'r', encoding='utf-8') as f:
    lines = f.read()

for item in re.findall('######(.*?)######', mytools.qu_kong_ge(lines)):
    for num in range(0, 120):
        if not os.path.exists(os.path.join(basedir, item)):
            os.makedirs(os.path.join(basedir, item))

        url = 'https://img.hywly.com/a/1/{}/{}.jpg'.format(item, num)
        filename = url.split('{}/'.format(item))[1]
        pic = requests.get(url, headers=headers)
        if pic.status_code == 200:
            with open(os.path.join(basedir, item, filename), 'wb') as fp:
                fp.write(pic.content)
                fp.close()
                mytools.random_wait(1)
