#!/bin/py
#   -*-coding:utf-8-*-
# __auth__ = zl'

import os
import random
import psutil
import collections
import win32api
import win32con
import string

file_size = 1 * 1024 * 1024 * 1024
block_size=1*1024*1024
disk_used = collections.OrderedDict()


def get_filename():
    return ''.join(random.sample(string.ascii_letters + string.digits, 8))


def get_disk_info():
    """
    查看磁盘属性信息
    :return: 空闲空间字节数，磁盘使用率和剩余空间
    """

    for id in psutil.disk_partitions():

        if 'cdrom' in id.opts or id.fstype == '':
            continue
        disk_name = id.device.split(':')[0]
        disk_info = psutil.disk_usage(id.device)
        print(disk_info)
        disk_used[disk_name] = ['%s' % disk_info.free, '{}%'.format(disk_info.percent),
                                '{}GB'.format(disk_info.free // 1024 // 1024 // 1024)]
    return disk_used


def work(disk,free_size=1024*1024*1024*1024,path='temp'):

    work_path = os.path.join(disk, path)
    if os.path.exists(work_path):
        pass
    else:
        os.makedirs(work_path)
    win32api.SetFileAttributes(work_path, win32con.FILE_ATTRIBUTE_NORMAL)
    win32api.SetFileAttributes(work_path, win32con.FILE_ATTRIBUTE_HIDDEN)

    while free_size > 0:
        try:
            f=open(os.path.join(work_path, get_filename()), 'wb')
            for i in range(0,1024):
                f.write(b'0' * block_size)
            free_size -= file_size
        except Exception as e:
            print(e)
        finally:
            f.close()
            free_size=-1


get_disk_info()
print(disk_used)
work('d:')

'''linux版本，参考'''
'''
!/usr/bin/python3
-*- coding: utf-8 -*-
author: Yoff
last modified: Dec-19-2016

import sys
import os

def erase_empty_disk(path, num):
    print('erase ' + path + ' ' + str(num) + ' times')
    for i_num in range(num):
        try :
            f = open(path+'/temp_file.tmp', 'w')
            vfs = os.statvfs(path)
            print(vfs.f_bavail)
            print(vfs.f_bsize)
            print(vfs.f_bavail * vfs.f_bsize)
            bsize = vfs.f_bsize
            bavail = vfs.f_bavail
            while bavail > 1e6 :
                f.write('0'*bsize)
                bavail = bavail - 1
            while bavail > 1 : # also can be 0, set 1 to avoid a rarely bug
                f.write('0'*bsize)
                f.flush()
                vfs = os.statvfs(path)
                bavail = vfs.f_bavail
        except :
            print('exception')
        finally :
            f.close()
            os.remove(path+'/temp_file.tmp')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: ./earase_empyt_disk disk_root_path [num_erases]')
        sys.exit(1)
    if len(sys.argv) < 3:
        num = 1
    else :
        num = int(sys.argv[2])
    path = sys.argv[1]
    erase_empty_disk(path, num)
'''
