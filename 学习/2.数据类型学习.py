#!/bin/py
#   -*-coding:utf-8-*-
import sys
#list是一种有序的集合，可以随时添加和删除其中的元素。用下标索引访问,从零开始编号,-1代表倒数第一,-2代表倒数第二
student=["张三","李四","王五"]
print(student[0],student[1],student[2])
print(student[-1],student[-2],student[-3])
#append方法往队列末尾添加元素
student.append("赵六")
print(student[-1])
#insert方法往指定的下标插入元素,pop()删除队列末尾元素,pop(i)删除第i个元素,直接对student[i]赋值替换该元素
#可以创建二维队列[[1,2,3],[4,5,6],[7,8,9]]
a=[[1,2,3],[4,5,6],[7,8,9]]
print(a)
print(a[1])
print(a[1][1])


#tuple和list非常类似，但是tuple一旦初始化就不能修改,没有append,insert,pop方法
classmate=("张三","李四","王五")
#创建空tulpe
classmate=()
#创建只有一个元素的tuple必须加个逗号,以免和赋值语句混了
classmate=(1,)
#tuple可以直接写成X=1,2,3,4,5这种不带空格的形式,但为了不产生歧义一般都带
#提供两种方法,index和count,分别返回指定元素在tuple中的便宜位置和统计出现的次数
x=1,2,3,3,3,3,4,2,1
print("count",x.count(3))         #统计3出现的次数
print("list",x.index(3))     #返回3出现的位置
#dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
#dict的key是不可变的对象,value是可变的
#dict内部存放的顺序和key放入的顺序是没有关系的。
score={'张三':85,'李四':98,'王五':62}
print(score)
#新增元素*************************
score['赵六']=90
print(score)
#访问方式,张三是key,85是值,如果张三不存在将报错
print(score['张三'])
score['张三']=74
print(score['张三'])
#测试是否存在张三这个key ,'XX' in dict ,返回布尔值真假
print('张三' in score)
#删除元素
score.pop("张三")
print(score)
#返回所有的key名list
print(score.keys())
#返回所有的value值list
print(score.values())
#访问或调用不存在的键值会返回错误，为避免这种情况先测试再试用如
if "张三" in score:
    print(score["张三"])
else:
    print("张三不存在")

#或者
print(score.get("张三","null"))
#或者
print(score["张三"] if "张三" in score else "null")

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。看作一个无序和无重复的集合
#要创建一个set，需要提供一个list作为输入集合
#集合也可以用花括号创建,如下
s={1,2,3,4,5}
print(s)
s=set([1,2,3,3,4,4,5])
#虽然传入了7个元素,但最终s只包含五个,重复的被删除,而且储存的顺序不是字面上看的顺序,是计算的hash值进行排序储存
print(len(s))
#add方法增加元素,每次只能增加一个,可以增加s中已有的元素但不会有效果,因为set中不会重复
s.add(5)
s.add(6)
print(s)
#remove方法删除元素,每次一个
s.remove(5)
print(s)

#set集合可以做交,并操作 & |
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
print(s1&s2)
print(s1|s2)

##注意,只有不变元素如数字,字符串可以放入集合set,可变元素一般是不行的,如list dict,tuple是可以的
ss=set([])
#ss.add([1,2,3])   #不行
#ss.add({'s':'3'})   #不行
ss.add(("1","2"))    #可以,因为tuple是不变的,可以计算hash
print(ss)
#讨论str字符串和list队列元素的可变和不可变
#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的,如a=[b,c,a],sort后变成[a,b,c]
#不可变对象如a='bca',方法a.replace('a','A'),replace方法是产生一个新的字符串对象返回.原来的a并不发生变化


#判断数据类型的三种方法
l=[1,2,3]
if type(l)==type([]):
    print("1是list")

if type(l)==list:
    print("2是list")

if isinstance(l,list):
    print("3是list")

####==是比较两个对象是否有相同的值,is是比较两个变量是指向同一内存对象,如下
L=[1,2]
M=L
print (M is L)   #真,指向同一list对象
L=[1,2]
print(M is L)    #假,L指向了另外一list对象
print(M==L)      #真,虽然内存单元不同,但其中的值相同

#在python中,常用的字符和小的整数被放在内存中等待被引用,以提高效率.如下,xy虽然是分别定义的,但is比较他们还是相同的存储单元
x=42
y=42
print(x==y)
print(x is y)

print(sys.getrefcount("i"))  #可以查存一个对象被引用了多少次


print("-"*80)

