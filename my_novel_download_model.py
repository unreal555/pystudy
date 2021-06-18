#!/bin/py
#   -*-coding:utf-8-*-

from my_html_tools import my_request
from my_html_tools import qu_huan_hang_fu
from my_html_tools import qu_te_shu_zi_fu
from my_html_tools import random_wait
from urllib import parse
from my_logger import my_logger
import re
import time
import os
import random

def get_novel_info(url):
    novel_index_page =  qu_huan_hang_fu(my_request(url))
    print(novel_index_page)
    title = find_useful(novel_index_page,novel_title_reg)
    author=find_useful(novel_index_page,novel_author_reg)
    desc=find_useful(novel_index_page,novel_desc_reg)
    category=find_useful(novel_index_page,novel_category_reg)
    chapters=find_useful(novel_index_page,chapter_reg)
    return title,author,category,desc,chapters

def find_useful(page,reg,debug=False):
    if reg==None:
        return ''
    if isinstance(reg,str):
        result=re.findall(reg,page)
        if debug:print(result)
        if len(result)==0:
            return None
        if len(result)==1:
            return result[0]
        if len(result)>1:
            return result

    if isinstance(reg,(list,tuple)):
        temp=re.findall(reg[0],page)
        if debug:print(temp)
        if len(temp)==1:
            temp= temp[0]
        result = re.findall(reg[0], temp)
        if debug:print(result)
        if len(result)==0:
            return None
        if len(result)==1:
            return result[0]
        if len(result)>1:
            return  result

def get_novel(url):
    scheme, netloc, path, query, fragment = parse.urlsplit(url)
    title, author, category, desc, chapters=get_novel_info(url)
    print( title,'\r\n',author,'\r\n',category,'\r\n',desc,'\r\n',chapters)

    title=qu_te_shu_zi_fu(title)
    author=qu_te_shu_zi_fu(author)
    category=qu_te_shu_zi_fu(category)

    filename=title+"_"+author+"_"+category+".txt"

    all=''
    if os.path.exists(filename) and os.path.isfile(filename):
        with open(filename,'r',encoding='utf-8') as f:
            all=f.read()

    for chapter_url,chapter_name in chapters:
        print(scheme+'://'+netloc+chapter_url,chapter_name)
        if chapter_url in all and chapter_name in all:
            print('%s%s已下载,跳过'%(chapter_name,chapter_url))
            continue

        print('%s%s开始下载' % (chapter_name, chapter_url))
        chapter_content=my_request(scheme+'://'+netloc+chapter_url,wait_from=0.1,wait_to=0.5)
        content=find_useful(chapter_content,chapter_content_reg)
        with open(filename,'a',encoding='utf-8') as f:
            f.write(chapter_name+'(((###'+chapter_url+'###)))'+'\r\n')
        for item in content:
            with open(filename, 'a', encoding='utf-8') as f:
                f.write('\t'+qu_huan_hang_fu(item)+'\r\n')

        random_wait(show=True)

if __name__ == '__main__':

    novel_title_reg = r'''var booktitle = "(.*?)"'''
    novel_author_reg = r'''<p>作&nbsp;&nbsp;&nbsp;&nbsp;者：(.*?)</p>'''
    novel_category_reg = r'''<a href="/">VIP中文</a> &gt; <a href=".*?">(.*?)</a>.*?</div><div id="maininfo"'''
    novel_desc_reg = r'''<meta name="description" content="(.*?)" />'''
    chapter_reg = r''' <dd><a href="(.*?)">(.*?)</a></dd> '''
    chapter_content_reg = reg=r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'
    codec='utf-8'
    debug=True

    get_novel(r'http://www.vipxs.la/62_62540/')





#
#
# novel_url=r'http://www.vipxs.la/62_62548/'#'http://www.vipxs.la/8_8601'#http://www.vipxs.la/
# scheme,netloc,path,query,fragment=parse.urlsplit(novel_url)
# print(parse.urlsplit(novel_url))
# response= requests.get(novel_url)
# page=response.content.decode("utf-8")
# chapter_reg=r'<dd><a href="(.*/?)">(.*?)</a></dd>'
# title_reg=r'<script language="javascript" type="text/javascript">var bookid = ".*?"; var booktitle = "(.*?)";</script>'
# author_reg=r'<p>作&nbsp;&nbsp;&nbsp;&nbsp;者：(.*?)</p>'
#
# chapter_list=re.findall(chapter_reg,page)
# title=re.findall(title_reg,page)
# author=re.findall(author_reg,page)
# path=os.path.join(".",title[0]+"_"+author[0])
# filename=title[0]+"_"+author[0]+".txt"
# print(title[0],author[0])
#
#
# if os.path.exists(path) and os.path.isdir(path):
#     for f in os.listdir(path):
#         os.remove(os.path.join(path,f))
# else:
#     os.mkdir(path)
#
# for chapter in chapter_list:
#     chapter_url,chapter_name=scheme+"://"+netloc+chapter[0],chapter[1]
#     print (chapter_url)
#
#     response= requests.get(chapter_url)
#     page =response.content.decode("utf-8")
#     reg=r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'
#     result=re.findall(reg,page)
#     text=chapter_name+"\r\n"+"\r\n"
#     # text+="\t"
#     flag=0
#     print(result)
#     for hang in result:
#         text=text+"\t"+hang+"\r\n"
#         text=text+"\r"
#     # for hang in result:
#     #     if hang!="……" and flag==0:
#     #         text=text+hang
#     #         continue
#     #     if hang=="……"  and flag==0:
#     #         flag+=1
#     #         continue
#     #     if hang=="……"  and flag==1:
#     #         text=text+"\r\n"
#     #         text=text+"\t"
#     #         flag=0
#     #         continue
#     #     if hang!="……" and flag==1:
#     #         text=text+"\r\n"
#     #         text=text+"\t"+'……'
#     #         flag=0
#     #         continue
#     text+="\r\n"+"\r\n"
#     with open(os.path.join(path,chapter_name+".txt"),"w",encoding="utf-8") as f1:
#         f1.write(text)
#     with open(os.path.join(path,filename),"a",encoding="utf-8") as f2:
#         f2.write(text)
#
#     s=random.randint(1,3)
#     print("停止{}秒".format(s))
#     time.sleep(s)
#
#
#
#
#
#
