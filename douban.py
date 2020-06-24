import requests
import re
import json
import mytools
import csv
from lxml import etree
import os
import wordcloud
import matplotlib.pyplot as plt


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}

def parse_html(url):
    print(url)
    response = requests.get(url, headers=headers)

    while response.status_code!=200:
        try:
            response = requests.get(url, headers=headers)
        except:
            pass


    text = mytools.qu_kong_ge(response.text)
    html=etree.HTML(text)
    print(text)




    daoyan=re.findall('''<spanclass='pl'>导演</span>:<spanclass='attrs'>(.*?)</span></span><br/>''',text,re.S)[0]
    daoyan=re.findall('<ahref=".*?"rel="v:directedBy">(.*?)</a>',daoyan,re.S)[0]

    print(daoyan)

    bianju=re.findall('''<span><spanclass='pl'>编剧</span>:<spanclass='attrs'>(.*?)</span></span><br/>''',text,re.S)[0]
    bianju=re.findall('''<ahref=".*?">(.*?)</a>''',bianju,re.S)

    print(bianju)

    actor=re.findall('''<spanclass="actor"><spanclass='pl'>主演</span>:<spanclass='attrs'>(.*?)</span></span><br/>''',text,re.S)[0]
    actor=re.findall('''<ahref=".*?">(.*?)</a>''',actor,re.S)

    print(actor)

    leixing=re.findall('''<spanclass="pl">类型:</span>(.*?)<br/>''',text,re.S)[0]
    leixing=re.findall('''<spanproperty="v:genre">(.*?)</span>''',leixing,re.S)
    print(leixing)

    guojia=re.findall('''<spanclass="pl">制片国家/地区:</span>(.*?)<br/>''',text,re.S)[0]
    print(guojia)

    yuyan=re.findall('''<spanclass="pl">语言:</span>(.*?)<br/>''',text,re.S)[0]
    print(yuyan)

    riqi=re.findall('''<spanclass="pl">上映日期:</span>(.*?)<br/>''',text,re.S)[0]
    print(riqi)


    pianchang=re.findall('''<spanclass="pl">片长:</span>(.*?)<br/>''',text,re.S)[0]
    print(pianchang)

    desc=re.findall('''<spanproperty="v:summary".*?>(.*?)</span>''',text,re.S)
    print(desc)

    rate=re.findall('<strongclass="llrating_num"property="v:average">(.*?)</strong>',text,re.S)[0]
    vote_count=re.findall('<spanproperty="v:votes">(.*?)</span>',text,re.S)[0]
    print(rate,vote_count)





    item={}
    item['url']=url
    item['daoyan']=daoyan
    item['bianju']=bianju
    item['actor']=actor
    item['leixing']=leixing
    item['guojia']=guojia
    item['yuyan']=yuyan
    item['riqi']=riqi
    item['pianchang']=pianchang
    item['rate']=rate
    item['vote_count']=vote_count
    item['desc']=desc
    write_movies_file(item)
    write_csv(item)

@mytools.execute_lasts_time
def main():
    url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=1000&page_start=0'
    page=requests.get(url,headers=headers).text
    result=json.loads(page)
    for i in result['subjects']:
        parse_html(i['url'])
        mytools.random_wait(1,10)


    # for offset in range(0, 250, 25):
    #     url = 'https://movie.douban.com/top250?start=' + str(offset) + '&filter='
    #     for item in parse_html(url):
    #         print(item)
    #


def write_movies_file(str):
    with open('./douban_film.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(str, ensure_ascii=False) + '\n')
        f.flush()


def write_csv(item):
    headers = ['url','daoyan','bianju','actor','leixing','guojia','yuyan','riqi','pianchang','rate','vote_count', 'desc',]

    if not os.path.exists('./douban_film.csv'):
        with open('./douban_film.csv', 'w', newline='',encoding='utf-8-sig') as f:
            # 标头在这里传入，作为第一行数据
            writer = csv.DictWriter(f, headers)
            writer.writeheader()
            f.flush()
    else:
        with open('./douban_film.csv', 'a', newline='',encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, headers)
            writer.writerow(item)
            f.flush()






def down_image(url, headers):
    r = requests.get(url, headers=headers)
    filename = re.search('/public/(.*?)$', url, re.S).group(1)
    with open(filename, 'wb') as f:
        f.write(r.content)



# def star_transfor(str):
#     if str == 'rating5-t':
#         return '五星'
#     elif str == 'rating45-t':
#         return '四星半'
#     elif str == 'rating4-t':
#         return '四星'
#     elif str == 'rating35-t':
#         return '三星半'
#     elif str == 'rating3-t':
#         return '三星'
#     elif str == 'rating25-t':
#         return '两星半'
#     elif str == 'rating2-t':
#         return '两星'
#     elif str == 'rating15-t':
#         return '一星半'
#     elif str == 'rating1-t':
#         return '一星'
#     else:
#         return '无星'


def create_ciyun():
    all={}
    temp=[]
    with open('./douban_film.txt','r',encoding='utf-8') as f:
        temp=f.readlines()

    for i in range(0,len(temp)):
        all[i]=json.loads(temp[i])

    count={}
    for key in all.keys():
        print(all[key]['riqi'])
        year=re.findall('(\d{4})',all[key]['riqi'])
        print(year)
        m=min(year)

        if str(m) not in count.keys():
            count[m]=1
        else:
            count[m]=count[m]+1
    print(count)

    result=[]
    for key in count.keys():
        result.append((key,count[key]))

    print(result)

    wc = wordcloud.WordCloud(font_path='C:/Windows/Fonts/simhei.ttf',max_words=200,     max_font_size=100)

    wc.generate_from_frequencies(count)
    plt.imshow(wc)
    plt.waitforbuttonpress(0)



if __name__ == '__main__':

    # main()
    create_ciyun()