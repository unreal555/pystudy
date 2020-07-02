# coding=gbk

import time
import re
import datetime
import os
import my_html_tools
'''
��õ�ǰʱ�䣬��������Ϊdatetime
'''



def get_now_time():
    temp=time.ctime()
    h,m,s=re.findall(" (\d+:\d+:\d+) ",temp)[0].split(':')
    now=datetime.datetime(1970,1,1,int(h),int(m),int(s))
    return now



def get_shutdown_time():
    while 1:
        temp=input('���뼸��ػ���HH:MM,ȡ���趨��ʱ���밴c:   ')
        temp=my_html_tools.qu_kong_ge(temp)
        temp=temp.replace('��',':')
        print(temp)

        if temp=='c' or temp=='C':
            print('1')
            return temp


        result=re.findall('(\d+:\d+)',temp)
        if result=='[]':
            print('2')
            continue
        else:
            setH, setM = result[0].split(':')
            setH, setM = int(setH), int(setM)
            if setH < 0 or setH > 23 or setM < 0 or setM > 59:
                print('����ʱ�����')
                continue
            return datetime.datetime(1970,1,1,setH,setM,0)


def check():
    flag=os.system('oa')


now=get_now_time()
shutdown_time=get_shutdown_time()


if shutdown_time=='c' or shutdown_time=='C':
    os.system('shutdown -a')
    exit(0)

if shutdown_time>now:
    count=(shutdown_time-now).seconds
    print(count)
    os.system('shutdown -t %s -s ' %count)
else:
    print('ֻ�����ý���������ʱ��')
    exit(0)









