from  tkinter import *
import tkinter
import sys,os
import  matplotlib.pyplot as plt
import pandas as pd

class Monitor():


    temp_path=os.path.join(os.getenv('temp'),'p.png')
    data = pd.read_excel('./接触电阻数据.xlsx')
    print(data)
    shijian = data['时间/S']
    dianya = data['电压/V']
    dianliu = data['电流/A']
    dianzu = data['电阻/Ω']
    yali = data['压力/N']

    def __del__(self):
        pass



    def __init__(self):
        self.root = Tk()

        self.root.title('接触电阻实时监控界面')
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


        self.label1=tkinter.Label(self.area1,text='实时电压')
        self.label1.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
        self.label2=tkinter.Label(self.area2,text='实时电流')
        self.label2.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
        self.label3 = tkinter.Label(self.area3, text='实时电阻')
        self.label3.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
        self.label4 = tkinter.Label(self.area4, text='实时压力')
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
        plt.ylabel('V',rotation = 0)
        plt.xlabel('S')
        plt.savefig(self.temp_path)
        self.dianya=tkinter.PhotoImage(file=self.temp_path)
        plt.close()

        plt.plot(self.shijian ,self.dianliu)
        plt.xticks(self.shijian)
        plt.ylabel('A',rotation = 0)
        plt.xlabel('S')
        plt.savefig(self.temp_path)
        self.dianliu=tkinter.PhotoImage(file=self.temp_path)
        plt.close()

        plt.plot(self.shijian ,self.dianzu)
        plt.xticks(self.shijian)
        plt.ylabel('Ω',rotation = 0)
        plt.xlabel('S')
        plt.savefig(self.temp_path)
        self.dianzu=tkinter.PhotoImage(file=self.temp_path)
        plt.close()

        plt.plot(self.shijian ,self.yali)
        plt.xticks(self.shijian)
        plt.ylabel('N',rotation = 0)
        plt.xlabel('S')
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
# <ButtonPress-n>     <Button-n>      <n>                         鼠标按钮n被按下，n为1左键，2中键，3右键
# <ButtonRelease-n>                                               鼠标按钮n被松开
# <Double-Button-n>                                               鼠标按钮n被双击
# <Triple-Button-n>                                               鼠标按钮n被三击
# <Motion>                                                        鼠标被按下，同时，鼠标发生移动
# <Bn-Motion>                                                     鼠标按钮n被按下，同时，鼠标发生移动
# <Enter>                                                         鼠标进入
# <Leave>                                                         鼠标离开
# <MouseWheel>                                                    鼠标滚轮滚动
# <Button-1>  鼠标左键
# <Button-2>   鼠标中间键（滚轮）
# <Button-3>  鼠标右键
# <Double-Button-1>   双击鼠标左键
# <Double-Button-3>   双击鼠标右键
# <Triple-Button-1>   三击鼠标左键
# <Triple-Button-3>   三击鼠标右键
