import  scrapy
import re
import os
from items import PicItem
header={
':authority':'www.mzitu.com',
':method':'GET',
':path':'/',
':scheme':'https',
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding':'gzip,deflat,br',
'accept-language':'zh-CN,zh;q=0.9',
'cache-control':'max-age=0',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0(WindowsNT6.1;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/66.0.3359.139Safari/537.36'}
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '125',
    # 'Content-Type': 'application/x-www-form-urlencoded'}

class Mzitu_Spider(scrapy.Spider):
    name = 'mzitu'
    allowed_domains = 'mzitu.com'

    def start_requests(self):
        yield scrapy.Request('https://www.mzitu.com/all/',headers=header)

    def parse(self,response):
        select=re.findall('<a href="(.*?)" target="_blank">(.*?)</a>',response.text)

        for i in select[1:]:
            print(i[0])
            yield scrapy.Request('https://www.mzitu.com/223294',headers=header,callback=self.get_page,dont_filter=True)
            break

    def get_page(self,response):
        select=re.findall('上一组</span></a><span>(.*?)<span>下一页',response.text)[0]

        urls=[]
        for i in range(1,int(max(re.findall(r'/(\d+)\'',select)))+1):
            urls.append('{}/{}'.format(response.url,i))
        print(urls)


        select=re.findall(r'<div class="currentpath">当前位置: <a href=.*?">(.*?)</a> &raquo; <a href=".*?" rel="category tag">(.*?)</a> &raquo; (.*?)</div>',response.text)[0]
        a,b,c=select
        print(a,b,b)
        path=os.path.join('d:/a',a,b,c)
        if os.path.exists(path):
            return
        else:
            os.makedirs(path)

        for url in urls:
            yield scrapy.Request(url, headers=header, callback=self.get_pic_url, dont_filter=True,meta={'path':path})
            break

    def get_pic_url(self,response):
        url=re.findall('<img src="(.*?)" alt=',response.text)
        path=response.meta['path']
        print(response.headers.getlist['Set-Cookie'])






















        item=PicItem(image_urls=url,image_path=path)

        yield item
