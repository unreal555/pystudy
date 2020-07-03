# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/2 0002 上午 8:50
# Tool ：PyCharm
import mytools
from mytools import my_request
import re
from my_csv_tools import write_csv
import time
import os

base_dir='.'
subdir='data'
# subdir=str(time.strftime('%Y-%m-%d'))
filename='新浪军事.csv'
abs_path=os.path.join(base_dir,subdir)
data_file_path=os.path.join(base_dir,subdir,filename)



columns_names=['title','content','riqi','pic','laiyuan','url',]

starts = {
    '国际军情':'''http://mil.news.sina.com.cn/roll/index.d.html?cid=57919''',
    '国内军情':'''http://mil.news.sina.com.cn/roll/index.d.html?cid=57918''',
    }

reg_part = '''<divclass="fixList"><ulclass="linkNews">(.*?)</ul></div>'''

reg_li = '''<li><ahref="(.*?)"target="_blank">(.*?)</a><spanclass="time">.*?</span'''

reg_content_part='''<divclass="article"id='article'>(.*?)<divclass="article-bottomclearfix"id='article-bottom'>'''

reg_content_line='''<p.*?>(.*?)</p>'''

reg_pic='''<imgsrc="(.*?)"alt=.*?>'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }

def get_news_index(url):

    page=my_request(url,headers=headers,debug=False)
    text=mytools.qu_kong_ge(page)
    part=re.findall(reg_part,text,re.S)
    if len(part)==0:
        print('提取失败')
        return False
    result=re.findall(reg_li,part[0],re.S)
    return result

def get_news_content(url):
    page=my_request(url,headers=headers,debug=False)
    text=mytools.qu_kong_ge(page)

    part=re.findall(reg_content_part,text,re.S)

    if len(part)==0:
        print('正文part提取失败')
        return

    if len(part)==0:
        return False
    else:
        part=part[0]

    pic_index_temp=re.findall(reg_pic,part,re.S)
    pic_index=[]
    if len(pic_index_temp)==0:
        pass
    else:
        for i in pic_index_temp:
            if 'http://' in i  or 'https://' in i:
                pic_index.append(i)
                continue
            if '//' in i:
                pic_index.append(i.replace('//','https://'))




    '''提取行,连接成段'''
    lines=re.findall(reg_content_line,part,re.S)
    content='.'.join(lines)
    content=mytools.qu_html_lable(content)
    print(content)

    return content,pic_index


def Main(logger):
    for key in starts.keys():

        news_index=get_news_index(url=starts[key])

        if news_index==False:
            print('未获得索引,检查索引页{}'.format(starts[key]))
            continue
        news_indexl=news_index.reverse()
        for news_url,news_titile in news_index:
            if logger.check(news_url)==True:
                print('{},{},已下载,跳过'.format(news_titile,news_url))
                continue

            news_time=re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}',news_url)[0]
            print(news_url,news_titile,news_time)
            item={}
            item['laiyuan']=key
            item['url']=news_url
            item['title']=news_titile
            item['content'],item['pic']=get_news_content(news_url)
            item['riqi']=news_time

            mytools.random_wait(1,3)
            write_csv(file_path=data_file_path,item=item,column_names=columns_names)
            logger.write(item['url'])




