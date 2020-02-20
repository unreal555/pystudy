#!/bin/py
#   coding=gb2312
'       说明               '
_author_ = 'zl'

from  selenium import webdriver
from time import sleep
import random
import re
from selenium.webdriver.common.keys import Keys

url='http://www.longbaidu.com/forum.php?mod=forumdisplay&fid=40&page=1'
liuyan=['谢谢分享，谢谢','感谢楼主分享资源','下个看看，谢谢楼主','感谢分享！！！谢谢的说！！！！','感谢楼主分享精彩资源','好东西，谢谢楼主分享！']


Browser=webdriver.Ie('IEDriverServer.exe')

Browser.get(url)
sleep(random.randint(1,7))
print( re.findall('立即注册',Browser.page_source))
while re.findall('立即注册',Browser.page_source)!=[]:
    Browser.find_element_by_name('username').send_keys('unreal5555')
    sleep(random.randint(1, 7))
    Browser.find_element_by_name('password').send_keys('594188')
    sleep(random.randint(1, 7))
    Browser.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[1]/td[3]/label').click()
    sleep(random.randint(1, 2))
    Browser.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button/em').click()
    sleep(random.randint(1, 7))
    break

title=Browser.title
print(Browser.title)
Browser.get(url)

sleep(random.randint(1,7))

print(Browser.page_source)
result=[]
count=0

#
#
#
# for i in re.findall('onclick=.*?href=".*?">\[(.*?)\]</a>',Browser.page_source,re.S):
#     now = ''
#     print(i)
#     if len(i)>40 and len(i)<90:
#
#         for c in i.split(']['):
#             if len(c)==4 or len(c)==2 or (len(c.split('/')))>=2 :
#                 continue
#             if len(c)>len(now):
#                 now=c
#         result.append(now)
#     print(now)
#
#
#
#
#
#
# while(1):
#     i=random.choice(result)
#     if count>11:
#         print('投票{}次，休息一小时'.format(count))
#         sleep(3600)
#
#
#     print(i)
#     try:
#         Browser.find_element_by_xpath("//*[contains(text(),'{}')]".format(i)).click()
#         sleep(random.randint(10,15))
#
#     except:
#         print('没有查到{}'.format(i))
#         Browser.get(url)
#         random.randint(1,7)
#         continue
#     try:
#         Browser.find_element_by_xpath('//*[@id="fastpostmessage"]').send_keys(Keys.END)
#         sleep(random.randint(1,6))
#     except:
#         print('无法定位留言框')
#         random.randint(1,6)
#         Browser.get(url)
#     try:
#
#         Browser.find_element_by_xpath('//*[@id="fastpostmessage"]').send_keys(random.choice(liuyan))
#         sleep(random.randint(1,6))
#     except:
#         print('无法发送留言')
#         random.randint(1,6)
#         Browser.get(url)
#     try:
#         Browser.find_element_by_xpath('//*[@id="fastpostsubmit"]/strong').click()
#         sleep(random.randint(1,6))
#     except:
#         print('无法点击留言按钮')
#         random.randint(1,6)
#         Browser.get(url)
#     try:
#         Browser.back()
#         sleep(random.randint(1,10))
#         if Browser.title!=title:
#             Browser.get(url)
#     except:
#         print('back失败')
#         random.randint(1,6)
#         Browser.get(url)
#     count=count+1
#     print('已留言{}次'.format(count))
#
#
#
# Browser.quit()
