import pymysql
import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

db = pymysql.connect(host=MYSQL_HOSTS,user=MYSQL_USER,password=MYSQL_PASSWORD,port=MYSQL_PORT,database=MYSQL_DB,charset='utf8')
cursor = db.cursor()

class Sql():
    @classmethod
    def insert_db_xici(cls,house_title,house_href,house_addr,house_num,house_price,house_people,house_stytle,house_ting,house_size,house_fangxiang,house_imgdir):
        sql = 'insert into lianjia(house_title,house_href,house_addr,house_num,house_price,house_people,house_stytle,house_ting,house_size,house_fangxiang,house_imgdir) values (%(house_title)s,%(house_href)s,%(house_addr)s,%(house_num)s,%(house_price)s,%(house_people)s,%(house_stytle)s,%(house_ting)s,%(house_size)s,%(house_fangxiang)s,%(house_imgdir)s)'
        value = {
            'house_title':house_title,
            'house_href':house_href,
            'house_addr':house_addr,
            'house_num':house_num,
            'house_price':house_price,
            'house_people':house_people,
            'house_stytle':house_stytle,
            'house_ting':house_ting,
            'house_size':house_size,
            'house_fangxiang':house_fangxiang,
            'house_imgdir':house_imgdir
        }
        try:
            cursor.execute(sql,value)
            db.commit()
            print('插入成功')
        except Exception as e:
            print('插入失败----',e)
            db.rollback()

    @classmethod
    def select_name(cls,house_title):
        sql = 'select exists(select 1 from lianjia where house_title=%(house_title)s)'
        value = {
            'house_title':house_title
        }
        cursor.execute(sql,value)
        return cursor.fetchall()[0]
