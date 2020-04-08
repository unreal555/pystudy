#!/bin/py
#   -*-coding:utf-8-*-
'       说明               '
_author_ = 'zl'

while True:
    reply=input("输入个数字")

    try:
        num=float(reply)
    except:
        if reply == 'stop': break
        print("bad num...   "*8)
        continue
    else:
        try:
            print(num ** 10)
        except:
            print("结果太大")


print('bye')
