import re
import requests
import mytools
import  os
import random
from time import sleep
import re
import sys
import os
import time


from zhon.hanzi import punctuation as ZHONG_WEN_BIAO_DIAN

from string import punctuation as YING_WEN_BIAO_DIAN

from string import ascii_lowercase as XIAO_XIE_ZI_MU

from string import ascii_uppercase as DA_XIE_ZI_MU

from string import digits as SHU_ZI

domain='http://www.ting89.com'
url='http://www.ting89.com/books/15633.html'

response=requests.get(url)
page=mytools.qu_kong_ge(response.content.decode('gbk'))

bookname=re.findall('<title>(.*?)</title>',page)[0]

print(bookname)

if os.path.exists(bookname):
    pass
else:
    os.makedirs(bookname)

all=re.findall('''<li><ahref='(.*?)'target="_blank">(.*?)</a></li>''',page)

count=0
for i in all:
    if count<30:
        print(domain+i[0])
        chapter=domain+i[0]
        response=requests.get(chapter)
        page=response.content.decode('gbk')
        page=mytools.qu_kong_ge(page)
        down=re.findall(r'''下载保存时请自行重命名</div><iframesrc="http://play.ting89.com/down/down.php\?url=(.*?)"height''',page)

        response=requests.get(down[0])
        with open('./{}/{}'.format(bookname,down[0].split('/')[-1]),'wb') as f:
            f.write(response.content)
    else:
        break