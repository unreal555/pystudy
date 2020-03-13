# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class PicItem(scrapy.Item):
    image_urls=scrapy.Field()
    image_path=scrapy.Field()
    image_log=scrapy.Field()
class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link=scrapy.Field()
    des=scrapy.Field()
    pic=scrapy.Field()
    video_link=scrapy.Field()

class Dianzishu(scrapy.Item):
    name=scrapy.Field()
    des=scrapy.Field()
    auther=scrapy.Field()
    zhonglei=scrapy.Field()
    chapter=scrapy.Field()
    chapter_count=scrapy.Field()

class WanBen(scrapy.Item):
    name=scrapy.Field()
    link=scrapy.Field()

class SkWen(scrapy.Item):
    name = scrapy.Field()
    des = scrapy.Field()
    auther = scrapy.Field()
    zhonglei = scrapy.Field()
    chapter = scrapy.Field()
    chapter_count = scrapy.Field()


        #
# class GuaZiErShouChe(scrapy.Ttem):
#     name=scrapy.Field()