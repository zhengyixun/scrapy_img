# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PhtotoItem(scrapy.Item):
    # define the fields for your item here like:
    nickname = scrapy.Field()
    imgurl = scrapy.Field()
    # pass
