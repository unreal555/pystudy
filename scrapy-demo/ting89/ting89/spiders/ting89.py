# coding=utf-8

import  scrapy
import re
import os
import sys
import time
import mytools

base_dir='d://mp3//'

domain='http://www.ting89.com'

log=os.path.join(base_dir,'log.txt')
wrong_log=os.path.join(base_dir,'wrong.txt')


class Ting89_Spider(scrapy.Spider):
    name = 'ting89'
    allowed_domains = 'ting89.com'

    if os.path.exists(base_dir):
        pass
    else:
        os.makedirs(base_dir)

    with open(log,'a',encoding='utf-8') as f:
        f.write(time.strftime('%Y-%m-%d %H-%M')+'\r\n\r\n')

    with open(os.path.join(wrong_log),'a',encoding='utf-8') as f:
        f.write(time.strftime('%Y-%m-%d %H-%M')+'\r\n\r\n')



    def start_requests(self):
        yield scrapy.FormRequest('http://www.ting89.com/topiclist/quanben-2.html', callback=self.parse,)


    def parse(self,response):
        result=response.xpath('//*[@id="channelright"]/div[2]/div[3]/ul/li')

        for i in result:
            book=re.findall('target="_blank"><b>(.*?)</b></a></p><p>(类型：.*?)</p><p>(作者：.*?)</p><p>(播音：.*?)</p><p>(时间：.*?)</p><p>(状态：.*?)</p><p><ahref="(.*?)"class="xq"title=".*?"target="_blank">下载</a>',mytools.qu_kong_ge(i.extract()))[0]
            if book==[]:
                with open(os.path.join(wrong_log),'a',encoding='utf-8') as f:
                    f.write(i+'\r\n\r\n')
                continue
            meta={}
            meta['book_name']=book[0]
            meta['book_leixing']=book[1]
            meta['book_author']=book[2]
            meta['book_boyin']=book[3]
            meta['book_shijian']=book[4]
            meta['book_zhangtai']=book[5]
            meta['book_url']=domain+book[6]
            # print(meta)
            yield scrapy.Request(meta['book_url'],meta=meta,callback=self.book_parse,dont_filter=True)
    def book_parse(self,response):
        print(response.meta)
