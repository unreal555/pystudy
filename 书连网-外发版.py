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

'''
账号13177551358
密码zxc123456
爬取小说
http://vip.shulink.com/files/article/info/68/68033.htm
http://vip.shulink.com/files/article/info/69/69330.htm
两个'''

domain = 'http://vip.shulink.com/'

# chapurl = 'http://vip.shulink.com/files/article/html/68/68033/index.html'
chapurl = 'http://vip.shulink.com/html/69/69330/indexasc.html2'

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
headers[
    'Cookie'] = '''PHPSESSID=fo8fjmqeaph67sq651rtfdro8h; jieqiUserInfo=jieqiUserId%3D379396%2CjieqiUserUname%3D%B6%AB%C4%DE%2CjieqiUserName%3D%26%23x4E1C%3B%26%23x9713%3B%2CjieqiUserGroup%3D3%2CjieqiUserGroupName%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserVip%3D1%2CjieqiUserHonorId%3D5%2CjieqiUserHonor%3D%26%23x65E0%3B%26%23x53CC%3B%26%23x9690%3B%26%23x58EB%3B%2CjieqiUserToken%3Ddc9d608a620ec41e3ceb6645d3c886cb%2CjieqiCodeLogin%3D0%2CjieqiCodePost%3D0%2CjieqiUserPassword%3Ddd9afc93112397f0cf6b597453bb6b8e%2CjieqiUserAccount%3D%26%23x4E1C%3B%26%23x9713%3B%2CjieqiUserLogin%3D1592737763; jieqiVisitInfo=jieqiUserLogin%3D1592737763%2CjieqiUserId%3D379396; jieqiVisitId=article_articleviews%3D68033%7C69330; jieqiRecentRead=68033.5036865.1.1592739461.379396'''

def get_chapter_list(s):
    temp=qu_kong_ge(s)
    temp = re.findall('<dlclass="index"(.*?)</dl>', temp, re.S)[0]
    chapter_list = re.findall('href="(.*?)"title=.*?>(.*?)</a>',temp, re.S)
    print(chapter_list)
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
print(response)
title=get_title(response)
filepath='./'+title+'.txt'
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
        f.write(chapter_name)
        f.write('\r\n\r\n')

    result = requests.get(url, headers=headers).content.decode('gbk')
    print(result)

    result = qu_kong_ge(result)



    result = re.findall('<divid="acontent"class="acontent">(.*?</div>)', result, re.S)[0]

    result=result.replace('</div>','<br/><br/>')

    print(result)

    result = re.findall('[&emsp;]*(.*?)<br/>', result, re.S)

    print(result)

    for i in result:
        print(i)
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write('\t' + i + '\r\n')

    with open(filepath, 'a', encoding='utf-8') as f:
        f.write('\r\n')
        f.flush()
    random_wait()
