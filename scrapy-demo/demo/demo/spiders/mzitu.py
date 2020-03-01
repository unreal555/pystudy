import  scrapy
import re
import os
import sys
import time
sys.path.append(r'D:\\pycharm-professional-2017.2.4\\pystudy\\scrapy-demo\\demo\\demo')
from items import PicItem
from settings import IMAGES_STORE

print(sys.path)
flag=0


class Mzitu_Spider(scrapy.Spider):
    name = 'mzitu'
    allowed_domains = 'mzitu.com'

    path=os.path.join(IMAGES_STORE,name)
    log_name='log.txt'

    if not os.path.exists(path):
        os.makedirs(os.path.join(path))

    def start_requests(self):

        print('进入索引页https://www.mzitu.com/all/')
        # yield scrapy.Request('https://www.mzitu.com/all/')
        yield scrapy.Request('https://www.mzitu.com/old/')

    def parse(self,response):

        print('获得索引页面，开始处理')
        if flag==1:print(response.text)
        select=re.findall('<a href="(https://www.mzitu.com/\d+)" target="_blank">(.*?)</a>',response.text)
        print('获得相册连接')
        print(len(select))


        if not os.path.exists(os.path.join(self.path,self.log_name)):
            with open(os.path.join(self.path,self.log_name),'a',encoding='utf-8') as f:
                count=0
                for i in select:
                    print("写入log文件{}{}".format(i[0],i[1]))
                    f.write('{}'.format('\t' + str(i[0]) + '\t' + str(i[1]) + '\r\n'))
                    count=count+1
                    print("提交相册连接{}{}".format(i[0],i[1]))
                    yield scrapy.Request(i[0], callback=self.get_page, dont_filter=True)
                print('共提交 {}  个相册'.format(count))
        else:
            with open(os.path.join(self.path,self.log_name), 'r', encoding='utf-8') as f:
                log=f.read()
            count=0
            with open(os.path.join(self.path, self.log_name), 'a', encoding='utf-8') as f:
                f.write(time.strftime('%Y-%m-%d %H-%M') + '\r\n')
            for i in select:
                if i[0] not in log:
                    with open(os.path.join(self.path,self.log_name), 'a', encoding='utf-8') as f:
                        print("写入log，新增相册{}{}".format(i[0],i[1]))
                        f.write('{}'.format('\t' + str(i[0]) + '\t' + str(i[1]) + '\r\n'))
                        count = count + 1
                        print('提交新增加相册{}{}'.format(i[0],i[1]))
                        yield scrapy.Request(i[0], callback=self.get_page, dont_filter=True)
            print('增量提交 {}  个相册'.format(count))



    def get_page(self,response):
        select=re.findall('''<a href='{}/(\d+)'>'''.format(response.url),response.text)#搜索相册中所有的图片页面编号
        print(select)
        for i in range(0,len(select)):      #讲页面编号由字符串转成整数
            select[i]=int(select[i])
        print(select)

        urls=[]
        for i in range(1,max(select)+1,1):
            urls.append('{}/{}'.format(response.url,i))
        print(urls)
        if flag==1:print(urls)


        select=re.findall(r'<div class="currentpath">当前位置: <a href=.*?">(.*?)</a> &raquo; <a href=".*?" rel="category tag">(.*?)</a> &raquo; (.*?)</div>',response.text)[0]
        a,b,c=select
        a=re.sub('[\/:*?"<>|]','-',a)
        b = re.sub('[\/:*?"<>|]', '-', b)
        c = re.sub('[\/:*?"<>|]', '-', c)

        if flag==1:print(a,b,c)

        subdir=os.path.join(a,b,c)
        xiangce_path=os.path.join(self.path,subdir)
        if os.path.exists(xiangce_path):
            return
        else:
            os.makedirs(xiangce_path)

        for url in urls:
            yield scrapy.Request(url,  callback=self.get_pic_url, dont_filter=True,meta={'path':xiangce_path})


    def get_pic_url(self,response):

        url=re.findall(r'<img src="(https://.*?\d+\..*?)" alt=',response.text)

        xiangce_path=response.meta['path']

        print('pic url =',url)

        item=PicItem()
        item['image_urls']=url
        item['image_path']=xiangce_path
        yield item
