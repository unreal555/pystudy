#!/bin/py
#   -*-coding:utf-8-*-

import requests
from urllib import parse
import re
import time
import os
import random

URL=r'http://www.022003.com/57_57619/'#http://www.vipxs.la/
scheme,netloc,path,query,fragment=parse.urlsplit(URL)
print(parse.urlsplit(URL))
response= requests.get(URL)
page=response.content.decode("utf-8")
chapter_reg=r'<dd><a href="(.*/?)">(.*?)</a></dd>'
title_reg=r'<script language="javascript" type="text/javascript">var bookid = ".*?"; var booktitle = "(.*?)";</script>'
author_reg=r'<p>作&nbsp;&nbsp;&nbsp;&nbsp;者：(.*?)</p>'

chapter_list=re.findall(chapter_reg,page)
title=re.findall(title_reg,page)
author=re.findall(author_reg,page)
path=os.path.join(".",title[0]+"_"+author[0])
filename=title[0]+"_"+author[0]+".txt"
print(title[0],author[0])


if os.path.exists(path) and os.path.isdir(path):
    for f in os.listdir(path):
        os.remove(os.path.join(path,f))
else:
    os.mkdir(path)

for chapter in chapter_list:
    chapter_url,chapter_name=scheme+"://"+netloc+chapter[0],chapter[1]
    print (chapter_url)

    response= requests.get(chapter_url)
    page =response.content.decode("utf-8")
    reg=r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'
    result=re.findall(reg,page)
    text=chapter_name+"\r\n"+"\r\n"
    # text+="\t"
    flag=0
    print(result)
    for hang in result:
        text=text+"\t"+hang+"\r\n"
        text=text+"\r"
    # for hang in result:
    #     if hang!="……" and flag==0:
    #         text=text+hang
    #         continue
    #     if hang=="……"  and flag==0:
    #         flag+=1
    #         continue
    #     if hang=="……"  and flag==1:
    #         text=text+"\r\n"
    #         text=text+"\t"
    #         flag=0
    #         continue
    #     if hang!="……" and flag==1:
    #         text=text+"\r\n"
    #         text=text+"\t"+'……'
    #         flag=0
    #         continue
    text+="\r\n"+"\r\n"
    with open(os.path.join(path,chapter_name+".txt"),"w",encoding="utf-8") as f1:
        f1.write(text)
    with open(os.path.join(path,filename),"a",encoding="utf-8") as f2:
        f2.write(text)

    s=random.randint(1,3)
    print("停止{}秒".format(s))
    time.sleep(s)






