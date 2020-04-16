# -*- coding: utf-8 -*-
import scrapy


class PreciosCotoSpider(scrapy.Spider):
    name = 'precios_coto'
    allowed_domains = ['cotodigital3.com.ar']
    start_urls = ['https://cotodigital3.com.ar/sitios/cdigi/browse/categoria-ofertas/', 'https://cotodigital3.com.ar/sitios/cdigi/']

    def parse(self, response):

        productos = response.xpath('//*[@class="product_info_container"]/a/@href').extract()
        for url in productos:
            yield {'Product Url':url}

        next_page_url = response.xpath('//*[@class="atg_store_pagination"]//*/a/@href').extract_first()

        if next_page_url is not None:
            absolute_next_page_url = 'https://www.cotodigital3.com.ar' + next_page_url
            print(absolute_next_page_url)
            next_page = response.urljoin(absolute_next_page_url)

            yield scrapy.Request(next_page, callback=self.parse)




        #yield scrapy.Request(absolute_next_page_url) --- , callback=self.parse
        #PreciosCotoSpider.callback=scrapy.Request(absolute_next_page_url)
