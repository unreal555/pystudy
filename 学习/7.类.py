#!/bin/py
#   -*-coding:utf-8-*-
'       说明               '
__author__ = 'zl'

import 学习requests

#类都可以继承object对象,类一般以大写字符开头
class Person(object):
#__slots__中不包含的属性,不能绑定给实例
    __slots__ = ("name","__age","age","__sex","address","grade")
#__init__方法就是构造函数,有了构造函数,在创建实例是就必须传入参数了.
#变量名前加__,说明这个变量是私有变量,不能直接用调用.
#以__开头__结尾的是特殊变量,不是私有变量,可以直接访问
#以_开头的变量不是私有变量,但是一般不直接引用,一般为将其视为私有变量,不能随意访问
    def __init__(self,name,age,sex):
        self.name=name
        self.__age=age
        self.__sex=sex

    def getAge(self):
        return self.__age

#调用构造函数
zhangsan=Person("张三","38","男")
print(zhangsan.name)    #可以,
#print(zhangsan.__age)     不行,私有变量
print(zhangsan._Person__age)   #私有变量__age在解释器被解释成_Person__age,想调用也是可以的.但是不建议这样使用.
print(zhangsan.getAge())     #可以,用方法返回年龄

#除了类中定义的属性,还可以给类的实例随意绑定其他属性,但只针对这一个实例有效
zhangsan.address="济南市"
print(zhangsan.address)
#类中定义的私有属性名可以和给实例绑定的属性名相同,但不是同一个属性
zhangsan.age="23"
print(zhangsan.getAge())     #返回38
print(zhangsan.age)          #返回23


#继承,多态,判断是否是实例,类一般以大写字母开头
#普通类都可以继承object,所有的类都是object的子类
#定义类animal,和move方法
class Animal(object):
    def __move__(self):
        print("anmial is moving")
#定义子类Bird,复写父类的move方法
class Bird(Animal):
    def __move__(self):
        print("bird is flying")

class Sheep(Animal):
    pass

#子类覆写了父类的方法,那么子类在调用该方法是都是使用子类覆写的方法
#子类直接继承父类的方法,那么子类就有了父类的方法
maque=Bird()
yang=Sheep()

#注意多态,根据传进来的对象不同,自动调用不同对象的move方法
def move(x):
    x.__move__()

move(maque)
move(yang)

#用isinstance判断一个对象是不是某个类的实例
#某个子类的实例一定是其本身和父类的实例
#但是父类的实例不能也看作子类的实例
print(isinstance(yang,Animal))
print(isinstance(maque,Animal))


#获取一个实例的类型用type,返回该实例所属的类
print(type([1,2,3]))
print(type(yang))

#dir可以返回一个实例所有的属性和方法
print(dir(yang))

##__xxx__这样的属性和方法都是有特殊用途的,除此之外的都是普通属性和方法
#类中使用__XXX__定义的方法,可以直接用如下方式调用,不用yang.__move__这样,__move__(yang)也是不对的
move(yang)
move(maque)


class Test(object):
    def __init__(self):
        self.x=9

    def power(self):
        return self.x*self.x

obj=Test()
#测试Test的实例obj是不是具有属性x
print(hasattr(obj,'x'))
#测试是否是属性y
print(hasattr(obj,'y'))
#obj增加y属性,值为19
setattr(obj,'y',19)
print(hasattr(obj,'y'))
#获取obj的power方法
fn=getattr(obj,"power")
print(fn)
print(fn())
#以上和obj.power()效果一致
print(obj.power())

#实例属性和类属性,由于可以直接给实例绑定属性,所有某个实例的属性包含类中的原始定义和运行中给他绑定的属性.
#如果使用相同的实例属性和类属性名,那么实例属性将屏蔽调类属性值,