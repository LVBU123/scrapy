from XcSpider.items import XcdlItem
from mysqlpipline.sql import Sql

class XiciDailiPipeline():
    def process_item(self,item,spider):
        if isinstance(item,XcdlItem):
            print('类型正确')
            ipaddress = item['ipaddress']
            ret = Sql.select_name(ipaddress)
            if ret[0] == 1:
                print('已经存在了。')
            else:
                print('开始插入')
                country = item['country']
                ipaddress = item['ipaddress']
                port = item['port']
                serveraddr = item['serveraddr']
                isanonymous = item['isanonymous']
                type = item['type']
                alivetime = item['alivetime']
                verificationtime = item['verificationtime']
                Sql.insert_db_xici(country,ipaddress,port,serveraddr,isanonymous,type,alivetime,verificationtime)
                print('插入完成')
        else:
            print('类型不对')