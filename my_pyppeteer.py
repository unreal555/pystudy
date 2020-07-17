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
import re
import os
import sys
from pyppeteer.launcher import launch  # 控制模拟浏览器用


class Broswer():
    __Broswer=''
    __page=''
    __counter = ''
    __loop = asyncio.get_event_loop()
    def createCounter(self):
        s = 0
        def counter():
            nonlocal s
            s = s + 1
            return s
        return counter


    async def go(self,page, url):
        while 1:
            num = count()
            print(num)

            try:
                await page.goto(url)
                break
            except Exception as e:
                print(e)
                random_wait(2, 4)
                continue

    def __init__(self):

        async  def init(self):
            self.__browser = await launch({'headless': False, 'dumpio': True, 'args': ['--window-size=16,12']})  # ,'--no-sandbox'
            self.__page = await self.__browser.newPage()
            await page.setUserAgent(
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')

        if self.__counter=='':
            self.__counter=self.createCounter(self)

        init(self)




          # 协程，开启个无限循环的程序流程，把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
        # self.loop.run_until_complete(main(url, self.__counter))


    async def wait(self):
        random_wait(0.1, 0.2)
        await self.__page.evaluate('window.scrollBy(0, document.body.scrollHeight)')

    async def get_innerText(self):
        try:
            s = await self.__page.evaluate('''() =>  document.querySelector("#content").innerText''')
        except Exception as e:
            print(e)
        return s

    async def close_page(self):
        await self.__page.close()

    async def close_browser(self):
        await self.__browserclose()





if __name__ == '__main__':
    b=Broswer()