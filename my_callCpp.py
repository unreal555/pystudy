# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/10/12 0012 下午 4:27
# Tool ：PyCharm

import logging

# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/10/12 0012 下午 4:09
# Tool ：PyCharm


import os
import ctypes

class My_Dlls():

    dlls=[]

    def __init__(self,lib_path='./dll'):
        for root, dirs, files in os.walk(lib_path):
            for file in files:
                if '.dll'  in str.lower(file):
                    self.dlls.append(os.path.join(root,file))

    def callCpp(self,func_name,*args):

        for dll in self.dlls:
            try:
                lib = ctypes.cdll.LoadLibrary(dll)
                try:
                    value = eval("lib.%s"%func_name)(*args)
                    print('命令为:', func_name, "    参数为:", str(args), " 调用的dll为:" ,dll, '  调用的返回值为:', value)
                    return value
                except Exception as e:
                    print(e)
                    print('库:%s中无函数:%s,尝试更换dll'%(dll,func_name))
                    continue
            except:
                print("库文件载入失败：",dll)
                continue
        print("没有找到函数入口！")
        return False

if __name__ == '__main__':

    a=My_Dlls('''./job/海康播放器/dll''')
    print(a.callCpp("NET_DVR_GetLastError"))