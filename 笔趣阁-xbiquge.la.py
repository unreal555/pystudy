#!/bin/py
#   -*-coding:utf-8-*-

import requests
from urllib import parse
import re
import time
import os
import random
import my_logger

def get_book(url):

    chapter_reg=r'''<dd><a href='(.*?)' >(.*?)</a></dd>'''
    title_reg=r'<script language="javascript" type="text/javascript">var bookid = ".*?"; var booktitle = "(.*?)";</script>'
    author_reg=r'<p>作&nbsp;&nbsp;&nbsp;&nbsp;者：(.*?)</p>'

    scheme,netloc,path,query,fragment=parse.urlsplit(url)
    print(scheme,netloc,path,query,fragment)

    response= requests.get(url)
    page=response.content.decode("utf-8")


    chapter_list=re.findall(chapter_reg,page)

    title=re.findall(title_reg,page)
    author=re.findall(author_reg,page)

    path=os.path.abspath(os.path.join(".",title[0]+"_"+author[0]))
    logger=my_logger.logger(dir=path)

    filename=title[0]+"_"+author[0]+".txt"



    print(title[0],author[0],chapter_list)


    if os.path.exists(path) and os.path.isdir(path):
        pass
    else:
        os.mkdir(path)

    for chapter in chapter_list:
        chapter_url,chapter_name=scheme+"://"+netloc+chapter[0],chapter[1]
        print (chapter_url)
        if logger.check(chapter_name)==True:
            print('{}已下载,跳过'.format(chapter))
            continue

        response= requests.get(chapter_url)
        page =response.content.decode("utf-8")
        reg=r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'
        result=re.findall(reg,page)
        text=chapter_name+"\r\n"+"\r\n"

        flag=0
        print(result)
        for hang in result:
            text=text+"\t"+hang+"\r\n"


        text+="\r\n"+"\r\n"
        # with open(os.path.join(path,chapter_name+".txt"),"w",encoding="utf-8") as f1:
        #     f1.write(text)
        with open(os.path.join(path,filename),"a",encoding="utf-8") as f2:
            f2.write(text)

        logger.write(chapter)

        s=random.randint(1,3)

        print("停止{}秒".format(s))
        time.sleep(s)



get_book('http://www.xbiquge.la/21/21488/')



