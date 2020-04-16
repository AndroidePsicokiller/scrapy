# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

class NwprodsSpider(scrapy.Spider):
    name = 'nwprods'
    allowed_domains = ['sigmaaldrich.com/catalog/product/']
    #start_urls = ['https://www.sigmaaldrich.com/catalog/product/sigald/179337?lang=en&region=US']

    def start_requests(self):

        self.drive = webdriver.Chrome(r'C:\Users\Aziernicki\Documents\AA\Scrapy\chromedriver_win32\chromedriver')
        drive.get('https://www.sigmaaldrich.com/catalog/product/sigald/179337?lang=en&region=US')

    def parse(self, response):
        pass
        sel.xpath('//*[@class="product-details-inner"]//*[@class="sku"]/p/text()').extract()
        # a = Response.xpath('//*[@id="row179337-500ML"]')
