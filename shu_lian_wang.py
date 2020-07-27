# -*-coding:utf-8-*-
import requests
import os
import re
import random
from time import sleep
from pubsub import pub

'''
readme
正常来说下载小说,最重要的就是下面两个参数,novel_url和headers['Cookie]
novel_url为这个下载的入口,定义了要下哪一部小说,具体地址为小说的全章节索引页面,直接复制过来黏贴好就可以了
headers['Cookie']用于携带登陆信息,为了速度,没有编写登陆模块,需要去浏览器获得cookie信息用于访问收费章节
若是下载正常,则不需要修改,但是如果收费内容下载不到,说明登陆的cookie信息已经失效,则需要重新到浏览器登陆账号,获得cookie信息复制到下面的变量位置
'''

# novel_url = 'http://vip.shulink.com/html/69/69330/indexasc.html'
novel_url ='http://vip.shulink.com/files/article/html/68/68033/index.html'
novel_url='http://vip.shulink.com/files/article/html/139/139522/index.html'

'''此处为小说入口,也就是该小说的章节索引页面'''

Cookie= '''PHPSESSID=ie2dts4ii60anit1mvk5bep9tr; jieqiUserInfo=jieqiUserId%3D369080%2CjieqiUserUname%3D%B6%AB%BC%D2%D6%D6%CA%F7%2A369080%2CjieqiUserName%3D%26%23x4E1C%3B%26%23x5BB6%3B%26%23x79CD%3B%26%23x6811%3B%26%23x002A%3B%26%23x0033%3B%26%23x0036%3B%26%23x0039%3B%26%23x0030%3B%26%23x0038%3B%26%23x0030%3B%2CjieqiUserGroup%3D3%2CjieqiUserGroupName%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserVip%3D1%2CjieqiUserHonorId%3D6%2CjieqiUserHonor%3D%26%23x4E16%3B%26%23x5916%3B%26%23x9AD8%3B%26%23x4EBA%3B%2CjieqiUserToken%3D051bf5fce761675b226e5ffb93b5ea8d%2CjieqiCodeLogin%3D0%2CjieqiCodePost%3D0%2CjieqiUserPassword%3D02822ce4eaa605e1653d8dfe5951d30c%2CjieqiUserAccount%3D%26%23x4E1C%3B%26%23x5BB6%3B%26%23x79CD%3B%26%23x6811%3B%26%23x002A%3B%26%23x0033%3B%26%23x0036%3B%26%23x0039%3B%26%23x0030%3B%26%23x0038%3B%26%23x0030%3B%2CjieqiUserLogin%3D1592825790; jieqiVisitInfo=jieqiUserLogin%3D1592825790%2CjieqiUserId%3D369080; jieqiRecentRead=68033.5036865.1.1592739508.379396-69330.5075005.1.1592742596.379396-139522.5203760.1.1592825793.369080'''
'''此处为登陆后的cookie信息,收费章节不携带cookie是无法下载的'''



domain = 'http://vip.shulink.com/'   #书连网域名

