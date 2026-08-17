# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
from pathlib import Path


class WebScraperPipeline:
    def open_spider(self,spider):
        self.file_path = Path("data/raw/price.csv")

        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        file_exists = (
            self.file_path.exists()
            and self.file_path.stat().st_size > 0
        )

        self.file = open(
            self.file_path,
            "a",
            newline="",
            encoding="utf-8"
        )

        self.writer = csv.DictWriter(
            self.file,
            fieldnames=[
                "timestamp",
                "gold_18k",
                "ons_gold",
                "silver",
                "coin"
            ]
        )

        if not file_exists:
            self.writer.writeheader()


    def process_item(self, item,spider):
        self.writer.writerow(dict(item))
        
        return item

    def close_spider(self,spider):
           self.file.close()
   
