# -*- coding: utf-8 -*-
import random

import os
import scrapy
from urllib import request

import time

from settings import headers
from items import LianjiaSpiderItem

class LjspiderSpider(scrapy.Spider):
    name = 'LJSpider'
    allowed_domains = ['lianjia.com']
    #start_urls = ['http://lianjia.com/']

    def start_requests(self):
        start_urls = []
        for page in range(1,5):
            url = 'https://cd.lianjia.com/zufang/jinjiang/pg{}l2rp3/#contentList'.format(page)
            start_urls.append(url)
        for start_url in start_urls:
            yield scrapy.Request(url=start_url,callback=self.parse,headers=headers,dont_filter=True)
    def parse(self, response):
        infos = response.xpath('//div[@class="content__list"]/div[@class="content__list--item"]')
        for info in infos:
            house_title = info.xpath('.//p[@class="content__list--item--title twoline"]/a/text()').extract()[0].strip()
            house_hrefs = info.xpath('.//p[@class="content__list--item--title twoline"]/a/@href').extract()[0].strip()
            house_href = 'https://cd.lianjia.com'+house_hrefs
            house_address = info.xpath('.//p[@class="content__list--item--des"]/a/text()').extract()
            house_addr = '-'.join(house_address)
            #print(house_addr)
            #time.sleep(random.choice(range(5)))
            yield scrapy.Request(url=house_href,callback=self.detail_parse,headers=headers,dont_filter=True,meta={'house_title':house_title,'house_href':house_href,'house_addr':house_addr})

    def detail_parse(self,response):
         infos = response.xpath('//div[@class="content clear w1150"]')
         for info in infos:
             house_nums = info.xpath('.//div[@class="content__subtitle"]/i[@class="house_code"]/text()').extract()[0].strip()
             house_num = house_nums.split('：')[-1]
             house_price = info.xpath('.//p[@class="content__aside--title"]/span/text()').extract()[0]
             house_price = house_price + '元/月'
             house_peoples = info.xpath('.//span[@class="contact_name"]/@title').extract()

             house_people = ''
             if len(house_peoples) != 0:
                 house_people = house_peoples[0]
             house_infos = info.xpath('.//p[@class="content__article__table"]//span/text()').extract()
             house_stytle,house_ting,house_size,house_fangxiang = house_infos[0],house_infos[1],house_infos[2],house_infos[3]
             house_imgdir = '/home/tlxy/tulingxueyuan/LianJiaSpider/LianJiaSpider/lianjia img'+'/'+response.meta['house_title']
             #print(house_imgdir)
             item = LianjiaSpiderItem()
             item['house_title'] = response.meta['house_title']
             item['house_href'] = response.meta['house_href']
             item['house_addr'] = response.meta['house_addr']
             item['house_num'] = house_num
             item['house_price'] = house_price
             item['house_people'] = house_people
             item['house_stytle'] = house_stytle
             item['house_ting'] = house_ting
             item['house_size'] = house_size
             item['house_fangxiang'] = house_fangxiang
             item['house_imgdir'] = house_imgdir

             yield item
             #
             # house_img_urls = response.xpath('.//div[@class="content__article__slide__item"]/img/@src').extract()[0]
             # if len(house_img_urls) != 0:
             #     for url in house_img_urls:
             #         img_name = str(time.time()) + '.jpg'
             #         if not os.path.exists(house_imgdir):
             #             os.makedirs(house_imgdir)
             #         request.urlretrieve(url,house_imgdir+'/'+img_name)

