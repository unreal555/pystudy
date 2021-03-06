﻿import requests
import re
import json
import my_html_tools
import csv
import os



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

    yuanshi=response.text
    text = my_html_tools.qu_kong_ge(response.text)
    print(url)
    print(text)


    name=re.findall('<span property="v:itemreviewed">(.*?)</span>',yuanshi,re.S)
    if len(name)==0:
        name=''
    else:
        name=name[0]
    print('name',name)

    daoyan=re.findall('''<spanclass='pl'>导演</span>:<spanclass='attrs'>(.*?)</span></span><br/>''',text,re.S)
    if len(daoyan)==0:
        daoyan=''
    else:
        daoyan=re.findall('<ahref=".*?"rel="v:directedBy">(.*?)</a>',daoyan[0],re.S)
    print('daoyan',daoyan)


    bianju=re.findall('''<span><spanclass='pl'>编剧</span>:<spanclass='attrs'>(.*?)</span></span><br/>''',text,re.S)
    if len(bianju)==0:
        bianju=''
    else:
        bianju=re.findall('''<ahref=".*?">(.*?)</a>''',bianju[0],re.S)
    print('bianju',bianju)


    actor=re.findall('''<spanclass="actor"><spanclass='pl'>主演</span>:<spanclass='attrs'>(.*?)</span></span><br/>''',text,re.S)
    if len(actor)==0:
        actor=''
    else:
        actor=re.findall('''<ahref=".*?">(.*?)</a>''',actor[0],re.S)
    print('actor',actor)


    leixing=re.findall('''<spanclass="pl">类型:</span>(.*?)<br/>''',text,re.S)
    if len(leixing)==0:
        leixing=''
    else:
        leixing=re.findall('''<spanproperty="v:genre">(.*?)</span>''',leixing[0],re.S)
    print('lexing',leixing)


    guojia=re.findall('''<spanclass="pl">制片国家/地区:</span>(.*?)<br/>''',text,re.S)
    if len(guojia)==0:
        guojia=''
    else:
        guojia=guojia[0]
    print('guoajia',guojia)

    yuyan=re.findall('''<spanclass="pl">语言:</span>(.*?)<br/>''',text,re.S)
    if len(yuyan)==0:
        yuyan=''
    else:
        yuyan=yuyan[0]
    print('yuyan',yuyan)

    riqi=re.findall('''<spanclass="pl">上映日期:</span>(.*?)<br/>''',text,re.S)
    if len(riqi)==0:
        riqi=''
    else:
        riqi=re.findall('''<spanproperty="v:initialReleaseDate"content=".*?">(.*?)</span>''',riqi[0],re.S)
    print('riqi',riqi)

    shoubo=re.findall('''<spanclass="pl">首播:</span>(.*?)<br/>''',text,re.S)
    if len(shoubo)==0:
        shoubo=''
    else:
        shoubo=re.findall('''<spanproperty="v:initialReleaseDate"content=".*?">(.*?)</span>''',shoubo[0],re.S)
    print('shoubo',shoubo)


    jishu=re.findall('''<spanclass="pl">集数:</span>(.*?)<br/>''',text,re.S)
    if len(jishu)==0:
        jishu=''
    else:
        jishu=jishu[0]
    print('jishu',jishu)


    danjipianchang=re.findall('''<spanclass="pl">单集片长:</span>(.*?)<br/>''',text,re.S)
    if len(danjipianchang)==0:
        danjipianchang=''
    else:
        danjipianchang=danjipianchang[0]
    print('danjipianchang',danjipianchang)


    imdb=re.findall('''<spanclass="pl">IMDb链接:</span><ahref="(.*?)"target="_blank"rel="nofollow">.*?</a><br>''',text,re.S)
    if len(imdb)==0:
        imdb=''
    else:
        imdb=imdb[0]
    print('imdb',imdb)

    othername=re.findall('''<spanclass="pl">又名:</span>(.*?)<br/>''',text,re.S)
    if len(othername)==0:
        othername=''
    else:
        othername=othername[0]
    print('othername',othername)



    pianchang=re.findall('''<spanclass="pl">片长:</span>(.*?)<br/>''',text,re.S)
    if len(pianchang)==0:
        pianchang=''
    else:
        pianchang=re.findall('''<spanproperty="v:runtime"content=".*?">(.*?)</span>''',text,re.S)
    print('pianchang',pianchang)

    desc=re.findall('''<span property="v:summary".*?>(.*?)</span>''',yuanshi,re.S)
    if len(desc)==0:
        desc=''
    else:
        desc=desc[0].replace('\u3000','').replace('<br/>','').replace('\n','').replace('                                    <br />','').replace('  ','')
    print('desc',desc)




    rate=re.findall('<strongclass="llrating_num"property="v:average">(.*?)</strong>',text,re.S)
    if len(rate)==0:
        rate=''
    else:
        rate=rate[0]
    vote_count=re.findall('<spanproperty="v:votes">(.*?)</span>',text,re.S)
    if len(vote_count)==0:
        vote_count=''
    else:
        vote_count=vote_count[0]

    print('rate,vote_count',rate,vote_count)


    print('-'*100)


    item={}
    item['name']=name
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
    item['shoubo']=shoubo
    item['jishu']=jishu
    item['imdb']=imdb
    item['danjipianchang']=danjipianchang
    item['othername']=othername
    write_movies_file(item)
    write_csv(item)

@my_html_tools.execute_lasts_time
def main():
    for i in range(0,500):
        url='https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={}'.format(i*20)
        page=requests.get(url,headers=headers).text
        result=json.loads(page)
        for i in result['data']:
            parse_html(i['url'])
            my_html_tools.random_wait(1,7)



def write_movies_file(str):
    with open('./douban_film.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(str, ensure_ascii=False) + '\n')
        f.flush()


def write_csv(item):
    headers = ['url','name','daoyan','bianju','actor','leixing','guojia','yuyan','riqi','shoubo','pianchang','rate','vote_count', 'desc','jishu','danjipianchang','imdb','othername']

    if not os.path.exists('./douban_film.csv'):
        with open('./douban_film.csv', 'w', newline='',encoding='utf-8-sig') as f:
            # 标头在这里传入，作为第一行数据
            writer = csv.DictWriter(f, headers)
            writer.writeheader()
            f.flush()

    with open('./douban_film.csv', 'a', newline='',encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, headers)
        writer.writerow(item)
        f.flush()


def down_image(url, headers):
    r = requests.get(url, headers=headers)
    filename = re.search('/public/(.*?)$', url, re.S).group(1)
    with open(filename, 'wb') as f:
        f.write(r.content)






if __name__ == '__main__':

    main()

