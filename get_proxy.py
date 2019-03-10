# coding=utf-8
import requests
import pymysql



class SelectMySQL(object):
    def select_data(self):
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        host = 'localhost'
        user = 'root'
        passwd = 'ddd123'
        port = 3306
        db = 'db_xici'
        result = []
        sql = "select type,ipaddress,port,id from xicidaili"
        try:
            conn = pymysql.connect(host=host,
                                   port=port,
                                   user=user,
                                   passwd=passwd,
                                   db=db,
                                   charset='utf8', )
            cur = conn.cursor()
            cur.execute(sql)
            alldata = cur.fetchall()
            print(alldata)
            for res in alldata:
                proxy = res[0].lower() + '://' + res[1] + ':' + str(res[2])
                print(type(res[1]))
                url = 'http://www.baidu.com'
                protocol = 'https' if 'https' in res else 'http'
                proxies = {
                    protocol: proxy,
                }
                print(proxies)
                try:
                    print('开始请求')
                    response = requests.get(url, headers=headers, proxies=proxies, timeout=8)
                    print(response.status_code)
                    if response.status_code == 200:
                        print('这个人头送的好' + proxy)
                        result.append(proxy)
                    #从mysql删除无效ip
                    else:
                        print('删除无效代理')
                        del_sql = 'delete from xicidaili where id= {}'.format(res[3])
                        cur.execute(del_sql)
                        conn.commit()
                        print('删除成功')
                except :
                    print('删除无效代理')
                    del_sql = 'delete from xicidaili where id={}'.format(res[3])
                    cur.execute(del_sql)
                    conn.commit()
                    print('删除成功')

        except Exception as e:
            print('无法连接数据库Error msg: ' + e)
        finally:
            cur.close()
            conn.close()

        return result

    def get_result(self):

        results = self.select_data()
        print('The amount of datas: %d' % (len(results)))
        with open('proxy.txt', 'w') as f:
            for result in results:
                f.write(str(result) + '\n')
        print('Data write is over!')
        return results


if __name__ == '__main__':

    select = SelectMySQL()
    result1 = select.get_result()
    print(result1)