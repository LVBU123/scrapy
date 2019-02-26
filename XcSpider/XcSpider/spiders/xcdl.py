# -*- coding: utf-8 -*-
import scrapy
from XcSpider.items import XcdlItem

class XcdlSpider(scrapy.Spider):
    name = 'xcdl'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/']

    def parse(self, response):
        tr1 = response.xpath('//tr[@class="odd"]')
        tr2 = response.xpath('//tr[@class=""]')
        trs = tr1 + tr2
        infos = XcdlItem()
        for tr in trs:
            countries = tr.xpath('./td[@class="country"]/img/@src').extract()
            if countries != []:
                country = countries[0]
            else:
                country = ''
            ipaddress = tr.xpath('./td[2]/text()').extract()
            try:
                ipaddress = ipaddress[0]
            except:
                ipaddress = ''
            port = tr.xpath('./td[3]/text()').extract()
            try:
                port = port[0]
            except:
                port = ''
            serveraddr = tr.xpath('./td[4]/text()').extract()
            try:
                serveraddr = serveraddr[0]
            except:
                serveraddr = ''
            isanonymous = tr.xpath('./td[5]/text()').extract()
            try:
                isanonymous = isanonymous[0]
            except:
                isanonymous = ''
            type = tr.xpath('./td[6]/text()').extract()
            try:
                type = type[0]
            except:
                type = ''
            alivetime = tr.xpath('./td[7]/text()').extract()
            try:
                alivetime = alivetime[0]
            except:
                alivetime = ''
            verificationtime = tr.xpath('./td[8]/text()').extract()
            try:
                verificationtime = verificationtime[0]
            except:
                verificationtime = ''

            print(ipaddress,port,serveraddr,isanonymous,type,alivetime,verificationtime)
            infos['country'] = country
            infos['ipaddress'] = ipaddress
            infos['port'] = port
            infos['serveraddr'] = serveraddr
            infos['isanonymous'] = isanonymous
            infos['type'] = type
            infos['alivetime'] = alivetime
            infos['verificationtime'] = verificationtime
            yield infos

