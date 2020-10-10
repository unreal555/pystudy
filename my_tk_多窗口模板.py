
# Team : JiaLiDun University
# Author：zl
# Date ：2020/9/30 0030 上午 9:39
# Tool ：PyCharm


from  tkinter import *
from tkinter.messagebox import *
import tkinter
import time
import os
from tkinter.filedialog import askopenfilename

class my_app():


    root=Tk()
    root.title('dhplay')
    root['bg'] = '#bcbcbc'
    #root.attributes("-alpha", 0.9)
    root.geometry("800x600")

    screen=9

    def get_hwnd(self,event):
        print(event.widget.winfo_id())

    def get_father_widget(self,event):
        return event.widget.nametowidget(event.widget.winfo_parent())

    def show_nine_play(self):
        self.video_play_1.pack_forget()
        self.video_play_2.pack_forget()
        self.video_play_3.pack_forget()
        self.video_play_4.pack_forget()
        self.video_play_5.pack_forget()
        self.video_play_6.pack_forget()
        self.video_play_7.pack_forget()
        self.video_play_8.pack_forget()
        self.video_play_9.pack_forget()
        self.video_play_area_1.pack_forget()
        self.video_play_area_2.pack_forget()
        self.video_play_area_3.pack_forget()
        self.video_play_area_1.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.video_play_area_2.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.video_play_area_3.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.video_play_1.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.video_play_2.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.video_play_3.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.video_play_4.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.video_play_5.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.video_play_6.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.video_play_7.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.video_play_8.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.video_play_9.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

    def show_one_play(self,event):

        self.video_play_1.pack_forget()
        self.video_play_2.pack_forget()
        self.video_play_3.pack_forget()
        self.video_play_4.pack_forget()
        self.video_play_5.pack_forget()
        self.video_play_6.pack_forget()
        self.video_play_7.pack_forget()
        self.video_play_8.pack_forget()
        self.video_play_9.pack_forget()
        self.video_play_area_1.pack_forget()
        self.video_play_area_2.pack_forget()
        self.video_play_area_3.pack_forget()
        father_frame = event.widget.nametowidget(event.widget.winfo_parent())
        father_frame.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        event.widget.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        print(event)


    def change_window(self,event):

        print(event, self.screen)

        if self.screen==9:

            self.show_one_play(event)

            self.screen =1

            print(self.screen)

        else:

            self.show_nine_play()

            self.screen=9

            print(self.screen)


        

    def __init__(self):

        self.list_area=tkinter.Frame(self.root,cursor='cross' ,bd=3, relief="sunken")

        self.video_area=tkinter.Frame(self.root ,bd=1, relief="sunken")

        self.list_area.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.video_area.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

        self.video_list=tkinter.Listbox(self.list_area)

        self.video_list.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

        self.video_play_area=tkinter.Frame(self.video_area ,bd=1, relief="sunken")

        self.video_control_area=tkinter.Frame(self.video_area, bd=1, relief="sunken")

        self.video_play_area.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

        self.video_control_area.pack(side=tkinter.BOTTOM, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.video_play_area_1=tkinter.Frame(self.video_play_area ,bd=1, relief="sunken")
        self.video_play_area_2=tkinter.Frame(self.video_play_area ,bd=1, relief="sunken")
        self.video_play_area_3=tkinter.Frame(self.video_play_area ,bd=1, relief="sunken")

        self.video_play_1 = tkinter.Frame(self.video_play_area_1 , cursor='plus',bd=2, relief="sunken")
        self.video_play_2 = tkinter.Frame(self.video_play_area_1 , cursor='plus',bd=2, relief="sunken")
        self.video_play_3 = tkinter.Frame(self.video_play_area_1 , cursor='plus',bd=2, relief="sunken")
        self.video_play_4 = tkinter.Frame(self.video_play_area_2 , cursor='plus',bd=2, relief="sunken")
        self.video_play_5 = tkinter.Frame(self.video_play_area_2 , cursor='plus',bd=2, relief="sunken")
        self.video_play_6 = tkinter.Frame(self.video_play_area_2 , cursor='plus',bd=2, relief="sunken")
        self.video_play_7 = tkinter.Frame(self.video_play_area_3 , cursor='plus',bd=2, relief="sunken")
        self.video_play_8 = tkinter.Frame(self.video_play_area_3 , cursor='plus',bd=2, relief="sunken")
        self.video_play_9 = tkinter.Frame(self.video_play_area_3 , cursor='plus',bd=2, relief="sunken")
        self.video_play_1.bind("<ButtonPress-1>", self.get_hwnd)
        self.video_play_2.bind("<ButtonPress-1>", self.get_hwnd)
        self.video_play_3.bind("<ButtonPress-1>", self.get_hwnd)
        self.video_play_4.bind("<ButtonPress-1>", self.get_hwnd)
        self.video_play_5.bind("<ButtonPress-1>", self.get_hwnd)
        self.video_play_6.bind("<ButtonPress-1>", self.get_hwnd)
        self.video_play_7.bind("<ButtonPress-1>", self.get_hwnd)
        self.video_play_8.bind("<ButtonPress-1>", self.get_hwnd)
        self.video_play_9.bind("<ButtonPress-1>", self.get_hwnd)
        self.video_play_1.bind("<Double-Button-1>", self.change_window)
        self.video_play_2.bind("<Double-Button-1>", self.change_window)
        self.video_play_3.bind("<Double-Button-1>", self.change_window)
        self.video_play_4.bind("<Double-Button-1>", self.change_window)
        self.video_play_5.bind("<Double-Button-1>", self.change_window)
        self.video_play_6.bind("<Double-Button-1>", self.change_window)
        self.video_play_7.bind("<Double-Button-1>", self.change_window)
        self.video_play_8.bind("<Double-Button-1>", self.change_window)
        self.video_play_9.bind("<Double-Button-1>", self.change_window)

        self.show_nine_play()

        self.open_button=tkinter.Button(self.video_control_area,text='打开')

        self.play_button=tkinter.Button(self.video_control_area,text='播放')

        self.speedup_button=tkinter.Button(self.video_control_area,text='加速')

        self.pause_button=tkinter.Button(self.video_control_area,text='暂停')

        self.stop_button=tkinter.Button(self.video_control_area,text='停止')

        self.open_button.grid(row=0, column=0)

        self.play_button.grid(row=0, column=1)

        self.speedup_button.grid(row=0, column=2)

        self.pause_button.grid(row=0, column=3)

        self.stop_button.grid(row=0, column=4)

        print('init finished')


app=my_app()
app.root.mainloop()





#
# class myapp():
#     root = Tk()
#     root2=Tk()
#
#     drag_flag=None
#
#     def __del__(self):
#         pass
#
#     def openfile(self):
#
#         file =  askopenfilename()
#         temp,ext=os.path.splitext(file)
#         print(file)
#
#
#
#
#
#     def mouse_down(self,event):
#         self.drag_flag=False
#
#     def mouse_move(self,event):
#         pass
#
#     def mouse_up(self,event):
#         self.drag_flag=True
#
#     def stop(self):
#
#         pass
#
#     def play(self):
#         pass
#
#     def play_fast(self):
#         pass
#
#     def pause(self):
#         pass
#
#     def onebyone(self):
#         pass
#
#     def catchpic(self):
#         pass
#
#     def __init__(self):
#
#         self.root2.title('2')
#         self.root2['bg'] = '#bcbcbc'
#         # self.root.attributes("-alpha", 0.9)
#
#         self.root2.geometry("800x600")
#
#
#                                        #定义图形界面
#         self.root.title('dhplay')
#         self.root['bg'] = '#bcbcbc'
#         # self.root.attributes("-alpha", 0.9)
#
#         self.root.geometry("800x600")
#
#
#         video = tkinter.Frame(self.root,bg='#bcbcbc')             #定义视频播放窗体
#
#         control=tkinter.Frame(self.root)
#
#         control1=tkinter.Frame(control)
#         control2=tkinter.Frame(control)
#
#         control1.pack(side=tkinter.LEFT,anchor=tkinter.S,expand=tkinter.NO,fill=tkinter.BOTH)
#         control2.pack(side=tkinter.RIGHT,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)
#
#
#         open_button=tkinter.Button(control1,text='打开',command=self.openfile())
#
#         play_button=tkinter.Button(control1,text='播放',command=self.play)
#
#         speedup_button=tkinter.Button(control1,text='加速',command=self.play_fast)
#
#         # pause_button=tkinter.Button(control1,text='暂停',command=self.pause)
#
#         onebyone_button=tkinter.Button(control1,text='单帧',command=self.onebyone)
#
#         catchpic_button = tkinter.Button(control1, text='截图', command=self.catchpic)
#
#         stop_button=tkinter.Button(control1,text='停止',command=self.stop)
#
#
#
#         open_button.grid(row=0, column=0)
#         play_button.grid(row=0, column=1)
#         speedup_button.grid(row=0, column=2)
#         # pause_button.grid(row=0, column=3)
#         onebyone_button.grid(row=0, column=4)
#         catchpic_button.grid(row=0, column=5)
#         stop_button.grid(row=0, column=6)
#
#         self.bar=tkinter.Scale(control2, from_=0, to=100, orient=tkinter.HORIZONTAL,showvalue=0,borderwidth=0.01,repeatinterval=0,tickinterval=25,font=('宋体',8),cursor='cross',
#                                sliderlength=13)
#
#         self.bar.bind("<ButtonPress-1>",self.mouse_down)
#         self.bar.bind("<ButtonRelease-1>",self.mouse_up)
#         self.bar.bind('<B1-Motion> ',self.mouse_move)
#         self.bar.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)
#
#         video.pack(side=tkinter.TOP,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)
#         control.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.NO,fill=tkinter.BOTH)
#         self.hwnd = video.winfo_id()        #获得视频窗体的句柄
#
#
#
#
#
#     def next_windwos(self):
#         self.root.destroy()
#         self.root.title('2')
#         self.root['bg'] = '#bcbcbc'
#         # self.root.attributes("-alpha", 0.9)
#
#         self.root.geometry("800x600")
#
#
#
#
# app=myapp()
# myapp.root.mainloop()




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


#frame cursor style
# "arrow"
# 
# "circle"
# 
# "clock"
# 
# "cross"
# 
# "dotbox"
# 
# "exchange"
# 
# "fleur"
# 
# "heart"
# 
# "heart"
# 
# "man"
# 
# "mouse"
# 
# "pirate"
# 
# "plus"
# 
# "shuttle"
# 
# "sizing"
# 
# "spider"
# 
# "spraycan"
# 
# "star"
# 
# "target"
# 
# "tcross"
# 
# "trek"
# 
# "watch"