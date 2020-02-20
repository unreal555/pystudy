#!/bin/py
#   -*-coding:utf-8-*-

#自定义模块,模块名不能是纯数字
from  ListSort import ListSort
import random

# x=[]
# for i in range(1,10000):
#     x.append(random.randint(1,100000))
# a=ListSort(x)
# a.setDebug(i=1)
# a.maopaoSort()

def sumTree(i):
    tot=0
    for x in i:
        if not isinstance(x,list):
            tot+=x
        else:
            tot+=sumTree(x)
    return tot

result=[]
def checkTree(i):

    for x in i:
        if not isinstance(x,list):
            # print('add',x)
            result.append(x)
        else:
            checkTree(x)
    return result
test=[1,[22,[222,3],[23,[33,[3],3]]]]

print(sumTree(test))

print(checkTree(test))