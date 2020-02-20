#!/bin/py
#   -*-coding:utf-8-*-
'       说明               '
_author_ = 'zl'
# Python中怎么创建闭包
# 在Python中创建一个闭包可以归结为以下三点：
# 闭包函数必须有内嵌函数
# 内嵌函数需要引用该嵌套函数上一级namespace中的变量
# 闭包函数必须返回内嵌函数
# 通过这三点，就可以创建一个闭包，是不是想到了上一篇中介绍的Python装饰器。没错，Python装饰器就是使用了闭包。
# 闭包使flag的状态保存在返回的函数中,使其生命周期得到延长

##nonlocal声明,使每一个闭包中的flag的状态得以保留,使用globle声明会覆盖其他闭包中的flag状态
def func(args):
    flag=args
    def test(label):
        nonlocal flag
        print(label,flag)
        flag+=1
    return test
a=func(0)
b=func(100)
print(a)
a("a")
a("b")
a("c")
b("a")
b("b")
b("c")
a("d")

def greeting(word):
    string=word
    def hello(name):
        print(word,name)
    return hello

a=greeting("nice to meet you,")
b=greeting("you come again ,my firend")
a("张三")
a("李四")
b("张三")
b("李四")
