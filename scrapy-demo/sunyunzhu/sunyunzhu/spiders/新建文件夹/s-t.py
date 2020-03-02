import  scrapy
import re
import os
import sys
sys.path.append(r'D:\\pycharm-professional-2017.2.4\\pystudy\\scrapy-demo\\demo\demo')
print(sys.path)
from items import PicItem
from settings import IMAGES_STORE
import requests
import hashlib
import random
import json
APP_ID='20200227000389406'
key='HuiaSVAxKxmWEhAOIdFx'
salt=str(random.randint(1000000000,9999999999))
f='auto'
t='zh'




class Sunyun_Spider(scrapy.Spider):
    name = 's-t'
    allowed_domains = 't-nani.co.kr'

    def start_requests(self):
        yield scrapy.Request('http://www.t-nani.co.kr')
        yield scrapy.Request('http://www.t-nani.co.kr/shop/shopbrand.html?type=P&xcode=005')
        yield scrapy.Request('http://www.t-nani.co.kr/shop/shopbrand.html?xcode=011&page=2')
        yield scrapy.Request('')
        yield scrapy.Request('')
        yield scrapy.Request('')
        yield scrapy.Request('')

    def parse(self,response):
        print(response.text)
        result=re.findall('<a href="(.*?\?branduid=\d+)&.*?">',response.text)
        for i in result:
            print(i)