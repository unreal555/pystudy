import requests
import re
import random
from selenium import webdriver
from  time import sleep

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
]

headers={}
headers['User-Agent']=random.choice(USER_AGENT_LIST)

headers['DNT']='1'
headers['Accept']='text/html,application/xhtml+xml, */*'
headers['Referer']='https://u.faloo.com/unreal555.html'
headers['Accept-Encoding']='gzip, deflate'


Browser = webdriver.Ie('.\IEDriverServer.exe')


def wait():
    temp = random.randint(1, 3)
    sleep(temp)
    print("wait {} second".format(temp))
    return


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
        sleep(1)
    wait()

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

login()
cookies=get_cookie()

Browser.quit()

response=requests.get('http://mm.faloo.com/xiaoshuo/518974.html',headers=headers)#,cookies=cookies

page=response.content.decode('gbk')
print(response.url)

for i in range(1,30):
    response=requests.get('https://b.faloo.com/p/518974/{}.html'.format(i),headers=headers)
    page=response.content.decode('gbk')
    page=re.sub('\s+','',page)

    title=re.findall('''<divclass="c_l_title">(.*?)&nbsp;&nbsp;&nbsp;(.*?)</div><divclass="c_l_info">''',page)
    result=re.findall('<divclass="noveContent">(.*?)<!--',page)[0].split('<br><br>')
    for i in result:
        print(i)
    print(title)
    print('____________________________________')
    wait()

response=requests.get('https://u.faloo.com/unreal555.html',headers=headers,cookies=cookies)#

page=response.content.decode('gbk')
print(page)
print(response.url)
