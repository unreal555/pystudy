# -*- coding: utf-8 -*-
from scrapy.pipelines.files import FilesPipeline
from scrapy.http import Request
import scrapy
import shutil
import os
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html




class LoPipeline(FilesPipeline):
    print('sssssss')

    def get_media_requests(self, item, info):
        print('aaaaaaaa')
        print('start {} download'.format(item['file_urls']))
        yield scrapy.Request(item['file_urls'])

    # def file_path(self, request, response=None, info=None):
    #     print('aaaaaaaa',request.url)
    #     filename=request.url.split('/')[-1]
    #     print(filename)
    #     return filename


    def item_completed(self, results, item, info):
        print(item)
        print(results)
        for i in results:
            if i[0]==True:
                shutil.move('e://'+i[1]['path'],item['file_path'])


