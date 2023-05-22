import scrapy
from scrapy_playwright.page import PageMethod

class SephoraSkinCareSpider(scrapy.Spider):
    name = "sephora_skin_care"
    
    custom_settings = {
        'FEEDS':{
            'sephoradata.json':{'format':'json', 'overwrite':True}
        }
    }

    def start_requests(self):
        yield scrapy.Request('https://www.sephora.com/shop/skincare', 
        meta= dict(
            playwright = True,
            playwright_include_page = True,
            playwright_page_methods = [
                PageMethod('wait_for_selector', 'div#css-1322gsb')
            ]
        ))


    async def parse(self, response):

        for product in response.css('div.css-1qe8tjm'):
            
            yield {
            'title':product.css('span.css-12z2u5.eanm77i0::text').get()
        }
