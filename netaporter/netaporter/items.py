# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NetaporterItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    Brand = scrapy.Field()
    Original_price = scrapy.Field()
    Sale_price = scrapy.Field()
    Image_url = scrapy.Field()
    Product_page_url = scrapy.Field()
    Product_category = scrapy.Field()

