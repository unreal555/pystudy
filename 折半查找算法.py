#!/bin/py
#   -*-coding:utf-8-*-

class halfquery():
    L = []
    x = 0
    low = 0
    high = len(L)
    def __init__(self,L=[],x=0):
        self.L=L
        self.x=x
        self.high=len(L)

    def seek(self):
        while self.low<self.high:
            middle = (self.low + self.high) // 2
            print(self.low, self.high, middle)
            if self.L[middle]==self.x:
                print("查找结束，第{}个".format(middle+1))
                break
            if self.L[middle]>self.x:
                self.high=middle
                continue
            elif self.L[middle]<self.x:
                self.low=middle+1
                continue
        else:
            print("查找不倒")


a=halfquery([1,2,3,4,5,6,7,87,100],1)

a.seek()