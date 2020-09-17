# coding=utf-8
import  scrapy
import re
import os
import sys
import time
import json

path=os.path.join(os.path.dirname(__file__),"..")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
print(path)
from ..items import PicItem
from ..settings import IMAGES_STORE
print(sys.path)
flag=0

'''
区域
cat   [10,11,8,19,20,23]   range(1,10)
8日本   790
10中国    778
11台湾     137
19韩国    6
20欧美    39
23泰国   42
'''

'''
机构
x    range(1,81)   range(1,20)

'''



key='cat'    #cat=区域  s=tag     x=机构

ids=[10,11,8,19,20,23] 
pages=range(1,20)


class TuJiDao_Spider(scrapy.Spider):
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
        formdata = {           #巨坑,单引号不行,必须双引号
            "way":"login",
            "username": "unreal555",
            "password": "594188"
        }
        yield scrapy.FormRequest('https://www.tujidao.com/?action=save', formdata=formdata,callback=self.start)



    #利用cookie访问相册索引页面,只传入首页，后续页面待本页面相册下载 完毕后提交
    def start(self,response):
        for id in ids:
            for page in pages:
                yield scrapy.Request('https://www.tujidao.com/{}/?id={}&page={}'.format(key,id,page), callback=self.parse,dont_filter=True)

    def parse(self,response):

        print('获得{}响应，开始处理'.format(response.url))
        # print(response.text)

        if response.status!=200:
            print('页面不存在,返回')
            return
        page = re.sub('[\s]+', '', response.text)
        print(page)


        #提取相册记录，总的
        select=re.findall(r'''(<liid=.*?><ahref="/a/\?id=.*?>.*?</a></p></li>)''',page)
        print(len(select))


        for i in select:
            print(i)
            #如果没有提取到相册数字代码，写入错误日志
            result=re.findall('<pclass="biaoti"><ahref="/a/\?id=(\d+)".*?>(.*?)</a></p></li>',i)
            if len(result)==0:
                with open(os.path.join(self.log_path,'wrong.txt'),'a',encoding='utf-8') as f:
                    f.write('{}'.format(time.strftime( '%Y-%m-%d %H-%M')+'\t' + response.url+'\r\n\r\n\r\n\r\n'))
                    return

            bianhao,biaoti=result[0]

            #如果没有提取到第一张图片地址，写入错误日志
            result=re.findall('''<imgsrc="(.*?)">''',i)
            if len(result)==0:
                with open(os.path.join(self.log_path,'wrong.txt'),'a',encoding='utf-8') as f:
                    f.write('{}'.format(time.strftime( '%Y-%m-%d %H-%M')+'\t' + response.url+'\r\n\r\n\r\n\r\n'))
                    return


            urls=result
            max=re.findall('''<spanclass="shuliang">(\d+)P</''',i)[0]



            jigou=re.findall('''<ahref="/x/\?id=\d+">(.*?)</a>''',i)
            if len(jigou)==0:
                print('没有提取到机构名 ，使用默认名‘无机构’')
                jigou='无机构'
            else:
                jigou=jigou[0]

            tag=''
            for s in re.findall('''<ahref="/s/\?id=\d+">(.*?)</a>''',i):
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
            item['image_path'] = xiangce_path
            item['image_log']=[bianhao,biaoti,self.log_path,self.log_name]
            yield item


