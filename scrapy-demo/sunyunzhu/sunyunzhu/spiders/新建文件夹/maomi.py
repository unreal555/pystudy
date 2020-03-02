# from __future__ import absolute_import
import scrapy
from items import DemoItem
import os
import time

item = DemoItem()



domain='https://www.96ney.com'

class Maomi_Spider(scrapy.Spider):
    name='maomi'
    #allowed_domains = ["96fhk.com"]

    urls=[]
    urls.append(r'{}/shipin/list-%E5%9B%BD%E4%BA%A7%E7%B2%BE%E5%93%81.html'.format(domain))
    for i in range(1,207):
        urls.append( r'{}/shipin/list-%E5%9B%BD%E4%BA%A7%E7%B2%BE%E5%93%81{}{}.html'.format(domain,'-',str(i)))

    start_urls=urls

    def my_page_parse(self,response):
        print("分析视频页面")
        result=response.xpath('//*[@id="shipin-detail-content-pull"]/div[1]/div/img')
        print(result.extract())

        item['des'] =result.xpath('./@title').extract_first()
        item['link']=response.url
        item['pic']=result.xpath('./@data-original').extract_first()
        result=response.xpath('//*[@id="lin1k0"]')
        item['video_link'] = result.xpath('./@value').extract_first()
        print(item)
        time.sleep(2)
        os.system('\"C:\\Program Files (x86)\\Thunder Network\\Thunder\\Program\\thunder.exe\" {}'.format(item['video_link']))
        time.sleep(1)
        os.system('\"C:\\Program Files (x86)\\Thunder Network\\Thunder\\Program\\thunder.exe\" {}'.format(item['pic']))
        time.sleep(2)
        yield item


    def parse(self, response):
         body=response.xpath('//*[@id="tpl-img-content"]/li/a')
         print('分析索引页')
         for i in body:

            item['link']=domain+i.xpath('./@href').extract_first()

            print(i,item['link'])
            yield scrapy.Request(url=item['link'],callback=self.my_page_parse,meta=item)





