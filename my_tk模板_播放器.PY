from  tkinter import *
from tkinter.messagebox import *
import tkinter
import time
import os
from tkinter.filedialog import askopenfilename



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

        self.drag_flag = None

        self.root.title('dhplay')
        self.root['bg'] = '#bcbcbc'
        # self.root.attributes("-alpha", 0.9)

        self.root.geometry("800x600")

        video = tkinter.Frame(self.root,bg='#bcbcbc')             #定义视频播放窗体

        control=tkinter.Frame(self.root)
        control1=tkinter.Frame(control)
        control2=tkinter.Frame(control)

        control1.pack(side=tkinter.LEFT,anchor=tkinter.S,expand=tkinter.NO,fill=tkinter.BOTH)
        control2.pack(side=tkinter.RIGHT,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)

        open_button=tkinter.Button(control1,text='打开',command=self.openfile)
        play_button=tkinter.Button(control1,text='播放',command=self.play)
        speedup_button=tkinter.Button(control1,text='加速',command=self.play_fast)
        # pause_button=tkinter.Button(control1,text='暂停',command=self.pause)
        onebyone_button=tkinter.Button(control1,text='单帧',command=self.onebyone)
        catchpic_button = tkinter.Button(control1, text='截图', command=self.catchpic)
        stop_button=tkinter.Button(control1,text='停止',command=self.stop)

        open_button.grid(row=0, column=0)
        play_button.grid(row=0, column=1)
        speedup_button.grid(row=0, column=2)
        # pause_button.grid(row=0, column=3)
        onebyone_button.grid(row=0, column=4)
        catchpic_button.grid(row=0, column=5)
        stop_button.grid(row=0, column=6)

        self.bar=tkinter.Scale(control2, from_=0, to=100, orient=tkinter.HORIZONTAL,showvalue=0,borderwidth=0.01,repeatinterval=0,tickinterval=25,font=('宋体',8),cursor='cross',
                               sliderlength=13)

        self.bar.bind("<ButtonPress-1>",self.mouse_down)
        self.bar.bind("<ButtonRelease-1>",self.mouse_up)
        self.bar.bind('<B1-Motion> ',self.mouse_move)
        self.bar.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)

        video.pack(side=tkinter.TOP,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)
        control.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.NO,fill=tkinter.BOTH)
        self.hwnd = video.winfo_id()        #获得视频窗体的句柄


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
