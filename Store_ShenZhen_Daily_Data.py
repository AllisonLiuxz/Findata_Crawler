# -*- coding: utf-8 -*-
import pymysql
import Get_SZSE_stock_Data as SZData


def connect():
    # 数据库连接配置
    config = {
        'host': '192.168.202.44',
        'port': 3306,
        'user': 'blizzard',
        'password': 'Blizzard1234!',
        'db': 'internet_data',
        'charset': 'utf8mb4'
    }
    # 创建连接
    conn = pymysql.connect(**config)
    return conn


def dict2sql(dic, date):
    items = ['zbmc', 'brsz', 'bsrzj', 'fd', 'bnzg', 'zgzrq']
    data_name = ['date']
    data_val = list()
    data_val.append("'%s'" % date)

    for item in items:
        data_name.append(item)
        data_val.append("'%s'" % dic[item])
    return data_name, data_val


def store(data, con, date):
    try:
        with con.cursor() as cursor:
            for index in data:
                key, value = dict2sql(index, date)
                sql = """insert into shenzhen_stock_exchange_dairy_stock_data(%s) VALUES(%s)""" % (','.join(key), ','.join(value))
                cursor.execute(sql)
                con.commit()
                # result = cursor.fetchall()
                # print result
    finally:
        con.close()


if __name__ == '__main__':

    # 想要获取数据的日期
    date_str = "2018-10-08"
    web_url = "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1803&TABKEY=tab1&txtQueryDate=" + date_str + "&random=0.6963441021133203"

    raw_data = SZData.get_rawdata(web_url, date_str)

    if not raw_data:
        print "There's no data today."
    else:
        connection = connect()
        store(raw_data, connection, date_str)



