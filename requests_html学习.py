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
# os.environ['PYPPETEER_HOME'] = 'E:\pycharm-professional-2017.2.4'
import pyppeteer.chromium_downloader
print('默认版本是：{}'.format(pyppeteer.__chromium_revision__))
print('可执行文件默认路径：{}'.format(pyppeteer.chromium_downloader.chromiumExecutable.get('win64')))
print('win64平台下载链接为：{}'.format(pyppeteer.chromium_downloader.downloadURLs.get('win64')))
import time,random
from pyppeteer.launcher import launch # 控制模拟浏览器用
from retrying import retry #设置重试次数用的
from mytools import qu_kong_ge,random_wait

async def goto(page,url):
    while 1:
        try:
            await page.goto(url)
            break
        except Exception as e:
            print(e)
            random_wait(5,20)

async def get_chapter_content(page,chapter_start_url):

    await goto(page,chapter_start_url)

    txt=await page.content()

    chapter_name=re.findall('<h1 class="page-title">(.*?)</h1>',txt)[0]
    print(chapter_name)

    chapter_page_list=[chapter_start_url]
    for i in re.findall('<a href="(\d+_\d+\.html)">【.*?】</a>',txt,re.S):
        chapter_page_list.append(url+i)
    print(chapter_page_list)

    next_chapter_url=qu_kong_ge(re.findall('''<a href=".*?" class="prev"><span>&lt;</span>上一章</a>.*?<a href="(.*?)" class="next">下一章<span>&gt;</span></a>''',txt,re.S)[0])
    print(next_chapter_url)


    result=''
    for i in chapter_page_list:
        result=result+get_text(await get_chapter_page_content(page,i))

    print(result)
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



    # result = result.replace('。', '。~!@#$')
    # result = result.replace('」。', '。」')
    # result = result.split('~!@#$')
    # content=[]
    # s=''
    # for i in result:
    #
    #     if '「' not in i and not '」' in i:
    #         content.append(i)
    #         continue
    #
    #     if '「' in i and '」' in i:
    #         content.append(i)
    #         continue
    #
    #     if '「'  in i:
    #         s=s+i
    #         continue
    #
    #     if  '」' in i:
    #         s=s+i
    #         content.append(s)
    #         s=''
    #         continue





    for i in result:
        print(i)
    print(next_chapter_url)

    return [chapter_name,result],next_chapter_url

async def get_chapter_page_content(page,url):
    await goto(page,url)
    random_wait(3,5)
    await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
    random_wait(3,5)
    try:
        # s = await page.evaluate(pageFunction='document.body.textContent', force_expr=True)
        s=await page.evaluate('''() =>  document.querySelector("#content").innerText''')
    except Exception as e:
        print(e)
    return s

def get_text(s):

    result=''
    for i in re.split('\r|\n|\r\n',s):
        try:
            i.encode('utf-8')
        except Exception as e:
            # print(e)
            continue
        if '   ' in  i:
            # print(i)
            result=result+qu_kong_ge(i)
    return result

async def main(url):# 定义main协程函数，
    browser = await launch({'headless':False ,'args':['--window-size=16,12']})#,'--no-sandbox'
    page = await browser.newPage()
    await page.setUserAgent( 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
    await goto(page,url)
    book_name=re.findall('<h1>(.*?)</h1>',await page.content())[0]
    print(book_name)

    chapter_start_url=url+re.findall('<a class="read start" href="(.*?)">.*?</a>',await page.content())[0]
    book=[book_name,[]]
    while 'html' in chapter_start_url:
        print(chapter_start_url,url,chapter_start_url==url)
        content,chapter_start_url=await get_chapter_content(page,chapter_start_url)
        chapter_start_url=url+chapter_start_url
        book[1].append(content)
    await browser.close()

    with open('E:/a/a/{}.txt'.format(book[0]),'w',encoding='utf-8') as f:
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
            print(chapter)
            f.write(chapter[0])
            f.write('\n\r')
            for line in chapter[1]:
                f.write('\n\r')
                line=line.replace(chapter[0].replace(' ',''),'').replace('努力加载中','')
                f.write('\t'+line+'\n\r')
            f.write('\n\r')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()  #协程，开启个无限循环的程序流程，把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
    for i in range(53,100):
        url = 'http://www.skwen.me/13/{}/'.format(i)
        loop.run_until_complete(main(url))












