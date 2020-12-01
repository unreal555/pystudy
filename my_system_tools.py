# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/9/11 0011 上午 11:58
# Tool ：PyCharm

import psutil
import time
import re
import os
import sys
import shutil
import pickle


def check_process(processname):
    result=[]
    try:
        pids= psutil.pids()
        for pid in pids:
            if str.lower(processname) in str.lower(psutil.Process(pid).name()) :
                result.append((pid,psutil.Process(pid).name()))
    except Exception as e:
        print(e)
    return result



def get_random_str(lenth=8):
    n=''.join(random.sample(string.ascii_letters + string.digits, lenth))
    print('获得的随机字符串为{}'.format(n))
    return n

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

def get_time(type='n'):
    if type=='s':
        return  time.strftime('%Y-%m-%d %H-%M-%S')
    if type=='n':
        return time.strftime('%Y%m%d%H%M%S')
    if type=='date':
        return time.strftime('%Y-%m-%d')
    if type=='time':
        return time.strftime('%H:%M:%S')

    return time.strftime('%Y-%m-%d %H-%M-%S')

def ques_and_answer(q=''):
    answer=input(q)
    while re.sub('[\r\n]]','',answer)=='':
        print('不能为空,请重新输入')
        answer = input(q)
    return answer

def destroy_exe(allow_times=0):
    if 'exe' not in sys.argv[0]:
        print('只处理exe')
        exit(0)

    temp_dir = os.getenv('temp')
    exec_file = os.sys.argv[0]
    exec_file_path, exec_file_name = os.path.split(exec_file)
    target_file = os.path.join(temp_dir, exec_file_name)
    config_file=os.path.join(temp_dir,os.path.splitext(exec_file_name)[0]+'.ini')

    print(exec_file)
    print(target_file)
    print(config_file)

    count=allow_times

    if allow_times!=0:
        if os.path.exists(config_file):
            with open(config_file, 'rb') as f:
                count=pickle.load(f)
            count-=1
            with open(config_file,'wb') as f:
                pickle.dump(count,f)
        else:
            count-=1
            with open(config_file,'wb') as f:
                pickle.dump(count,f)


    if count<=0:
        try:
            if os.path.exists(target_file) and os.path.isfile(target_file):
                os.remove(target_file)
            shutil.move(exec_file,target_file)
        except Exception as e:
            print(e)





if __name__ == '__main__':
    destroy_exe(10000000)
