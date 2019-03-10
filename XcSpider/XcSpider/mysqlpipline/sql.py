import pymysql
from XcSpider import settings
import requests

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

db = pymysql.connect(host=MYSQL_HOSTS,user=MYSQL_USER,password=MYSQL_PASSWORD,port=MYSQL_PORT,database=MYSQL_DB,charset='utf8')
cursor = db.cursor()



class Sql():
    @classmethod
    def insert_db_xici(cls,country,ipaddress,port,serveraddr,isanonymous,type,alivetime,verificationtime):
        sql = 'insert into xicidaili(country,ipaddress,port,serveraddr,isanonymous,type,alivetime,verificationtime) values (%(country)s,%(ipaddress)s,%(port)s,%(serveraddr)s,%(isanonymous)s,%(type)s,%(alivetime)s,%(verificationtime)s)'
        value = {
            'country':country,
            'ipaddress':ipaddress,
            'port':port,
            'serveraddr':serveraddr,
            'isanonymous':isanonymous,
            'type':type,
            'alivetime':alivetime,
            'verificationtime':verificationtime
        }
        try:
            cursor.execute(sql,value)
            db.commit()
            print('插入成功')
        except Exception as e:
            print('插入失败----',e)
            db.rollback()

    @classmethod
    def select_name(cls,ipaddress):
        sql = 'select exists(select 1 from xicidaili where ipaddress=%(ipaddress)s)'
        value = {
            'ipaddress':ipaddress
        }
        cursor.execute(sql,value)
        return cursor.fetchall()[0]

class SelectMySQL():
    @classmethod
    def select_data(cls, ipaddress, type, port):
        try:
            proxy = type.lower() + '://' + ipaddress + ':' + str(port)
            url = 'http://www.baidu.com'
            protocol = 'https' if type == 'https' else 'http'
            proxies = {
                protocol: proxy,
            }
            print(proxies)
            try:
                print('开始请求')
                response = requests.get(url, proxies=proxies, timeout=5)
                print(response.status_code)
                if response.status_code == 200:
                    return True
            except:
                pass
        except:
            pass