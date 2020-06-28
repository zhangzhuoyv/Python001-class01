# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# 明确目标，前 10 个电影名称、电影类型和上映时间
import scrapy


# class SpidersItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class SpidersItem(scrapy.Item):
    name = scrapy.Field() #电影名称
    tag = scrapy.Field()   #电影类型
    time =scrapy.Field()    #上映时间
