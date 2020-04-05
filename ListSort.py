#!/bin/py
#   -*-coding:utf-8-*-
'       说明               '
_author_ = 'zl'
import time



class ListSort(object):

    def __init__(self,args=[]):
        self.__debug = 1
        if self.__debug:print(type(args),args)

        if isinstance(args,str):
            self.__List=[int(x) for x in args.split(",")]
        if isinstance(args,list):
            self.__List=args
        if self.__debug: print(type(self.__List), self.__List)

        if not self.__List:
            self.__List = []
        else:

            for i in self.__List:
                if isinstance(i,str):
                    raise Exception(i,"type error")
                    break

        if self.__debug:print(self.__List)

    def setDebug(self,i):

        self.__debug=i


    ##装饰器,返回程序执行的时间
    def execTime(func):
        def warpper(*args,**kw):
            start=time.clock()
            result=func(*args,**kw)
            exectime=time.clock()-start
            print("%s执行时间为%.6f秒"%(func.__name__,exectime))
            return result
        return  warpper

    ##插入排序算法,从第一个元素开始放入新队列,比较新元素与已有元素,将其插入合适位置
    @execTime
    def insertSort(self):
        result=[]
        count=1   #元素计数器
        result.append(self.__List[0])    #放入第一个元素
        if self.__debug:print('添加第1个元素')
        while count<len(self.__List):
            if self.__debug:print('添加第{}个元素'.format(count+1))
            if self.__List[count] >=result[count - 1]:
                result.append(self.__List[count])
            for i in range(0,count):
                if self.__List[count]<=result[i]:
                    result.insert(i,self.__List[count])
                    break
            count+=1
            if self.__debug:print(result)
        if self.__debug:print("排序完成,结果为{}".format(result))
        self.__List = result
        return self.__List

    ##反转函数
    @execTime
    def exchangList(self):
        lenth=len(self.__List)
        for i in range(0,lenth//2):
            self.__List[0+i],self.__List[lenth-1-i]=self.__List[lenth-1-i],self.__List[0+i]
        if self.__debug:print("队列已经反转{}".format(list))
        return  self.__List

    ##冒泡排序算法
    @execTime
    def maopaoSort(self):
        count=0   #计数器
        flag=0
        totleFlag=0
        while count<len(self.__List)-1:
            flag=0
            for i in range(0, len(self.__List)-1):
                if self.__List[i]>self.__List[i+1]:
                    self.__List[i],self.__List[i+1]=self.__List[i+1],self.__List[i]
                    flag+=1
            count+=1
            totleFlag+=flag
            if self.__debug:print("共有元素%s个,第%s次循环,位置共交换%s次,本次循环共交换%s"%(len(self.__List),count,totleFlag,flag))
            if self.__debug:print(self.__List)
            if flag==0:
                if self.__debug:print("队列是有序的")
                break
        return self.__List


    ##选择交换的算法,从第一个开始比较,记录最小的元素偏移,完成后和第一个交换位置,以此类推
    @execTime
    def xuanzeSort(self):
        count=0
        while count<(len(self.__List)-1):
            offset=0
            min = self.__List[count]
            for i in range(count,len(self.__List)):
                if  min>=self.__List[i]:
                    min=self.__List[i]
                    offset=i
            if offset==0:
                if self.__debug:print("本身是有序队列,无需排序")
                break
            else:
                self.__List[count],self.__List[offset]=self.__List[offset],self.__List[count]
            count+=1
            if self.__debug:print("共有{}个元素,第{}次交换,结果为{}".format(len(self.__List),count,self.__List))
        return  self.__List

    @execTime
    def tongjiNum(self):
        count={}
        for i in self.__List:
            if i not in count.keys():
                count[i]=1
            else:
                count[i]+=1

        for x in sorted(count.keys()):
            if self.__debug:print("数字%10d出现了:%d次"%(x,count[x]))
        return count



######注意注意,在maopaoSort和,xuanzeSort中,直接操作的对象就是list,所以不需要return返回值,原有的队列已经被修改成有序的.






if __name__ == '__main__':   ######加本句,如果模块是直接运行的,下面的代码会执行,如果是被导入的,下面的不会被运行
    test = [12, 22323, 23, 34, 463, 23, 23, 3343, 34, 34, 2, 2, 423, 56.24, 356, 2376, 3586, 456, 8456, 8458645, 68,
                456, 845, 9856, 90879, 56874,
                56, 73456, 243, 562, 345, 234, 6, 23, 74, 3874, 357, 56, 2345, 623, 62, 346, 234, 64, 58745, 6873, 5, 68,
                56, 876, 90, 87, 5, 476, 45, 7,
                32, 62, 46, 23, 745, 8, 65835, 732, 6243, 52, 462, 7645, 8, 5, 7, 35, 234, 62, 42, 3, 354, 23, 232, 23, 232,
                433434, 4, 3, 34, 6, 3, 2345, 2,
                53, 235, 23, 5, 235, 23, 5, 25, 2, 6, 243, 6345, 7, 45, 685, 679, 4, 76843, 567, 3456345, 6345, 6, 34256,
                23456243, 64324, 6, 234, 642357645,
                7345, 7345, 6235, 623, 623464, 323554, 4, 5, 67, 7, 8, 98232, 4, 4, 53323, 23, 2, 345, 45, 4342, 23, 234,
                2534, 342, 2323, 1]
    a = ListSort(test)
    print(a.tongjiNum())
    print(a.insertSort())
    print(a.exchangList())
    print(a.insertSort())
    a.maopaoSort()
    a.xuanzeSort()
