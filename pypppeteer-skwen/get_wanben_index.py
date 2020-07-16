# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/16 0016 下午 2:19
# Tool ：PyCharm
import requests
import my_html_tools
import  re
import os
import my_txt_writer

index='./index.txt'

all=''
if os.path.exists(index):
    with open(index,'r',encoding='utf-8') as f:
        all=f.read()


domain='http://www.skwen.me/shuku'
for i in range(1,200):
    response=requests.get('http://www.skwen.me/shuku/0-lastupdate-2-{}.html'.format(i))   #1-178
    page=my_html_tools.qu_kong_ge(response.content.decode('gbk'))
    result=re.findall(r'<aclass="name"href="(.*?)">(.*?)</a>',page)

    for i in result:
        if i[0] in all:
            print('{}已存在,跳过'.format(i))
            continue

        my_txt_writer.write_txt(file=index,data=str(i),tab=1,enter=0)
    my_html_tools.random_wait(1,3)
