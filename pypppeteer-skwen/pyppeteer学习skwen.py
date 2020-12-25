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
from mytools import qu_kong_ge, random_wait,qu_te_shu_zi_fu
from zhon.hanzi import punctuation as zhongwenbiaodian
from string import punctuation as yingwenbiaodian


def createCounter():
    s = 0

    def counter():
        nonlocal s
        s = s + 1
        return s

    return counter


async def go(page,url):
    while 1:
        num = count()
        print(num)

        try:
            await page.goto(url)
            break
        except Exception as e:
            if 1:print(e)
            random_wait(2, 4)
            continue


async def get_chapter_content(page, chapter_start_url):
    result = ''
    
    while 1:
        try:
            result = result + await get_chapter_page_content(page, chapter_start_url)
            txt = await page.content()
            chapter_name = re.findall('<h1 class="page-title">(.*?)</h1>', txt)[0]

            if 1:print(chapter_name)
            
            chapter_page_list = [chapter_start_url]

            
            for i in re.findall('<a href="(\d+_\d+\.html)">【.*?】</a>', txt, re.S):
                if 0:print(i)
                chapter_page_list.append(url + i)
                


            next_chapter_url = qu_kong_ge(re.findall('''上一章</a>.*?<ahref="(.*?)"class="next">下一章''',qu_kong_ge(txt), re.S)[0])
            
            if 1:print(next_chapter_url)
            
            break
        except Exception as e:
            if 1:print(e)
            continue
    

    if 0:print(chapter_page_list)

    
    for i in chapter_page_list[1:]:
        result = result + await get_chapter_page_content(page, i)
    if 0:print(result)

    result = result.replace('】', '」')
    result = result.replace('【', '「')
    result = result.replace('”', '」')
    result = result.replace('“', '「')


    result = result.replace('[', '「')
    result = result.replace(']', '」')
    
    result = result.replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '')



    result = result.replace('。」', '」juahojuhao')
    result = result.replace('。', '。\t\t\t\t\t')
    result = result.replace('」juahojuhao','。」' )
    
    

    
    result = result.replace('。」', '。」\t\t\t\t\t')
    result = result.replace('！」', '！」\t\t\t\t\t')
    result = result.replace('……」', '……」\t\t\t\t\t')
    result = result.replace('?」', '?」\t\t\t\t\t')
    result = result.replace('.」', '.」\t\t\t\t\t')
    result = result.replace('!」', '!」\t\t\t\t\t')
    result = result.replace('？」', '？」\t\t\t\t\t')





    
    result = result.split('\t\t\t\t\t')

    for i in result:
        if 0:print(i)
    if 0:print(next_chapter_url)

    return [chapter_name, result], next_chapter_url


