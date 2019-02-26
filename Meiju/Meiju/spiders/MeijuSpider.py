# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from Meiju.items import MeijuSpiderItem
class MeijuspiderSpider(scrapy.Spider):
    name = 'MeijuSpider'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        content = etree.HTML(response.body.decode('GBK'))
        movies = content.xpath('//ul[@class="top-list fn-clear"]/li')
        for movie in movies:
            a_list = movie.xpath('./h5/a')
            a_name = a_list[0].text
            a_state = movie.xpath('./span[@class="state1 new100state1"]/font')[0].text
            item = MeijuSpiderItem()
            item['name'] = a_name
            item['state'] = a_state
            yield item
            