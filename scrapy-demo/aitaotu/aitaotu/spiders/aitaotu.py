import  scrapy
import re
import os
import sys
import time
sys.path.append(r'D:\\pycharm-professional-2017.2.4\\pystudy\\scrapy-demo\\aitaotu\\aitaotu')
from items import PicItem
from settings import IMAGES_STORE
print(sys.path)
flag=0



class AiTaoTu_Spider(scrapy.Spider):
    name = 'aitaotu'
    allowed_domains = 'aitaotu.com'

    path=os.path.join(IMAGES_STORE,name)
    log_name='log.txt'

    if not os.path.exists(path):
        os.makedirs(os.path.join(path))
    with open(os.path.join(path,log_name),'a',encoding='utf-8') as f:
        f.write(time.strftime('%Y-%m-%d %H-%M')+'\r\n\r\n')


    def start_requests(self):
        # for i in range(50000,50050):
        #     yield scrapy.Request('https://www.aitaotu.com/guonei/{}.html'.format(i))
        for i in range(1,2):
            yield scrapy.Request('https://www.aitaotu.com/guonei/list_{}.html'.format(i))


    def parse(self,response):

        print('获得{}响应，开始处理'.format(response.url))
        print(response.url,response.status)

        if response.status!=200:
            print('页面不存在,返回')
            return

        page = re.sub('[\s]+', '', response.text)
        select=re.findall('''<span><ahref="(/.*?/\d+.html)"target="_blank">(.*?)</a></span>''',page)


        if flag==1:print(response.text)

        with open(os.path.join(self.path,self.log_name), 'r', encoding='utf-8') as f:
            log=f.read()

        with open(os.path.join(self.path, self.log_name), 'a', encoding='utf-8') as f:
            for i in select:
                if i[0] not in log:

                    print("写入log，新增相册{}".format(i[0],i[1]))
                    f.write('{}'.format(time.strftime( '%Y-%m-%d %H-%M') + '\t' +str(i[0])+'\t'+ str(i[1]) + '\r\n\r\n'))
                    print('提交新增加相册{}'.format(i[0],i[1]))
                    print(response.url.split('list')[0]+i[0])
                    yield scrapy.Request('https://www.aitaotu.com'+i[0], callback=self.get_page, dont_filter=True)

        # yield scrapy.Request(response.url, callback=self.get_page, dont_filter=True)


    def get_page(self,response):
        # page = re.sub('[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+','',response.text )

        page = re.sub('[\s]+','',response.text )

        select=re.findall('''当前位置：</span><ahref=".*?">(.*?)</a>.*?<ahref=".*?">(.*?)</a>&nbsp;&gt;&nbsp;(.*?)</div><divclass=".*?"id="photos">.*?<spanid="picnum">\(<spanclass="nowpage">.*?</span>/<spanclass="totalpage">(.*?)</span>\)''',page)[0]#搜索相册中所有的图片页面编号

        print(select)

        a,b,c,num=select
        a=re.sub('[\/:*?"<>|]','-',a)
        b = re.sub('[\/:*?"<>|]', '-', b)
        c = re.sub('[\/:*?"<>|]', '-', c)

        if flag==1:print(a,b,c)

        subdir=os.path.join(a,b,c)
        xiangce_path=os.path.join(self.path,subdir)
        if os.path.exists(xiangce_path):
            return
        else:
            os.makedirs(xiangce_path)



        urls=[]
        for i in range(1,int(num)+1,1):
            urls.append('{}_{}.html'.format(response.url.split('.html')[0],i))
        print(urls)
        if flag==1:print(urls)



        for url in urls:
            yield scrapy.Request(url,  callback=self.get_pic_url, dont_filter=True,meta={'path':xiangce_path})


    def get_pic_url(self,response):

        urls=re.findall('''<a href=".*?"><img src="(.*?)" alt=".*?".*?></a>''',response.text)
        urls.remove('https://img.aitaotu.cc:8089/Thumb/2018/footer_tp8.jpg')
        xiangce_path=response.meta['path']

        print('pic url =',urls)

        item=PicItem()
        item['image_urls']=urls
        item['image_path']=xiangce_path
        yield item
