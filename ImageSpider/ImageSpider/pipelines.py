# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
class ImagespiderPipeline(object):
    def process_item(self, item, spider):
        return item

class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for img in item["img"]:
            yield Request(img)

