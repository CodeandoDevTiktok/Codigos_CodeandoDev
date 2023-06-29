import scrapy
import pandas as pd

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/page/1/']
    
    # Esta lista contendrá todas las citas
    quotes_list = []

    def parse(self, response):
        for quote in response.css('div.quote'):
            self.quotes_list.append({
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            })

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        else:
            self.write_to_excel()

    def write_to_excel(self):
        df = pd.DataFrame(self.quotes_list)
        df.to_excel('quotes.xlsx', index=False)


