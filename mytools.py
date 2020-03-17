#!/bin/py
#   -*-coding:utf-8-*-

import random
from time import sleep
import base64
import re

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
     ]

Http_Proxy_List= ['',
                  'http://test2:594188@58.59.25.122:1234',
                  'http://test:594188@58.59.25.123:1234']
Https_Proxy_List=['',
                  'https://test2:594188@58.59.25.122:1234',
                  'https://test:594188@58.59.25.123:1234']



def get_Proxy(url):
    with open('./proxy.txt','r',encoding='utf-8') as f:
        content=re.sub('[\'|\s+]','',f.read())
    result=re.findall('\((.*?)\)',content)

    for i in result:

        ip,port,locate,des=i.split(',')
        # print(des=='HTTPS',des=='HTTP',des,type(des),len(des),len('HTTP'))
        if des=='HTTP':
            Http_Proxy_List.append('http://{}:{}'.format(ip,port))
        if des=='HTTPS':
            Https_Proxy_List.append('https://{}:{}'.format(ip,port))

    # print(Http_Proxy_List)
    # print(Https_Proxy_List)
    print(url.split('://')[0],type(url.split('://')[0]))
    if url.split('://')[0]=='http':
        print('选择http代理')
        proxies={'http':random.choice(Http_Proxy_List)}
        return proxies
    if url.split('://')[0]=='https':
        print('选择https代理')
        proxies={'http':random.choice(Https_Proxy_List)}
        return  proxies


def random_wait(n=1,m=3,*args):

    if not (isinstance(n,int) and isinstance(m,int)):
        print('参数输入错误，不是整数，采用默认值1，3')
        n=1
        m=3

    if n>m:
        n,m=m,n
    temp = random.randint(n, m)
    print("wait {} second".format(temp))
    sleep(temp)



def tras_header(s):

    temp=s.split('\n')
    # print(s)
    # print(strs)
    result={}
    for item in temp:
        key,value=item.split(': ')
        # print(key,value)
        result[key]=str(value)

    print('返回字典：',result)


    print
    print('{')
    for i in result:
        print('\'{}\':\'{}\','.format(i,result[i]))
    print('}')

    return result


if __name__ == '__main__':

    s=''':authority: you.ctrip.com
    :method: POST
    :path: /destinationsite/TTDSecond/SharedView/AsynCommentView
    :scheme: https
    accept: */*
    accept-encoding: gzip, deflate, br
    accept-language: zh-CN,zh;q=0.9
    content-length: 119
    content-type: application/x-www-form-urlencoded'''
    tras_header(s)

    proxies=get_Proxy('https://www.sohu.com')
    print(proxies)

    proxies=get_Proxy('http://www.sohu.com')
    print(proxies)