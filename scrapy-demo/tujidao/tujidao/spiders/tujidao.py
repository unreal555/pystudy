# coding=utf-8


#
import  scrapy
import re
import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from items import PicItem
from settings import IMAGES_STORE
print(sys.path)
flag=0

start=1
end=700
step=1

class MeiTuLu_Spider(scrapy.Spider):
    name = 'tujidao'
    allowed_domains = 'tujidao.com'

    log_path=os.path.join(IMAGES_STORE,name)
    log_name='log.txt'

    #日志文件
    if not os.path.exists(log_path):
        os.makedirs(os.path.join(log_path))
    with open(os.path.join(log_path,log_name),'a',encoding='utf-8') as f:
        f.write(time.strftime('%Y-%m-%d %H-%M')+'\r\n\r\n')

    #登录
    def start_requests(self):
        formdata = {
            't0': 'unreal555',
            't1': '594188'
        }
        yield scrapy.FormRequest('http://www.tujidao.com/u/?action=loginsave', formdata=formdata,callback=self.login_check)

    #检查登录状态，获得cookie传递
    def login_check(self,response):

        set_cookie=response.headers.getlist('Set-Cookie')
        cookies={}
        for i in set_cookie:
            for j in i.decode('utf-8').replace(' ','').split(';'):
                a,b=j.split('=')
                cookies[a]=b
        print('cookies',cookies)

        yield scrapy.Request('http://www.tujidao.com/u/?', callback=self.after_login,dont_filter=True,cookies=cookies,meta={'cookies':cookies})

    #利用cookie访问相册索引页面,只传入首页，后续页面待本页面相册下载 完毕后提交
    def after_login(self,response):
        print('传递过来的cookie',response.meta['cookies'])

        # for i in range(1650,1005,-1):#1630-1500-1200-1000
        #     yield scrapy.Request('http://www.tujidao.com/cat/?id=0&page={}'.format(i),callback=self.parse,dont_filter=True)

        yield scrapy.Request('http://www.tujidao.com/cat/?id=0&page={}'.format(start), callback=self.parse,dont_filter=True)

    def parse(self,response):

        print('获得{}响应，开始处理'.format(response.url))

        if response.status!=200:
            print('页面不存在,返回')
            return
        page = re.sub('[\s]+', '', response.text)
        # print(page)

        #提取相册记录，总的
        select=re.findall('''(<li><ahref="/a/.*?</a></p></li>)''',page)


        for i in select:
            #如果没有提取到相册数字代码，写入错误日志
            result=re.findall('<pclass="biaoti"><ahref="/a/\?id=(\d+)"target="_blank">(.*?)</a></p></li>',i)
            if len(result)==0:
                with open(os.path.join(self.log_path,'wrong.txt'),'a',encoding='utf-8') as f:
                    f.write('{}'.format(time.strftime( '%Y-%m-%d %H-%M')+'\t' + response.url+'\r\n\r\n\r\n\r\n'))
                    return
            bianhao,biaoti=result[0]

            #如果没有提取到第一张图片地址，写入错误日志
            result=re.findall('''<imgclass="lazy"data-original="(.*?)"></a>''',i)
            if len(result)==0:
                with open(os.path.join(self.log_path,'wrong.txt'),'a',encoding='utf-8') as f:
                    f.write('{}'.format(time.strftime( '%Y-%m-%d %H-%M')+'\t' + response.url+'\r\n\r\n\r\n\r\n'))
                    return

            urls=result
            max=re.findall('''<spanclass="shuliang">(\d+)P</''',i)[0]

            jigou=re.findall('''<ahref=/x/\?id=\d+>(.*?)</a>''',i)
            if len(jigou)==0:
                print('没有提取到机构名 ，使用默认名‘无机构’')
                jigou='无机构'
            else:
                jigou=jigou[0]

            tag=''
            for s in re.findall('''<ahref=/s/\?id=\d+>(.*?)</a>''',i):
                tag=tag+s+'-'
            tag=tag+str(max)
            print(bianhao,'---',biaoti,'---',urls,'---',max,'---',tag,'---',jigou)
            biaoti=re.sub('[\/:*?"<>|]','-',biaoti)
            tag=re.sub('[\/:*?"<>|]','-',tag)
            jigou==re.sub('[\/:*?"<>|]','-',jigou)


            with open(os.path.join(self.log_path,self.log_name), 'r', encoding='utf-8') as f:
                log = f.read()
            if bianhao  in log:
                print('{}{} 已经下载，跳过'.format(bianhao,biaoti))
                continue

            if os.path.exists(os.path.join(self.log_path, 'wrong.txt')):
                with open(os.path.join(self.log_path, 'wrong.txt'), 'r', encoding='utf-8') as f:
                    wrong_log = f.read()
                if bianhao in wrong_log:
                    print('{}{} 已经在错误日志，跳过'.format(bianhao, biaoti))
                    continue

            sub_path=os.path.join(jigou,biaoti+'-tag-'+tag)
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

        now=re.findall('id=0&page=(\d+)',response.url)[0]
        next=int(now)+step
        if int(now)!=end:
            yield scrapy.Request('http://www.tujidao.com/cat/?id=0&page={}'.format(next), callback=self.parse,dont_filter=True)
        else:
            return



