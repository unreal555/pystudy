from  tkinter import *
from matplotlib.pyplot import MultipleLocator
import tkinter
import sys,os
import  matplotlib.pyplot as plt
import pandas as pd

class Monitor():


    temp_path=os.path.join(os.getenv('temp'),'p.png')
    data = pd.read_excel('./接触电阻数据.xlsx')
    print(data)
    shijian = data['时间/mS']
    dianya = data['摩擦力/mN']
    dianliu = data['电流/mA']
    dianzu = data['电阻/mΩ']
    yali = data['压力/mN']

    def __del__(self):
        pass



    def __init__(self):
        self.root = Tk()

        self.root.title('实时监控界面')
        self.root['bg'] = '#bcbcbc'
        self.root.attributes("-alpha", 0.9)

        self.root.geometry("1920x1080")

        self.up=tkinter.Frame(self.root,bd=0, relief="sunken")
        self.up.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

        self.down=tkinter.Frame(self.root,bd=0, relief="sunken")
        self.down.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

        self.area1=tkinter.Frame(self.up,bd=1, relief="sunken")
        self.area2=tkinter.Frame(self.up,bd=1, relief="sunken")
        self.area3 = tkinter.Frame(self.down,bd=1, relief="sunken")
        self.area4 = tkinter.Frame(self.down,bd=1, relief="sunken")

        self.area1.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.area2.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.area4.pack(side=tkinter.RIGHT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.area3.pack(side=tkinter.RIGHT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)


        self.label1=tkinter.Label(self.area1,text='摩擦力')
        self.label1.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
        self.label2=tkinter.Label(self.area2,text='电流')
        self.label2.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
        self.label3 = tkinter.Label(self.area3, text='电阻')
        self.label3.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
        self.label4 = tkinter.Label(self.area4, text='压力')
        self.label4.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.geo1= tkinter.Canvas(self.area1,bd=1)
        self.geo1.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.geo2 = tkinter.Canvas(self.area2,bd=1)
        self.geo2.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.geo3 = tkinter.Canvas(self.area3,bd=1)
        self.geo3.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.geo4 = tkinter.Canvas(self.area4,bd=1)
        self.geo4.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

        fig, ax = plt.subplots()  
        plt.plot(self.shijian ,self.dianya)
        plt.xticks(self.shijian)
        ax.xaxis.set_major_locator(MultipleLocator(10))
        plt.ylabel('mN',rotation = 0)
        plt.xlabel('mS')
        plt.savefig(self.temp_path)
        self.dianya=tkinter.PhotoImage(file=self.temp_path)
        plt.close()

        fig, ax = plt.subplots()
        plt.plot(self.shijian ,self.dianliu)
        plt.xticks(self.shijian)
        ax.xaxis.set_major_locator(MultipleLocator(10))
        plt.ylabel('mA',rotation = 0)
        plt.xlabel('mS')
        plt.savefig(self.temp_path)
        self.dianliu=tkinter.PhotoImage(file=self.temp_path)
        plt.close()

        fig, ax = plt.subplots()
        plt.plot(self.shijian ,self.dianzu)
        plt.xticks(self.shijian)
        ax.xaxis.set_major_locator(MultipleLocator(10))
        plt.ylabel('mΩ',rotation = 0)
        plt.xlabel('mS')
        plt.savefig(self.temp_path)
        self.dianzu=tkinter.PhotoImage(file=self.temp_path)
        plt.close()
        
        fig, ax = plt.subplots()
        plt.plot(self.shijian ,self.yali)
        plt.xticks(self.shijian)
        ax.xaxis.set_major_locator(MultipleLocator(10))
        plt.ylabel('mN',rotation = 0)
        plt.xlabel('mS')
        plt.savefig(self.temp_path)
        self.yali=tkinter.PhotoImage(file=self.temp_path)
        plt.close()



        self.geo1.create_image(0,0,image=self.dianya,anchor='nw')
        self.geo2.create_image(0, 0, image=self.dianliu, anchor='nw')
        self.geo3.create_image(0, 0, image=self.dianzu, anchor='nw')
        self.geo4.create_image(0, 0, image=self.yali, anchor='nw')






app=Monitor()
app.root.mainloop()




#
