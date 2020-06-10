#!/bin/py
# -*-coding:utf-8-*-
import requests
import re
import os
import requests
import re
import mytools
import os
import random
from time import sleep



domain = 'http://vip.shulink.com/'
chapurl = 'http://vip.shulink.com/files/article/html/139/139548/index.html'

headers = {}
headers['Accept-Encoding'] = 'gzip, deflate'
headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
headers['Accept-Language'] = 'zh-CN,zh;q=0.9'
headers['Cache-Control'] = 'no-cache'
headers['Connection'] = 'Keep-Alive'
headers['Host'] = 'vip.shulink.com'
headers['Pragma'] = 'no-cache'
headers['Referer'] = 'http://vip.shulink.com/files/article/html/139/139522/index.html'
headers['Upgrade-Insecure-Requests'] = '1'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'


def get_chapter_list(s):
    temp = re.findall('<dl class="index"(.*?)</dl>', s, re.S)[0]
    chapter_list = re.findall('href="(.*?)" title=.*?>(.*?)</a>',temp, re.S)
    return chapter_list

def get_title(s):
    return qu_te_shu_zi_fu(re.findall('<title>(.*?)</title>', s)[0])

def create_file(filepath):
    if os.path.exists(filepath):
        pass
    else:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(title)
            f.write('\r\n\r\n')

def qu_te_shu_zi_fu(s):
    if isinstance(s, str):
        return re.sub('[\/:*?"<>|]','-',s)
    else:
        print('给字符串')
        return 0
    
def random_wait(n=1,m=3,*args):
    if not (isinstance(n, (int, float)) and isinstance(m, (int, float))):
        print('参数输入错误，不是整数或小数，采用默认值1，3')
        n=1
        m=3

    if n>m:
        n,m=m,n
    temp = random.uniform(n, m)
    print("wait {} second".format(temp))
    sleep(temp)


def qu_kong_ge(s):
    if isinstance(s, str):
        return re.sub('\s+', '', s)
    else:
        print('老兄，给字符串')
        return 0



response = requests.get(chapurl, headers=headers).content.decode('gbk')

title=get_title(response)
filepath='./'+title
chapter_list=get_chapter_list(response)
create_file(filepath)

with open(filepath, 'r', encoding='utf-8') as f:
    now = f.read()

for chapter_url,chapter_name in chapter_list:

    if chapter_name in now:
        print(chapter_name + '已下载')
        continue

    url = domain + chapter_url

    print(url, chapter_name)

    with open(filepath, 'a', encoding='utf-8') as f:
        f.write('\t' + chapter_name)
        f.write('\r\n\r\n')

    result = requests.get(url, headers=headers).content.decode('gbk')

    result = qu_kong_ge(result)

    result = re.findall('<divid="acontent"class="acontent">(.*?)</div>', result, re.S)

    result = re.findall('&emsp;&emsp;(.*?)<br/><br/>', result[0], re.S)

    for i in result:
        print(i)
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write('\t' + i + '\r\n\r\n')

    with open(filepath, 'a', encoding='utf-8') as f:
        f.write('\r\n\r\n')
        f.flush()
    random_wait()
