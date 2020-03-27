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
import os
import re
os.environ['PYPPETEER_HOME'] = 'E:\pycharm-professional-2017.2.4'
import pyppeteer.chromium_downloader
print('默认版本是：{}'.format(pyppeteer.__chromium_revision__))
print('可执行文件默认路径：{}'.format(pyppeteer.chromium_downloader.chromiumExecutable.get('win64')))
print('win64平台下载链接为：{}'.format(pyppeteer.chromium_downloader.downloadURLs.get('win64')))
import time,random
from pyppeteer.launcher import launch # 控制模拟浏览器用
from retrying import retry #设置重试次数用的
from mytools import qu_kong_ge


async def get_content(page,url):

    await page.goto(url)
    time.sleep(3)
    await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')

    try:
        # s = await page.evaluate(pageFunction='document.body.textContent', force_expr=True)
        s=await page.evaluate('''() =>  document.querySelector("#content").innerText''')
    except Exception as e:
        print(e)

    return await get_text(s)
async def get_text(s):

    result=''
    for i in re.split('\r|\n|\r\n',s):
        try:
            i.encode('utf-8')
        except Exception as e:
            # print(e)
            continue
        if '   ' in  i:
            print(i)
            result=result+qu_kong_ge(i)
    return result

async def main(url):# 定义main协程函数，
    browser = await launch({'headless': False ,'args':['--window-size=16,12']})#,'--no-sandbox'
    page = await browser.newPage()
    await page.setUserAgent( 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
    await page.goto(url)
    print('开始阅读')
    await page.evaluate('''document.querySelector("body > div.container > div.mod.detail > div.ft > table > tbody > tr > td:nth-child(1) > a").click()''')
    print('1111')
    num=re.findall('【(.*?)】',await page.evaluate('''() =>  document.querySelector("#content").innerText'''))
    print(num)


if __name__ == '__main__':
    url = 'http://www.skwen.me/13/13577/'
    loop = asyncio.get_event_loop()  #协程，开启个无限循环的程序流程，把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
    loop.run_until_complete(main(url))











