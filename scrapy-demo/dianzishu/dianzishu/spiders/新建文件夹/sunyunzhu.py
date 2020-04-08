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




class Sunyunzhu_Spider(scrapy.Spider):
    name = 'sunyunzhu'
    allowed_domains = 't-nani.co.kr'

    def trans(self,q):
        sign = APP_ID + q + salt + key
        sign = hashlib.md5(sign.encode(encoding='utf-8')).hexdigest()
        req = 'http://api.fanyi.baidu.com/api/trans/vip/translate?q={}&from={}&to={}&appid={}&salt={}&sign={}'.format(q,f,t,APP_ID,salt,sign)
        print(req)
        response = requests.get(req)
        s = response.content.decode('unicode_escape')
        s = json.loads(s)
        s = s['trans_result'][0]['dst']
        print(s, type(s))
        print('输入{}翻译成{}'.format(q, s))
        return s

    def start_requests(self):
        for i in range(1999474,1550000,-1):
            yield scrapy.Request('https://www.t-nani.co.kr/shop/shopdetail.html?branduid={}&'.format(i),dont_filter=True,callback=self.parse)

    def parse(self,response):
        if len(re.findall('alert',response.text))!=1:
            with open(os.path.join(IMAGES_STORE,sun_log.txt),'a',encoding='utf-8') as f:
                f.write(response.url+'\r\n')
            urls=[]
            for url in re.findall('src="(http://.*?\.jpg)">',response.text):
                if 'jpg' not in url and  'jepg' not in url and  'png' not in url and  'bmp' not in url and  'gif' not in url:
                    pass

                if '?'in url:
                    urls.append(url.split('?')[0])

                if 'http://' in url or 'https://' in url:
                    urls.append(url)
            urls=set(urls)




            print(urls)
            title=re.findall('<title>(.*?)</title>',response.text)[0]
            num_title=re.findall('branduid=(\d+)&',response.url)[0]

            kor_title = re.sub('[\[\/:*?"<>|\]]', '', title)
            cn_title=self.trans(kor_title)
            dir_name='{}_{}_{}'.format(cn_title,num_title,kor_title)
            abspath=os.path.join(IMAGES_STORE,dir_name)
            print(abspath)
            n=1
            while os.path.exists(abspath):
                abspath=abspath+str(n)
                n+= 1
            os.makedirs(abspath)
            item=PicItem()
            item['image_urls']=urls
            item['image_path']=abspath

            yield item
        else:
            print(response.url,'bucunzai')
            return

