import scrapy

class WhiskySpider(scrapy.Spider):
    name = "whisky"
    user_agent = 'Google Chrome/106.0 (Kali Linux x86_64) Gecko/20100101'
    start_urls = ["https://www.whiskyshop.com/scotch-whisky/all?item_availability=In+Stock"]

    def parse(self, response):
        for products in response.css("div.product-item-info"):
            try:
                yield {
                    "name": products.css('a.product-item-link::text').get(),
                    "price": products.css('span.price::text').get().replace("£", ""),
                    "link": products.css('a.product-item-link').attrib["href"] 
                }
            except:
                yield {
                    "name": products.css('a.product-item-link::text').get(),
                    "price": "not presented",
                    "link": products.css('a.product-item-link').attrib["href"] 
                }


        next_page = response.css("a.action.next")
        if next_page:
            link = next_page.attrib["href"]
            if link is not None:
                yield response.follow(link, callback=self.parse)
        