#!/bin/py
#   coding=gb2312
'       ˵��               '
_author_ = 'zl'

from  selenium import webdriver
from time import sleep
import random
import re
from selenium.webdriver.common.keys import Keys

url='http://www.longbaidu.com/forum.php?mod=forumdisplay&fid=40&page=1'
liuyan=['лл����лл','��л¥��������Դ','�¸�������лл¥��','��л��������лл��˵��������','��л¥����������Դ','�ö�����лл¥������']


Browser=webdriver.Ie('IEDriverServer.exe')

Browser.get(url)
sleep(random.randint(1,7))
print( re.findall('����ע��',Browser.page_source))
while re.findall('����ע��',Browser.page_source)!=[]:
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
#         print('ͶƱ{}�Σ���ϢһСʱ'.format(count))
#         sleep(3600)
#
#
#     print(i)
#     try:
#         Browser.find_element_by_xpath("//*[contains(text(),'{}')]".format(i)).click()
#         sleep(random.randint(10,15))
#
#     except:
#         print('û�в鵽{}'.format(i))
#         Browser.get(url)
#         random.randint(1,7)
#         continue
#     try:
#         Browser.find_element_by_xpath('//*[@id="fastpostmessage"]').send_keys(Keys.END)
#         sleep(random.randint(1,6))
#     except:
#         print('�޷���λ���Կ�')
#         random.randint(1,6)
#         Browser.get(url)
#     try:
#
#         Browser.find_element_by_xpath('//*[@id="fastpostmessage"]').send_keys(random.choice(liuyan))
#         sleep(random.randint(1,6))
#     except:
#         print('�޷���������')
#         random.randint(1,6)
#         Browser.get(url)
#     try:
#         Browser.find_element_by_xpath('//*[@id="fastpostsubmit"]/strong').click()
#         sleep(random.randint(1,6))
#     except:
#         print('�޷�������԰�ť')
#         random.randint(1,6)
#         Browser.get(url)
#     try:
#         Browser.back()
#         sleep(random.randint(1,10))
#         if Browser.title!=title:
#             Browser.get(url)
#     except:
#         print('backʧ��')
#         random.randint(1,6)
#         Browser.get(url)
#     count=count+1
#     print('������{}��'.format(count))
#
#
#
# Browser.quit()
