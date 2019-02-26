# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MeijuPipeline(object):
    def process_item(self, item, spider):
        return item

class MeijuSpiderPipeline(object):
    def __init__(self):
        self.file = open('meiju.json','w',encoding='utf-8')
    def process_item(self,item):
        json.dump(dict(item),open('meiju.json','a'),ensure_ascii=False)
        return item
    def close_item(self):
        self.file.close()