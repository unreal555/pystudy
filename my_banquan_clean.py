# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/1 0001 下午 2:32
# Tool ：PyCharm
import sys
import os
import win32api
import win32con


def get_path():

    paths = []
    for path in sys.path:
        if os.path.isdir(path):
            try:
                win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_HIDDEN)
                win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_READONLY)
                paths.append(os.path.join(path, 'info'))
            except Exception as e:
                print(e)
    print(paths)
    return paths


def clean(paths):
    for path in paths:
        print('REMOVE',path)
        if os.path.isfile(path):
            try:

                win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_NORMAL)
                os.remove(path)
                print('REMOVE',path)
            except:
                pass

def do():
    paths=get_path()
    clean(paths)


if __name__=='__main__':

    do()