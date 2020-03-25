import requests
import re
import random
from selenium import webdriver
from  time import sleep
from mytools import  USER_AGENT_LIST
from mytools import random_wait
from mytools import qu_kong_ge
from mytools import qu_te_shu_zi_fu
import json
import os
from mytools import check_ban_quan

headers={}
headers['User-Agent']=random.choice(USER_AGENT_LIST)
headers['DNT']='1'
headers['Accept']='text/html,application/xhtml+xml, */*'
headers['Referer']='https://u.faloo.com/unreal555.html'
headers['Accept-Encoding']='gzip, deflate'

def login():

    random_wait()
    Browser.get('https://u.faloo.com/regist/Login.aspx?backurl=/unreal555.html')
    while 1:
        print('等待登录...')
        try:
            if '退出' in Browser.page_source:
                print('已登录')
                break
            if '注册' in Browser.page_source and '登录' in Browser.page_source:
                print('未登录,请登录')

        except:
            print('登录 异常 请 检查 重新 登录 ')
            Browser.get('https://u.faloo.com/regist/Login.aspx?backurl=/unreal555.html')
        finally:
            pass
        random_wait()


def get_cookie():
    cookies={}
    print('获得cookie....')
    for i in Browser.get_cookies():
        print(i)
    for i in Browser.get_cookies():
        if  i['name'] in ['UU12345678','comment_reply', 'KeenFire','KeenFire', 'host4chongzhi']:
            cookies[i['name']]=i['value']
    for i in cookies:
        cookies[i]=str(cookies[i])
    print(cookies)
    return cookies

def save_cookies(cookies):

    with open('user_info.json', 'w', encoding='utf-8') as json_file:
        json.dump(cookies, json_file, ensure_ascii=False)
        print("write json file success!")

def load_cookies():
    if os.path.exists(os.path.join('.','user_info.json')):
        with open('user_info.json', 'r', encoding='utf-8') as json_file:
            cookies = json.load(json_file)
        print(type(cookies),cookies)
        return cookies
    else:
        print('无cookie信息')
        return False

def check_login(cookies):
    page=requests.get('https://u.faloo.com',headers=headers,cookies=cookies)
    # print(page.text)
    # print('退出' in page.text,'注册' in page and '登录' in page.text)
    if '退出' in page.text:
        print('cookie有效，已登录')
        return True
    if '注册' in page.text and '登录' in page.text:
        print('cookie无效，使用人工登录')
        return False

if __name__ == '__main__':
    if check_ban_quan(48)==False:
        exit()

    cookies=load_cookies()

    if cookies==False:
        print('开始人工登录')
        Browser = webdriver.Ie('.\IEDriverServer.exe')
        login()
        cookies=get_cookie()
        save_cookies(cookies)
        Browser.quit()
    else:
        if check_login(cookies)==True:
            pass
        else:
            Browser = webdriver.Ie('.\IEDriverServer.exe')
            print('开始人工登录')
            login()
            cookies=get_cookie()
            save_cookies(cookies)
            Browser.quit()



    response=requests.get('https://u.faloo.com/S/0/1.html',headers=headers,cookies=cookies)
    print(response.text)



    response=requests.get('http://mm.faloo.com/xiaoshuo/518974.html',headers=headers)#,cookies=cookies

    page=response.content.decode('gbk')
    print(response.url)


    for i in range(1,30):
        url='https://b.faloo.com/p/518974/{}.html'.format(i)
        headers['Referer']=url
        response=requests.get(url,headers=headers,cookies=cookies)
        page=response.content.decode('gbk')
        page=qu_kong_ge(page)
        novel,chapter=re.findall('''<divclass="c_l_title">(.*?)&nbsp;&nbsp;&nbsp;(.*?)</div><divclass="c_l_info">''',page)[0]
        result=re.findall('<divclass="noveContent">(.*?)<!--',page)[0].split('<br><br>')

        print('____________________________________')
        print(novel,chapter)
        with open('./%s.txt'%novel,'a',encoding='utf-8') as f:
            f.write(novel+'\t\t'+chapter+'\r\n\r\n')
        for i in result:
            print(i)
            with open('./%s.txt'%novel,'a',encoding='utf-8') as f:
                f.write('    '+i+'\r\n')
        with open('./%s.txt'%novel,'a',encoding='utf-8') as f:
            f.write('\r\n')


        random_wait(1,5)

