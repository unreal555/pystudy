import  scrapy
import re
import os
import sys
sys.path.append(r'D:\\pycharm-professional-2017.2.4\\pystudy\\scrapy-demo\\demo\demo')
print(sys.path)

from items import PicItem

from settings import IMAGES_STORE


flag=0


class Mzitu_Spider(scrapy.Spider):
    name = 'mzitu'
    allowed_domains = 'mzitu.com'



    def start_requests(self):

        print('进入索引页https://www.mzitu.com/all/')
        yield scrapy.Request('https://www.mzitu.com/all/')
        yield scrapy.Request('https://www.mzitu.com/old/')

    def parse(self,response):

        print('获得索引页面，开始处理')
        if flag==1:print(response.text)
        select=re.findall('<a href="(https://www.mzitu.com/\d+)" target="_blank">(.*?)</a>',response.text)
        print('获得相册连接')
        print(len(select))
        f=open('{}/index.txt'.format(IMAGES_STORE),'a',encoding='utf-8')
        f.write(response.url)
        for i in select:
            f.write('{}'.format('\t'+str(i)+'\r\n'))
        for i in select[1:]:
            # time.sleep(random.choice(range(10,1000)))
            if flag==1:print(i[0])
            print("提交相册连接{}".format(i[0]))

            yield scrapy.Request(i[0],callback=self.get_page,dont_filter=True)

    def get_page(self,response):
        urlst=re.findall('上一组</span></a><span>(.*?)<span>下一页',response.text)


        a,b,c=re.findall(r'<div class="currentpath">当前位置: <a href=.*?">(.*?)</a> &raquo; <a href=".*?" rel="category tag">(.*?)</a> &raquo; (.*?)</div>',response.text)[0]

        a=re.sub('[\/:*?"<>|]','-',a)
        b = re.sub('[\/:*?"<>|]', '-', b)
        c = re.sub('[\/:*?"<>|]', '-', c)

        if flag==1:print(a,b,c)

        subdir=os.path.join(a,b,c)
        path=os.path.join(IMAGES_STORE,subdir)
        if os.path.exists(path):
            return
        else:
            os.makedirs(path)

        for url in urls:
            yield scrapy.Request(urls[-1],  callback=self.get_pic_url, dont_filter=True,meta={'path':subdir})


    def get_pic_url(self,response):

        url=re.findall(r'<img src="(https://.*?\d+\..*?)" alt=',response.text)

        path=response.meta['path']

        print('pic url =',url)

        item=PicItem()
        item['image_urls']=url
        item['image_path']=path
        yield item
