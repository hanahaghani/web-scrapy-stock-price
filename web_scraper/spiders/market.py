import scrapy
from web_scraper.items import marketitem
from datetime import datetime
import requests
import asyncio


class marketspider(scrapy.Spider):
    name = 'market'
    allowed_domains = ["tgju.org"]

    start_urls = [
        'https://call4.tgju.org/ajax.json?rev=XjM9klM7SZvEdbsegxr3y3K3i3fZyi79VnB3ACfQhUTFLoakHIDorJz3nfT4'
    ]

    async def start(self):
        response = await asyncio.to_thread(
            requests.get,
            self.start_urls[0],
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        current = data['current']

        gold_18k = current['geram18']
        ons_gold = current['ons']
        silver = current['silver_999']
        coin = current['sekee']

        item = marketitem()

        item['timestamp'] = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        item['gold_18k'] = gold_18k['p']
        item['ons_gold'] = ons_gold['p']
        item['silver'] = silver['p']
        item['coin'] = coin['p']

        yield item