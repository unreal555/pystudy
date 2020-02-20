#!/bin/py
#   -*-coding:utf-8-*-
from functools import reduce
##函数名可以作为变量赋值给其他变量,那么函数名也可以作为变量,被其他函数所调用,这种调用函数的函数,称为高阶函数.
##reduce()需要导入库from functools import reduce
#map(),接受接受两个参数,一个是函数名,一个是iterable对象,将函数名函数作用于iterable的每一个对象,返回一个iterator
##输出
def cheng(x):
    return x*x
result=map(cheng,[1,2,3,4,5])
print(result) #输出<map object at 0x00BEEAD0>
print(*result) #输出1 4 9 16 25

##reduce()接收函数名和iterable,这个函数名函数必须接受两个参数,将iterable序列中的前两个作为函数名参数计算后结果和序列中下个数作为参数
#继续传递给函数名函数,直到iterable序列完毕.
def s(x,y):
    return x+y
print(reduce(s,[1,2,3,4,5,6,7,8,9]))


###合起来用,将一个字符串数字转换成int
def c(x,y):
    return 10*x+y
def s(x):
    a={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return(a[x])
print(type(reduce(c,map(s,'12134454342322'))))

