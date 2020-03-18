import requests
import re
import random
from selenium import webdriver
from  time import sleep
from mytools import  USER_AGENT_LIST
from mytools import random_wait
from mytools import qu_kong_ge
from mytools import qu_te_shu_zi_fu

headers={}
headers['User-Agent']=random.choice(USER_AGENT_LIST)
headers['DNT']='1'
headers['Accept']='text/html,application/xhtml+xml, */*'
headers['Referer']='https://u.faloo.com/unreal555.html'
headers['Accept-Encoding']='gzip, deflate'


Browser = webdriver.Ie('.\IEDriverServer.exe')





def login():
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
            Browser.get('https://u.faloo.com/regist/Login.aspx?backurl=/unreal555.html')
            raise '登录 异常 请 检查 重新 登录 '

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


if __name__ == '__main__':
    login()
    cookies=get_cookie()
    Browser.quit()

    response=requests.get('http://mm.faloo.com/xiaoshuo/518974.html',headers=headers)#,cookies=cookies

    page=response.content.decode('gbk')
    print(response.url)

    for i in range(1,30):
        response=requests.get('https://b.faloo.com/p/518974/{}.html'.format(i),headers=headers)
        page=response.content.decode('gbk')
        page=qu_kong_ge(page)

        title=re.findall('''<divclass="c_l_title">(.*?)&nbsp;&nbsp;&nbsp;(.*?)</div><divclass="c_l_info">''',page)
        result=re.findall('<divclass="noveContent">(.*?)<!--',page)[0].split('<br><br>')
        for i in result:
            print(i)
        print(title)
        print('____________________________________')
        random_wait()

    response=requests.get('https://u.faloo.com/unreal555.html',headers=headers,cookies=cookies)#

    page=response.content.decode('gbk')
    print(page)
    print(response.url)
