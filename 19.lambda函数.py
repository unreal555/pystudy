#!/bin/py
#   -*-coding:utf-8-*-
'       说明               '
_author_ = 'zl'
import sys
from tkinter import Button,mainloop

f=(lambda x,y:x if x<y else y)
print(f(20,3))

print((lambda x,y:x if x<y else y)(20,3))

x=5
a={
    2:lambda x:x*x,
    3:lambda x:x**3,
    4:lambda x:x**4,
    5:lambda x:x**5}[x]
print(a(9))

f=(lambda x=5,y=6,z=7:print("{}*{}*{}".format(x,y,z),x*y*z))
f()
f(1)
f(1,2)
f(1,2,3)

x=Button(
    text="Press me",
    command=(lambda :print( "sss"))
)
x.pack()
mainloop()
