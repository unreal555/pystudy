import scrapy
import re
import time
import random
import  json
from items import Dianzishu

#由于每个start_url将保存到一个独立的文件，所以item初始化必须放在parse方法中作为parse的局部变量，不能作为class的全面变量，否则每个start_url的parse方法都会重写item的内容

#每个start_url生成如下数据结构，其中item设计为list是为了在将章节具体url提交page_parse方法处理时，能够将其带入修改，直接传值会导致值不变
# item['name'] = ''
# item['des'] = ''
# item['auther'] = ''
# item['zhonglei'] = ''
# item['chapter'] = []
# item['chapter_count'] = ['0']
# item['chapter']={'chapter_name':'','chapter_url':'','chapter_content':['第一行','第二行','第三行','第n行']}

domain = 'https://www.xyangguiweihuo.com'
reg_chapter_content=r'br />(.*?)<br'
reg_chapter_list=r'<dd><a href ="(.*?)">(.*?)</a></dd>'
reg_chapter_auther=r'<meta property="og:novel:author" content="(.*?)"/>'
reg_novel_name=r'<meta property="og:novel:book_name" content="(.*?)"/>'
reg_novel_des=r'<meta property="og:description" content="(.*?)"/>'

class Dianzishu_Spider(scrapy.Spider):
    name='dianzishu'
    allowed_domains='xyangguiweihuo.com'
    start_urls=[
                 '{}/57/57010/'.format(domain)
                # '{}/56/56957/'.format(domain),
                # '{}/11/11518/'.format(domain),
                # '{}/15/11516/'.format(domain),
                ]

    # def start_requests(self):
    #     urls=[]
    #     file=open('./list1.txt', 'r', encoding='utf-8')  #读取文件文件中的页面地址信息
    #
    #     try:
    #         while True:
    #             line=file.readline()
    #             if line:
    #                 print(line)
    #                 url=json.loads(line)
    #                 urls.append(url['link'])
    #
    #             else:
    #                 break
    #     finally:
    #         file.close()
    #     urls=set(urls)
    #     for url in urls:
    #         yield scrapy.Request(url)

    def chapter_parse(self, response):
        item=response.meta['item']         #item通过response的meta携带过来，传址不传值
        chapter_content_temp = re.findall(reg_chapter_content, response.text)   #提取章节的内容
        count = item['chapter_count']  #计数器获得章节的总数，以便计算已经处理完毕的章节数
        for chapter in item['chapter']:          #在item的chapter的list中，查找章节url的对应的字典，以便将章节内容写入对应的章节字典
            if chapter['chapter_url']==response.url:
                content=chapter['chapter_content']
        for i in chapter_content_temp:
            i=i.replace('手机用户请浏览阅读，更优质的阅读体验。','').replace('&nbsp;','',30).replace('/r', '').replace(' ', '',100).replace('&1t;/p&gt;','',3).replace('\u3000','',30)
            content.append(i)
            print(i)
        print(content)
        count[0]=count[0]-1
        if count[0]<=0:
            print(r'小说“{}”下载完毕 ，提交储存'.format(item['name']))
            yield item
        else:
            print('《{}》还有 {} 章要下'.format(item['name'],count[0]))

    def parse(self, response):
        item=Dianzishu()
        item['name']=''
        item['des']=''
        item['auther']=''
        item['zhonglei']=''
        item['chapter']=[]
        item['chapter_count']=['0']
        print('开始分析页面')
        chapter_list=re.findall(reg_chapter_list,response.text)



        for i in chapter_list:
            if chapter_list.count(i)>1:
                chapter_list.remove((i))
                print('重复章节，丢弃',i)
        print(len(chapter_list))

        item['name']=re.findall(reg_novel_name,response.text)[0]
        item['chapter_count'][0]=len(chapter_list)
        item['des'] = re.findall(reg_novel_des,response.text)[0]
        item['auther'] = re.findall(reg_chapter_auther,response.text)[0]
        item['zhonglei'] =re.findall('<meta property="og:novel:category" content="(.*?)"/>',response.text)[0]



        print('提取到{}张',format(len(chapter_list)))



        for i in chapter_list:
            print(i)
            item['chapter'].append(dict(chapter_name=i[1],chapter_url='{}{}'.format(domain,i[0]),chapter_content=[]))

        print('小说 {} 分析完成,共 {} 章，作者是 {}，类型是 {}'.format(item['name'],item['chapter_count'][0],item['auther'],item['zhonglei']))

        for i in item['chapter']:
            print('提交  {}  章节'.format(i['chapter_name']))

            yield scrapy.Request(i['chapter_url'],callback=self.chapter_parse, dont_filter=True,meta={'item':item})
