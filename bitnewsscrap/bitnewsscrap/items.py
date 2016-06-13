# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class BitnewsscrapItem(scrapy.Item):
    # define the fields for your item here like:

    title = Field()
    description = Field()
    link = Field()
    pubdate = Field()

class BitnewsscrapItem2(scrapy.Item):
    # define the fields for your item here like:

    title = Field()
    description = Field()
    link = Field()
    image = Field()
    pubdate = Field()