#***coding=utf-8***
import  scrapy
import re
import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from  ..items import PicItem
from ..settings import IMAGES_STORE
print(sys.path)
flag=0



class MeiTuLu_Spider(scrapy.Spider):
    name = 'meitulu'
    allowed_domains = 'meitulu.com'

    path=os.path.join(IMAGES_STORE,name)
    log_name='log.txt'

    if not os.path.exists(path):
        os.makedirs(os.path.join(path))
    with open(os.path.join(path,log_name),'a',encoding='utf-8') as f:
        f.write(time.strftime('%Y-%m-%d %H-%M')+'\r\n\r\n')


    def start_requests(self):
        yield scrapy.Request('https://www.meitulu.com/guochan/')
        for i in range(2,100):
            yield scrapy.Request('https://www.meitulu.com/guochan/{}.html'.format(i))


    def parse(self,response):

        print('获得{}响应，开始处理'.format(response.url))
        print(response.url,response.status)

        print(response.text)
        if response.status!=200:
            print('页面不存在,返回')
            return

        page = re.sub('[\s]+', '', response.text)
        print(page)
        select=re.findall('''<pclass=p_title><ahref="(.*?)"target="_blank">(.*?)</a></p>''',page)

        if flag==1:print(response.text)

        with open(os.path.join(self.path,self.log_name), 'r', encoding='utf-8') as f:
            log=f.read()

        with open(os.path.join(self.path, self.log_name), 'a', encoding='utf-8') as f:
            for i in select:
                if i[0] not in log:

                    print("写入log，新增相册{}".format(i[0],i[1]))
                    f.write('{}'.format(time.strftime( '%Y-%m-%d %H-%M') + '\t' +str(i[0])+'\t'+ str(i[1]) + '\r\n\r\n'))
                    print('提交新增加相册{}'.format(i[0],i[1]))

                    yield scrapy.Request(i[0], callback=self.get_page, dont_filter=True)
                    break




    def get_page(self,response):
        # page = re.sub('[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+','',response.text )

        page = re.sub('[\s]+','',response.text )
        print(page)
        select=re.findall('''<divclass="weizhi"><span>当前位置：<ahref=".*?">(.*?)</a>><ahref=".*?">(.*?)</a>></span><h1>(.*?)</h1></div>''',page)[0]#搜索相册中所有的图片页面编号
        a,b,c=select
        a=re.sub('[\/:*?"<>|]','-',a)
        b = re.sub('[\/:*?"<>|]', '-', b)
        c = re.sub('[\/:*?"<>|]', '-', c)
        if  '[' in c and ']' in c:
            c=os.path.join(*re.split('[\[\]]',c))
        if flag==1:print(a,c)
        subdir=os.path.join(a,c)
        xiangce_path=os.path.join(self.path,subdir)

        print(xiangce_path)
        if os.path.exists(xiangce_path):
            return
        else:
            os.makedirs(xiangce_path)
        # des=[]
        # print(re.findall('''<p>(发行机构：)<ahref=".*?"target="_blank"class="tags">(.*?)</a></p>''', page))

        # print(re.findall('''<p>(模特姓名：)<ahref=".*?"target="_blank"class="tags">(.*?)</a></p>''', page))
        # print(re.findall('''<p>(发行时间：.*?)</p></div>''', page)[0])
        # print(re.findall('''<pclass="buchongshuoming"><span>(补充说明：)</span>(.*?)</p>''', page))


        bianhao=re.findall('/(\d+)\.',response.url)[0]
        max=re.findall('''<p>期刊编号：.*?</p><p>图片数量：(.*?)张</p>''', page)[0]





        print(max)
        urls=[]
        for i in range(1,int(max)+1):
            urls.append('https://mtl.gzhuibei.com/images/img/{}/{}.jpg'.format(bianhao,i))
        print(urls)
        if flag==1:print(urls)


        item=PicItem()
        item['image_urls']=urls
        item['image_path']=xiangce_path

        yield item


#
# #https://mtl.gzhuibei.com/images/img/20666/90.jpg,                    https://www.meitulu.com/item/20666.html>

        # for url in urls:
        #     yield scrapy.Request(url,  callback=self.get_pic_url, dont_filter=True,meta={'path':xiangce_path})


    # def get_pic_url(self,response):
    #
    #     urls=re.findall('''<a href=".*?"><img src="(.*?)" alt=".*?".*?></a>''',response.text)
    #     urls.remove('https://img.aitaotu.cc:8089/Thumb/2018/footer_tp8.jpg')
    #     xiangce_path=response.meta['path']
    #
    #     print('pic url =',urls)
    #
    #
    #
