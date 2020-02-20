#!/bin/py
#   -*-coding:utf-8-*-
'       说明               '
_author_ = 'zl'
import os
import pickle

l={}
for x in 'abcdefghijklmnopqrstuvwxyz':
    l[x]=x.upper()

with open(r'a.dat','wb') as f:
    pickle.dump(l,f)



with open(r'a.dat','rb') as f:
    print(pickle.load(f))



