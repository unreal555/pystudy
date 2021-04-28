from  tkinter import *
import tkinter
import os
from tkinter.filedialog import askopenfilename

import turtle



class player():


    def __del__(self):
        pass

    def openfile(self):

        file =  askopenfilename()
        temp,ext=os.path.splitext(file)
        print(file)


    def mouse_down(self,event):
        self.drag_flag=False

    def mouse_move(self,event):
        pass

    def mouse_up(self,event):
        self.drag_flag=True

    def stop(self):

        pass

    def play(self):
        pass

    def play_fast(self):
        pass

    def pause(self):
        pass

    def onebyone(self):
        pass

    def catchpic(self):
        pass

    def __init__(self):
        self.root = Tk()
        self.root.title('画图板')
        self.root['bg'] = '#bcbcbc'
        # self.root.attributes("-alpha", 0.9)
        self.root.geometry("1024x600")

        self.color='black'
        self.fillcolor='white'

        self.colorPanelArea=tkinter.Frame(self.root, bd=2, relief="sunken",height=10)
        self.downArea=tkinter.Frame(self.root, bd=2, relief="sunken",height=10)
        self.colorPanelArea.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
        self.downArea.pack(side=tkinter.BOTTOM, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        
        self.drawArea=tkinter.Frame(self.downArea, bd=2, relief="sunken",height=10)
        self.toolsArea=tkinter.Frame(self.downArea, bd=2, relief="sunken",height=10)
        self.drawArea.pack(side=tkinter.RIGHT,  expand=tkinter.YES, fill=tkinter.BOTH)
        self.toolsArea.pack(side=tkinter.LEFT,  expand=tkinter.NO, fill=tkinter.Y)

        self.redButton=tkinter.Button(self.colorPanelArea,text='红色',bg='red')
        self.redButton.pack(side=tkinter.LEFT,  expand=tkinter.NO, fill=tkinter.X)
        self.redButton.bind("<ButtonPress-1>",self.setLineColor)
        
        self.greenButton=tkinter.Button(self.colorPanelArea,text='绿色',bg='green')
        self.greenButton.pack(side=tkinter.LEFT,  expand=tkinter.NO, fill=tkinter.X)
        self.greenButton.bind("<ButtonPress-1>", self.setLineColor)
        
        self.drawLineButton=tkinter.Button(self.toolsArea,text='线',command=self.drawLine)
        self.drawLineButton.pack(side=tkinter.TOP,  expand=tkinter.NO, fill=tkinter.X)
        
        self.drawPeiQiButton=tkinter.Button(self.toolsArea,text='佩奇',command=self.drawPeiQi)
        self.drawPeiQiButton.pack(side=tkinter.TOP,  expand=tkinter.NO, fill=tkinter.X)
    
        self.cv=tkinter.Canvas(self.drawArea)
        self.cv.pack(side=tkinter.LEFT,  expand=tkinter.YES, fill=tkinter.BOTH)
        

    def drawLine(self):
        self.cv.create_line(1,1,520,520,fill=self.fillcolor)
        
    def setLineColor(self,event):
        print(event.widget['bg'])
        self.fillcolor=event.widget['bg']
    
    def drawPeiQi(self):
        cv=self.cv
        w = turtle.TurtleScreen(cv)
        t = turtle.RawTurtle(w)
        t.pensize(4)
        # t.hideturtle()
        t.color((1, 0.6, 0.75), "pink")
        # t.setup(840, 500)
        t.speed(10)

        # 鼻子
        t.pu()
        t.goto(100,-50)
        t.pd()
        t.seth(-30)
        t.begin_fill()
        a = 0.4
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a = a + 0.08
                t.lt(3)  # 向左转3度
                t.fd(a)  # 向前走a的步长
            else:
                a = a - 0.08
                t.lt(3)
                t.fd(a)
        t.end_fill()

        t.pu()
        t.seth(90)
        t.fd(25)
        t.seth(0)
        t.fd(10)
        t.pd()
        t.pencolor(1, 0.6, 0.75)
        t.seth(10)
        t.begin_fill()
        t.circle(5)
        t.color(0.62, 0.33, 0.18)
        t.end_fill()

        t.pu()
        t.seth(0)
        t.fd(20)
        t.pd()
        t.pencolor(1, 0.6, 0.75)
        t.seth(10)
        t.begin_fill()
        t.circle(5)
        t.color(0.62,0.32 , 0.18)
        t.end_fill()

        # 头
        t.color((1, 0.6, 0.75), "pink")
        t.pu()
        t.seth(90)
        t.fd(41)
        t.seth(0)
        t.fd(0)
        t.pd()
        t.begin_fill()
        t.seth(180)
        t.circle(300, -30)
        t.circle(100, -60)
        t.circle(80, -100)
        t.circle(150, -20)
        t.circle(60, -95)
        t.seth(161)
        t.circle(-300, 15)
        t.pu()
        t.goto(100, -50)
        t.pd()
        t.seth(-30)
        a = 0.4
        for i in range(60):
            if 0 <= i < 30 or 60 <= i < 90:
                a = a + 0.08
                t.lt(3)  # 向左转3度
                t.fd(a)  # 向前走a的步长
            else:
                a = a - 0.08
                t.lt(3)
                t.fd(a)
        t.end_fill()

        # 耳朵
        t.color((1, 0.6, 0.75), "pink")
        t.pu()
        t.seth(90)
        t.fd(-7)
        t.seth(0)
        t.fd(70)
        t.pd()
        t.begin_fill()
        t.seth(100)
        t.circle(-50, 50)
        t.circle(-10, 120)
        t.circle(-50, 54)
        t.end_fill()

        t.pu()
        t.seth(90)
        t.fd(-12)
        t.seth(0)
        t.fd(30)
        t.pd()
        t.begin_fill()
        t.seth(100)
        t.circle(-50, 50)
        t.circle(-10, 120)
        t.circle(-50, 56)
        t.end_fill()

        # 眼睛
        t.color((1, 0.6, 0.75), "white")
        t.pu()
        t.seth(90)
        t.fd(-20)
        t.seth(0)
        t.fd(-95)
        t.pd()
        t.begin_fill()
        t.circle(15)
        t.end_fill()

        t.color("black")
        t.pu()
        t.seth(90)
        t.fd(12)
        t.seth(0)
        t.fd(-3)
        t.pd()
        t.begin_fill()
        t.circle(3)
        t.end_fill()

        t.color((1, 0.6, 0.75), "white")
        t.pu()
        t.seth(90)
        t.fd(-25)
        t.seth(0)
        t.fd(40)
        t.pd()
        t.begin_fill()
        t.circle(15)
        t.end_fill()

        t.color("black")
        t.pu()
        t.seth(90)
        t.fd(12)
        t.seth(0)
        t.fd(-3)
        t.pd()
        t.begin_fill()
        t.circle(3)
        t.end_fill()

        # 腮
        t.color((1, 0.6, 0.75))
        t.pu()
        t.seth(90)
        t.fd(-95)
        t.seth(0)
        t.fd(65)
        t.pd()
        t.begin_fill()
        t.circle(30)
        t.end_fill()

        # 嘴
        t.color(0.94, 0.27, 0.075)
        t.pu()
        t.seth(90)
        t.fd(15)
        t.seth(0)
        t.fd(-100)
        t.pd()
        t.seth(-80)
        t.circle(30, 40)
        t.circle(40, 80)

        # 身体
        t.color("red", (1, 0.39, 0.28))
        t.pu()
        t.seth(90)
        t.fd(-20)
        t.seth(0)
        t.fd(-78)
        t.pd()
        t.begin_fill()
        t.seth(-130)
        t.circle(100, 10)
        t.circle(300, 30)
        t.seth(0)
        t.fd(230)
        t.seth(90)
        t.circle(300, 30)
        t.circle(100, 3)
        t.color((1, 0.6, 0.75), (1, 0.39, 0.39))
        t.seth(-135)
        t.circle(-80, 63)
        t.circle(-150, 24)
        t.end_fill()

        # 手
        t.color((1, 0.6, 0.75))
        t.pu()
        t.seth(90)
        t.fd(-40)
        t.seth(0)
        t.fd(-27)
        t.pd()
        t.seth(-160)
        t.circle(300, 15)
        t.pu()
        t.seth(90)
        t.fd(15)
        t.seth(0)
        t.fd(0)
        t.pd()
        t.seth(-10)
        t.circle(-20, 90)

        t.pu()
        t.seth(90)
        t.fd(30)
        t.seth(0)
        t.fd(237)
        t.pd()
        t.seth(-20)
        t.circle(-300, 15)
        t.pu()
        t.seth(90)
        t.fd(20)
        t.seth(0)
        t.fd(0)
        t.pd()
        t.seth(-170)
        t.circle(20, 90)

        # 脚
        t.pensize(10)
        t.color((0.94, 0.5, 0.5))
        t.pu()
        t.seth(90)
        t.fd(-75)
        t.seth(0)
        t.fd(-180)
        t.pd()
        t.seth(-90)
        t.fd(40)
        t.seth(-180)
        t.color("black")
        t.pensize(15)
        t.fd(20)

        t.pensize(10)
        t.color((0.94,0.5,0.5))
        t.pu()
        t.seth(90)
        t.fd(40)
        t.seth(0)
        t.fd(90)
        t.pd()
        t.seth(-90)
        t.fd(40)
        t.seth(-180)
        t.color("black")
        t.pensize(15)
        t.fd(20)

        # 尾巴
        t.pensize(4)
        t.color((1, 0.6, 0.75))
        t.pu()
        t.seth(90)
        t.fd(70)
        t.seth(0)
        t.fd(95)
        t.pd()
        t.seth(0)
        t.circle(70, 20)
        t.circle(10, 330)
        t.circle(70, 30)

app=player()
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


# play_button=tkinter.Button(control1,text='播放',command=self.play)
# speedup_button=tkinter.Button(control1,text='加速',command=self.play_fast)
# # pause_button=tkinter.Button(control1,text='暂停',command=self.pause)
# onebyone_button=tkinter.Button(control1,text='单帧',command=self.onebyone)
# catchpic_button = tkinter.Button(control1, text='截图', command=self.catchpic)
# stop_button=tkinter.Button(control1,text='停止',command=self.stop)
#
# open_button.grid(row=0, column=0)
# play_button.grid(row=0, column=1)
# speedup_button.grid(row=0, column=2)
# # pause_button.grid(row=0, column=3)
# onebyone_button.grid(row=0, column=4)
# catchpic_button.grid(row=0, column=5)
# stop_button.grid(row=0, column=6)
#
# self.bar=tkinter.Scale(control2, from_=0, to=100, orient=tkinter.HORIZONTAL,showvalue=0,borderwidth=0.01,repeatinterval=0,tickinterval=25,font=('宋体',8),cursor='cross',
#                        sliderlength=13)
#
# self.bar.bind("<ButtonPress-1>",self.mouse_down)
# self.bar.bind("<ButtonRelease-1>",self.mouse_up)
# self.bar.bind('<B1-Motion> ',self.mouse_move)
# self.bar.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)
#
# video.pack(side=tkinter.TOP,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)
# control.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.NO,fill=tkinter.BOTH)
# self.hwnd = video.winfo_id()        #获得视频窗体的句柄