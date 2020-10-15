# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/10/15 0015 下午 1:36
# Tool ：PyCharm

import time
import random

def get_str_time():
    return time.strftime('%Y-%m-%d %H:%M:%S')

def random_wait(n=1,m=3,show=True,*args):
    t = get_random_num(n,m)
    print("wait {} second".format(t))

    if show == True:
        while t>1:
            print('\r','%-20s'%'counting down.',t,end='',flush=True)
            time.sleep(0.3)
            print('\r', '%-20s'%'counting down..', t, end='', flush=True)
            time.sleep(0.4)
            print('\r', '%-20s'%'counting down...', t, end='', flush=True)
            time.sleep(0.3)
            t=t-1
        time.sleep(t)
        print('\r','wait end,continue work',flush=True)
    else:
        time.sleep(t)
    return True

def get_random_num(n=1,m=3,*args):
    if not (isinstance(n, (int, float)) and isinstance(m, (int, float))):
        print('参数输入错误，不是整数或小数，采用默认值1，3')
        n=1
        m=3

    if n>m:
        print('m,n不是小-大顺序,自动调换mn数值')
        n,m=m,n
    num=random.uniform(n, m)
    #print('获得的随机数为{}'.format(num))
    return num

if __name__ == '__main__':
    print(get_str_time())
    random_wait(1,3)