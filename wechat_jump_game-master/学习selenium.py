# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from lxml import  etree
import re


browser=webdriver.Chrome('E:\pycharm-professional-2017.2.4\chromedriver_win32\chromedriver.exe')
browser.get(r'https://www.yangguiweihuo.com/11/11516/')   #必须加http://
html=etree.HTML(browser.page_source)

chapter_list= []    #重要重要，xpath 用法
flag=-1
for i in html.xpath('/html/body/div[5]/dl/*') :

    if flag==1:
        for j in i:
            chapter_list.append([j.text,j.xpath('@href')])
    if i.text!=None:
        print('000')
        if i.text.find("最新")>=0:
            print(i.text.find("最新"))
            continue
        if i.text.find("正文")>=0:
            print(i.text.find("正文"))
            flag=1
            continue

print(chapter_list)

for i in chapter_list:

    time.sleep(1)
    select=browser.find_element_by_partial_link_text(i[0])
    time.sleep(1)
    select.click()
    print(browser.page_source)
    reg = '<div id="content" class="showtxt">(.*?)</div>'
    chapterContent = re.findall(reg, browser.page_source, re.S)
    # print(chapterContent[0])
    with open('/1.html','a', encoding='utf-8') as f:
        f.write('<h3>')
        f.write(i[0])
        f.write('</h3><br /><br /><br />')
        print(chapterContent[0])
        f.write(chapterContent[0])
        f.write('<br /><br /><br />')
        time.sleep(1)
    browser.back()
browser.close()