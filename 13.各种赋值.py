#!/bin/py
#   -*-coding:utf-8-*-
'       说明               '
_author_ = 'zl'
#基本
a='aaaaa'
print(a)

#元组赋值语句(位置性),下面例子中,a,b代表了一个元组,多目标赋值
h=a,b='sss','dddd'
print('元组赋值',h,a,b)
#输出为元组赋值 ('sss', 'dddd') sss dddd

#序列赋值运算,通用性(变量和参数个数应该相等,否则用下面的扩展序列解包赋值
a,b,c,d,e,f='adaklj'
print(a,b,c,d,e,f)
#输出a d a k l j
a,b,c,d,e,f=[1,2,3,4,5,6]
print(a,b,c,d,e,f)
#输出1 2 3 4 5 6

#扩展序列解包,前面的变量名和参数一一对应,后面多于的参数扩展为list赋值给最后一个*c
a,b,*c="saaffsadfa"
print(a,b,c)
#输出s a ['a', 'f', 'f', 's', 'a', 'd', 'f', 'a']
a,b,*c="saaffsadfa"
print(a,b,c)

#多目标赋值
a=b=c="sda"
print(a,b,c)
print(a is b)
print(a is c)
#输出 sda sda sda
# True
# True

red,green,blue=range(3)
print(red,green,blue)
#0 1 2

#+= -=,增强的赋值语句
#增强的赋值语句包含运算,对于可变对象来说是直接修改对象本身,而a=a+1,是先计算左边产生一个新的对象,再赋值给a,计算较慢
#对于不变的对象如字符串等影响不大,但对可变对象一定区分两者的区别
a=[1,2,3]
b=a
b=b+[4,5]
print(a,b)
#[1, 2, 3] [1, 2, 3, 4, 5]

#extend也是直接修改可变对象本身
a=[1,2,3]
b=a
b.extend([3,4])
print(a,b)
#[1, 2, 3, 3, 4] [1, 2, 3, 3, 4]
#+=直接修改对象本身,不产生新的对象
a=[1,2,3]
b=a
b+=[4,5]
print(a,b)
#[1, 2, 3, 3, 4] [1, 2, 3, 3, 4]