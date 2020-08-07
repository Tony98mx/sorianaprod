# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SorianapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    pricel = scrapy.Field()
    priceh = scrapy.Field()
    percent = scrapy.Field()
    direccion = scrapy.Field()
