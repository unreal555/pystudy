#!/bin/py
#  -*-:utf-8-*-
#输出多行可以用\转义,可以用'''直接输出.
print('''aaa                    
bbb''')
print("aaa\nbbb\nccc")
# r""包裹的内容不进行转义,原样输出
print(r"aaa\naaa")
# 格式化字符串 输出,$s%d%f%x,分别代表字符串,整数,浮点数,八进制数替换
#如果字符串里的%是个正常的内容,不用作占位符,需要用'%%'转义成单一%
print('%.4f%%' % (5/3))
# {}为占位,用,分隔多个替换对象
print('{}+{}={}'.format("2","4",(2+4)))
#这种是以unicode编码存放在内存中的,若要保存到磁盘,必须转换成byte编码
a='adflasdkjf'
#b''表示以byte编码
b=b'adkjlajdlfaldj'
c='中文'

#纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编
# 码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码
# 的范围，Python会报错。
print(a.encode('ascii'))
print(c.encode('utf-8'))
#我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))
