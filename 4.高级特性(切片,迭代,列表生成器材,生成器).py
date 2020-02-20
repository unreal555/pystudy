#!/bin/py
#   -*-coding:utf-8-*-
from collections import Iterable

###切片###
#切片用于提取list,tuple的一部分,python对list,tuple的规则是取头不取尾巴
list1 = ['Michael', 'Sarah', 'Tracy', 'Bob']
#切片,规则是取头,不取尾巴,1是sarah,3是bob,但是切片后值取1-2两个元素,输出'Sarah', 'Tracy'
print(list1[1:3])
#输出'Michael', 'Sarah', 'Tracy'
print(list1[:3])
#输出'Bob'
print(list1[3:])
L=[range(0,100)]
#L[:]代表这个队列本身
l=L[:]
#前三十个数,每隔3个输出一个
print(L[:30:3])
print(l)
#字符串也可以切片
str='今天天气真好'
print(str[0:2])

#去除一个字符串头尾空格的函数
def trim(s):
    while s[:1]==' ':
        s=s[1:]
    while s[-1:]==' ':
        s=s[:-1]
    return s

print(trim("  sssd  "))


##迭代,简单来说就是用for...in遍历可迭代的对象
for i in [1,2,3]:
    print(i)

#迭代dict对象是,模式迭代的是key,下面例子输出的是a b c,注意迭代时的顺序不是看到的排列顺序
dict1={'a':1,'b':2,"c":3}
for i in dict1:
    print(i)
#要迭代value值,输出1,2,3
for i in dict1.values():
    print(i)
#迭代key和value,此时i类型是tuple
for i in dict1.items():
    print(type(i),i)

#使用下标循环的方式迭代一个list
for i, value in enumerate(['A', 'B', 'C']):
   print(i, value)
#输出
#0 A
#1 B
#2 c

###列表生成器
##range不是切片,用","分隔
print(list(range(1,100,3)))
a=[]
##这种[1*1,2*2,...]
for i in range(1,11):
    a.append("{} * {}".format(i,i))
print(a)
a=[]
##这种直接[1,4,9....]
for i in range(1,11):
    a.append(i*i)
print(a)

###以上方式可以换个写法

a=[i*i for i in range(1,11)]
print(a)

a=["{}*{}".format(i,i) for i in range(1,10)]
print(a)

a=[{"{}*{}".format(i,j):i*j} for i in range(1,10) for j in range(1,10)]
print(a)

#加判断生成1-10之间偶数平方的队列
a=[x * x for x in range(1, 11) if x%2==0]
print(a)

##生成两个字符串的全排列,输出如['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
print([m + n for m in 'ABC' for n in 'XYZ'])

a={'a':2,"b":3,"c":4}
for x,y in a.items():
    print("{}={}".format(x,y))


#generator.表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面
# 几个元素，那后面绝大多数元素占用的空间都白白浪费了。
#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续
# 的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边
# 计算的机制，称为生成器：generator。
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就
#创建了一个generato
g = (x * x for x in range(11))
#直接打印g是打印不出来的,报<generator object <genexpr> at 0x00BBA170>
#访问使用next(g)
#迭代生成器可以直接调用next方法,不需要每次在next了
for i in  g:
    print(i)

#函数的return 换成yield,该函数就变成一个generator
#这个需要理解

#迭代器
#可以被for迭代的对象,包括list,tuple,set,generator,dict,str,这些类型的对象通称为
#Iterable,可迭代对象.可以用函数isinstance()判断一个对象是不是可迭代的.
#isinstance(xxx,Iterable),先导入Iterable包,from collections import Iterable
a=[1,2,3]
b=12
print(isinstance(a,Iterable))
print(isinstance(b,Iterable))
#from collections import Iterable

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的
# 为什么list、dict、str等数据类型不是Iterator？
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。