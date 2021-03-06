import os
import sys
import re
import  scrapy
import mytools

from ..items import BiqugeItem
import collections


'''
每部小说，生成一个item，通过meta在函数间传递，不要用全局变量

'''


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

class Biquge_Spider(scrapy.Spider):
    name='biquge'
    allowed_domains = 'biquge5200.cc'

    def start_requests(self):

        urls=['https://www.biquge5200.cc/60_60852/',
             'https://www.biquge5200.cc/0_860/',
             'https://www.biquge5200.cc/59_59734/',
             'https://www.biquge5200.cc/60_60363/',
             'https://www.biquge5200.cc/1_1523/',
             'https://www.biquge5200.cc/61_61727/',
             'https://www.biquge5200.cc/60_60430/',
             'https://www.biquge5200.cc/35_35723/',
             'https://www.biquge5200.cc/60_60188/',
             ]
        for url in urls:

            yield scrapy.Request(url,dont_filter=True,callback=self.get_novel_index)


    def get_novel_index(self,response):

        index = re.findall('<dd><a href="(.*?)">(.*?)</a></dd>', response.text)

        item = BiqugeItem()

        item['title']=re.findall('''<meta property="og:title" content="(.*?)"/>''',response.text)[0]
        item['des']=re.findall('''<meta property="og:description" content="(.*?)"/>''',response.text)[0]
        item['category']=re.findall('''<meta property="og:novel:category" content="(.*?)"/>''',response.text)[0]
        item['author'] = re.findall('''<meta property="og:novel:author" content="(.*?)"/>''',response.text)[0]
        item['count']=len(index)

        meta={}
        meta['item']=item
        for i in index:
            print(i)
        print(item['count'])

        item['chapter']=collections.OrderedDict()


        for chapter_url,chapter_name in index:
            item['chapter'][chapter_url]=[chapter_name]

        for i in item['chapter']:

            yield scrapy.Request(i,callback=self.get_content,dont_filter=True,meta=meta)





    def get_content(self,response):
        print(response.url)
        content=response.xpath('//*[@id="content"]/p').extract()
        print(content)
        item=response.meta['item']
        item['chapter'][response.url].append(content)
        item['count']-=1
        print(item['count'])

        mytools.random_wait(0.2,0.4)

        if item['count']<=0:
            yield item













