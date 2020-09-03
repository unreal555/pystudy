import re
from selenium import webdriver
import time
import random
import my_logger
import my_csv_tools

min_s=0.1
max_s=0.2
n=201
proxy='--proxy-server=http://58.59.25.122:1234'
proxy=''


# chrome_options.add_argument("--headless")
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')

ops = webdriver.ChromeOptions()
ops.add_experimental_option('excludeSwitches', ['enable-automation'])

if proxy!='':
    ops.add_argument(proxy)

driver = webdriver.Chrome(options=ops,executable_path=".\chromedriver.exe")

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"""})

logger=my_logger.logger()

csv_header=['登记号','相关登记号','药物名称','药物类型','备案号','适应症','试验专业题目','试验通俗题目','试验方案编号','方案最新版本号','版本日期','方案是否为联合用药','申请人名称','联系人姓名','联系人座机',
            '联系人手机号','联系人Email','联系人邮政地址','联系人邮编','试验目的','试验分类','试验分期','设计类型','随机化','盲法','试验范围','受试者年龄','受试者性别','健康受试者','入选标准','排除标准',
            '试验药','对照药','主要终点指标及评价时间','次要终点指标及评价时间','主要研究者信息','各参加机构信息','伦理委员会信息','数据安全监查委员会','为受试者购买试验伤害保险',
            '主要研究者信息','各参加机构信息','伦理委员会信息','试验状态','试验人数','受试者招募及试验完成日期','临床试验结果摘要']
def createCounter():
    s = 0
    def counter():
        nonlocal s
        s = s + 1
        return s
    return counter

def qu_html_lable(s):
    reg = re.compile(r'<[^>]+>', re.S)
    if isinstance(s, str):
        return reg.sub('', s)
    else:
        print('老兄，给字符串')
        return False

def get_random_num(n=1,m=3,*args):
    if not (isinstance(n, (int, float)) and isinstance(m, (int, float))):
        print('参数输入错误，不是整数或小数，采用默认值1，3')
        n=1
        m=3

    if n>m:
        print('m,n不是小-大顺序,自动调换mn数值')
        n,m=m,n
    num=random.uniform(n, m)
    print('获得的随机数为{}'.format(num))
    return num

def random_wait(n=1,m=3,show=True,*args):
    t = get_random_num(n,m)
    print("wait {} second".format(t))

    if show == True:
        while t>1:
            print('\r','counting:',t,end='',flush=True)
            time.sleep(1)
            t=t-1
        time.sleep(t)
        print(print('\r','wait end,continue work',end='',flush=True))

    else:
        time.sleep(t)

    return True


def qu_kong_ge(s):
    t= re.sub('[\t\r\n]','',s)
    t=re.sub('\xa0',' ',t)
    return t


def geshihua(s):

    l=[]

    for i in s:
        l.append(qu_html_lable(i))

    
    if len(l)==0:
        return ''
    
    if len(l)==1:
        return  l[0]

    if len(l)==2:
        if l[0]==l[1]:
            return l[0]
        else:
            return l

    if len(l)>=3:
        
        return l
    

    
        
    


def get_content(driver,url,logger,counter):

    if (counter())%15==0:
        random_wait(3600,3700)
    
    driver.delete_all_cookies()
    driver.get(url)   

    html=driver.page_source

    html=qu_kong_ge(html)


    retry_time=5

    while 1:
        if retry_time<=0:
            print('重试超限,放弃')
            return
        
        if len(re.findall(r'''<th.*?>登记号</th><td.*?>(.*?)</td>''',html,re.S))==0:
            if (counter()) % 15 == 0:
                random_wait(3600, 3700)
            print('有异常情况,开始重试',len(re.findall(r'''<th.*?>登记号</th><td.*?>(.*?)</td>''',html,re.S)))
            random_wait(0.5,1)
            driver.back()
            random_wait(0.5,1)
            driver.delete_all_cookies()
            driver.get(url)
            random_wait(0.5, 1)
            html=driver.page_source
            html=qu_kong_ge(html)
            retry_time=retry_time-1
        else:
            break
                    
    
    item={}
    
    item['登记号']=geshihua(re.findall(r'''<th.*?>登记号</th><td.*?>(.*?)</td>''',html,re.S))



    if logger.check(item['登记号']):
        print('{}已录入,跳过'.format(item['登记号']))
        return

    
    item['相关登记号']=geshihua(re.findall(r'''<th.*?>相关登记号</th><td.*?>(.*?)</td>''',html,re.S))
    item['药物名称']=geshihua(re.findall(r'''<th.*?>药物名称</th><td.*?>(.*?)</td>''',html,re.S))
    item['药物类型']=geshihua(re.findall(r'''<th.*?>药物类型</th><td.*?>(.*?)</td>''',html,re.S))
    item['备案号']=geshihua(re.findall(r'''<th.*?>备案号</th><td.*?>(.*?)</td>''',html,re.S))
    item['适应症']=geshihua(re.findall(r'''<th.*?>适应症</th><td.*?>(.*?)</td>''',html,re.S))
    item['试验专业题目']=geshihua(re.findall(r'''<th.*?>试验专业题目</th><td.*?>(.*?)</td>''',html,re.S))
    item['试验通俗题目']=geshihua(re.findall(r'''<th.*?>试验通俗题目</th><td.*?>(.*?)</td>''',html,re.S))
    item['试验方案编号']=geshihua(re.findall(r'''<th.*?>试验方案编号.*?</th><td.*?>(.*?)</td>''',html,re.S))
    item['方案最新版本号']=geshihua(re.findall(r'''<th.*?>方案最新版本号</th><td.*?>(.*?)</td>''',html,re.S))
    item['版本日期']=geshihua(re.findall(r'''<th.*?>版本日期.*?</th><td.*?>(.*?)</td>''',html,re.S))                  #<th>版本日期:</th><td>2020-07-17</td>
    item['方案是否为联合用药']=geshihua(re.findall(r'''<th.*?>方案是否为联合用药.*?</th><td.*?>(.*?)</td>''',html,re.S))

    
#    print(登记号,相关登记号,药物名称,药物类型,备案号,适应症,试验专业题目,试验通俗题目,试验方案编号,方案最新版本号,版本日期,方案是否为联合用药)

    item['申请人名称']=geshihua(re.findall(r'''<th>申请人名称</th><td.*?>(.*?)</td>''',html,re.S))
    item['联系人姓名']=geshihua(re.findall(r'''<th.*?>联系人姓名</th><td.*?>(.*?)</td>''',html,re.S))
    item['联系人座机']=geshihua(re.findall(r'''<th.*?>联系人座机</th><td.*?>(.*?)</td>''',html,re.S))
    item['联系人手机号']=geshihua(re.findall(r'''<th.*?>联系人手机号</th><td.*?>(.*?)</td>''',html,re.S))
    item['联系人Email']=geshihua(re.findall(r'''<th.*?>联系人Email</th><td.*?>(.*?)</td>''',html,re.S))
    item['联系人邮政地址']=geshihua(re.findall(r'''<th.*?>联系人邮政地址</th><td.*?>(.*?)</td>''',html,re.S))
    item['联系人邮编']=geshihua(re.findall(r'''<th.*?>联系人邮编</th><td.*?>(.*?)</td>''',html,re.S))
#    print(申请人名称,联系人姓名,联系人座机,联系人手机号,联系人Email,联系人邮政地址,联系人邮编)


    item['试验目的']=geshihua(re.findall(r'''div.*?>.*?试验目的</div>(.*?)<div''',html,re.S))
    item['试验分类']=geshihua(re.findall(r'''<th.*?>试验分类</th><td.*?>(.*?)</td>''',html,re.S))
    item['试验分期']=geshihua(re.findall(r'''<th.*?>试验分期</th><td.*?>(.*?)</td>''',html,re.S))
    item['设计类型']=geshihua(re.findall(r'''<th.*?>设计类型</th><td.*?>(.*?)</td>''',html,re.S))
    item['随机化']=geshihua(re.findall(r'''<th.*?>随机化</th><td.*?>(.*?)</td>''',html,re.S))
    item['盲法']=geshihua(re.findall(r'''<th.*?>盲法</th><td.*?>(.*?)</td>''',html,re.S))
    item['试验范围']=geshihua(re.findall(r'''<th.*?>试验范围</th><td.*?>(.*?)</td>''',html,re.S))
#    print(试验目的,试验分类,试验分期,设计类型,随机化,盲法,试验范围)

    item['受试者年龄']=geshihua(re.findall(r'''<th.*?>年龄</th><td.*?>(.*?)</td>''',html,re.S))
    item['受试者性别']=geshihua(re.findall(r'''<th.*?>性别</th><td.*?>(.*?)</td>''',html,re.S))
    item['健康受试者']=geshihua(re.findall(r'''<th.*?>健康受试者</th><td.*?>(.*?)</td>''',html,re.S))   
    item['入选标准']=geshihua(re.findall(r'''<th.*?>入选标准</th><td.*?><table.*?>(.*?)</table></td>''',html,re.S))
    item['排除标准']=geshihua(re.findall(r'''<th.*?>排除标准</th><td.*?><table.*?>(.*?)</table></td>''',html,re.S))
    
#    print(受试者年龄,受试者性别,健康受试者,入选标准,排除标准)



    item['试验药']=geshihua(re.findall(r'''<th.*?>试验药</th><td.*?><table.*?>(.*?)</table></td>''',html,re.S))    
    item['对照药']=geshihua(re.findall(r'''<th.*?>试验药</th><td.*?><table.*?>(.*?)</table></td>''',html,re.S))
    
#    print(试验药,对照药)



    item['主要终点指标及评价时间']=geshihua(re.findall(r'''<th.*?>主要终点指标及评价时间</th><td.*?><table.*?>(.*?)</table></td>''',html,re.S))
            
    item['次要终点指标及评价时间']=geshihua(re.findall(r'''<th.*?>次要终点指标及评价时间</th><td.*?><table.*?>(.*?)</table></td>''',html,re.S))   
    #    print(主要终点指标及评价时间,次要终点指标及评价时间)




    item['数据安全监查委员会']=geshihua(re.findall(r'''<div.*?>6、数据安全监查委员会.*?</div>(.*?)<div''',html,re.S))
#    print( 数据安全监查委员会)

    item['为受试者购买试验伤害保险']=geshihua(re.findall(r'''<div.*?>7、为受试者购买试验伤害保险</div>(.*?)<div''',html,re.S))
#    print(为受试者购买试验伤害保险)


    item['主要研究者信息']=geshihua(re.findall(r'''<div.*?>.*?主要研究者信息</div><table.*?>(.*?)</table>''',html,re.S))
    
    item['各参加机构信息']=geshihua(re.findall(r'''<div.*?>.*?各参加机构信息</div><table.*?>(.*?)</table>''',html,re.S)) 
    
    item['伦理委员会信息']=geshihua(re.findall(r'''<div.*?>.*?伦理委员会信息</div><table.*?>(.*?)</table>''',html,re.S))
    
#    print(主要研究者信息,各参加机构信息,伦理委员会信息)


    item['试验状态']=geshihua(re.findall(r'''<div.*?>.*?试验状态</div>(.*?)<div ''',html,re.S))
    item['试验人数']=geshihua(re.findall(r'''<div.*?>.*?试验人数</div><table.*?>(.*?)</table>''',html,re.S))
    item['受试者招募及试验完成日期']=geshihua(re.findall(r'''<div.*?>.*?受试者招募及试验完成日期</div><table.*?>(.*?)</table>''',html,re.S))   
    item['临床试验结果摘要']=geshihua(re.findall(r'''<div.*?>.*?临床试验结果摘要</div>(.*?)<div ''',html,re.S))

    
#    print(试验状态,试验人数,受试者招募及试验完成日期,临床试验结果摘要)
    
    print(item)

    my_csv_tools.write_csv(item,file_path='./result.csv',column_names=csv_header)

    logger.write(item['登记号'],re.findall('currentpage=(.*?)&sort',url))





    
for i in range(n,20000):

    counter=createCounter()
    
    url='http://www.chinadrugtrials.org.cn/clinicaltrials.searchlistdetail.dhtml?currentpage={}&sort=desc&sort2=desc&rule=CTR'.format(i)

    get_content(driver=driver,url=url,logger=logger,counter=createCounter())

    random_wait(min_s,max_s)


