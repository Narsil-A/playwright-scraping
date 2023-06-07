import scrapy
from scrapy_playwright.page import PageMethod
import time
class SephoraSkinCareSpider(scrapy.Spider):
    name = "sephora_skin_care"
    
    custom_settings = {
        'FEEDS':{
            'pdbdata.json':{'format':'json', 'overwrite':True}
        }
    }

    def start_requests(self):
        yield scrapy.Request('https://www.sephora.com/shop/skincare/', 
        meta= dict(
            playwright = True,
            playwright_include_page = True,
            playwright_page_methods = [
                PageMethod('wait_for_selector', 'div.ProductGrid'),
                PageMethod('evaluate', "window.scrollBy(0, document.body.scrolHeight)"),
                # PageMethod('scroll_to', 'document.body.scrollHeight'),
            ],
            errback = self.errback
        ))


    async def parse(self, response):

        for product in response.css('a.css-klx76'): # this selector is the problem
            
            yield {
            'title':product.css('span.css-12z2u5.eanm77i0::text').get(),
        }

    #         # Add a delay of 1 second before making the next request
    #     time.sleep(3)
        
    #     # Scroll to the bottom of the page again
    #     await self.scroll_to_bottom(response)

    # async def scroll_to_bottom(self, response):
    #     await response.playwright_page.scroll_to(0, 0)  # Scroll to the top first
    #     await response.playwright_page.scroll_to(0, "document.body.scrollHeight")

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()