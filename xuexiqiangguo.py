#!/bin/py
#   -*-coding:utf-8-*-
'       说明               '
_author_ = 'zl'

from selenium import webdriver;
from time import sleep
import requests
from selenium.webdriver.common.keys import Keys
import re
import random
import os
import threading

import json
import requests

global news_page_time, count, video_page_time, news_list, cookie, video_list, news_time_score, news_count_score, video_time_score, video_conut_score
user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
Browser = webdriver.Ie('.\IEDriverServer.exe')
news_page_time = 180
video_page_time = 180
news_count_score = None
video_conut_score = None
news_time_score = None
video_time_score = None
news_list = []
video_list = []
count = 8
cookie = {}


def wait():
    temp = random.randint(1, 8)
    sleep(temp)
    print("wait {} second".format(temp))
    return


def watch_page(url):

    try:
        Browser.get(url)
        print(Browser.page_source)
        if 'notFound' in Browser.current_url:
            return
    except exception as e:
        print(e)

    print('打开{}'.format(url))
    temp = 0
    Browser.execute_script("window.scrollBy(0,600)")
    while 1:
        if temp < news_page_time:
            temp += 1
            print('wait {} 秒'.format(news_page_time - temp))
            sleep(1)
            continue
        else:
            break


def check_point():
    global cookie, news_count_score, news_time_score, video_conut_score, video_time_score
    while (1):
        print('启动check point')
        page = requests.get(r'https://pc-api.xuexi.cn/open/api/score/today/queryrate', cookies=cookie)
        a = page.text
        a = str.replace(a, '<html><head></head><body>', '')
        a = str.replace(a, '</body></html>', '')
        a = json.loads(a, encoding='utf-8')
        print("读取账户积分")
        print(a['data']['dayScoreDtos'][0]['currentScore'], a['data']['dayScoreDtos'][0]['name'])
        print(a['data']['dayScoreDtos'][1]['currentScore'], a['data']['dayScoreDtos'][1]['name'])
        print(a['data']['dayScoreDtos'][9]['currentScore'], a['data']['dayScoreDtos'][9]['name'])
        print(a['data']['dayScoreDtos'][11]['currentScore'], a['data']['dayScoreDtos'][11]['name'])
        news_count_score = a['data']['dayScoreDtos'][0]['currentScore']
        video_conut_score = a['data']['dayScoreDtos'][1]['currentScore']
        news_time_score = a['data']['dayScoreDtos'][9]['currentScore']
        video_time_score = a['data']['dayScoreDtos'][11]['currentScore']
        if news_count_score + news_time_score + video_conut_score + video_time_score >= 24:
            print('check_point线程退出')
            break
        sleep(10)



def login():
    Browser.get('https://pc.xuexi.cn/points/my-points.html')
    while 1:
        print('等待登录...')
        try:
            if Browser.current_url == 'https://pc.xuexi.cn/points/my-points.html' or Browser.current_url == r'https://pc.xuexi.cn/points/my-study.html':
                print('已登录')
                break
            if r'notFound' in Browser.current_url or '?' in Browser.current_url:
                print('qingdaomadneglu')
        except:
            print('登录 异常 请 检查 重新 登录 ')
            Browser.get('https://pc.xuexi.cn/points/my-points.html')

        finally:
            pass
        sleep(3)
    Browser.get('https://www.xuexi.cn')
    wait()


def get_news_list():
    global news_list

    page = requests.get('https://www.xuexi.cn/lgdata/35il6fpn0ohq.json')
    for i in json.loads(page.content, encoding='utf-8'):
        # a, b=str.split(i['publishTime'],' ')
        # if a not in news_list.keys():
        #
        #     news_list[a]=[]
        #     news_list[a].append(i['url'])
        # else:
        #     news_list[a].append(i['url'])
        news_list.append(i['url'])

    page = requests.get('https://www.xuexi.cn/lgdata/1jscb6pu1n2.json')
    for i in json.loads(page.content, encoding='utf-8'):
        # a, b = str.split(i['auditTime'], ' ')
        # print(a, i['url'])
        # if a not in news_list.keys():
        #     news_list[a] = []
        #     news_list[a].append(i['url'])
        # else:
        #     news_list[a].append(i['url'])
        news_list.append(i['url'])
    print(news_list)

def get_video_list():
    global video_list
    page = requests.get('https://www.xuexi.cn/lgdata/1novbsbi47k.json')
    for i in json.loads(page.content, encoding='utf-8'):
        #
        # a, b = str.split(i['publishTime'], ' ')
        # print(a, i['url'])
        # if a not in video_list.keys():
        #     video_list[a] = []
        #     video_list[a].append(i['url'])
        # else:
        #     video_list[a].append(i['url'])
        video_list.append(i['url'])
    print(video_list)


def get_cookie():
    print('获得cookie....')
    global cookie
    for i in Browser.get_cookies():
        if i['name'] in ['__UID__', 'tmzw', 'token', 'uaToken', 'webUmidToken', 'zwfigprt']:
            print('写入{},{}'.format(i['name'], i['value']), type(cookie))
            cookie[i['name']] = '{}'.format(i['value'])
    cookie = requests.utils.cookiejar_from_dict(cookie)
    print('获得cookie为', cookie)


def start():
    global news_time_score, news_count_score, video_time_score, video_conut_score,Browser
    print('进入主程序')

    while 1:
        wait()
        print(news_count_score,news_time_score,video_conut_score,video_time_score)
        if news_time_score != None and news_count_score != None and video_time_score != None and video_conut_score != None:

            if video_time_score < 3:
                print('新闻联播')
                Browser.get('https://www.xuexi.cn/8e35a343fca20ee32c79d67e35dfca90/7f9f27c65e84e71e1b7189b7132b4710.html')
                sleep(600)
                Browser.execute_script("window.scrollBy(0,400)")


            while news_time_score + news_count_score < 12:
                watch_page(random.choice(news_list))
            while video_time_score + video_conut_score < 12:
                watch_page(random.choice(video_list))
        Browser.close()
        print('主线程退出')
        break


if __name__ == '__main__':
    get_news_list()
    wait()
    get_video_list()
    login()
    wait()
    get_cookie()
    wait()
    print(news_list, '\n', video_list)

    threads = []
    t1 = threading.Thread(target=check_point)
    threads.append(t1)
    t2 = threading.Thread(target=start)
    threads.append(t2)

    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()
        t.join()

    print('刷分完毕，程序退出')



