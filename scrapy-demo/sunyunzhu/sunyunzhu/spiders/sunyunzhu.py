import scrapy
import re
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
print(sys.path)
from items import PicItem
from settings import IMAGES_STORE
import requests
import hashlib
import random
import json
import time

APP_ID = '20200227000389406'
key = 'HuiaSVAxKxmWEhAOIdFx'
salt = str(random.randint(2000000,3000000))
f = 'auto'
t = 'zh'


class Sunyunzhu_Spider(scrapy.Spider):
    name = 'sunyunzhu'
    allowed_domains = 't-nani.co.kr'

    def trans(self, q):
        sign = APP_ID + q + salt + key
        sign = hashlib.md5(sign.encode(encoding='utf-8')).hexdigest()
        req = 'http://api.fanyi.baidu.com/api/trans/vip/translate?q={}&from={}&to={}&appid={}&salt={}&sign={}'.format(q,
                                                                                                                      f,
                                                                                                                      t,
                                                                                                                      APP_ID,
                                                                                                                      salt,
                                                                                                                      sign)
        print(req)

        print('开始翻译')
        sign = APP_ID + q + salt + key
        sign = hashlib.md5(sign.encode(encoding='utf-8')).hexdigest()
        while 1:
            req = 'http://api.fanyi.baidu.com/api/trans/vip/translate?q={}&from={}&to={}&appid={}&salt={}&sign={}'.format(
                q, f, t, APP_ID, salt, sign)
            print('生成请求链接', req)
            response = requests.get(req)
            print('响应信息为', response.text)
            s = response.content.decode('unicode_escape')
            print('响应信息解码', s)
            if 'error_code' in s:
                time.sleep(1.5)
                continue
            s = json.loads(s)
            s = s['trans_result'][0]['dst']
            print(s, type(s))
            print('输入{}翻译成{}'.format(q, s))
            return s


    # urls = ['http://www.t-nani.co.kr/shop/shopdetail.html?branduid=1989895&',
    #         'http://www.t-nani.co.kr/shop/shopdetail.html?branduid=1989896&'
    #         ]
    def start_requests(self):
        # for i in self.urls:
        #     yield scrapy.Request(i,dont_filter=True,callback=self.parse)
        for i in range(1997100, 1998000):  # 1676000--2314000
            yield scrapy.Request('https://www.t-nani.co.kr/shop/shopdetail.html?branduid={}&'.format(i),dont_filter=True,callback=self.parse)


    def parse(self, response):
        if len(re.findall('alert', response.text)) != 1:  # 判断请求页面是不是存在

            with open(os.path.join(IMAGES_STORE, 'sun_log.txt'), 'a', encoding='utf-8') as f:  # 如果页面存在，写入日志
                f.write(response.url + '\r\n')

            urls = []  # 生成url数组
            for url in re.findall('src="(http://.*?\.jpg)">', response.text):
                if 'jpg' not in url and 'jepg' not in url and 'png' not in url and 'bmp' not in url and 'gif' not in url:
                    continue
                if 'tnanilogo.jpg' in url or 'modelsize.jpg' in url:
                    continue

                if '?' in url:
                    urls.append(url.split('?')[0])

                if 'http://' in url or 'https://' in url:
                    urls.append(url)

            urls = set(urls)  # 去重

            title = re.findall('<title>(.*?)</title>', response.text)[0]
            num_title = re.findall('branduid=(\d+)&', response.url)[0]

            kor_title = re.sub('[\/:*?"<>| ]', '', title)
            cn_title = self.trans(kor_title)
            dir_name = '{}_{}_{}'.format(num_title, cn_title, kor_title)
            abspath = os.path.join(IMAGES_STORE, dir_name)

            n = 1
            while os.path.exists(abspath):
                abspath = abspath + "_" + str(n)
                n += 1
            os.makedirs(abspath)
            item = PicItem()
            item['image_urls']=urls
            item['image_path'] = abspath
            yield item

        else:
            print('相册不存在',response.url,)
            return
