import requests
import my_logger
import re
import time


quanben=my_logger.my_logger(name='wanben.log')

max=2817


for i in range(1405,max+1):

    url='http://www.skwen.me/shuku/0-lastupdate-2-{}.html'.format(i)
    print(url)
    html=requests.get(url).content.decode('utf-8')
    print(html)


    reg='<a class="name" href="/(\d+)/(\d+)/">(.*?)</a>'
    for x,y,z in re.findall(reg,html):
        quanben.write(x,y,z)
        
    time.sleep(1)
