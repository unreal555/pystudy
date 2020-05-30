# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class PicItem(scrapy.Item):
    chapter_urls=scrapy.Field()
    book_path=scrapy.Field()
    book_url = scrapy.Field()

