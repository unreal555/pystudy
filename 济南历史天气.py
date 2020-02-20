#!/bin/py


import  requests
import json
import re
from time import sleep
import csv

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

def getWeather(url):

    response=requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code!=200:
        return(0)
    page=response.content.decode('gbk')
    result = re.findall(
        r'''{ymd:'(.*?)',bWendu:'(.*?)',yWendu:'(.*?)',tianqi:'(.*?)',fengxiang:'(.*?)',fengli:'(.*?)',aqi:'(.*?)',aqiInfo:'(.*?)',aqiLevel:'(.*?)'}''',
        page)
    print(result)

    with open('weather.csv','a',encoding='utf-8') as f:
        writer=csv.writer(f)
        for i in result:
            writer.writerow(i)
        f.close()

for year in range(2020,2010,-1):
    for month in range(12,0,-1):
        url='http://tianqi.2345.cn/com/wea_history/js/{}{:0>2}/54823_{}{:0>2}.js'.format(year,month,year,month)
        print(url)
        getWeather(url)