def get_headers():
    '''
    返回headers,本函数只是为了整洁才定义
    '''
    headers = {}  # 定义requests的请求头信息
    headers['Accept-Encoding'] = 'gzip, deflate'
    headers[
        'Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    headers['Accept-Language'] = 'zh-CN,zh;q=0.9'
    headers['Cache-Control'] = 'no-cache'
    headers['Connection'] = 'Keep-Alive'
    headers['Host'] = 'vip.shulink.com'
    headers['Pragma'] = 'no-cache'
    headers['Referer'] = 'http://vip.shulink.com/files/article/html/139/139522/index.html'
    headers['Upgrade-Insecure-Requests'] = '1'
    headers[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    headers['Cookie'] = '''PHPSESSID=fo8fjmqeaph67sq651rtfdro8h; jieqiUserInfo=jieqiUserId%3D379396%2CjieqiUserUname%3D%B6%AB%C4%DE%2CjieqiUserName%3D%26%23x4E1C%3B%26%23x9713%3B%2CjieqiUserGroup%3D3%2CjieqiUserGroupName%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserVip%3D1%2CjieqiUserHonorId%3D5%2CjieqiUserHonor%3D%26%23x65E0%3B%26%23x53CC%3B%26%23x9690%3B%26%23x58EB%3B%2CjieqiUserToken%3Ddc9d608a620ec41e3ceb6645d3c886cb%2CjieqiCodeLogin%3D0%2CjieqiCodePost%3D0%2CjieqiUserPassword%3Ddd9afc93112397f0cf6b597453bb6b8e%2CjieqiUserAccount%3D%26%23x4E1C%3B%26%23x9713%3B%2CjieqiUserLogin%3D1592737763; jieqiVisitInfo=jieqiUserLogin%3D1592737763%2CjieqiUserId%3D379396; jieqiVisitId=article_articleviews%3D68033%7C69330; jieqiRecentRead=68033.5036865.1.1592739461.379396'''
    return headers

def get_chapter_list(s):
    '''函数用于获取章节名和章节链接的队列'''
    temp = re.findall('<dlclass="index"(.*?)</dl>', s, re.S)[0]   #使用正则提取章节索引

    chapter_list = re.findall('href="(.*?)"title=.*?>(.*?)</a>',temp, re.S)     #使用正则提取具体章节信息

    print(chapter_list)

    if chapter_list!=[]:        #如果提取到的信息不为空,说明成功取到了章节信息,返回,否则说明没有取到数据,返回false
        return chapter_list
    else:
        return False

def get_title(s):

    '''
    用于提取小说的名称,作者等信息
    若提取的到信息长度为1,说明提取成功,因为需要用该信息生成小说文件的名车,所以使用qu_te_shu_zi_fu函数清除掉不能作为文件名使用的字符.
    若提取到的信息长度为0,也就是[],则文章名提取失败,返回false
    '''
    result=re.findall('<title>(.*?)</title>', s)  #正则表达式提取

    if len(result)==1:
        return qu_te_shu_zi_fu(result[0])
    else:
        return False

def create_file(filepath,title):
    '''
    根据filepath,创建小说存储文件,如果文件存在,则略过,若不存在,则创建文件并写入小说的标题
    '''
    if os.path.exists(filepath):
        pass
    else:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(title)
            f.write('\r\n\r\n')

def qu_te_shu_zi_fu(s):
    '''
    将不能作为文件名的特殊字符'[\/:*?"<>|]替换成-
    '''
    if isinstance(s, str):
        return re.sub('[\/:*?"<>|]','-',s)
    else:
        print('给字符串')
        return False
    
def random_wait(n=1,m=3,*args):
    '''
    用于随机等待一段n-m的时间,防止请求速度过快,被网站屏蔽
    '''
    if not (isinstance(n, (int, float)) and isinstance(m, (int, float))):   #判断n和m是不是正数或小数
        print('参数输入错误，不是整数或小数，采用默认值1，3')
        n=1
        m=3
    if n>m:
        n,m=m,n
    temp = random.uniform(n, m)             #生成一个n-m之间的随机数
    print("wait {} second".format(temp))    #提示要等待多久
    sleep(temp)                               #等待这个随机数的时间

def qu_kong_ge(s):
    '''
    去除html页面的所有空格和隐藏的控制字符,清洗网页垃圾信息,方便正则提取
    '''
    if isinstance(s, str):             #判断给的是不是str字符串,如果是,则通过re.sub清洗空格等字符,并返回
        return re.sub('\s+', '', s)
    else:                             #如果给的不是字符串,返回false
        print('老兄，给字符串')
        return False

def start():

    headers=get_headers()         #获得请求头信息

    headers['Cookie']=Cookie       #若cookie有变化,则覆盖

    index_html = requests.get(novel_url, headers=headers).content.decode('gbk')
    '''请求章节索引页面,用于提取章节名和章节的链接'''

    index_html=qu_kong_ge(index_html)
    '''去除章节索引页面中所有空白字符,方便正则公式提取需要的信息'''

    title=get_title(index_html)
    '''调用函数,获取小说的标题'''

    filepath=os.path.join('./',title+'.txt')
    '''根据小说标题,生成文件路径'''
    print(filepath)

    chapter_list=get_chapter_list(index_html)
    '''调用函数,获得章节信息,包含名称和链接'''

    create_file(filepath,title)
    '''根据filepath创建文件,若文件已存在,则略过,不存在,则创建'''

    with open(filepath, 'r', encoding='utf-8') as f:
        finished = f.read()
    '''读取小说文件内的数据,存入finished'''

    for chapter_url,chapter_name in chapter_list:
        print(chapter_url,chapter_name)


    for chapter_url,chapter_name in chapter_list:

        url = domain + chapter_url           #通过域名和章节链接拼接成章节的真实url

        if url in finished:            #若该章节名称已经存在于文件中,说明本章已经下载,跳过
            print(chapter_name + '已下载')
            continue                        #已下载章节,不再下载,continue直接跳入下一次循环,若if判断为真本语句执行,之后的语句全部略过不再执行


        pub.sendMessage('stat',msg=url+'   '+chapter_name+'\r\n')          #输出章节和章节的url,用于调试纠错和

        result = requests.get(url, headers=headers).content.decode('gbk')      #请求章节页面

        result = qu_kong_ge(result)                           #调用函数,去除页面文件中的空格,

        result = re.findall('<divid="acontent"class="acontent">(.*?</div>)', result, re.S)[0]    #提取内容

        result=result.replace('</div>','<br/><br/>')

        print(result)

        result = re.findall('[&emsp;]*(.*?)<br/>', result, re.S)



        if result!=[]:     #如果提取到的result不是空的,那么说明已经取到了章节内容,则开始把章节写入文件

            with open(filepath, 'a', encoding='utf-8') as f:      #本语句写入章节的名称
                f.write(url+'\r\n')
                f.write(chapter_name.replace('&emsp;','  '))
                f.write('\r\n\r\n')

            for i in result:                                 #本循环,用于将章节的每一句写入文件
                print(i)
                with open(filepath, 'a', encoding='utf-8') as f:
                    f.write('\t' + i + '\r\n')

            with open(filepath, 'a', encoding='utf-8') as f:             #本语句,用于在一章的结束,多写入一个换行
                f.write('\r\n')
                f.flush()


        random_wait()        #随机等待1-3秒,开始请求下一章

if __name__ == '__main__':
    start()