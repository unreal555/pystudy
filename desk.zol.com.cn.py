#!/bin/py
#  -*-conding:utf-8-*-
import re
import os
from urllib import request
from bs4 import BeautifulSoup
import time


def getAlumLink(url):
    print(url)
    response = request.urlopen(url)
    page = response.read()
    soup = BeautifulSoup(page, 'html.parser', from_encoding='gbk')
    list = []
    for i in soup.find_all('li', class_="photo-list-padding"):
        link = 'http://desk.zol.com.cn%s' % i.find_all('a')[0]['href']
        title = i.find_all('img')[0]['alt']
        temp = {'title': title, 'link': link}
        list.append(temp)
    return list

def getPicLink(url):
    response = request.urlopen(url)
    page = response.read().decode('gbk')
    reg=r'<a href="(.*?)">.*?width="144" height="90"'
    temp= re.findall(reg,page,re.S)

    reg=r'<a target="_blank" id=".*?" href="(.*?)">.*?</a>'
    imgUrl = []
    for i in temp:
        if i=='/':
            imgUrl.append(url)
            print('____')
            continue
        imgUrl.append('http://desk.zol.com.cn%s' % i)

    return imgUrl
for count in range(1,5):
    for i in getAlumLink('http://desk.zol.com.cn/chemo/%s.html'% count):
         try:
            os.mkdir(i['title'])
         except:
             break
         n=1
         for j in getPicLink(i['link']):
               respones=request.urlopen(j)
               page=respones.read().decode('gbk')
               reg=r'<a target="_blank" id=".*?" href="(.*?)">.*?</a>'
               temp= 'http://desk.zol.com.cn%s' % (re.findall(reg,page))[0]
               print(temp)
               response=request.urlopen(temp)
               page=response.read().decode('gbk')

               reg='src="(.*?)"'
               link=re.findall(reg,page)[0]
               print(link)

               try:
                   time.sleep(1)
                   img=request.urlopen(link).read()
               except:
                   pass

               with open('%s\\%s.jpg'%(i['title'],n),'wb') as f:
                   f.write(img)
                   n+=1

