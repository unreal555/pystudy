import requests
import re
import socket
import time
import random
from concurrent.futures import ThreadPoolExecutor

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}

def get_ip(url):
    page=requests.get(url,headers=headers,)
    print(page.url)
    page_source=page.text.replace(' ','').replace('\n','').replace('\r ','')
    print(page_source)
    result=re.findall(r'<tr><.*?"IP">(\d+).(\d+).(\d+).(\d+)</td><.*?"PORT">(\d+)</td>.*?<.*?"类型">(.*?)<.*?"位置">(.*?)</td><.*?"响应速度">.*?</td>.*?"最后验证时间">.*?</td></tr>',page_source)
    print(result)
    return result

def test_proxy(i):

    print(i)
    ip1, ip2, ip3, ip4, port, des, area=i[0],i[1],i[2],i[3],i[4],i[5],i[6]
    if int(port)>65535 or int(port)<0:
        print('port wrong',('{}.{}.{}.{}'.format(ip1,ip2,ip3,ip4),port))
        return 0
    if int(ip1)>255 or int(ip1)<1 or int(ip2)>255 or int(ip2)<1 or int(ip3)>255 or int(ip3)<1or  int(ip4)>255 or int(ip4)<1:
        print('port wrong', ('{}.{}.{}.{}'.format(ip1, ip2, ip3, ip4), port))
        return 0


    ip='{}.{}.{}.{}'.format(ip1,ip2,ip3,ip4)
    print(ip,des)

    url='icanhazip.com'
    if des=='HTTP':
        proxies={'http':'http://'+ip+':'+str(port)}
        # proxies={'http': 'http://test2:594188@58.59.25.122:1234'}
        try:
            s=requests.get('http://'+url,proxies=proxies,headers=headers)

            print('s.test',s.text)
            print('proxy',ip)
            print('http比较',ip in s.text)
            if ip in s.text:
                return(ip,port,area,des)
        except Exception as E:
            print(E)
            print('wrong',ip,port)
            return 0

    if des=='HTTPS':
        proxies={'https':'https://'+ip+':'+str(port)}
        # proxies={'https': 'https://test:594188@58.59.25.122:1234'}
        try:
            s=requests.get('https://'+url,proxies=proxies,headers=headers)
            print('s.test',s.text)
            print('proxy',ip)
            print('https比较',ip in s.text)
            if ip in s.test:
                return(ip,port,area,des)
            else:
                return 0
        except Exception as E:
            # print(E)
            # print('wrong',ip,port)
            return 0


def save(obj):
    print(obj)
    proxy=obj.result()
    print(proxy)
    if proxy==0 or proxy==None:
        pass
    else:
        print('write',proxy)
        with open('./proxy.txt','a',encoding='utf-8') as f:
            f.write('{}{}'.format(str(proxy),'\r\n'))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(10)
    for i in range(1,1000):

        for j in get_ip('https://www.kuaidaili.com/free/inha/{}/'.format(i)):
            # a=['58','59','25','122','1234','yt','er']
            pool.submit(test_proxy, j).add_done_callback(save)

        time.sleep(random.choice(range(15, 25)))
