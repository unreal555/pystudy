#!/bin/py
#   -*-coding:utf-8-*-

# 通过ID获取（getElementById）
# 通过name属性（getElementsByName）
# 通过标签名（getElementsByTagName）
# 通过类名（getElementsByClassName）
# 获取html的方法（document.documentElement）
# 获取body的方法（document.body）
# 通过选择器获取一个元素（querySelector）
# 通过选择器获取一组元素（querySelectorAll）

import asyncio
from  my_html_tools import random_wait
wait_from=1
wait_to=3
import re
import os
import sys
from pyppeteer.launcher import launch  # 控制模拟浏览器用

def createCounter():
    s = 0
    def counter():
        nonlocal s
        s = s + 1
        return s
    return counter


counter=createCounter()
browser=''
page=''


async def init():
    browser = await launch({'headless': False, 'dumpio': True, 'args': ['--window-size=1024,768']})  # ,'--no-sandbox'
    page = await browser.newPage()
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
    return (browser,page)

async def go(page, url,retry=-1):
    count=0
    while 1:
        num = counter()
        print('累计加载 {} 个网页'.format(num))
        try:
            await page.goto(url)
            print('页面{}打开成功'.format(url))
            count+=1
            return True
        except Exception as e:
            print(e)

            if count==retry:
                print('重试已达{}次,不再尝试加载页面{}'.format(retry,url))
                return False
            else:
                print('重试{}次,继续加载页面{}'.format(count, url))
                random_wait(wait_from, wait_to)
                continue
        self.loop.run_until_complete(self.work)

async def scroll(page,to='document.body.scrollHeight'):
    await page.evaluate('window.scrollBy(0, {})'.format(str(to)))
    random_wait(wait_from,wait_to)

async def get_innerText(page,obj='''#content'''):
    try:
        s = await page.evaluate('''() =>  document.querySelector("{}").innerText'''.format(obj))
    except Exception as e:
        print(e)
    return s

async def close_page(page):
    await page.close()

async def close_browser(self):
    await browser.close()




async def main():
    browser,page=await init()
    await go(page,'https://www.taobao.com')
    # print(await  get_innerText(page,obj='''body > div.wrapper-box > div.area.clearfix.public.content-yule.channel-content > div.main.left > div:nth-child(2) > div.main-box.clearfix.yule-news'''))
    await scroll(page,to=500)





loop = asyncio.get_event_loop()  # 协程，开启个无限循环的程序流程，把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
loop.run_until_complete(main())


