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
@execute_lasts_time
def tras_header(str,debug=False):
    '''定义返回值'''
    result={}

    '''以换行符转成list'''
    s=re.split('\n',str)
    if debug:print('转换成的list为',s)

    '''遍历每一行'''
    for item in s:
        '''如为空行，跳过'''
        if debug:print(item)
        if item.replace(' ','')=='':
            if debug:print('本行为空行，跳过')
            continue

        '''以冒号为分隔符分割元素'''
        if debug:print(re.split(': ',item))
        key,value=re.split(': ',item)
        key=qu_kong_ge(key)
        if key[0]==':':
            key=key[1:]
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
        return False

def qu_str(source,*grabage):      #去除source中的垃圾,grabage为list,存储垃圾
    target=source

    print('去除以下垃圾字符{}'.format(grabage))
    if len(grabage)==0 :
        print('要消除的字符串是什么？')
        return False

    if not isinstance(grabage, (list,tuple)):
        print('垃圾信息只接受队列')
        return False

    if (not isinstance(source,str)) or source=='':
        print('原始字符串错误')
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

def my_request(url,headers={'User-Agent':user_anent},proxies={},codec='utf-8',retry_times=5,wait_from=1,wait_to=3,debug=False,keyword=''):
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
    if debug: print('proxies', proxies)
    if debug: print('codec', codec)


    count=0
    content=''
    while count<retry_times:
        try:
            response=requests.get(url,headers=headers,proxies=proxies)
            if debug:print(response.headers)
            text=response.content.decode(codec)

            if debug:print('text',qu_kong_ge(text))
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
                if debug: print('页面正常返回,但是不包含key中的字符串,重试')
                count+=1
                random_wait(wait_from,wait_to)
                continue



        except Exception as e:
            if debug:print('第{}次请求页面失败,原因是{}'.format(count,e))
            count+=1
            random_wait(wait_from,wait_to)

    if debug: print('达到最大重试次数{}'.format(retry_times))
    return False


def get_proxie():
    return random.choice(Proxy)

def download(url,fname='',headers={'User-Agent':user_anent},proxies={},retry_times=5,wait_from=1,
             wait_to=3,debug=False):
    '''
    :param url: 请求的url
    :param fname:  保存的文件路径+文件名
    :param headers: 请求头
    :param retry_times: 若是发生错误的重试次数
    :param debug: 是否打开调试显示
    :param keyword:  *****重要,表示页面不是所需页面的关键字,有这个关键字,说明页面请求是失败的,要重试
    :return: 返回页面的text
    '''
    if debug: print('url', url)
    if debug: print('headers', headers)
    if debug: print('retry_times', retry_times)
    if debug: print('debug', debug)
    if debug: print('wait from {} to {} sec'.format(wait_from,wait_to))
    if debug: print('proxies', proxies)
    if debug: print('fname',fname)


    def get_fname(fname):

        dir, filename = os.path.split(fname)

        if dir == '':
            dir = 'download'

        if filename == '':
            filename = url.split('/')[-1]

        basename,extname=os.path.splitext(filename)

        if debug: print('文件存储的目录为{},文件名{},扩展名为{}'.format(dir,basename,extname))

        count=1
        while os.path.exists(os.path.join(dir,basename+extname)) and os.path.isfile(os.path.join(dir,basename+extname)):
            if debug: print('{}{}文件重名,尝试更名'.format(basename,extname))

            reg=r'\(\d+\)'
            if re.findall(reg,basename)==[]:
                basename=basename+r'({})'.format(count)
                count=count+1
            else:
                print(re.split(reg,basename))
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
                if debug:print('下载失败,状态码不为200,为{}'.format(r.status_code))
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
        if debug:print('写入文件失败,原因是:{}'.format(e))
        return False

if __name__ == '__main__':

    # url='http://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word=睡觉&x_bfe_rqs=03E80&x_bfe_tjscore=0.580106&tngroupname=organic_news&newVideo=12&pn=260'
    # page=my_request(url=url,keyword='timeout-button',proxies=get_proxie(),retry_times=10,wait_from=1,wait_to=2,debug=True)
    download(url='https://img.tupianzj.com/uploads/allimg/160531/9-160531223943.gif',fname='./d/',debug=True)





    #
    # s = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    # Accept-Encoding: gzip, deflate
    # Accept-Language: zh-CN,zh;q=0.9
    # Connection: keep-alive
    # Cookie: Province=0530; City=0531; _ntes_nnid=1ac836af6b79d21869a8ef8c0f71ad92,1592528750159; UM_distinctid=172ca1c4fdd124-02d4e1bf8b5945-464c092c-140000-172ca1c4feac2; _ntes_nuid=1ac836af6b79d21869a8ef8c0f71ad92; NNSSPID=299545cb18b7427cb17e8f2e8ae04319; vinfo_n_f_l_n3=6459bb65b72ee59d.1.16.1592528750168.1593422727306.1593569116469
    # Host: www.163.com
    # Upgrade-Insecure-Requests: 1
    # User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'''
    # print(tras_header(s))