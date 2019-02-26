import scrapy
from ImageSpider.items import ImageItem
class ImageSpider(scrapy.Spider):
    name = 'Image'
    allow_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self,response):
        item = ImageItem()
        imgs = response.css(".post img::attr(src)").extract()
        item['img'] = imgs
        yield item
