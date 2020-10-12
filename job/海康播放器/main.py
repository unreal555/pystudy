# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/10/12 0012 下午 4:09
# Tool ：PyCharm


import os
import ctypes

lib_path='./dll'

def file_name(lib_path):
    pathss=[]
    for root, dirs, files in os.walk(lib_path):
        for file in files:
            pathss.append(os.path.join(lib_path,file))
    return pathss

dll_list=file_name(lib_path=lib_path)

def callCpp(func_name,*args):
    for HK_dll in dll_list:
        try:
            lib = ctypes.cdll.LoadLibrary(HK_dll)
            try:
                value = eval("lib.%s"%func_name)(*args)
                print("调用的库："+HK_dll)
                print("执行成功,返回值："+str(value))
                return value
            except:
                continue
        except:
            print("库文件载入失败："+HK_dll)
            continue
    print("没有找到接口！")
    return False


print('init',callCpp("NET_DVR_Init"))# app = my_app()
print('init result',callCpp("NET_DVR_GetLastError"))

