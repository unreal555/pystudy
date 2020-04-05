#!/bin/py
#   -*-coding:utf-8-*-
'       说明               '
_author_ = 'zl'
##任何文档的第一行字符串都被当作模块的说明
##_author_变量引入作者

import sys       ##引入sys模块\
print(sys.argv)   ##sys模块,argv变量用list存储了脚本执行的所有参数,至少有一个参数,就是文档的路径文件名.

def test():
    print("当前文件是主文件,不是被import的")

#若一个模块是直接执行的,不是被import的,那么该模块的__name__变量被设为__mian__,通过判断该__name__的值
#可以判断文件的状态
if __name__=='__main__':
    test()

##__name__,__author__这种特殊变量一般有特殊用途,可以被引用但个人不定义这种变量
##_xx这种变量是私有变量,虽然python没有机制能限制人引用它,但一般不去引用它
##作用用于在模块,类中封装,私有函数变量不对外提供,只提供public的函数和变量,如下

def _private_1(name):
    print ('Hello, %s' % name)

def _private_2(name):
    print ('Hi, %s' % name)

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

greeting("张三三")