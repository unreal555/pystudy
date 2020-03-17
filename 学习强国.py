import requests
import re
import json
from lxml import etree

class Spider:
    def __init__(self, headers, url,fp=None):
        self.headers = headers
        self.url=url
        self.fp=fp

    def open_file(self):
        self.fp = open('学习强国2.txt', 'w', encoding='utf8')

    def get_data(self):
       return requests.get(url=self.url, headers=self.headers).text

    def parse_home_data(self):
        ex = '"static_page_url":"(.*?)"'
        home_data=self.get_data()
        return re.findall(ex,home_data)

    def parse_detail_data(self):
        detail_url=self.parse_home_data()
        print(detail_url)
        i = 0
        for url in detail_url:
            i += 1
            '''<title>系统维护中</title> 坑人'''
            try:
                self.url = url.replace(r'/e', r'/datae').replace('html', 'js')
                detail_data = self.get_data()
                detail_data = detail_data.replace('globalCache = ', '')[:-1]
                dic_data = json.loads(detail_data)
#获取字典中的第一个键值对的key
                first = list(dic_data.keys())[0]
                title = dic_data[first]['detail']['frst_name']
                content_html = dic_data[first]['detail']['content_list'][0]['content']
                tree = etree.HTML(content_html)
                content_list = tree.xpath('.//p/text()')
            except Exception as e:
                print(e)
                continue
            self.fp.write('第{i}章' + title + '\n' + ''.join(content_list) + '\n\n')

    def close_file(self):
        self.fp.close()

    def run(self):
        self.open_file()
        self.parse_detail_data()
        self.close_file()

if __name__ == '__main__':
    headers = {
        'Host': 'www.xuexi.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    }
    url = 'https://www.xuexi.cn/f997e76a890b0e5a053c57b19f468436/data018d244441062d8916dd472a4c6a0a0b.js'
    spider=Spider(url=url,headers=headers)
    spider.run()