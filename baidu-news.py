import mytools
import requests
import re
from lxml import html
import os
import time
import csv
from snownlp import SnowNLP

cookie='''
Bdpagetype: 3
Bdqid: 0xa7b4e0bd00199627
Cache-Control: private
Connection: keep-alive
Content-Encoding: gzip
Content-Type: text/html;charset=utf-8
Cxy_all: news+c71ed6154a66be9805cd64b17485852c
Cxy_ex: 1593424468+1149599857+04facb4783bb7a7f6e8dd636577c4939
Date: Mon, 29 Jun 2020 09:54:27 GMT
P3p: CP=" OTI DSP COR IVA OUR IND COM "
Server: BWS/1.1
Set-Cookie: BDRCVFR[C0p6oIjvx-c]=mk3SLVN4HKm; path=/; domain=.baidu.com
Set-Cookie: delPer=0; path=/; domain=.baidu.com
Set-Cookie: BD_CK_SAM=1;path=/
Set-Cookie: PSINO=5; domain=.baidu.com; path=/
Set-Cookie: BDSVRTM=528; path=/
Set-Cookie: H_PS_PSSID=; path=/; domain=.baidu.com
Strict-Transport-Security: max-age=172800
Traceid: 1593424467069695489012084530802497000999
Transfer-Encoding: chunked
Vary: Accept-Encoding
X-Ua-Compatible: IE=Edge,chrome=1'''

cookie=mytools.tras_header(cookie)
print(cookie)
headers=['title','url','laiyuan','shijian','senti']#%E6%88%BF%E8%B4%B7

keys=['房贷','商贷','公积金','首付','购房','买房','房价','房产税','楼盘','不动产','商品房','限购','限贷','土地拍卖','土拍','土地市场','地王','一手房','二手房','新房','房地产','楼市']
def do(key):

    for n in range(0,100):
        count=0
        url='http://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word={}&x_bfe_rqs=03E80&x_bfe_tjscore=0.580106&tngroupname=organic_news&newVideo=12&pn={}'.format(key,10*n)
        print(url)
        result=requests.get(url,cookies=cookie)

        text=mytools.qu_kong_ge(result.text)

        if os.path.exists('./{}.csv'.format(key)):
            with open('./{}.csv'.format(key),'r',encoding='utf-8') as f:
                all=f.read()
        else:
            all=''
            with open('./{}.csv'.format(key), 'w', newline='',encoding='utf-8-sig') as f:
                # 标头在这里传入，作为第一行数据
                writer = csv.DictWriter(f, headers)
                writer.writeheader()
                f.flush()


        while 1:
            print(url)
            print(text)
            print('''<!--STATUSOK-->''' in text)
            if  '''<!--STATUSOK-->''' in text:

                result=re.findall('''<h3class="c-title"><ahref="(.*?)data.*?target="_blank">(.*?)</a></h3>.*?<pclass="c-author">(.*?)&nbsp;&nbsp;(.*?)</p>''',text)
                print(result)
                for url,title,laiyuan,shijian in result:
                    item={}
                    item['url']=url.split('&')[0].replace('"','')
                    item['title']=mytools.qu_html_lable(title)
                    item['laiyuan'] = mytools.qu_html_lable(laiyuan)

                    item['shijian'] = mytools.qu_html_lable(shijian)

                    item['senti']=SnowNLP(item['title']).sentiments
                    if '前' in item['shijian']:
                        item['shijian']=time.strftime("%Y-%m-%d")


                    print(item)

                    if item['title'] in all:
                        print(item['title']+'已重复')
                        count=count+1

                        if count>8:
                            return


                    with open('./{}.csv'.format(key), 'a', newline='',encoding='utf-8-sig') as f:
                        writer = csv.DictWriter(f, headers)
                        writer.writerow(item)
                        f.flush()


                mytools.random_wait(1,8)
                break
            else:
                mytools.random_wait(1,8)
                result=requests.get(url,cookies=cookie)

                text=mytools.qu_kong_ge(result.text)
                print('x')

for key in keys:
    do(key)



