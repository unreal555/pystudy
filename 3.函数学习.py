#!/bin/py
#   -*-coding:utf-8-*-

#可以将一个函数名赋给变量,相当于给函数起了个别名,直接用变量名调用函数
test=abs
print('测试函数别名:',test(-234))
#如果想定义一个什么事也不做的空函数，可以用pass语句.pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
# 比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nodo():
    pass

#pass还可以用在其他语句里，比如：缺少了pass，代码运行就会有语法错误。
age=8
if age >= 18:
    pass
print('age=',age)

#函数的参数检查,检查传入的x是否为整型浮点型,不是将抛出错误
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。

#函数位置参数,定义函数X计算n的2.3.4或者n次方的函数,如果定义成X(n,m),则必须使用X加两个参数调用,X(n),将报缺少参数的错误
#可以定义成X(n,m=2),默认将第二个参数设置为2,这样可以实现X(n)直接计算平方,X(n,m)计算n的m次方
def X(m, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = m * s
    return s
print('测试函数位置参数',X(4))
print(X(4,8))
# 默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。




def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。见上例,多数人的城市和年龄都一样,这样函数只提供name和gender就好了
# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender
# 这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
#
# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，
# 意思是，city参数用传进去的值，其他默认参数继续使用默认值。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！



#可变参数,利用list或者tuple实现,def 函数名(*变量),允许传入任意个参数,包括0个
def calu(*num):
    sum=0
    for i in num:
        sum=sum+i
    print(sum)

list=[1,2,3,4]
#calu(list),这样是不行的
calu(*list)
calu(1,2,3,4,5,6)
calu()

#关键字参数,关键字参数,允许接受零到任意多个参数,在函数内部组成一个dict
def person(name,age,**info):
    print("姓名:",name,"年龄:",age,"其他信息:",info)
#注意必须是XX=XXX形式,单纯的河南,已婚是不行的
person('张三',18,籍贯='河南',婚姻='已婚')


#命名关键字参数,必须接收指定名称的参数,和关键字参数不同,调用必须给出值
def person(name,age,*,city,job):
    pass
#person("张三",18,"济南","工程师")这个调用是错误的
#person("张三",18)这个也是错误的,必须给出city和age
person("张三",18,city="济南",job="工程师")


#可变参数和命名关键字参数混合,后面的命名关键字参数可以不加"*,"
def person(name,age,*args,city,job):
    print("姓名:", name, "年龄:", age, "其他信息:",args,city,job)
person("张三",18,"ssadf","dadd",job="工程师",city="济南")

#总结 *变量名对应可变参数,类型是list或者tuple,**变量名对应可变参数,类型是dict

#递归函数,自己调用自己,必须有退出条件,否则死循环
def jiecheng(n=1):
    if n==1:
        return 1
    return n*jiecheng(n-1)

print('测试递归函数,阶乘',jiecheng(8))


# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(9, 'A', 'B', 'C')