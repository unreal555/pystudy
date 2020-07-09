# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/8 0008 下午 5:11
# Tool ：PyCharm

import random

n=random.randint(1000,10000)

count=1

s=-1

while s!=n:
    s = input('猜\r\n')
    try:
        s=int(s)
    except :
        s = input('猜\r\n')
    if s>n:
        print('太大了')
    if s<n:
        print('太小了')

    count=count+1

print('恭喜,猜对了,共用了{}次'.format(count))



                  
              
