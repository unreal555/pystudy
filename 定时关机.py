from subprocess import Popen

import re

reg='[0-2]{0,1}[0-9]{0,1}:[0-9]{0,1}[0-9]{1,1}'

t=input('请输入重新启动的时间,格式为XX:XX  ')

while re.match(reg,t)==None:
    
    t=input('输入错误,请输入重新启动的时间,格式为XX:XX  ')

if t=='00:00':
    Popen("shutdown -a") 
    
else:    
    Popen("at {} shutdown -t 60 -r".format(t)) 
    
    
    






