# -*- coding: utf-8 -*-
import os
import scrapy


class LanrentukuSpider(scrapy.Spider):
    name = 'lanrentuku'
    allowed_domains = ['lanrentuku.com']
    start_urls = ['http://www.lanrentuku.com/vector/flower/p1.html']
    # base_urls = 'http://www.lanrentuku.com/vector/flower/p%s.html'
    # for page in range(1,2):
    #     start_urls.append(base_urls % page)
    root_dir = 'tuku'
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

    def parse(self, response):
        dd_list = response.xpath('//div[@class="list-pic"]/dl/dd')
        for dd in dd_list:
            src = dd.xpath('./a/img/@src').extract()
            if len(src) != 0:
                src = src[0]
            else:
                src = ''

            href = dd.xpath('./a/@href').extract()
            if len(href) != 0:
                href = 'http://www.lanrentuku.com' + href[0]
                yield scrapy.Request(url=href,callback=self.detail_page)

    def detail_page(self,response):
        img = response.xpath('//div[@class="content-a"]/p/img/@src').extract()[0]
        yield  scrapy.Request(url=img,callback=self.download_pic)

    def download_pic(self,response):
        paths = response.url.split('/')[-1]
        filename = self.root_dir + "/" + paths
        with open(filename,'wb')as f:
            f.write(response.body)




