import os
import sys
import re
import  scrapy
import mytools
import collections
from ..items import BiqugeItem
import collections





sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

class Biquge_Spider(scrapy.Spider):
    name='biquge'
    allowed_domains = 'biquge5200.cc'

    def start_requests(self):

        url='https://www.biquge5200.cc/0_584/'
        yield scrapy.Request(url,dont_filter=True,callback=self.get_novel_index)


    def get_novel_index(self,response):

        index = re.findall('<dd><a href="(.*?)">(.*?)</a></dd>', response.text)

        global item
        item = BiqugeItem()

        item['title']=re.findall('''<meta property="og:title" content="(.*?)"/>''',response.text)[0]
        item['des']=re.findall('''<meta property="og:description" content="(.*?)"/>''',response.text)[0]
        item['category']=re.findall('''<meta property="og:novel:category" content="(.*?)"/>''',response.text)[0]
        item['author'] = re.findall('''<meta property="og:novel:author" content="(.*?)"/>''',response.text)[0]
        item['count']=len(index)


        for i in index:
            print(i)
        print(item['count'])

        item['chapter']=collections.OrderedDict()


        for chapter_url,chapter_name in index:
            item['chapter'][chapter_url]=[chapter_name]

        for i in item['chapter']:

            yield scrapy.Request(i,callback=self.get_content,dont_filter=True)





    def get_content(self,response):
        print(response.url)
        content=response.xpath('//*[@id="content"]/p').extract()
        print(content)
        item['chapter'][response.url].append(content)
        item['count']-=1
        print(item['count'])

        if item['count']==0:
            yield item












