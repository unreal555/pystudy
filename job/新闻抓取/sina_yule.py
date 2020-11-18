# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/3 0003 上午 9:01
# Tool ：PyCharm

import mytools
from mytools import my_request
import re
from my_csv_tools import write_csv
import time
import os
import json

base_dir='.'
subdir='data'
# subdir=str(time.strftime('%Y-%m-%d'))
filename='新浪娱乐.csv'
abs_path=os.path.join(base_dir,subdir)
data_file_path=os.path.join(base_dir,subdir,filename)



columns_names=['title','content','riqi','pic','laiyuan','url',]

starts = {
    '娱乐要闻4':'''https://cre.mix.sina.com.cn/api/v3/get?cateid=1Q&cre=tianyi&mod=pcent&merge=3&statics=1&length=15&up=4&down=0''',
    '娱乐要闻3':'''https://cre.mix.sina.com.cn/api/v3/get?cateid=1Q&cre=tianyi&mod=pcent&merge=3&statics=1&length=15&up=3&down=0''',
    '娱乐要闻2':'''https://cre.mix.sina.com.cn/api/v3/get?cateid=1Q&cre=tianyi&mod=pcent&merge=3&statics=1&length=15&up=2&down=0''',
    '娱乐要闻1':'''https://cre.mix.sina.com.cn/api/v3/get?cateid=1Q&cre=tianyi&mod=pcent&merge=3&statics=1&length=15&up=1&down=0''',

    }

reg_part = ''''''

reg_li = ''''''

reg_photo_part='''<articleclass="s_cardarticle_box">(.*?)</article>'''

reg_photo_url='''<sectionclass="section-item">.*?src="(.*?)"data-pid.*?<pclass="hd_img_info"><e.*?</em>.*?</p></section>'''

reg_content_part='''<sectionclass="art_pic_cardart_content(.*?)</section>'''

reg_content_line='''<p.*?>(.*?)</p>'''

reg_pic='''<p.*?><imgsrc="(.*?)".*?alt=".*?"></p>'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }

def get_news_index(url):

    page=my_request(url,headers=headers,debug=True)
    temp=json.loads(page)

    if len(temp)==0:
        print('提取失败')
        return
    result=[]
    for i in temp['data']:
        print(i)
        # print(i['surl'],i['title'],i['ctime'],i['reason_text'])
        result.append([i['surl'],i['title'],i['ctime'],i['reason_text']])
    return result

def get_news_content(url):
    page=my_request(url,headers=headers,debug=False)
    text=mytools.qu_kong_ge(page)
    print(text)
    part=''


    if '''://photo''' in url:
        part=re.findall(reg_photo_part,text,re.S)
        print(part)
        if len(part) == 0:
            print('正文part提取失败{}'.format(url))
            return False
        else:
            part = part[0]

        pic_index=re.findall(reg_photo_url,part,re.S)
        print(pic_index)

        '''提取行,连接成段'''
        lines = re.findall(reg_content_line, part, re.S)
        content = '.'.join(lines)
        content = mytools.qu_html_lable(content)
        print(content)

        return content, pic_index

    if '''://video''' in url:
        return False


    part=re.findall(reg_content_part,text,re.S)
    print(part)
    if len(part)==0:
        print('正文part提取失败{}'.format(url))
        return False
    else:
        part=part[0]

    pic_index=re.findall(reg_pic,part,re.S)
    print(pic_index)

    '''提取行,连接成段'''
    lines=re.findall(reg_content_line,part,re.S)
    content='.'.join(lines)
    content=mytools.qu_html_lable(content)
    print(content)

    return content,pic_index



    '''提取行,连接成段'''
    lines=re.findall(reg_content_line,part,re.S)
    content='.'.join(lines)
    content=mytools.qu_html_lable(content)
    print(content)

    return content,pic_index


def Main(logger):
    for key in starts.keys():

        news_index=get_news_index(url=starts[key])

        if news_index==False:
            print('未获得索引,检查索引页{}'.format(starts[key]))
            continue
        news_indexl=news_index.reverse()

        for news_url,news_titile,news_time,news_laiyuan in news_index:
            print(news_url,news_titile,news_time,news_laiyuan)

            if logger.check(news_url)==True:
                print('{},{},已下载,跳过'.format(news_titile,news_url))
                continue

            timeStamp = news_time

            timeArray = time.localtime(timeStamp)

            news_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)


            temp = get_news_content(news_url)
            if temp==False or len(temp)<2:
                print('{}提取有误,跳过')
                continue
            item = {}
            item['laiyuan']=news_laiyuan
            item['url']=news_url
            item['title']=news_titile
            item['riqi']=news_time

            item['content'], item['pic']=temp
            print(item)
            mytools.random_wait(1,3)

            write_csv(file_path=data_file_path,item=item,column_names=columns_names)
            logger.write(item['url'])




