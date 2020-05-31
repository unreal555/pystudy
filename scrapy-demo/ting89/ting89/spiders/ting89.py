# coding=utf-8

import  scrapy
import re
import os
import sys
import time
import mytools
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from ..items import FileItem

base_dir='e://mp3//'

domain='http://www.ting89.com'

log=os.path.join(base_dir,'log.txt')
wrong_log=os.path.join(base_dir,'wrong.txt')
down_log=os.path.join(base_dir,'down_log.txt')


class Ting89_Spider(scrapy.Spider):
    name = 'ting89'
    allowed_domains = 'ting89.com'

    if os.path.exists(base_dir):
        pass
    else:
        os.makedirs(base_dir)

    with open(log,'a',encoding='utf-8') as f:
        f.write(time.strftime('%Y-%m-%d %H-%M')+'\r\n\r\n')

    with open(wrong_log,'a',encoding='utf-8') as f:
        f.write(time.strftime('%Y-%m-%d %H-%M')+'\r\n\r\n')

    with open(down_log,'a',encoding='utf-8') as f:
        f.write(time.strftime('%Y-%m-%d %H-%M')+'\r\n\r\n')



    def start_requests(self):
        n=input('要下那一页（输入2-500之间的整数后回车）：')
        if n=='':
            yield scrapy.FormRequest('http://www.ting89.com/topiclist/quanben.html', callback=self.parse)

        else:
            try:
                n=int(n)
            except:
                print('输入错误，关闭重新运行')

            if 2<=n<=500:
                yield scrapy.FormRequest('http://www.ting89.com/topiclist/quanben-{}.html'.format(n), callback=self.parse)






    def parse(self,response):
        result=response.xpath('//*[@id="channelright"]/div[2]/div[3]/ul/li')
        for i in result:
            i=mytools.qu_kong_ge(i.extract())
            book_url=re.findall('<li><ahref="(.*?)"title=',i)[0]
            book_url=domain+book_url
            info=re.findall('target="_blank"><b>(.*?)</b></a></p><p>(类型：.*?)</p><p>(作者：.*?)</p><p>(播音：.*?)</p><p>(时间：.*?)</p><p>(状态：.*?)</p><p><ahref=".*?"class="xq"title=".*?"target="_blank">下载</a>',i)[0]
            if info==[]:
                with open(os.path.join(wrong_log),'a',encoding='utf-8') as f:
                    f.write(i+'\r\n\r\n')
                continue
            meta={}
            meta['book_url']=book_url
            meta['book_name']=info[0]
            meta['book_leixing']=info[1]
            meta['book_author']=info[2]
            meta['book_boyin']=info[3]
            meta['book_shijian']=info[4]
            meta['book_zhuangtai']=info[5]

            yield scrapy.Request(meta['book_url'],meta=meta,callback=self.book_parse,dont_filter=True)



    #
    def book_parse(self,response):
        meta=response.meta
        result=response.xpath('/html/body/div[5]/div[1]/div[4]/div/ul/li')
        all=[]
        for i in result:
            print(i)
            i=mytools.qu_kong_ge(i.extract())
            i=domain+re.findall('<li><ahref="(.*?)"target="_blank">.*</a></li>',i)[0]
            all.append(i)

        print(all)
        meta['all']=all
        meta['path']='e://mp3//{}'.format(meta['book_name'])

        if not os.path.exists(meta['path']):
            os.makedirs(meta['path'])


        for i in meta['all']:
            print(i)
            yield scrapy.Request(i,meta=meta,callback=self.get_link,dont_filter=True)
        with open(log,'a',encoding='utf-8') as f:
            f.write(meta['book_name']+'\r\n')

    def get_link(self,response):
        meta=response.meta

        page=mytools.qu_kong_ge(response.text)
        print(page)
        url=re.findall('''<iframesrc="http://play.ting89.com/down/down.php\?url=(.*?)".*</iframe>''',page)[0]
        print(url)
        item=FileItem()
        item['file_urls']=url
        item['file_path']=os.path.join(meta['path'],url.split('/')[-1])
        item['file_down_log']=down_log
        yield item

