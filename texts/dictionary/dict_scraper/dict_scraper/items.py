# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DictScraperItem(Item):
    twi = Field()
    english = Field()
    pos = Field()
