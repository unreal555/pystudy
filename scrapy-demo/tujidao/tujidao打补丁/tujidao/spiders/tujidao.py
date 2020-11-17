# coding=utf-8
import  scrapy
import re
import os
import sys
import time
import json
import pickle

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


'''
key='cat'    #cat=区域  s=tag     x=机构


cat=int(input('cat 8日本10中国11台湾19韩国20欧美23泰国42 0采用默认值'))
start=int(input('start'))
end=int(input('end'))




ids=[10,11,8,19,20,23]
ids=ids[::-1]
pages=range(900,0,-1)

if cat!=0:

    if cat in ids:
        ids=range(cat,cat+1)

    pages=range(start,end+1)

    print(ids,pages)

'''    

with open('C://Users//Administrator//Desktop//tujidao//result.dat','rb') as f:


    result=pickle.load(f)

min=295
max=350

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
      
        yield scrapy.Request('https://www.tujidao.com/cat/?id=1&page=1',callback=self.parse,dont_filter=True)

    def parse(self,response):

            
        for sssss in result:
            bianhao,biaoti,jigou=sssss
            bianhao=str(bianhao)
            tag=bianhao

            biaoti=re.sub('[\/:*?"<>|]','-',biaoti)
            tag=re.sub('[\/:*?"<>|]','-',tag)
            jigou==re.sub('[\/:*?"<>|]','-',jigou)



    

            with open(os.path.join(self.log_path,self.log_name), 'r', encoding='utf-8') as f:
                log = f.read()
            if '##'+bianhao+'##'  in log:
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


            urls=[]


            
            for i in range(min-1,int(max)+1):
                urls.append('https://lns.hywly.com/a/1/{}/{}.jpg'.format(str(bianhao),str(i)))
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
            

