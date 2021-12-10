import scrapy

# This spider is example of how to scrape data from product list page which has pagination
class ToscrapeSpider(scrapy.Spider):
    name = 'toscrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com//']

    def parse(self, response):
        products = response.xpath('//ol/li')

        for product in products:
            yield {
                'Name': product.xpath('.//h3/a/@title').get(),
                'Price': product.xpath('.//div[contains(@class,"price")]/p[contains(@class,"price")]/text()').get(),
                'Url': response.urljoin(product.xpath('.//h3/a/@href').get())
            }

        next_page = response.xpath('//li[contains(@class,"next")]/a/@href').get()

        if next_page:
            yield response.follow(url=next_page, callback=self.parse)