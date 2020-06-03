#  -*-conding:gbk-*-

import time
import re
import datetime
import os


now=time.ctime()
h,m,s=re.findall(" (\d+:\d+:\d+) ",now)[0].split(':')
print(h,m,s)
h,m,s=int(h),int(m),int(s)

flag=input('输入几点关机，HH:MM,取消设定的时间请按c:   ')

if flag=='c':
   
    os.system('shutdown -a')
    exit(0)

result=re.findall('(\d+:\d+)',flag)

print(result==[])



if result==[]:
    print('输入错误')
    exit(0)
else:
    setH,setM=result[0].split(':')
    setH ,setM=int(setH),int(setM)
    if setH<0 or setH>24 or setM<0 or setM>60:
        print('时间不对')
        exit(0)

now=datetime.datetime(1970,1,1,h,m,s)

set_time=datetime.datetime(1970,1,1,setH,setM,0)

print((now-set_time).seconds)

count=(set_time-now).seconds

os.system('shutdown -t %s -s '%count)