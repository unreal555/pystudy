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
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..",'chrome-win32')))
import my_logger
import pyppeteer.chromium_downloader

print('默认版本是：{}'.format(pyppeteer.__chromium_revision__))
print('可执行文件默认路径：{}'.format(pyppeteer.chromium_downloader.chromiumExecutable.get('win64')))
print('win64平台下载链接为：{}'.format(pyppeteer.chromium_downloader.downloadURLs.get('win64')))
from pyppeteer.launcher import launch  # 控制模拟浏览器用
from mytools import qu_kong_ge, random_wait
from zhon.hanzi import punctuation as zhongwenbiaodian
from string import punctuation as yingwenbiaodian


def createCounter():
    s = 0

    def counter():
        nonlocal s
        s = s + 1
        return s

    return counter


async def go(page, url):
    while 1:
        num = count()
        print(num)

        try:
            await page.goto(url)
            break
        except Exception as e:
            print(e)
            random_wait(5, 20)
            continue


async def get_chapter_content(page, chapter_start_url):
    while 1:
        try:
            await go(page, chapter_start_url)
            txt = await page.content()
            chapter_name = re.findall('<h1 class="page-title">(.*?)</h1>', txt)[0]
            chapter_page_list = [chapter_start_url]
            for i in re.findall('<a href="(\d+_\d+\.html)">【.*?】</a>', txt, re.S):
                chapter_page_list.append(url + i)
            print(chapter_page_list)

            next_chapter_url = qu_kong_ge(re.findall(
                '''<a href=".*?" class="prev"><span>&lt;</span>上一章</a>.*?<a href="(.*?)" class="next">下一章<span>&gt;</span></a>''',
                txt, re.S)[0])
            print(next_chapter_url)
            break
        except Exception as e:
            print(e)
            continue

    result = ''
    for i in chapter_page_list:
        result = result + get_text(await get_chapter_page_content(page, i))
    # print(result)
    result = result.replace('”', '」')
    result = result.replace('“', '「')
    result = result.replace(' ', '').replace('\r', '').replace('\n', '')
    result = result.replace('。」', '。」\t\t\t\t\t')
    result = result.replace('！」', '！」\t\t\t\t\t')
    result = result.replace('……」', '……」\t\t\t\t\t')
    result = result.replace('?」', '?」\t\t\t\t\t')
    result = result.replace('.」', '.」\t\t\t\t\t')
    result = result.replace('!」', '!」\t\t\t\t\t')
    result = result.replace('？」', '？」\t\t\t\t\t')
    result = result.split('\t\t\t\t\t')

    for i in result:
        print(i)
    print(next_chapter_url)

    return [chapter_name, result], next_chapter_url


async def get_chapter_page_content(page, url):
    while 1:
        try:
            await go(page, url)
            random_wait(2, 3)
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            random_wait(2, 3)
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            random_wait(2, 3)
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            # s = await page.evaluate(pageFunction='document.body.textContent', force_expr=True)
            s = await page.evaluate('''() =>  document.querySelector("#content").innerText''')
            return s
        except Exception as e:
            print(e)
            continue


def get_text(s):
    result = ''
    for i in re.split('\r|\n', s):
        yuanshi = qu_kong_ge(i)
        tiqu = re.findall('[{}{}\u4e00-\u9fa5a-zA-Z0-9]'.format(zhongwenbiaodian, yingwenbiaodian), yuanshi)
        print(tiqu)
        t = ''.join(tiqu)
        yuanshichangdu = len(yuanshi)
        tiquchangdu = len(tiqu)
        print(tiqu, yuanshichangdu - tiquchangdu)
        if yuanshichangdu - tiquchangdu == 0:
            print(t)
            result = result + t
    return result


async def init():
    browser = await launch({'headless': False, 'dumpio': True, 'args': ['--window-size=16,12']})  # ,'--no-sandbox'
    return browser


async def main(url, count):  # 定义main协程函数，

    try:
        browser = await init()
        page = await browser.newPage()
        await page.setUserAgent(
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
        await go(page, url)
        book_name = re.findall('<h1>(.*?)</h1>', await page.content())[0]
        print(book_name)
        chapter_start_url = url + re.findall('<a class="read start" href="(.*?)">.*?</a>', await page.content())[0]
        book = [book_name, []]
        await page.close()
    except Exception as e:
        print(e)
    while 'html' in chapter_start_url:
        try:
            page = await browser.newPage()
            await page.setUserAgent(
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
            print(chapter_start_url, url, chapter_start_url == url)
            content, chapter_start_url = await get_chapter_content(page, chapter_start_url)
            chapter_start_url = url + chapter_start_url
            book[1].append(content)
            await  page.close()

        except Exception as e:
            print(e)
    await browser.close()

    with open('E:/a/a/{}.txt'.format(book[0]), 'w', encoding='utf-8') as f:
        f.write(book[0])
        f.write('\n\r')
        f.write('\n\r')
        f.write('\n\r')
        for chapter in book[1]:
            f.write('\t')
            f.write(chapter[0])
            f.write('\n\r')
        f.write('\n\r')
        f.write('\n\r')
        for chapter in book[1]:
            f.write(chapter[0])
            f.write('\n\r')
            for line in chapter[1]:
                f.write('\n\r')
                line = line.replace(chapter[0].replace(' ', ''), '').replace('努力加载中', '')
                f.write('\t' + line + '\n\r')
            f.write('\n\r')


if __name__ == '__main__':
    count = createCounter()
    loop = asyncio.get_event_loop()  # 协程，开启个无限循环的程序流程，把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
    logger=my_logger.logger()
    with open('./index.txt','r',encoding='utf-8') as f:
        result=(re.findall('''\(\'(.*?)\',.*?\'(.*?)\'\)''',f.read()))
    for url,title in result:
        url='http://www.skwen.me'+url
        if logger.check(url)==True:
            print('{}{}已下载,跳过'.format(url,title))
            continue
        else:
            loop.run_until_complete(main(url, count=createCounter()))
            logger.write(url,title)



    # for i in range(1, 50):  # 53
    #
    #     loop.run_until_complete(main(url, count=createCounter()))
