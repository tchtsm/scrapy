# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SlaveItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    direct = scrapy.Field()
    floor = scrapy.Field()
    decorat = scrapy.Field()
    start = scrapy.Field()
    village = scrapy.Field()
    position = scrapy.Field()
    user = scrapy.Field()
    phone = scrapy.Field()
    pass
