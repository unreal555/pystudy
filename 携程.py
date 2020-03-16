import requests
import re
from time import sleep
import random




headers={
        'authority':'you.ctrip.com',
        'method':'POST',
        'path':'/destinationsite/TTDSecond/SharedView/AsynCommentView',
        'scheme':'https',
        'accept':'*/*',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9',
        'content-type':'application/x-www-form-urlencoded',
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }



def wait():
    temp = random.randint(2, 4)
    sleep(temp)
    print("wait {} second".format(temp))
    return



url='https://you.ctrip.com/sight/hongyegu128/50902.html'

response=requests.get(url,headers=headers)
page=re.sub('\s+','',response.text)

# 'resourceid'    资源序号，系统指定
# 'resourcetype'    资源类型，系统指定
# 'districtid'      城市的id
# 'districtename'   城市的代码
# 'star'              0全部    5很好   4好  3一般   2差   1很差
# 'tourist'          0不选          1商务旅行     2朋友出游    3情侣出游   4家庭亲子   5单独旅行
# 'order'          3只能排序，2有用数量排序，1时间排序
# 'poiid'
# 'pagenow'    页码
# 'usefulDataId'   是否有用


keys=['resourceid','resourcetype','districtid','districtename','star','tourist','order','poiid','pagenow','usefulDataId']
values=re.findall('varresourceid="(.*?)";varresourcetype="(.*?)";vardistrictid="(.*?)";vardistrictename="(.*?)";varstar="(.*?)";vartourist="(.*?)";varorder="(.*?)";varpoiid="(.*?)";varpagenow="(.*?)";varusefulDataId=""(.*?)',page)[0]
form=dict(zip(keys,values))

numpage=re.findall('<bclass="numpage">(\d+)</b>页</span><aclass="gopage"',page)[0]

print(form)

url='https://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView'



for i in range(1,int(numpage)):
    form['pagenow']=str(i)
    response=requests.post(url, data=form,headers=headers)
    page = re.sub('\s+', '', response.text)
    page=re.sub('&#x0A','',page)
    result=re.split('<!--开始标注一条评论-->',page)
    num=1
    for j in result:
        if 'userimg' not in j or 'author' not in j:
            continue
        username=re.findall('''<aitemprop="author"href=".*?title="(.*?)"target="_blank">(.*?)</a></span>''',j)[0][0]
        comment = re.findall('''<liitemprop="description"class="main_con"><spanclass="heightbox">(.*?)</span><pclass="commenttoggle">''',j)[0]
        time=re.findall('''<spanclass="time_line"><emitemprop="datePublished">(\d+-\d+-\d+)</em></span>''',j)[0]

        print('共{}页评论，第{}页第{}条评论:--时间：{}   评论者：{}    内容：{}'.format(numpage,i,num,time,username ,comment))
        num+=1
    wait()

