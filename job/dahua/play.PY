from  tkinter import *
import tkinter 
import ctypes
from ctypes import *
import time
import functools
from tkinter.filedialog import askopenfilename


#tkinter.messagebox.showinfo("源目录错误", "{}不是目录,或者目录不存在,请重新输入".format(source))
class myapp():

    def get_nPort(dll):
        port = c_long()  # 定义视频通道类型
        nPort = c_long(dll.PLAY_GetFreePort(byref(port)))  # 调用函数获得视频通道编号
        return nPort

    dll = ctypes.windll.LoadLibrary('./dhplay.dll')  # 加载动态库为dh
    root=Tk() 

    nPort=get_nPort(dll)

    hwnd=''

    scorll_bar=''



    def openfile(self):
        file =  askopenfilename()
        file=file.encode('unicode_escape')
        print(file)
        file = ctypes.c_char_p(file)  # 转换文件地址为c字符指针类型
        self.dll.PLAY_OpenFile(self.nPort,file)
        self.dll.PLAY_Play(self.nPort, self.hwnd)

    def get_pos(self):

        try:
            full=self.dll.PLAY_GetFileTime(self.nPort)
        
            past=self.dll.PLAY_GetPlayedTime(self.nPort)

        

            pos=int(past/full*100)

            print(full,past,pos)
        
            return pos
        except Exception as e:
            print(e)
            return 0

    def refresh_data(self):
        # 需要刷新数据的操作
        # 代码...

        pos=self.get_pos()
        
        if isinstance(pos,int):
            self.scorll_bar.set(pos)

        
        self.root.after(1000, self.refresh_data )   # 这里的10000单位为毫秒
    


    def stop(self):

        self.dll.PLAY_Stop(self.nPort)


    def play(self):
        self.dll.PLAY_Play(self.nPort,self.hwnd)
        

    def play_fast(self):
        self.dll.PLAY_Fast(self.nPort)

    def __init__(self):

                                       #定义图形界面
        self.root.title('dhplay')
        self.root['bg'] = '#bcbcbc'
        #root.attributes("-alpha", 0.9)

        self.root.geometry("800x600")

        
        video = tkinter.Frame(self.root)             #定义视频播放窗体

        control=tkinter.Frame(self.root)

        control1=tkinter.Frame(control)
        control2=tkinter.Frame(control)

        control1.pack(side=tkinter.LEFT,anchor=tkinter.S,expand=tkinter.NO,fill=tkinter.BOTH)
        control2.pack(side=tkinter.RIGHT,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)
              

        open_button=tkinter.Button(control1,text='open',command=self.openfile)

        play_button=tkinter.Button(control1,text='play',command=self.play)

        speedup_button=tkinter.Button(control1,text='speed',command=self.play_fast)

        stop_button=tkinter.Button(control1,text='stop',command=self.stop)

        open_button.grid(row=0, column=0)
        play_button.grid(row=0, column=1)
        speedup_button.grid(row=0, column=2)
        stop_button.grid(row=0, column=3)

        scorll_bar=tkinter.Scale(control2, from_=0, to=100, orient=tkinter.HORIZONTAL,showvalue=0)
        scorll_bar.pack(side=tkinter.RIGHT,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)

        self.scorll_bar=scorll_bar
        
        video.pack(side=tkinter.TOP,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)
        control.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.NO,fill=tkinter.BOTH)


        self.hwnd = video.winfo_id()        #获得视频窗体的句柄

        print(self.hwnd)        #输出句柄







        self.refresh_data()

        self.root.mainloop()



app=myapp()





