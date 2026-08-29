import scrapy
from web_scraper.items import marketitem
from datetime import datetime

class marketspider(scrapy.Spider):
    name='market'
    allowed_domains=["tgju.org"]
    #api url
    start_urls=['https://call2.tgju.org/ajax.json?rev=Yt2ebnCSHS0J1dKrN7wGxtpR3g9t28WVgweDXFYgrGTcBEbsXyxKgBnDEcHq']

    def parse(self,response):

        data=response.json()

        current=data['current']
        
        gold_18k=current['tgju_gold_irg18']
        gold_18k_p=gold_18k['p']

        ons_gold=current['ons']
        ons_gold_p=ons_gold['p']

        silver=current['silver_999']
        silver_p=silver['p']

        coin=current['sekee']
        coin_p=coin['p']

        item=marketitem()

        item['timestamp']=datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        item['gold_18k']=gold_18k_p
        item['ons_gold']=ons_gold_p
        item['silver']=silver_p
        item['coin']=coin_p


        yield item