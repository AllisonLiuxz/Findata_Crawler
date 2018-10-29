# -*- coding: utf-8 -*-
import requests
import json


# def get_data(raw_daily_data):
    # print type()


def get_rawdata(url, search_date, prod_type):
    querystring = {"jsonCallBack": "jsonpCallback11398",
                   "searchDate": search_date,
                   "prodType": prod_type,
                   "_": "1539697296432"
                   }
    headers = {'Referer': "http://www.sse.com.cn/market/stockdata/overview/day/",
               'cache-control': "no-cache",
               'Postman-Token': "caeab566-4ca8-4787-9bac-8a849cf31776"
               }

    # 返回 Response 对象
    r = requests.request("GET", url, headers=headers, params=querystring)

    # text属性（其实是装饰器将由text方法变的）会返回处理好的网页内容，是unicode格式的字符串
    # 需转换成string处理成json数据的格式
    result = str(r.text)[19:-1]
    # print result

    # 由json库中的方法将json直接解析成字典
    result = json.loads(result)
    # print result, type(result)

    raw_data = result['result']
    # print raw_data[0]
    return raw_data


if __name__ == '__main__':

    web_url = "http://query.sse.com.cn/marketdata/tradedata/queryTradingByProdTypeData.do"
    date_str = "2018-10-10"
    pro_type = "gp"
    data = get_rawdata(web_url, date_str, pro_type)














"""
# js拿数据，Python调用js方法，较复杂不推荐
import execjs


def get_js():
    js_f = open(".js", 'r', encoding='UTF-8')
    line = js_f.readline()
    file_str = ''
    while line:
        file_str += line
        line = js_f.readline()
    return file_str


def run_js(datastr):
    js_str = get_js()
    com_js = execjs.compile(js_str)
    com_js.call(, 'datastr')

"""
