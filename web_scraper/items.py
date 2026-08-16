# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass
import scrapy

@dataclass
class WebScraperItem:
    # define the fields for your item here like:
    # name: str | None = None
    pass


class marketitem(scrapy.Item):
    timestamp=scrapy.Field()
    gold_18k=scrapy.Field()
    ons_gold=scrapy.Field()
    usd=scrapy.Field()
    coin=scrapy.Field()