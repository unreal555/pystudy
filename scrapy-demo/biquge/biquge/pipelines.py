# -*- coding: utf-8 -*-
import scrapy
import mytools
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
space='\t'
enter='\r\n'



class BiqugePipeline:


    def process_item(self, item, spider):

        with open('./{}-{}-{}.txt'.format(item['title'],item['author'],item['category']),'a',encoding='utf-8') as f:
            f.write(item['title'])
            f.write(space+item['des'])
            f.write(enter)
            f.write(enter)

            f.write('目录')
            f.write(enter)
            f.write(enter)
            for i in item['chapter']:
                chapter_name=item['chapter'][i][0]
                f.write(space + chapter_name)
                f.write(enter)
                f.write(enter)




            for i in item['chapter']:
                chapter_name,chapter_content=item['chapter'][i]
                f.write(space + chapter_name)
                f.write(enter)
                for j in chapter_content:
                    j=mytools.qu_kong_ge(j)
                    j=mytools.qu_html_lable(j)
                    f.write(space+space + j)
                    f.write(enter)
                f.write(enter)
