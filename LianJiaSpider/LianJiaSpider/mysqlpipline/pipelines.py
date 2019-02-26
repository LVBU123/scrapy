from items import LianjiaSpiderItem
from mysqlpipline.sql import Sql

class XiciDailiPipeline():
    def process_item(self,item,spider):
        if isinstance(item,LianjiaSpiderItem):
            print('类型正确')
            house_title = item['house_title']
            ret = Sql.select_name(house_title)
            if ret[0] == 1:
                print('已经存在了。')
            else:
                print('开始插入')

                house_title = item['house_title']
                house_href = item['house_href']
                house_addr = item['house_addr']
                house_num = item['house_num']
                house_price = item['house_price']
                house_people = item['house_people']
                house_stytle = item['house_stytle']
                house_ting = item['house_ting']
                house_size = item['house_size']
                house_fangxiang = item['house_fangxiang']
                house_imgdir = item['house_imgdir']
                Sql.insert_db_xici(house_title,house_href,house_addr,house_num,house_price,house_people,house_stytle,house_ting,house_size,house_fangxiang,house_imgdir)
                print('插入完成')
        else:
            print('类型不对')