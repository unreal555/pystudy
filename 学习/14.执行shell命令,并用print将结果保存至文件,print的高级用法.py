#!/bin/py
#   -*-coding:utf-8-*-
'       说明               '
_author_ = 'zl'
#语法,print([object,....],[sep='任意的分割符号'][,end="\n"][,file=sys.stdout]
#sep指定打印对象的间隔,end代表默认的行尾字符,默认为换行,更改输出文件可以将打印结果输出到任意用write方法打开的文档中
import sys
import os

process=os.popen(r'dir/s')
list2=process.read()
process.close()
print(list2)

print(type(list2))

a="ssss"
b=1,2,3
c={}
print(a,b,c)
print(a,b,c,sep="----\n....",end='\nend')
with open('test.txt','w') as f:
    print(list2,file=f)


with open('test.txt','r') as f:
    for line in f:
        print(line)

# C:\Python34\python.exe D:/pycharm2017pjb/study/14.执行shell命令,并用print将结果保存至文件,print的高级用法.py
# ssss (1, 2, 3) {}
# ssss----
# ....(1, 2, 3)----
# ....{}
# end
