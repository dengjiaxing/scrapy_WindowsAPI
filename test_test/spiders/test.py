import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class novalSpider(scrapy.Spider):
    name = "test"
    allowed_domains=["daomubiji.com"]
    #allowed_domains = ["lagou.com/zhaopin/"]
    start_urls = ["http://www.daomubiji.com/"]

    def parse(self, response):
    	print response.body