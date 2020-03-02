import scrapy
from items import DemoItem
import os
import time
import re
import requests
import random

item = DemoItem()
debug=0


domain='http://www.skwen.me'

class Skwen_Spider(scrapy.Spider):
    name='skwen'
    allowed_domains = ["skwen.me"]
    start_urls=['http://www.skwen.me/13/13434/',
                ]

    def parse(self, response):
        u=response.url[:-1]
        if debug:print(response.url,response.status)
        reg='''<li><a href="/(.*?)/(.*?)/(.*?).html">(.*?)</a></li>|<li><a href="javascript:readbook\((.*?),(.*?),(.*?)\);">(.*?)</a></li>'''
        result=flag=re.findall(reg,response.text)

        retry=3
        for i in range(2,10000):
            t='{}_{}/'.format(u,i)
            if debug:print(t)
            page=requests.get(t)
            if page.status_code==200:
                page=page.content.decode('gbk')
                if debug:print(page)
                thistime_result=re.findall(reg,page)
                if thistime_result==flag:
                    break
                else:
                    flag=thistime_result
                    for i in thistime_result:
                        result.append(i)
                    time.sleep(1)

        urls = [[],[],[]]   #章节名，小说编码，章节编码
        url = []
        for i in result:
            for j in i:
                if j == '':
                    if debug:print('丢空格')
                    continue

                else:
                    if debug:print('拼接')
                    url.append(j)

            if debug:print('判断',url[3],urls[0])
            if url[3].replace(' ','') not in urls[0]:
                if debug:print('增加url')

                urls[0].append(url[3].replace(' ',''))
                urls[1].append('/{}/{}/'.format(url[0],url[1]))
                urls[2].append(url[2])
            url=[]
        if debug:print(urls)
        for i in range(0,len(urls[0])):
            if debug:print(urls[0][i],urls[1][i],urls[2][i],)


        for i in range(0,len(urls[0])):
            print('asfsdasdfasdfasdfadfasdf=',i)
            print('{}{}{}.html'.format(domain,urls[1][i],urls[2][i]))
            page=requests.get('{}{}{}.html'.format(domain,urls[1][i],urls[2][i]))
            page=page.content.decode('gbk')
            title = re.findall('<h1 class="page-title">(.*?)</h1>', page)

            if debug:print(page)
            if title==[]:
                time.sleep(10)
                continue
            else:
                title=title[0].replace(' ','')
                zhunque=urls[0].index(title)
                urls[2][zhunque]=urls[2][i]
                ponit=i
                break

        novel={}
        for i in range(0,len(urls[0])):
            novel[i]=['{}'.format(urls[0][i]),[]]


        def get_page(url):
            page=requests.get(url)
            page=page.content.decode('gbk')
            print(page)
            result=re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br /><br /></p></div><div><p>',page)
            print(result)


        get_page('http://www.skwen.me/13/13577/185654.html')




