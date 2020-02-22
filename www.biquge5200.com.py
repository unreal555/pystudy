#*/bin/python
#  -*-coding:utf-8-*-
____author____='zl'

import 学习requests
import re
import pymysql

conn = pymysql.connect(
    host='192.168.1.240',
    port=3306,
    user='zl',
    password='594188',
    charset='utf8'                   #不是utf-8
)

cursor=conn.cursor()

def getNovelList():
    response=学习requests.get('http://www.biquge5200.com/xiaoshuodaquan/')
    page=response.text
    reg=r'<li><a href="(.*?)">.*?</a></li>'
    novelList=re.findall(reg,page)
    return novelList

def getInfo(url):
    response=学习requests.get(url)
    page=response.text
    reg = r'<meta property="og:novel:book_name" content="(.*?)"/>'
    novelName=re.findall(reg,page)[0]
    reg=r'<meta property="og:novel:category" content="(.*?)"/>'
    novelCaregory=re.findall(reg,page)[0]
    reg=r'<meta property="og:description" content="(.*?)"/>'
    novelDesc=re.findall(reg,page)[0]
    reg=r'<meta property="og:novel:author" content="(.*?)"/>'
    novelAuthor=re.findall(reg,page)[0]
    reg=r'<dd><a href="(.*?)">(.*?)</a></dd>'
    chapterList=re.findall(reg,page)
    return novelName,novelCaregory,novelDesc,novelAuthor,chapterList
n=1
for novelUrl in getNovelList():
   if(n<10):
       n=n+1
       print(n,novelUrl)
   else:
       print(novelUrl)
       novelName, novelCaregory, novelDesc, novelAuthor, chapterList = getInfo(novelUrl)

       print (novelName,novelCaregory,novelDesc,novelAuthor,chapterList)


       for charterUrl,novelName in chapterList:
           response=学习requests.get(charterUrl)
           page=response.text
           reg='<div id="content">(.*?)</div>'
           chapterContent=re.findall(reg,page,re.S)
           print(chapterContent)
           break



       break


conn.close()
