import scrapy
from web_scraper.items import marketitem
from datetime import datetime

class marketspider(scrapy.Spider):
    name='market'
    allowed_domains=["tgju.org"]
    start_urls=['https://www.tgju.org/']

    def parse(self,response):
        gold_18k=response.css("li#l-geram18 span.info_value span.info_price::text").get()
        ons_gold=response.css("li#l-ons span.info_value span.info_price::text").get()
        usd=response.css("li#l-price_dollar_rl span.info_value span.info_price::text").get()
        coin=response.css("li#l-sekeesc span.info_value span.info_price::text").get()

        item=marketitem()

        item['timestamp']=datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        item['gold_18k']=gold_18k
        item['ons_gold']=ons_gold
        item['usd']=usd
        item['coin']=coin


        yield item