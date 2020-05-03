# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:01:20 2020

@author: Aziernicki
"""


from scrapy.selector import Selector
import time
import requests
# requests import *
#from csv import writer



apiUrl_and_key = 'http://api.scrapestack.com/scrape?access_key=550d14c0f33c4fee2f4f39cce0079c2b'
headers_Option = 'keep_headers=1'
start_Url='http://www.cotodigital3.com.ar/sitios/cdigi/browse/categoria-ofertas/'
url_Objetivo = start_Url
iteracion = 0
errores = 0
items = 0
paginas = 0
start_time = time.strftime("%H:%M:%S", time.localtime())

while iteracion < 501:
    print('')
    print('Iteration: {0}'.format(iteracion))
    url = apiUrl_and_key+'&url='+url_Objetivo+'&'+headers_Option
    
    print('{0} - Get request...'.format(time.strftime("%H:%M:%S", time.localtime())))
    r = requests.get(url)
    
    try:
        print('{0} - Xpath query...'.format(time.strftime("%H:%M:%S", time.localtime())))    
        sel = Selector(text=r.text)
        productos = sel.xpath('//*[@class="product_info_container"]/a/@href').extract()
        next_page_url = sel.xpath('//*[@class="atg_store_pagination"]//*/a/@href').extract()[len(sel.xpath('//*[@class="atg_store_pagination"]//*/a/@href').extract())-1]
        
        print('{0} - Writting csv...'.format(time.strftime("%H:%M:%S", time.localtime())))
        with open('Apify_scraping.csv','a') as fd:
            for i in productos:
                d = '{0},{1}\n'.format(ascii(i),time.strftime("%H:%M:%S", time.localtime()))
                fd.write(d)


        url_Objetivo = 'https://www.cotodigital3.com.ar' + next_page_url
        paginas += 1
        items += len(productos)
    except:
        print('{0} - An exception ocurred...'.format(time.strftime("%H:%M:%S", time.localtime())))
        print('Wating 15 seconds to do the request again...')
        print(r.text)
        time.sleep(15)
        
        errores += 1
    
    iteracion += 1


       
with open('Apify_scraping.csv','a') as fd:
    d = 'Scraped pages:,{0}\nScraped items:,{1}\nErrors:,{2}\nIterations:,500\nStart time:,{3}\nEnd time:,{4}'.format(paginas,items, errores, start_time,time.strftime("%H:%M:%S", time.localtime()))
    fd.write(d)
    
print('Finished')