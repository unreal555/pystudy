#!/bin/py
#   -*-coding:utf-8-*-
from functools import reduce
from datetime import datetime

##函数名可以作为变量赋值给其他变量,那么函数名也可以作为变量,被其他函数所调用,这种调用函数的函数,称为高阶函数.
##reduce()需要导入库from functools import reduce
# map(),接受接受两个参数,一个是函数名,一个是iterable对象,将函数名函数作用于iterable的每一个对象,返回一个iterator
##输出
def pingfang(x):
    return x * x

def cheng(x,y):
    return x*y

result = map(pingfang, [1, 2, 3, 4, 5])
print(result)  # 输出<map object at 0x00BEEAD0>
print(*result)  # 输出1 4 9 16 25

###传入多个list,每次从多个队列中中取一个参与计算
result=map(cheng,range(1,10),range(1,10))
print(*result)


##reduce()接收函数名和iterable,这个函数名函数必须接受两个参数,将iterable序列中的前两个作为函数名参数计算后结果和序列中下个数作为参数
# 继续传递给函数名函数,直到iterable序列完毕.
def s(x, y):
    return x + y


print(reduce(s, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


###合起来用,将一个字符串数字转换成int
def c(x, y):
    return 10 * x + y
def s(x):
    a = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return (a[x])


print(type(reduce(c, map(s, '12134454342322'))))


###匿名函数，lambda开头，：前是未知数，：后算式是返回值，不需要写return
#以下两种用法
print(list(filter(lambda x:x%2==1,list(range(1,100)))))

g=lambda x:x*x*x
print(g(99))



###修饰器，在不影响原函数执行的前提下实现某些附加功能，如下，调用函数时输出函数执行时间
#修饰器应定义在函数之前，否则无法调用
def exec_time(k):
    def wrapper(*args, **kw):
        start=datetime.now()
        k(*args, **kw)
        end=datetime.now()
        est=end-start
        print("程序耗时",est)
    return wrapper

@exec_time
def calc(x):
    sum=0
    for i in range(1,x):
        sum=sum+i
    print("和为",sum)

calc(10000000)

