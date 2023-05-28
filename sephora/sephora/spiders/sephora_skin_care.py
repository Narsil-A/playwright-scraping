import scrapy
from scrapy_playwright.page import PageMethod

class SephoraSkinCareSpider(scrapy.Spider):
    name = "sephora_skin_care"
    
    custom_settings = {
        'FEEDS':{
            'pdbdata.json':{'format':'json', 'overwrite':True}
        }
    }

    def start_requests(self):
        yield scrapy.Request('https://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.structure_determination_methodology%22%2C%22operator%22%3A%22exact_match%22%2C%22value%22%3A%22experimental%22%7D%7D%5D%2C%22logical_operator%22%3A%22and%22%7D%5D%2C%22logical_operator%22%3A%22and%22%2C%22label%22%3A%22text%22%7D%5D%2C%22logical_operator%22%3A%22and%22%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22scoring_strategy%22%3A%22combined%22%2C%22results_content_type%22%3A%5B%22experimental%22%5D%2C%22paginate%22%3A%7B%22start%22%3A0%2C%22rows%22%3A25%7D%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22query_id%22%3A%22e0fff76e6009d1aefc3970505b66f430%22%7D%7D', 
        meta= dict(
            playwright = True,
            playwright_include_page = True,
            playwright_page_methods = [
                PageMethod('wait_for_selector', 'div.results-item')
            ]
        ))


    async def parse(self, response):

        for product in response.css('div.results-item'): # this selector is the problem
            
            yield {
            'title':product.css('h4 a::::text').get(),
            'link':product.css('a::attr(href)::text').get(),
            'authors':product.css('p a span::text').get()
        }
