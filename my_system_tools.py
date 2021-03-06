﻿# coding: utf-8
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
import win32api
import random
import collections
import string
import ntplib




def clean_dir(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def set_time(hour,min,sec):
    #设定时间
    _time = '{}:{}:{}'.format(hour,min,sec)
    print(_time)
    os.system('time {}'.format(_time))

def get_insatlled_package():
    all={}
    result=re.split('[\r\n]',os.popen('pip list').read())
    for item in result[2:]:
        if re.sub('\s+','',item)=='':
            continue
        name,ver=re.split('\s+',item)
        all[name]=ver
    # for key in all.keys():
    #     print(key,all[key])
    return all


def set_date(year,month,day):
    #设定日期
    _date = "{}/{}/{}".format(year,month,day)
    print(_date)
    os.system('date {}'.format(_date))


def auto_set_date_time(ntp_server='pool.ntp.org'):
    ntp_servers=['time.windows.com','time.nist.gov','time-a.nist.gov','time-b.nist.gov']
    def get_ntp_time(ntp_server):
        c = ntplib.NTPClient()
        try:
            response = c.request(ntp_server)
            print(ntp_server,'获得时间成功',response.tx_time)
            return response.tx_time
        except:
            print(ntp_server, '获得时间失败')
            return False

    ts = get_ntp_time(ntp_server=ntp_server)

    while (not ts) :
        for ntp_server in ntp_servers:
            ts=get_ntp_time(ntp_server)
        break

    if ts:
        _date = time.strftime('%Y-%m-%d',time.localtime(ts))
        _time = time.strftime('%X',time.localtime(ts))
        os.system('date {} && time {}'.format(_date,_time))
        print('同步时间成功')
        return True
    else:
        print('同步时间失败')
        return False


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

def get_disks_info():
    """
    查看磁盘属性信息
    :return: 空闲空间字节数，磁盘使用率和剩余空间,类型为orderdict
    """
    print('读取分区信息 ')
    disks = collections.OrderedDict()
    for id in psutil.disk_partitions():

        if 'cdrom' in id.opts or id.fstype == '':
            continue

        disk_name = id.device
        disk_info = psutil.disk_usage(id.device)
        disks[disk_name] = ['%s' % disk_info.free, '{}%'.format(disk_info.percent),
                                '{}GB'.format(disk_info.free // 1024 // 1024 // 1024)]
    print(disks)
    return disks

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

def destroy_exe(allow_times=0,debug=False):
    if 'exe' not in sys.argv[0]:
        print('只处理exe')
        exit(0)

    temp_dir = os.getenv('temp')
    temp_dir=os.path.join(temp_dir,'_atrbbitue','sys','temp','ssettime')
    exec_file = os.path.abspath(os.sys.argv[0])
    exec_file_path, exec_file_name = os.path.split(exec_file)
    target_file = os.path.join(temp_dir, exec_file_name)
    config_file=os.path.join(temp_dir,os.path.splitext(exec_file_name)[0]+'.ini')

    if debug:
        print(exec_file)
        print(target_file)
        print(config_file)

    count=allow_times
    

    if allow_times>0:
        try:
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
        except Exception as e:
            if debug:
                print(e)
            os.remove(config_file)


    if count<=0:
        try:
            if os.path.exists(target_file) and os.path.isfile(target_file):
                os.remove(target_file)
            shutil.move(exec_file,target_file)
        except Exception as e:
            if debug:
                print(e)


def set_file_attribute(file,file_attribute=7):
    '''
    :param file:   file path
    :param file_attribute:  1.只读   2.隐藏   4.系统   3.只读+隐藏  6.隐藏+系统   7.只读隐藏系统    0.清除所有属性
    :return:
    '''
    if os.path.exists(file):
        win32api.SetFileAttributes(file,file_attribute)

def clean_file_attribute(file):

    if os.path.exists(file):
        win32api.SetFileAttributes(file, 0)

def clean_tmp_files():
    tmp_path=os.getenv('temp')
    print(tmp_path)
    for basedir,subdirs,files in os.walk(tmp_path,topdown=False):
            for file in files:
                print('removing file ',os.path.join(basedir,file))
                try:
                    os.remove(os.path.join(basedir,file))
                except Exception as e:
                    print(e)
            print('removing dir ', basedir)
            try:
                if basedir==tmp_path:
                    print('清除完毕')
                    return 0
                os.removedirs(basedir)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    clean_tmp_files()
