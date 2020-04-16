# -*- coding: utf-8 -*-
import scrapy


class SigmaspiderSpider(scrapy.Spider):
    name = 'sigmaspider'
    allowed_domains = ['www.sigmaaldrich.com/catalog/product/']
    start_urls = ['http://www.sigmaaldrich.com/catalog/product/mm/106302?lang=en&region=US']

    def parse(self, response):
        next_page_url = [   '/mm/106302?lang=en&region=US',
                            '/mm/106302?lang=en&region=US',
                            '/mm/173017?lang=en&region=US',
                            '/mm/505145?lang=en&region=US',
                            '/sigma/56500?lang=en&region=US',
                            '/mm/807471?lang=en&region=US',
                            '/mm/814444?lang=en&region=US',
                            '/mm/817500?lang=en&region=US',
                            '/mm/818153?lang=en&region=US',
                            '/mm/821814?lang=en&region=US',
                            '/mm/845127?lang=en&region=US',
                            '/sigma/a7638?lang=en&region=US',
                            '/sial/d0710000?lang=en&region=US',
                            '/sigma/hutr00526?lang=en&region=US',
                            '/sigma/hutr02984?lang=en&region=US',
                            '/sigma/hutr02997?lang=en&region=US',
                            '/sigma/hutr03219?lang=en&region=US',
                            '/sigma/hutr03399?lang=en&region=US',
                            '/sigma/hutr03651?lang=en&region=US',
                            '/sigma/hutr08479?lang=en&region=US',
                            '/sigma/hutr08989?lang=en&region=US',
                            '/sigma/hutr09033?lang=en&region=US',
                            '/sigma/hutr09961?lang=en&region=US',
                            '/sigma/hutr10960?lang=en&region=US',
                            '/sigma/hutr12170?lang=en&region=US',
                            '/sigma/hutr12406?lang=en&region=US',
                            '/sial/l0551000?lang=en&region=US',
                            '/sial/m0400000?lang=en&region=US',
                            '/sigma/res3041t?lang=en&region=US',
                            '/sigma/res3041t?lang=en&region=US',
                            '/sial/s1000000?lang=en&region=US',
                            '/sial/s1100000?lang=en&region=US',
                            '/sial/y0000574?lang=en&region=US',
                            '/sial/05089?lang=en&region=US',
                            '/sigma/z720070?lang=en&region=US',
                            '/saj/270210?lang=en&region=US',
                            '/sigma/02071?lang=en&region=US',
                            '/sigma/02065?lang=en&region=US'
                            ]

        boxes = response.xpath('//*[@class="product-details-inner"]')
        for box in boxes:
            datos =
