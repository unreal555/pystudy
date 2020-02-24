# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
from settings  import IMAGES_STORE
import scrapy
import shutil
import os
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
outHtml=0
outTxt=1


import codecs
import json
import re


class Normal_File_Pipeline(object):


    def __init__(self):# 初始化，打开文件
        pass

        # 这里用codecs库来打开文件，目的是编码不会出错

    def process_item(self, item, spider):  # 写入文件

        if spider.name=='wanben' or spider.name=='maomi':
            self.wanbenfile = codecs.open('./list1.txt', 'a', encoding="utf-8")
            print('储存list')
            lines = json.dumps(dict(item), ensure_ascii=False)+'\r\n'
            print(lines)
            self.wanbenfile.write(lines)
            print('写入完成')
            self.wanbenfile.close()
            return item
        else:
            return item
    def spider_closed(self, spider):  # 关闭文件
            pass
class Dianzishu_Pipeline(object):
    def process_item(self, item, spider):

        if spider.name!='dianzishu' or spider.name!='biquge':
            print('dfsafdkjasdklgaskjdhgakhdgkahsdkjgkajsdkjha')
            item = item
            reg=r'''[\$\#\&\@\{\}\[\]\(\)\-\=\+\^\%\?\"\'\s\!]*'''


            def check_file_name():
                item['name']=re.sub(reg,'',item['name'])

                item['auther'] = re.sub(reg, '', item['auther'])

                item['zhonglei'] = re.sub(reg, '', item['zhonglei'])


            check_file_name()

            if outHtml==0 and  outTxt==0:
                print("啥都不输出")

            if outTxt!=0:

                with open('./{}.{}.{}.txt'.format(item['name'],item['auther'],item['zhonglei']), 'w',encoding='utf-8') as file:
                    file.write(item['name'])
                    file.write('\r\n\r\n\r\n')

                    file.write('\t\t章节列表')
                    file.write('\r\n\r\n\r\n')

                    for i in item['chapter']:
                        line = '\t\t'+i['chapter_name'] + '\r\n'
                        file.write(line)

                    file.write('\r\n\r\n\r\n')
                    file.write('正文')
                    file.write('\r\n\r\n\r\n')

                    for i in item['chapter']:

                        file.write('\t'+i['chapter_name'])

                        file.write('\r\n\r\n')
                        for j in i['chapter_content']:
                            file.write(j+'\r\n')
                        file.write('\r\n\r\n')

                    file.close()
                    print('{}文本格式储存完毕'.format(item['name']))
            if outHtml!=0:

                with open('./{}.{}.{}.html'.format(item['name'],item['auther'],item['zhonglei']), 'w',encoding='utf-8') as file:
                    file.write(item['name'])
                    file.write('<br/>''<br/>')

                    file.write('\t\t章节列表')
                    file.write('<br/>''<br/>')

                    for i in item['chapter']:
                        print(line)
                        line = '\t\t'+ r'<a href="#{}">{}</a>'.format(i['chapter_name'],i['chapter_name']) + '<br/>'
                        file.write(line)

                    file.write('<br/>''<br/>')
                    file.write('正文')
                    file.write('<br/>''<br/>')

                    for i in item['chapter']:
                        file.write('<a name="{}"></a>'.format(i['chapter_name']))
                        file.write('{}'.format(i['chapter_name']))

                        file.write('<br/>''<br/>')

                        for j in i['chapter_content']:
                                file.write(j)
                                file.write('<br/>')

                        file.write('<br/>''<br/>')
                    file.close()
                    print('{}储存完毕'.format(item['name']))
        else:
            return item



class PicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):

        for image_url in item['image_urls']:

            yield scrapy.Request(image_url)

    def file_path(self, request, response=None, info=None):
        print('aaaaaaaa',request.url)
        filename=request.url.split('/')[-1]

        print(filename)

        return filename


    def item_completed(self, results, item, info):

        for url in  item['image_urls']:
            filename=os.path.join(IMAGES_STORE,url.split('/')[-1])
            path=os.path.join(IMAGES_STORE,item['image_path'])
            shutil.move(filename,path)
