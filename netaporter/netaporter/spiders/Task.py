import scrapy
from ..items import NetaporterItem


class TaskSpider(scrapy.Spider):
    name = 'Task'
    start_urls = [
        # 'https://www.net-a-porter.com/en-in/shop/clothing/tops'                      # links to be crawled
        'https://www.net-a-porter.com/en-in/shop/shoes'                                # links to be crawled
    ]

    def parse(self, response):
        items = NetaporterItem()                                                       # creating instance

        products = response.css('.ProductItem24__p')                                   # General selection of all items

        for a in products:                                                             # using loop to get required details of each items

            name = a.css('.ProductItem24__name::text').extract()                       # using css selector extracting required details
            brand = a.css('.ProductItem24__designer::text').extract()
            price = a.css('.PriceWithSchema9__value span::text').extract()
            image = a.css('.Image18__image::attr(src)').extract()
            product_url = a.css('::attr(content)').extract()
            category = ['footwear']

            items['Name'] = name
            items['Brand'] = brand
            items['Original_price'] = price
            items['Sale_price'] = price
            items['Image_url'] = image
            items['Product_page_url'] = product_url
            items['Product_category'] = category

            yield items

            next_page = response.css('.Pagination7__next::attr(href)').get()           # used for extracting details of upto 25 pages
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)