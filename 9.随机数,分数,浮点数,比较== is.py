#!/bin/py
#   -*-coding:utf-8-*-
import random
from decimal import *
from fractions import Fraction

a=0b1110101
b=0b1001011
print(a,a>>2,bin(a>>2))
print(a,a<<3,bin(a<<3))
print(bin(a&b))
#random方法随机选0-1之间的浮点数
print(random.random())
#下面俩类似,只是range方法可以设步长
print(random.randint(1,100))
print(random.randrange(1,100,2))
#随机在队列中选取一个元素
print(random.choice(["1","2","3"]))

#记住浮点数是不精确的,如下应该打印零,但实际是5.551115123125783e-17,最好不要用==比较浮点数作判断条件,用<and>比较好
print(0.1+0.1+0.1-0.3)
#精确的应该试用decimal,integer,这样为零
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))

#查看目前的demical设置进度等信息
print(getcontext())
#设置精度为2位小数
getcontext().prec=2

print(Decimal('2')/Decimal('3'))

#使用分数
x=Fraction(1,3)
y=Fraction(1,3)
print((x+y),x*y,x/y,x-y)
#浮点数可以创建分数
print(Fraction(1.75))          #7/4
#但浮点数是不精确的,创建的分数也不会精确
print(Fraction(0.45))    #8106479329266893/18014398509481984,应该是9/20
