# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:11:27 2020

@author: Aziernicki
"""

from selenium import webdriver
from scrapy.selector import Selector
from time import sleep
#import csv

urls = ['https://www.sigmaaldrich.com/catalog/product/mm/106302?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/mm/106302?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/mm/173017?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigald/179337?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigald/179337?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigald/179337?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/aldrich/192732?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/aldrich/362832?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/41698?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigald/459828?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/mm/505145?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/56500?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/76245?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/mm/807471?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/mm/814444?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/mm/817500?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/mm/818153?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/mm/821814?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/mm/845127?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/92835?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/a5597?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/a7638?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sial/d0710000?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/hutr00526?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/hutr02984?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/hutr02997?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/hutr03219?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/hutr03399?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/hutr03651?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/hutr08479?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/hutr08989?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/hutr09033?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/hutr09961?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/hutr10960?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/hutr12170?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/hutr12406?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sial/l0551000?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sial/m0400000?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/aldrich/o5500?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/res3041t?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/res3041t?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sial/s1000000?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sial/s1100000?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sial/y0000574?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sial/05089?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/z720070?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/saj/270210?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/02071?lang=en&region=US',
'https://www.sigmaaldrich.com/catalog/product/sigma/02065?lang=en&region=US'
]

drive = webdriver.Chrome(r'C:\Users\Aziernicki\Documents\AA\Scrapy\chromedriver_win32\chromedriver')
#drive.get('https://www.sigmaaldrich.com/catalog/product/sigald/179337?lang=en&region=US')
for url in urls:
    
    drive.get(url)
    sleep(5)
    sel = Selector(text=drive.page_source)
    title = sel.xpath('//*[@itemprop="name"]/text()').extract_first()
    desc = sel.xpath('//*[@itemprop="description"]/text()').extract_first()
    sku = sel.xpath('//*[@class="product-details-inner"]//*[@class="sku"]/p/text()').extract()
    size = []
    for it in sku:
        row = "row"+it
        a = sel.xpath('//*[@class="product-details-inner"]//*[@id="{0}"]//*[@class="packSize"]/text()'.format(row)).extract_first()
        size.append(a)
    
    skuPack = set(zip(sku,size))
    
    with open('scrapCabeza.csv','a') as fd:
        for i in skuPack:
            d = '{0},{1},{2},{3}\n'.format(title,desc,i[0],i[1])
            fd.write(d)
            