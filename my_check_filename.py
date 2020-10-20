# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/10/20 0020 上午 9:42
# Tool ：PyCharm
import os
import re
import time
import random
import string

def get_str_time():
    return time.strftime('%Y-%m-%d %H:%M:%S')

def get_random_str(lenth=8):
    rand=''.join(random.sample(string.ascii_letters + string.digits, lenth))
    print('获得的随机字符串为{}'.format(rand))
    return rand

def check_fname(fname,mode='''t'''):
    '''
    检查fname路径的文件是否存在,若不存在,则创建文件储存的目录,返回fname值
    若文件存在,则尝试返回另外一个名字
    :param fname:
    :param mode 若重名,0 增加日期时间,1 跟随八位随机数,2 数字顺序增长
    :return:  fname
    '''
    fname=str.lower(fname)
    file_dir, file_name = os.path.split(fname)
    file_basename,file_extname=os.path.splitext(file_name)
    mode=str.lower(mode)
    if mode not in ['s','t','n']:
        print('mode 错误,必须选择 t,n,s(时间,数字,随机字符串)')
        print('设置为默认模式t,时间')
        mode='t'


    if file_dir == '':
        print('fname:{}没有路径,路径设为当前路径'.format(fname))
        file_dir = '.'

    if file_name == '':
        print('fname:{}没有文件名,程序退出'.format(fname))
        return False

    print('''输入文件,目录为:"{}",文件名为:"{}",扩展名为:"{}"'''.format(file_dir,file_basename,file_extname))

    count=1
    while os.path.exists(os.path.join(file_dir,file_basename+file_extname)) and os.path.isfile(os.path.join(file_dir,file_basename+file_extname)):
        print('{}{}文件重名,尝试更名'.format(file_basename,file_extname))

        reg = r'\(\(\d+\)\)'

        if mode=='''n''':
            if re.findall(reg,file_basename)==[]:
                file_basename=file_basename+r'(({}))'.format(count)
                count=count+1
            else:
                file_basename=re.split(reg,file_basename)[0]+r'(({}))'.format(count)
                count = count + 1

        if mode=='''s''':
            if re.findall(reg,file_basename)==[]:
                file_basename=file_basename+r'(({}))'.format(get_random_str())
                count=count+1
            else:
                file_basename=re.split(reg,file_basename)[0]+r'(({}))'.format(get_random_str())
                count = count + 1

        if mode=='''t''':

            if re.findall(reg,file_basename)==[]:
                file_basename=file_basename+r'(({}))'.format(get_str_time())
                count=count+1
            else:
                file_basename=re.split(reg,file_basename)[0]+r'(({}))'.format()
                count = count + 1


    result=os.path.join(file_dir,file_basename+file_extname)


    if not os.path.exists(file_dir):
        print('{}目录不存在,创建'.format(file_dir))
        os.makefile_dirs(file_dir)

    abspath=os.path.abspath(result)
    print('''检查完毕,返回文件全路径为{}'''.format(abspath))
    return result

if __name__ == '__main__':

    check_fname('./pic/2.jpg',mode='r')