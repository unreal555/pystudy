import mytools
import requests
import re
from lxml import html

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


for n in range(0,100):

    url='http://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word=%E6%88%BF%E8%B4%B7&x_bfe_rqs=03E80&x_bfe_tjscore=0.580106&tngroupname=organic_news&newVideo=12&pn={}'.format(10*n)
    print(url)
    result=requests.get(url,cookies=cookie)

    text=mytools.qu_kong_ge(result.text)


    while 1:
        print(url)
        print(text)
        print('''<!--STATUSOK-->''' in text)
        if  '''<!--STATUSOK-->''' in text:

            result=re.findall('''<h3class="c-title"><ahref=".*?"target="_blank">(.*?)</a>''',text)
            with open('./baidu.txt','r',encoding='utf-8') as f:
                all=f.read()


                for i in result:
                    x=mytools.qu_html_lable(i)

                    if x in all:
                        exit()

                    with open('./baidu.txt','a',encoding='utf-8') as f:

                        print(x)
                        f.write(x+'\r\n')
                        f.flush()

                mytools.random_wait(1,8)
                break
        else:
            mytools.random_wait(1,8)
            result=requests.get(url,cookies=cookie)

            text=mytools.qu_kong_ge(result.text)
            print('x')