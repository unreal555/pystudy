import scrapy
import re
from items import WanBen

item=WanBen()

class Wanben_Spider(scrapy.Spider):
    name = 'wanben'

    domain = 'https://www.52bqg.com'
    allowed_domains = '52bqg.com'


    def start_requests(self):
        for i in range(1,128000,1):
            url='{}/book_{}'.format(self.domain,str(i))
            print(url)
            yield    scrapy.Request(url)

    def parse(self, response):
        if response.state_code==200:
            flag=re.findall('<meta property="og:novel:status" content="(.*?)"/>',response.text)[0]
            if flag.find('完')!=-1:
                item['name']=re.findall('<meta property="og:novel:book_name" content="(.*?)"/>',response.text)[0]
                item['link']=response.url
                print(item['name'],item['link'])
                yield item
        else:
            return

