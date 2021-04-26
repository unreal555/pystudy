#!/bin/py
#   -*-coding:utf-8-*-
import time

class prime():
    ##生成器，用于生成数字序列
    values=[]
    def gen(self,x=2,lim=1000):
        x=int(x)
        if x>lim:
            print("区间错误")
        while x<=lim:
            yield x
            x=x+1

    def find(self):
        for num in self.N:
            #print(num)
            if num<=1 or not isinstance(num,int):
                # print(num,"worng")
                continue
            if num==2 or num==3:
                self.values.append(num)
                continue
            i=2
            while i<=(num//2):
                if num%i==0:
                    #print("{}可以整除{}".format(num,i),"所以",num,"不是质数")
                    break
                if i==num//2:
                    #print(num,"是质数")
                    self.values.append(num)
                    break
                i = i + 1

    def __init__(self,x=2,lim=100):
        self.N=self.gen(x,lim)
        self.find()


start=time.time()
prime(1,100000)
print('个数:',len(prime.values),prime.values)
print(time.time()-start)