# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class PicItem(scrapy.Item):
    image_urls=scrapy.Field()
    image_path=scrapy.Field()
    image_log = scrapy.Field()

