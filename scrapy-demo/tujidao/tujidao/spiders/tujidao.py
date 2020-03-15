# coding=utf-8


#
import  scrapy
import re
import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from  items import PicItem
from settings import IMAGES_STORE
print(sys.path)
flag=0




class MeiTuLu_Spider(scrapy.Spider):
    name = 'tujidao'
    allowed_domains = 'tujidao.com'

    log_path=os.path.join(IMAGES_STORE,name)
    log_name='log.txt'

    if not os.path.exists(log_path):
        os.makedirs(os.path.join(log_path))
    with open(os.path.join(log_path,log_name),'a',encoding='utf-8') as f:
        f.write(time.strftime('%Y-%m-%d %H-%M')+'\r\n\r\n')


    def start_requests(self):

        formdata = {
            't0': 'unreal555',
            't1': '594188'
        }
        yield scrapy.FormRequest('http://www.tujidao.com/u/?action=loginsave', formdata=formdata,callback=self.login_check)



    def login_check(self,response):

        set_cookie=response.headers.getlist('Set-Cookie')
        cookies={}
        for i in set_cookie:
            for j in i.decode('utf-8').replace(' ','').split(';'):
                a,b=j.split('=')
                cookies[a]=b
        print('cookies',cookies)
        yield scrapy.Request('http://www.tujidao.com/u/?', callback=self.after_login,dont_filter=True,cookies=cookies,meta={'cookies':cookies})

    def after_login(self,response):
        print('传递过来的cookie',response.meta['cookies'])

        for i in range(1501,1300,-1):#1630-1620-1500-1300
            yield scrapy.Request('http://www.tujidao.com/cat/?id=0&page={}'.format(i),callback=self.parse,dont_filter=True)


    def parse(self,response):

        print('获得{}响应，开始处理'.format(response.url))
        print(response.url,response.status)

        print(response.text)
        if response.status!=200:
            print('页面不存在,返回')
            return

        page = re.sub('[\s]+', '', response.text)
        print(page)

        select=re.findall('''(<li><ahref="/a/.*?</a></p></li>)''',page)

        for i in select:
            print('target', i)
            bianhao,biaoti=re.findall('<pclass="biaoti"><ahref="/a/\?id=(\d+)"target="_blank">(.*?)</a></p></li>',i)[0]
            urls=re.findall('''<imgclass="lazy"data-original="(.*?)"></a>''',i)
            max=re.findall('''<spanclass="shuliang">(\d+)P</''',i)[0]
            tag=''
            for s in re.findall('''<ahref=/s/\?id=\d+>(.*?)</a>''',i):
                tag=tag+s+'-'
            tag=tag+str(max)

            biaoti=re.sub('[\/:*?"<>|]','-',biaoti)
            tag=re.sub('[\/:*?"<>|]','-',tag)

            print(bianhao,biaoti,urls,max,tag)

            with open(os.path.join(self.log_path,self.log_name), 'r', encoding='utf-8') as f:
                log = f.read()

            with open(os.path.join(self.log_path,self.log_name), 'a', encoding='utf-8') as f:

                if bianhao  in log:
                    continue


            if  '[' in biaoti and ']' in biaoti:
                a,b,c=re.split('[\[\]]',biaoti)
                sub_path=os.path.join(b,c+'-tag-'+tag)
                xiangce_path = os.path.join(self.log_path, sub_path)
            print(xiangce_path)

            url_first,url_last=urls[0].split('0.')
            for i in range(1,int(max)+1):
                urls.append('{}{}{}{}'.format(url_first,i,'.',url_last))
            print(urls)

            if os.path.exists(xiangce_path):
                pass
            else:
                os.makedirs(xiangce_path)




            item = PicItem()
            item['image_urls'] = urls
            # item['image_urls']=['https://ii.hywly.com/a/1/899/2.jpg','https://ii.hywly.com/a/1/899/7.jpg']
            item['image_path'] = xiangce_path
            item['image_log']=[bianhao,biaoti,self.log_path,self.log_name]
            yield item






