import scrapy

# This spider is example of how to scrap data from category to product list page
class FakePlantsSpider(scrapy.Spider):
    name = 'fake-plants'
    allowed_domains = ['www.fake-plants.co.uk']
    start_urls = ['https://www.fake-plants.co.uk/']

    def parse(self, response):
        for category in response.xpath('//li[contains(@class,"product-category")]/a/@href'):
            yield response.follow(category.get(), callback=self.list_page_data)

    def list_page_data(self, response):
        for product in response.xpath('//ul[contains(@class,"product")]/li'):
            yield {
                "Name": product.xpath('.//h2[contains(@class,"product") and contains(@class,"title")]/text()').get().strip(),
                "Url": product.xpath('.//div[contains(@class,"summary")]/a[contains(@class,"link")]/@href').get(),
                "Cat": product.css('span.ast-woo-product-category::text').get().strip(),
            }
        