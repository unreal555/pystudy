# coding: utf-8
# Team : None
# Author：zl
# Date ：2020/6/30 0030 上午 9:00
# Tool ：PyCharm

import requests
import random
import re
import time
import string
from zhon.hanzi import punctuation as ZHONG_WEN_BIAO_DIAN
from string import punctuation as YING_WEN_BIAO_DIAN
from string import ascii_lowercase as XIAO_XIE_ZI_MU
from string import ascii_uppercase as DA_XIE_ZI_MU
from string import digits as SHU_ZI

ZHONG_WEN_ZI_FU_FOR_RE=r'\u4e00-\u9fa5'

YING_WEN_ZI_FU_FOR_RE='a-zA-Z0-9'

USER_AGENT_LIST = {
    'chrome':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',   #chrome
    'firefox':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',     #fireFox
    'ie':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'                                              #IE11
}

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
    if not (isinstance(n, (int, float)) and isinstance(m, (int, float))):
        print('参数输入错误，不是整数或小数，采用默认值1，3')
        n=1
        m=3

    if n>m:
        n,m=m,n
    temp = random.uniform(n, m)
    print("wait {} second".format(temp))
    time.sleep(temp)

def get_random_str(lenth=8):
    return ''.join(random.sample(string.ascii_letters + string.digits, lenth))

def get_random_num(n=1,m=3,*args):
    if not (isinstance(n, (int, float)) and isinstance(m, (int, float))):
        print('参数输入错误，不是整数或小数，采用默认值1，3')
        n=1
        m=3

    if n>m:
        n,m=m,n
    temp = random.uniform(n, m)
    return temp



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
        key=qu_kong_ge(key)
        if key[0]==':':
            key=key[1:]

        result[key]=value

    print('{')
    for i in result:
        print('\'{}\':\'{}\','.format(i,result[i]))
    print('}')
    print(result)
    return result

def qu_kong_ge(s):
    if isinstance(s, str):
        return re.sub('\s+', '', s)
    else:
        print('老兄，给字符串')
        return 0

def qu_str(source,grabage):      #去除source中的垃圾,grabage为list,存储垃圾
    target=source
    print(grabage)
    if len(grabage)==0 :
        print('要消除的字符串是什么？')
        return 1

    if not isinstance(grabage, list):
        print('垃圾信息只接受队列')
        return 1

    if (not isinstance(source,str)) or source=='':
        print('原始字符串错误')
        return 2

    for i in grabage:
        target=target.replace(i,'')
    return target

def qu_html_lable(s):
    reg = re.compile(r'<[^>]+>', re.S)
    if isinstance(s, str):
        return reg.sub('', s)
    else:
        print('老兄，给字符串')
        return 0

def qu_te_shu_zi_fu(s):
    if isinstance(s, str):
        return re.sub('[\/:*?"<>|]','-',s)
    else:
        print('老兄，给字符串')
        return 0


def my_request(url,headers={'User-Agent':USER_AGENT_LIST['chrome']},code='utf-8',retry_times=5,wait_from=1,wait_to=3,debug=True,keyword=''):
    '''
    :param url: 请求的url
    :param headers: 请求头
    :param retry_times: 若是发生错误的重试次数
    :param debug: 是否打开调试显示
    :param keyword:  *****重要,表示页面不是所需页面的关键字,有这个关键字,说明页面请求是失败的,要重试
    :param encoding:页面的编码方式,默认为utf-8
    :return: 返回页面的text
    '''

    if debug: print('url', url)
    if debug: print('headers', headers)
    if debug: print('retry_times', retry_times)
    if debug: print('debug', debug)
    if debug: print('wait from {} to {} sec'.format(wait_from,wait_to))
    if debug: print('keyword',keyword)


    count=0
    content=''
    while count<retry_times:
        try:
            response=requests.get(url,headers=headers)
            text=response.content.decode(code)

            if debug:print('text',text)
            if debug:print('status_code',response.status_code)

            if response.status_code!=200:
                if debug: print('status_code', response.status_code)
                count+=1
                random_wait(wait_from,wait_to)
                continue

            if response.status_code == 200  and keyword =='':
                return text

            if response.status_code == 200  and keyword not in text:
                return text

            if response.status_code == 200  and keyword  in text:
                if debug: print('status_code', response.status_code)
                count+=1
                random_wait(wait_from,wait_to)
                continue



        except Exception as e:
            if debug:print('第{}次请求页面失败,原因是{}'.format(count,e))
            count+=1
            random_wait(wait_from,wait_to)

    if debug: print('达到最大重试次数{}'.format(retry_times))
    return False




if __name__ == '__main__':

    url='http://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word=睡觉&x_bfe_rqs=03E80&x_bfe_tjscore=0.580106&tngroupname=organic_news&newVideo=12&pn=260'
    print(my_request(url=url,keyword='timeout-button',retry_times=3,wait_from=1,wait_to=2))

