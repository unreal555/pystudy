1  # coding: utf-8
2  # Team : None
3  # Author：zl
4  # Date ：2020/6/30 0030 下午 12:08
5  # Tool ：PyCharm


import requests
import re
import os
import csv
import random
import time

headers={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
# 'Host':'www.hbjc.gov.cn',
'Referer':'http://www.hbjc.gov.cn/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}

table_names=['title','content','riqi','desc','url']

print('111')

def qu_html_lable(s):
    reg = re.compile(r'<[^>]+>', re.S)
    if isinstance(s, str):
        return reg.sub('', s)
    else:
        print('老兄，给字符串')
        return 0

def parse_index(link,desc):
    response=requests.get(link,headers=headers)

    text=response.text

    result=re.findall('''<ul class="artlist" style="overflow-y:auto;">(.*?)</ul>''',text,re.S)[0]

    result=re.findall('''<li><a href="(.*?)">(.*?)</a><span class="date" style="right:10px;">\[(.*?)\]</span></li>''',result,re.S)

    for url,title,riqi in result:
        if url in log:
            print('曾经已经下载,跳过')
            continue


        item = {}
        item['desc']=desc
        if '../.' in url:
            continue
        else:
            item['url']=url.replace('./',desc)
        item['title']=title
        item['riqi']=riqi
        item['content']=get_content(item['url'])

        print(item)
        time.sleep(random.randint(1,3))
        write_csv(item)

        with open('./log.txt', 'a', encoding='utf-8') as f:
            f.write(url+'\r\n')

def get_content(page_url):

    print(page_url)
    response=requests.get(page_url,headers=headers)
    if 'www.spp.gov.cn/' in page_url:
        text=response.content.decode('utf-8')

        result=re.findall('<p style="margin-bottom: 1.5em; text-indent: 2em;">(.*?)</p>',text,re.S)

        result = '.'.join(result)
        result=qu_html_lable(result)
        return(result)

    else:
        text=response.text
        result = re.findall(''' <!--正文开始-->(.*?)<!--正文结束-->''', text, re.S)[0]
        result = qu_html_lable(result)
        result = result.replace(' ', '').replace('\u3000', '').replace('\n', '')
        return (result)




def write_csv(item):
    filename=item['desc'].split('/')[-2]
    if os.path.exists('./{}.csv'.format(filename)):
        with open('./{}.csv'.format(filename), 'a', newline='', encoding='utf-8-sig') as f:

            writer = csv.DictWriter(f, table_names)
            writer.writerow(item)
            f.flush()
    else:
        with open('./{}.csv'.format(filename), 'w', newline='', encoding='utf-8-sig') as f:
            # 标头在这里传入，作为第一行数据
            writer = csv.DictWriter(f, table_names)
            writer.writeheader()
            writer.writerow(item)
            f.flush()






ajxx=['http://www.hbjc.gov.cn/qwfb/ajxx/']  #权威发布子版块案件信息索引页,共18页
for i in range(1,18):
    ajxx.append('http://www.hbjc.gov.cn/qwfb/ajxx/index_{}.shtml'.format(i))

zdal=['http://www.hbjc.gov.cn/qwfb/zdal/',
      'http://www.hbjc.gov.cn/qwfb/zdal/index_1.shtml'
      ]  #权威发布子版块指导案例索引页,共2页

ndbg=['http://www.hbjc.gov.cn/gzbg/ndbg/',
      'http://www.hbjc.gov.cn/gzbg/ndbg/index_1.shtml'
      ]  #工作报告子版块年度报告索引页,共两页

bnbg=['http://www.hbjc.gov.cn/gzbg/bnbg/'] #工作报告子版块半年报告索引页,一页
ztbg=['http://www.hbjc.gov.cn/gzbg/ztbg/']#工作报告子版块专题报告索引页,一页


print(ajxx)
print(zdal)
print(ndbg)
print(bnbg)
print(ztbg)

log=''

if os.path.exists('./log.txt'):
    with open('./log.txt','r',encoding='utf-8') as f:
        log=f.read()
else:
    with open('./log.txt', 'w', encoding='utf-8') as f:
        f.write('')
    log=''

for i in zdal:
    print('下载指导案例' + i)
    parse_index(i,desc='http://www.hbjc.gov.cn/qwfb/zdal/')



for i in ndbg:
    print('下载年度报告' + i)
    parse_index(i, desc='http://www.hbjc.gov.cn/gzbg/ndbg/')

for i in bnbg:
    print('下载半年报告' + i)
    parse_index(i, desc='http://www.hbjc.gov.cn/gzbg/bnbg/')

for i in ztbg:
    print('下载工作报告' + i)
    parse_index(i, desc='http://www.hbjc.gov.cn/gzbg/ztbg/')

for i in ajxx:
    print('下载案件信息'+i)
    parse_index(i,desc='http://www.hbjc.gov.cn/qwfb/ajxx/')

