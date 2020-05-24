#!/bin/py
#   -*-coding:utf-8-*-
import random
from time import sleep
import re
import sys
import os
import time
import win32api
import win32con

from zhon.hanzi import punctuation as ZHONG_WEN_BIAO_DIAN

from string import punctuation as YING_WEN_BIAO_DIAN

from string import ascii_lowercase as XIAO_XIE_ZI_MU

from string import ascii_uppercase as DA_XIE_ZI_MU

from string import digits as SHU_ZI

ZHONG_WEN_ZI_FU_FOR_RE=r'\u4e00-\u9fa5'

YING_WEN_ZI_FU_FOR_RE='a-zA-Z0-9'



USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',   #chrome
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',     #fireFox
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'                                              #IE11
     ]

Http_Proxy_List= ['',
                  'http://test2:594188@58.59.25.122:1234',
                  'http://test:594188@58.59.25.123:1234']

Https_Proxy_List=['',
                  'https://test2:594188@58.59.25.122:1234',
                  'https://test:594188@58.59.25.123:1234']

#装饰器,用于返回函数名和执行时间
def execute_lasts_time(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        lasts_time=time.time()-start_time
        print('%s执行时间为:%s'%(func.__name__,lasts_time),'\r')
        return result
    return warpper

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

def tras_header(str):
    '''定义返回值'''
    result={}

    '''以换行符转成list'''
    s=re.split('\n',str)
    print('转换成的list为',s)



    '''遍历每一行'''
    for item in s:
        '''如为空行，跳过'''
        print(item)
        if item.replace(' ','')=='':
            print('本行为空行，跳过')
            continue

        '''以冒号为分隔符分割元素'''
        print(re.split(': ',item))
        key,value=re.split(': ',item)
        print(key,value)

        result[key]=value

    print('{')
    for i in result:
        print('\'{}\':\'{}\','.format(i,result[i]))
    print('}')

    return result

def qu_kong_ge(s):
    if isinstance(s, str):
        return re.sub('\s+', '', s)
    else:
        print('老兄，给字符串')
        return 0

def qu_te_shu_zi_fu(s):
    if isinstance(s, str):
        return re.sub('[\/:*?"<>|]','-',)
    else:
        print('老兄，给字符串')
        return 0

def check_ban_quan(hour=24):   #思路，在sys.path目录下创建空文件，设置隐藏，只读属性，程序启动检查这三个文件的创建时间，任何
                                # 一个存在，且创建时间超过n小时的，返回真值,参数为允许运行的小时数,默认为24小时
                                 #返回为真，表示未到期，返回false，表示已到期
    debug=False

    if debug:print('程序期限为%s小时'%hour)
    qixian=hour*60*60

    def get_path():
        paths=[]
        for path in sys.path:
            if os.path.isdir(path):
                paths.append(os.path.join(path,'info.ini'))
        if debug:print(paths)
        return paths

    def creat_file(paths):
        for path in paths:
            if os.path.exists(path):
                pass
            else:
                # try:
                    with open(path,'w',encoding='utf-8') as f:
                        f.write(str(time.time()))
                    win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_HIDDEN)
                    win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_READONLY)
                # except:
                    pass

    def check(paths):    #检测文件是不是存在，存在返回创建和运行的时间差，不存在返回0
        for path in paths:

            # print(path)
            if os.path.exists(path):
                try:
                    with open(path,'r',encoding='utf-8') as f:
                        creat_time=f.read()
                        creat_time=float(creat_time)
                        lasts=time.time()-creat_time    #day:86400    hour:3600
                        return lasts
                    break
                except:
                    pass
            return False

    paths=get_path()
    lasts=check(paths)
    if lasts==False:
        creat_file(paths)
    if abs(lasts)>qixian:
        print('到期,程序退出')
        return False
    else:
        print('程序加载中')
        return True

@execute_lasts_time             ###清除版权信息
def clean_ban_quan():
    debug=False
    def get_path():
        paths=[]
        for path in sys.path:
            if os.path.isdir(path):
                try:
                    win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_HIDDEN)
                    win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_READONLY)
                    paths.append(os.path.join(path,'info.ini'))
                except Exception as e:
                    if debug:print(e)
        if debug:print(paths)
        return paths

    def clean(paths):
        for path in paths:
            print('REMOVE',path)
            if os.path.isfile(path):
                try:

                    win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_NORMAL)
                    os.remove(path)
                    print('REMOVE',path)
                except:
                    pass

    paths=get_path()
    clean(paths)

if __name__ == '__main__':

    s='''
accept-ranges: bytes
access-control-allow-methods: GET
access-control-allow-origin: *
age: 294
ali-swift-global-savetime: 1588878378
content-length: 7979
content-md5: UJMfxWiVhhfRcmnrdBQcPQ==
content-type: text/css; charset=utf-8
date: Sun, 24 May 2020 03:58:13 GMT
eagleid: 2f66ea9c15902929872341717e
etag: "50931FC568958617D17269EB74141C3D"
last-modified: Wed, 15 Aug 2018 12:37:31 GMT
server: Tengine
status: 200
timing-allow-origin: *
vary: Accept-Encoding
via: cache2.cn1806[0,200-0,H], cache8.cn1806[,0]
x-alicdn-tsign-info: One slice success
x-cache: HIT TCP_MEM_HIT dirn:0:163120335
x-oss-cdn-auth: success
x-oss-hash-crc64ecma: 10640200318906159902
x-oss-object-type: Normal
x-oss-request-id: 5EC9F0D58C697F70356EC4D7
x-oss-server-time: 1
x-oss-storage-class: Standard
x-swift-cachetime: 900
x-swift-savetime: Sun, 24 May 2020 03:58:13 GMT
    '''

    s=tras_header(s)
    print(s)




