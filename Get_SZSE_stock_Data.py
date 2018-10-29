# -*- coding: utf-8 -*-
import requests
import json


# def get_data(raw_daily_data):
    # print type()


def get_rawdata(url, search_date):

    r = requests.request("GET", url)
    # print r.text

    # 由json库中的方法将json直接解析成字典
    result = json.loads(r.text)
    # print type(result), len(result)
    data = result[0]['data']
    if not data:
        return None

    return data


if __name__ == '__main__':
    date_str = "2018-10-10"
    web_url = "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1803&TABKEY=tab1&txtQueryDate=" + date_str + "&random=0.6963441021133203"

    get_rawdata(web_url, date_str)

