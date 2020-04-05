#!/bin/py
#   -*-coding:utf-8-*-
import time

class prime():
    ##生成器，用于生成数字序列
    def gen(self,x=2,lim=1000):
        x=int(x)
        if x>lim:
            print("区间错误")
        while x<=lim:
            yield x
            x=x+1

    def find(self):
        for num in self.N:
            if num<=1 or not isinstance(num,int):
                # print(num,"worng")
                continue
            if num==2 or num==3:
                self.result.append(num)
                continue
            i=2
            while i<=(num//2):
                if num%i==0:
                    # print("{}可以整除{}".format(num,i),"所以",num,"不是质数")
                    i=i+1
                    break
                elif i==num//2:
                    # print(num,"是质数")
                    self.result.append(num)
                    break
                else:
                    # print("{}不可以整除{}".format(num, i), "继续测试")
                    i=i+1
        print(self.result,self.result.__len__())

    def __init__(self,x=2,lim=100):
        self.result=[]
        self.N=self.gen(x,lim)
        print('init',self.result,self.N)
        self.find()


start=time.time()
prime(1,100000)
print(time.time()-start)