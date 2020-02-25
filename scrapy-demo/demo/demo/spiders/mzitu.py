import  scrapy
import re
import os
from items import PicItem
import base64
import time
import random
flag=0


class Mzitu_Spider(scrapy.Spider):
    name = 'mzitu'
    allowed_domains = 'mzitu.com'

    def start_requests(self):

        print('进入索引页https://www.mzitu.com/all/')
        yield scrapy.Request('https://www.mzitu.com/all/')

    def parse(self,response):
        print('获得索引页面，开始处理')
        if flag==1:print(response.text)
        select=re.findall('<a href="(.*?)" target="_blank">(.*?)</a>',response.text)
        print('获得相册连接')
        for i in select[1:]:
            time.sleep(random.choice(range(10,1000)))
            if flag==1:print(i[0])
            print("提交相册{}".format(i[0]))
            yield scrapy.Request(i[0],callback=self.get_page,dont_filter=True)


    def get_page(self,response):

        
        select=re.findall('上一组</span></a><span>(.*?)<span>下一页',response.text)[0]

        urls=[]
        for i in range(1,int(max(re.findall(r'/(\d+)\'',select)))+1):
            urls.append('{}/{}'.format(response.url,i))
        if flag==1:print(urls)


        select=re.findall(r'<div class="currentpath">当前位置: <a href=.*?">(.*?)</a> &raquo; <a href=".*?" rel="category tag">(.*?)</a> &raquo; (.*?)</div>',response.text)[0]
        a,b,c=select
        if flag==1:print(a,b,b)
        basedir='d:/a'
        subdir=os.path.join(a,b,c)
        path=os.path.join(basedir,subdir)
        if os.path.exists(path):
            return
        else:
            os.makedirs(path)


        yield scrapy.Request(urls[-1],  callback=self.get_pic_url, dont_filter=True,meta={'path':subdir})


    def get_pic_url(self,response):
        print('',re.findall(r'<img src="https://(.*?)/(.*?)/(.*?)/(.*?)(\d+).(.*?)" alt=',response.text)[0])
        a,b,c,d,e,f=re.findall(r'<img src="https://(.*?)/(.*?)/(.*?)/(.*?)(\d+)\.(.*?)" alt=',response.text)[0]
        urls=[]
        for i in range(1,int(e)+1):
            urls.append('https://{}/{}/{}/{}{}.{}'.format(a,b,c,d,str(i).rjust(len(e),'0'),f))
        path=response.meta['path']
        for i in urls:
            print(i)

        item=PicItem()
        item['image_urls']=urls
        item['image_path']=path
        yield item
