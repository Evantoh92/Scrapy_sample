# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChubbyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    calories = scrapy.Field()
    carbs = scrapy.Field()
    category = scrapy.Field()
    name = scrapy.Field()
    restaurant = scrapy.Field()
    
    '''restaurant = scrapy.Field()
    slug = scrapy.Field()'''
    
