#!/bin/py
#   -*-coding:utf-8-*-
#!/bin/py
#   -*-coding:utf-8-*-
import math
import time
import pickle


class FindPrime():

    def find(self):
        for num in self.N:
            sqrt_num=int(math.sqrt(num))
            temp_prime=[]
            if num<=1 or not isinstance(num,int):
                continue
            if num==2 or num==3:
                self.values.append(num)
                continue

            for i in self.prime:
                if i<=sqrt_num:
                    temp_prime.append(i)
            count=0
            for i in temp_prime:
                if num%i==0:
                    count+=1
                    break
            if count==0:
                print(num)
                self.values.append(num)
                if num not in self.prime:
                    self.prime.append(num)


    def __init__(self,x=2,y=100):
        with open('./prime.dat','rb') as f:
            temp=pickle.load(f)
            
        self.prime=temp
        self.values=temp
        minPrime=self.prime[0]
        maxPrime=self.prime[-1]

        print(x,y,minPrime,maxPrime)

        if x<=0 or y<=0:
            
            print('区间{}-{}错误'.format(x,y))

        if x<=maxPrime<=y:
            print('部分区间已计算，优化为{}-{}'.format(maxPrime+1,y))
            self.N=range(maxPrime+1,abs(int(y)))
            self.find()
        
        if  minPrime<=y<=maxPrime:
            print('区间{}-{}已计算'.format(x,y))
                    




start=time.time()
p=FindPrime(1,39100000)
with open('prime.dat','wb') as f:
    pickle.dump(p.values,f)

print(len(p.values))
print(time.time()-start)
