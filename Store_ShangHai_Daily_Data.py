# -*- coding: utf-8 -*-
import pymysql
import Get_SHSE_Jsonp_Data as SHData


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


def dict2sql(dic, typename):
    items = ['marketValue', 'negotiableValue', 'trdVol', 'trdAmt', 'trdTm', 'profitRate', 'exchangeRate']
    data_name = ['date', 'market']
    data_val = list()
    data_val.append("'%s'" % dic['searchDate'])
    data_val.append("'%s'" % typename)

    # data_name.append(items[0])
    # data_val.append("'%s'" % dic[items[0]])

    for item in items:
        data_name.append(item)
        data_val.append("'%s'" % dic[item])
    return data_name, data_val


def store(data, con):
    try:
        with con.cursor() as cursor:
            for market in data:
                if market['productType'] == '1':
                    prod_type = u'A股'
                elif market['productType'] == '2':
                    prod_type = u'B股'
                elif market['productType'] == '12':
                    prod_type = u'上海市场'
                else:
                    continue

                key, value = dict2sql(market, prod_type)
                # sql = "select * from sh_stock_exchange_dairy_data"
                sql = """insert into shanghai_stock_exchange_dairy_stock_data(%s) VALUES(%s)""" % (','.join(key), ','.join(value))
                cursor.execute(sql)
                con.commit()
                # result = cursor.fetchall()
                # print result
    finally:
        con.close()


if __name__ == '__main__':

    web_url = "http://query.sse.com.cn/marketdata/tradedata/queryTradingByProdTypeData.do"
    # 想要获取数据的日期
    date_str = "2018-10-02"
    # 想要获取数据的类型——"gp":股票
    pro_type = "gp"
    raw_data = SHData.get_rawdata(web_url, date_str, pro_type)
    if not raw_data[0]['istVol']:
        print "There's no data today."
    else:
        connection = connect()
        store(raw_data, connection)



