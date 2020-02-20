#!/bin/py
#   -*-coding:utf-8-*-

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


#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。看作一个无序和无重复的集合
#要创建一个set，需要提供一个list作为输入集合
s=set([1,2,3,3,4,4,5])
#虽然传入了7个元素,但最终s只包含五个,重复的被删除,而且储存的顺序不是字面上看的顺序,是计算的hash值进行排序储存
print(s)
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

#讨论str字符串和list队列元素的可变和不可变
#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的,如a=[b,c,a],sort后变成[a,b,c]
#不可变对象如a='bca',方法a.replace('a','A'),replace方法是产生一个新的字符串对象返回.原来的a并不发生变化

