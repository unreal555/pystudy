import requests
import re
import socket
import time
import random

header={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Host': 'www.66ip.cn',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}

def get_ip(url):
    page=requests.get(url,headers=header)
    page_source=page.content.decode('gbk')
    result=re.findall("<td>(\d+).(\d+).(\d+).(\d+)</td><td>(\d+)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)",page_source)
    return result

def test_proxy(i):
    ip1, ip2, ip3, ip4, port, area, des=i[0],i[1],i[2],i[3],i[4],i[5],i[6]
    ip='{}.{}.{}.{}'.format(ip1,ip2,ip3,ip4)
    if int(port)>65535 or int(port)<0:
        print('port wrong',ip,port)
        return 0
    if int(ip1)>255 or int(ip1)<1 or int(ip2)>255 or int(ip2)<1 or int(ip3)>255 or int(ip3)<1or  int(ip4)>255 or int(ip4)<1:
        print('ip wrong',ip, port)
        return 0
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # print(s)
        s.settimeout(5)
        # print(s)
        s.connect(('{}'.format(ip),int(port)))
        print('ok',s)
        return(ip,port,area,des)
    except Exception as E:
        print(E)
        print('wrong',ip,port)
        return 0

# except:
    #     print('socket error',ip,port)
    #     return 0
    # if linker:
    #     return (ip,port,area,des)
f=open('./proxy.txt','w',encoding='utf-8')
for i in range(1,1000):
    time.sleep(random.choice(range(3,10)))
    for j in get_ip('http://www.66ip.cn/{}.html'.format(i)):
        # a=['58','59','25','122','1234','yt','er']
        proxy=test_proxy(j)
        print(proxy)
        if proxy==0:
            continue
        else:
            print('write',proxy)
            f.write('{}{}'.format(str(proxy),'\r\n'))
            f.flush()
f.close()