async def get_chapter_page_content(page, url):
    if 0:print('get_chapter_page_content')
    while 1:
        try:
            await go(page, url)
            random_wait(0.1,0.2)
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            random_wait(0.1,0.2)
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            random_wait(0.1,0.2)
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            random_wait(0.1,0.2)
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            random_wait(0.1,0.2)
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            random_wait(0.1,0.2)
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            random_wait(0.1,0.2)
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            random_wait(0.1,0.2)
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            random_wait(0.1,0.2)
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            random_wait(0.1,0.2)
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            random_wait(0.1,0.2)
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            random_wait(0.1,0.2)
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            


            order_content = await page.evaluate('''() =>  document.querySelector("#content").innerText''')

            html=await page.content()

            

            
            html=qu_kong_ge(html,include_space=True)



            content_part=re.findall(r'''class="bd".*?>(.*?)<divid="cload".*?>''',html)[0]



            order_content_has_grabage=[]

            for line in re.split('\r|\n',order_content):

                line=qu_kong_ge(line,include_space=True)
                line=line.replace('&nbsp;','')
                
                if len(line)==0:
                    continue
                else:
                    order_content_has_grabage.append(line)

        
            
            reg='<p.*?>[&nbsp;]{0,}(.*?)</p>'


            has_png=[]
            no_png=[]


            for line in set(re.findall(reg,content_part)):

                if 0:print(line)

  
                line=line.replace('<br>','').replace('\t','').replace('&nbsp;','').replace('&amp;','&').replace('&quot;','"').replace('&gt;','>').replace('&lt;','<')#&nbsp|&quot|&amp|&lt|&gt等html字符转义_wusuopuBUPT的专...

                if len(line)==0:
                    continue
                
                else:
                    has_png.append(line)
                    no_png.append(re.sub('<img.*?png">','',line))


            result=[]


            for line in order_content_has_grabage:
                
                
                #  print(line,no_png.index(line) ,has_png[no_png.index(line)])
                
                try:

                    no=no_png.index(line)

                    result.append(has_png[no])

                except ValueError as e:

                    pass
                




            

            temp=[]
            for i in result:
                    temp.append(re.sub('<imgsrc=".*?">','',i))



            lost1=set(temp)-set(no_png)
            
            lost2=set(no_png)-set(temp)
         
            
            if (len(lost1)!=0) or (len(lost2)!=0):
                
                print(url,len(result),len(has_png),'内容可能丢失，重试')
                    
                #print(temp)

                #print(no_png)

                print('lost:',lost1,lost2)


                #for i in  order_content_has_grabage:
                #    try:
                #        print(i)
               #     except Exception as e:
                #        print(e)
            else:
                print('貌似本节无错')
                



            
            return ''.join(result)
            
        except Exception as e:
            
            if 1:print(e)
            
            
            continue



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

        txt=qu_kong_ge(await page.content(),include_space=False)
        
        book_name = re.findall('<h1>(.*?)</h1>',txt)[0]
        if 0:print(book_name)

        author=re.findall('<a href="/author/.*?">(.*?)</a>',txt)[0]
        if 0:print(author)
        
        fenlei=re.findall('类型：(.*?)<br>',txt)[0]
        if 0:print(fenlei)

        desc=re.findall('<div class="mod book-intro">.*?<div class="bd">(.*?)</div>',txt)[0]

        if 0:print(desc)
        
        chapter_start_url = domain+re.findall('<a class="read start" href="(.*?)">.*?</a>', await page.content())[0]
        print(chapter_start_url)


        filename=qu_te_shu_zi_fu(book_name+'_'+fenlei+'_'+author)
        book = [filename, []]
        
        await page.close()
        
    except Exception as e:
        if 0:print(e)
        
    while 'html' in chapter_start_url:
        
        try:
            page = await browser.newPage()
            await page.setUserAgent(
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
            if 0:print(chapter_start_url, url, chapter_start_url == url)

            
            content, chapter_start_url = await get_chapter_content(page, chapter_start_url)


            chapter_start_url = url+ chapter_start_url
            
            book[1].append(content)
            await  page.close()


        except Exception as e:
            if 0:print(e)
        
    await browser.close()

    with open('./a/{}.txt'.format(book[0]), 'w', encoding='utf-8') as f:
        
        f.write(book[0])
        f.write('\r\n')
        f.write('\r\n')
        f.write('\r\n')

        f.write(desc)
        f.write('\r\n')
        f.write('\r\n')
        f.write('\r\n')
        
        for chapter in book[1]:
            f.write(chapter[0])
            f.write('\r\n')
        f.write('\r\n')
        f.write('\r\n')
        
        for chapter in book[1]:
            f.write('\t'+chapter[0])
            f.write('\r\n')
            for line in chapter[1]:
                f.write('\r\n')
                line = line.replace(chapter[0].replace(' ', ''), '').replace('努力加载中', '')
                f.write('\t' + line + '\r\n')
            f.write('\r\n')


if __name__ == '__main__':
    domain='http://www.skwen.me'
    

    
    count = createCounter()
    loop = asyncio.get_event_loop()  # 协程，开启个无限循环的程序流程，把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
    logger=my_logger.my_logger()
    
    with open('wanben.log','r',encoding='utf-8') as f:
        result=(re.findall(''' # # # \d+-\d+-\d+ \d+:\d+:\d+	\d+	(\d+)	(.*?) # # # ''',f.read()))
    for n,title in result:
        url=domain+'/0/{}/'.format(6)
        if logger.check(url)==True and logger.check(title)==True:
            print('{}已下载,跳过'.format(url))
            continue
        else:
            loop.run_until_complete(main(url, count=createCounter()))
            logger.write(url,title)
    


   # for i in range(5, 6):  # 53
    
   #      loop.run_until_complete(main(url, count=createCounter()))
