# coding: utf-8
# Team : None
# Author：zl
# Date ：2020/6/30 0030 上午 9:00
# Tool ：PyCharm

import random
import re
import time
import string
import requests
import os
import logging


Proxy = [
    {'http': '', 'https': ''},
    {'http': 'http://test:594188@58.59.25.122:1234', 'https': 'https://test:594188@58.59.25.122:1234'},
    {'http': 'http://test:594188@58.59.25.123:1234', 'https': 'https://test:594188@58.59.25.123:1234'}
]

user_anent='chrome''Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
#装饰器,用于返回函数名和执行时间
def execute_lasts_time(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        lasts_time=time.time()-start_time
        print('%s执行时间为:%s'%(func.__name__,lasts_time),'\r')
        return result
    return warpper

def random_wait(n=1,m=3,*args):
    temp = get_random_num(n,m)
    print("wait {} second".format(temp))
    time.sleep(temp)
    return True

def get_random_str(lenth=8):
    n=''.join(random.sample(string.ascii_letters + string.digits, lenth))
    print('获得的随机字符串为{}'.format(n))
    return n

def get_random_num(n=1,m=3,*args):
    if not (isinstance(n, (int, float)) and isinstance(m, (int, float))):
        print('参数输入错误，不是整数或小数，采用默认值1，3')
        n=1
        m=3

    if n>m:
        print('m,n不是小-大顺序,自动调换mn数值')
        n,m=m,n
    num=random.uniform(n, m)
    print('获得的随机数为{}'.format(num))
    return num

@execute_lasts_time
def tras_header(str):
    '''定义返回值'''
    result={}


    '''以换行符转成list'''
    s=re.split('\n',str)
    print('转换成的list为{}'.format(s))

    '''遍历每一行'''
    for item in s:
        '''跳过如为空行，'''
        print('正在处理{}'.format(item))
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

    print('转换结果:\n')
    print(('{'))
    for i in result:
        print(('\'{}\':\'{}\','.format(i,result[i])))
    print(('}'))
    return result

def qu_kong_ge(s):
    if isinstance(s, str):
        return re.sub('\s+', '', s)
    else:
        print('老兄，给字符串')
        return False

def qu_str(source,*grabage):      #去除source中的垃圾,grabage为list,存储垃圾
    target=source

    print('去除以下垃圾字符{}'.format(grabage))
    if len(grabage)==0 :
        print('要消除的垃圾信息为空,请检查grabage？')
        return False

    if not isinstance(grabage, (list,tuple)):
        print('垃圾信息只接受队列和元组')
        return False

    if (not isinstance(source,str)) or source=='':
        print('待处理的source字符串为空,或不是str类型')
        return False

    for i in grabage:
        target=target.replace(i,'')
    return target

def qu_html_lable(s):
    reg = re.compile(r'<[^>]+>', re.S)
    if isinstance(s, str):
        return reg.sub('', s)
    else:
        print('老兄，给字符串')
        return False

def qu_te_shu_zi_fu(s):
    if isinstance(s, str):
        return re.sub('[\/:*?"<>|]','-',s)
    else:
        print('老兄，给字符串')
        return False

def my_request(url,headers={'User-Agent':user_anent},proxies={},codec='utf-8',retry_times=5,wait_from=1,wait_to=3,keyword=''):
    '''
    :param url: 请求的url
    :param headers: 请求头
    :param retry_times: 若是发生错误的重试次数
    :param debug: 是否打开调试显示
    :param keyword:  *****重要,表示页面不是所需页面的关键字,有这个关键字,说明页面请求是失败的,要重试
    :param encoding:页面的编码方式,默认为utf-8
    :return: 返回页面的text
    '''

    print('url:{}'.format(url))
    print('headers:{}'.format(headers))
    print('retry_times:{}'.format(retry_times))
    print('wait from {} to {} sec'.format(wait_from,wait_to))
    print('keyword:{}'.format(keyword))
    print('proxies:{}'.format(proxies))
    print('codec:{}'.format(codec))

    count=0
    content=''
    while count<retry_times:
        try:
            response=requests.get(url,headers=headers,proxies=proxies)
            print('response.header为{}'.format(response.headers))
            text=response.content.decode(codec)

            print('text:   {}'.format(qu_kong_ge(text)))
            print(print('请求{},返回状态码为{}:'.format(url,response.status_code)))

            if response.status_code!=200:
                count+=1
                random_wait(wait_from,wait_to)
                continue

            if response.status_code == 200  and keyword =='':
                return text

            if response.status_code == 200  and keyword not in text:
                return text

            if response.status_code == 200  and keyword  in text:
                print('页面正常返回,但是不包含key中的字符串,重试')
                count+=1
                random_wait(wait_from,wait_to)
                continue



        except Exception as e:
            print('第{}次请求页面失败,原因是{}'.format(count,e))
            count+=1
            random_wait(wait_from,wait_to)

    print('达到最大重试次数{}'.format(retry_times))
    return False

def check_fname(fname):
    '''
    检查fname路径的文件是否存在,若不存在,则创建文件储存的目录,返回fname值
    若文件存在,则尝试返回另外一个名字
    :param fname:
    :return:  fname
    '''
    dir, filename = os.path.split(fname)

    if dir == '':
        print('fname:{}没有路径,路径设为当前路径'.format(fname))
        dir = '.'

    if filename == '':
        print('fname:{}没有文件名,程序退出'.format(fname))
        return False

    basename,extname=os.path.splitext(filename)

    print('输入文件,目录为{},文件名{},扩展名为{}'.format(dir,basename,extname))

    count=1
    while os.path.exists(os.path.join(dir,basename+extname)) and os.path.isfile(os.path.join(dir,basename+extname)):
        print('{}{}文件重名,尝试更名'.format(basename,extname))

        reg=r'\(\(\d+\)\)'
        if re.findall(reg,basename)==[]:
            basename=basename+r'(({}))'.format(count)
            count=count+1
        else:
            print(re.split(reg,basename))
            basename=re.split(reg,basename)[0]+r'(({}))'.format(count)
            count = count + 1

    fname=os.path.join(dir,basename+extname)

    if not os.path.exists(dir):
        print('{}目录不存在,创建'.format(dir))
        os.makedirs(dir)

    return fname

def get_random_proxie():
    proxies= random.choice(Proxy)
    print('随机选择代理为{}'.format(proxies))
    return random.choice(Proxy)

def download(url,fname='',headers={'User-Agent':user_anent},proxies={},retry_times=5,wait_from=1,wait_to=3):
    '''
    :param url: 请求的url
    :param fname:  保存的文件路径+文件名
    :param headers: 请求头
    :param retry_times: 若是发生错误的重试次数
    :param keyword:  *****重要,表示页面不是所需页面的关键字,有这个关键字,说明页面请求是失败的,要重试
    :return: 返回页面的text
    '''
    print('url:{}'.format(url))
    print('headers:{}'.format(headers))
    print('retry_times:{}'.format(retry_times))
    print('wait from {} to {} sec'.format(wait_from,wait_to))
    print('proxies:{}'.format(proxies))
    print('fname:{}'.format(fname))


    def get_fname(fname):

        dir, filename = os.path.split(fname)

        if dir == '':
            dir = 'download'

        if filename == '':
            filename = url.split('/')[-1]

        basename,extname=os.path.splitext(filename)

        print('文件存储的目录为{},文件名{},扩展名为{}'.format(dir,basename,extname))

        count=1
        while os.path.exists(os.path.join(dir,basename+extname)) and os.path.isfile(os.path.join(dir,basename+extname)):
            print('{}{}文件重名,尝试更名'.format(basename,extname))

            reg=r'\(\d+\)'
            if re.findall(reg,basename)==[]:
                basename=basename+r'({})'.format(count)
                count=count+1
            else:
                basename=re.split(reg,basename)[0]+r'({})'.format(count)
                count = count + 1

        fname=os.path.join(dir,basename+extname)

        if not os.path.exists(dir):
            os.makedirs(dir)

        return fname

    count=0
    r=''
    while count < retry_times:
        try:
            print('开始尝试第{}第下载,url为{}'.format(count + 1, url))
            r = requests.get(url, headers=headers,proxies=proxies)
            print(r.status_code)
            print(r.content)
            if r.status_code == 200:
                break
            if r.status_code!=200:
                print('下载失败,状态码不为200,为{}'.format(r.status_code))
                count=count+1
                random_wait(wait_from,wait_to)
                continue
        except Exception as e:
            if debug: print('失败,原因为{}'.format(e))
            count=count+1
            random_wait(wait_from, wait_to)
            continue



    fname=get_fname(fname=fname)

    try:
        with open(fname, 'wb') as f:
            f.write(r.content)
            return True
    except Exception as e:
        print('写入文件失败,原因是:{}'.format(e))
        return False

if __name__ == '__main__':
    url='''http://www.imomoe.in/player/2-0-0.html'''

    page=my_request((url),codec='gbk')
    print(page)

<a href="/list/2.html" target="_blank" title="日本动漫">日本动漫</a> &gt; <a href="/search.asp?searchword=%B0%AE%C7%E9">爱情</a>&nbsp;&nbsp;<a href="/search.asp?searchword=%D0%A3%D4%B0">校园</a>&nbsp;&nbsp;&gt; <a href="/view/2.html" title="苍之彼方的四重奏" target="_blank">苍之彼方的四重奏</a> <span>12全集</span>


