# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class FileItem(scrapy.Item):
    file_urls=scrapy.Field()
    file_path=scrapy.Field()
    file=scrapy.Field()
    file_down_log=scrapy.Field()

