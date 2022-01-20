# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo                                                                       # importing pymongo library

class NetaporterPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient(                                              # connecting pymongo db
            'localhost',
            27017
        )
        db = self.conn['Akshay']
        self.collection = db['Scrapped_tb']                                            # collection name

    def process_item(self, item, spider):
        self.collection.insert(dict(item))                                             # inserting data
        return item
