#!/bin/py
# -*-coding:utf-8-*-
import requests
import re
import mytools
import os

headers = {}

domain = 'http://vip.shulink.com/'

headers['Accept-Encoding'] = 'gzip, deflate'
headers[
    'Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
headers['Accept-Language'] = 'zh-CN,zh;q=0.9'
headers['Cache-Control'] = 'no-cache'
headers['Connection'] = 'Keep-Alive'
headers['Host'] = 'vip.shulink.com'
headers['Pragma'] = 'no-cache'
headers['Referer'] = 'http://vip.shulink.com/files/article/html/139/139522/index.html'
headers['Upgrade-Insecure-Requests'] = '1'
headers[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
headers[
    'Cookie'] = '''PHPSESSID=kt6ivbputhckcch8cu239gte4g; jieqiUserInfo=jieqiUserId%3D369080%2CjieqiUserUname%3D%B6%AB%BC%D2%D6%D6%CA%F7%2A369080%2CjieqiUserName%3D%26%23x4E1C%3B%26%23x5BB6%3B%26%23x79CD%3B%26%23x6811%3B%26%23x002A%3B%26%23x0033%3B%26%23x0036%3B%26%23x0039%3B%26%23x0030%3B%26%23x0038%3B%26%23x0030%3B%2CjieqiUserGroup%3D3%2CjieqiUserGroupName%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserVip%3D1%2CjieqiUserHonorId%3D6%2CjieqiUserHonor%3D%26%23x4E16%3B%26%23x5916%3B%26%23x9AD8%3B%26%23x4EBA%3B%2CjieqiUserToken%3D91b313368769da4bdb9979a68b0c765b%2CjieqiCodeLogin%3D0%2CjieqiCodePost%3D0%2CjieqiUserAccount%3D%26%23x4E1C%3B%26%23x5BB6%3B%26%23x79CD%3B%26%23x6811%3B%26%23x002A%3B%26%23x0033%3B%26%23x0036%3B%26%23x0039%3B%26%23x0030%3B%26%23x0038%3B%26%23x0030%3B%2CjieqiUserLogin%3D1590120689; jieqiVisitInfo=jieqiUserLogin%3D1590120689%2CjieqiUserId%3D369080; '''
chapurl = 'http://vip.shulink.com/files/article/html/139/139522/index.html'

response = requests.get(chapurl, headers=headers).content.decode('gbk')

response = re.findall('<dl class="index">(.*?)</dl>', response, re.S)

chap_list = re.findall('<a href="(.*?)" title=.*?>(.*?)</a>', response[0], re.S)

print(chap_list)

if os.path.exists('./all.txt'):
    pass
else:
    with open('./all.txt', 'a', encoding='utf-8') as f:
        f.write('梦落千年爱上你')
        f.write('\r\n\r\n')

with open('./all.txt', 'r', encoding='utf-8') as f:
    now = f.read()
for i in chap_list:

    if i[1] in now:
        print(i[1] + '已下载')
        continue

    url = domain + i[0]

    print(url, i[1])

    with open('./all.txt', 'a', encoding='utf-8') as f:
        f.write('\t' + i[1])
        f.write('\r\n\r\n')

    result = requests.get(url, headers=headers).content.decode('gbk')

    result = mytools.qu_kong_ge(result)

    result = re.findall('<divid="acontent"class="acontent">(.*?)</div>', result, re.S)

    result = re.findall('&emsp;&emsp;(.*?)<br/><br/>', result[0], re.S)

    for i in result:
        print(i)
        with open('./all.txt', 'a', encoding='utf-8') as f:
            f.write('\t' + i + '\r\n\r\n')
    with open('./all.txt', 'a', encoding='utf-8') as f:
        f.write('\r\n\r\n')
        f.flush()
    mytools.random_wait()
