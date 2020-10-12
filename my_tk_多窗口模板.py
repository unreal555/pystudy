
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
    root.attributes("-alpha", 0.9)
    root.geometry("1080x720")
    window_des = [('单窗口', 1), ('四窗口', 4), ('九窗口', 9)]
    v_num=''
    is_single_playing=False
    windows_status={
        'num_1':'',
        'num_2': '',
        'num_3': '',
        'num_4': '',
        'num_5': '',
        'num_6': '',
        'num_7': '',
        'num_8': '',
        'num_9': '',
    }


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
        self.is_single_playing = False

    def show_four_play(self):
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
        self.video_play_1.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.video_play_2.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.video_play_4.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.video_play_5.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.is_single_playing = False

    def show_single_play(self,event):
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
        if event==None:
            self.video_play_area_1.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
            self.video_play_1.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        else:
            father_frame = event.widget.nametowidget(event.widget.winfo_parent())
            father_frame.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
            event.widget.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.is_single_playing=True

    def change_window(self,event):
        print(event, self.v_num.get(),self.is_single_playing)
        if self.v_num.get == 1:
               pass
        if self.is_single_playing==False and self.v_num.get() == 9:
            self.show_single_play(event)
        elif self.is_single_playing == True and self.v_num.get() == 9:
            self.show_nine_play()
        elif self.is_single_playing==False and self.v_num.get() == 4:
            self.show_single_play(event)
        elif self.is_single_playing == True and self.v_num.get() == 4:
            self.show_four_play()

    def show_window(self):

        print(self.v_num.get(),self.is_single_playing)

        if self.v_num.get()==9:

            self.show_nine_play()

        if self.v_num.get() == 4:

            self.show_four_play()

        if self.v_num.get() == 1:

            self.show_single_play(event=None)


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

        self.v_num = IntVar()
        self.v_num.set(1)

        for lang, num in self.window_des:
            self.b = Radiobutton(self.video_control_area, text=lang, variable=self.v_num, value=num,indicatoron=False,command=self.show_window)
            self.b.pack(side=tkinter.RIGHT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.show_window()

        self.open_button=tkinter.Button(self.video_control_area,text='打开')

        self.play_button=tkinter.Button(self.video_control_area,text='播放')

        self.speedup_button=tkinter.Button(self.video_control_area,text='加速')

        self.pause_button=tkinter.Button(self.video_control_area,text='暂停')

        self.stop_button=tkinter.Button(self.video_control_area,text='停止')

        self.open_button.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.play_button.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.speedup_button.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.pause_button.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.stop_button.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

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

#
# class my_app():
#
#     window_num=[('单窗口',1),('四窗口',4),('九窗口',9)]
#
#     v_num=''
#
#
#     root=Tk()
#     root.title('dhplay')
#     root['bg'] = '#bcbcbc'
#     root.attributes("-alpha", 0.9)
#     root.geometry("800x600")
#
#
#     def set_video_area(self,*args):
#
#
#         if int(self.v_num.get())==1:
#             print(self.v_num.get())
#             args[0].grid(row=0, column=0)
#
#         if int(self.v_num.get()) == 4:
#             print(self.v_num.get())
#             args[0].grid(row=0, column=0)
#             args[1].grid(row=0, column=1)
#             args[2].grid(row=1, column=0)
#             args[3].grid(row=1, column=1)
#
#
#         if int(self.v_num.get()) == 9:
#             print(self.v_num.get())
#             args[0].grid(row=0, column=0)
#             args[1].grid(row=0, column=1)
#             args[2].grid(row=0, column=2)
#             args[3].grid(row=1, column=0)
#             args[4].grid(row=1, column=1)
#             args[5].grid(row=1 ,column=2)
#             args[6].grid(row=2, column=0)
#             args[7].grid(row=2, column=1)
#             args[8].grid(row=2, column=2)
#
#     def __init__(self):
#
#         control_area=tkinter.Frame(self.root, bd=1, relief="sunken")
#         video_area=tkinter.Frame(self.root ,bd=1, relief="sunken")
#
#         video_list_area=tkinter.Frame(video_area,cursor='cross' ,bd=3, relief="sunken")
#         video_window_area=tkinter.Frame(video_area ,bd=1, relief="sunken")
#
#         control_area.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
#         video_area.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
#
#         video_list_area.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
#         video_window_area.pack(side=tkinter.RIGHT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
#
#         video_list=tkinter.Listbox(video_list_area)
#         video_list.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
#
#         self.v_num = IntVar()
#         self.v_num.set(1)
#
#         for lang, num in self.window_num:
#             b = Radiobutton(control_area, text=lang, variable=self.v_num, value=num,indicatoron=False,command=lambda : self.set_video_area(video_play_1,video_play_2,video_play_3,video_play_4,video_play_5,video_play_6,video_play_7,video_play_8,video_play_9))
#             b.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
#
#         video_play_1 = tkinter.Canvas  (video_window_area ,bd=1, relief="sunken")
#         video_play_2 = tkinter.Canvas  (video_window_area , bd=1, relief="sunken")
#         video_play_3 = tkinter.Canvas  (video_window_area , bd=1, relief="sunken")
#         video_play_4 = tkinter.Canvas  (video_window_area , bd=1, relief="sunken")
#         video_play_5 = tkinter.Canvas  (video_window_area , bd=1, relief="sunken")
#         video_play_6 = tkinter.Canvas  (video_window_area , bd=1, relief="sunken")
#         video_play_7 = tkinter.Canvas  (video_window_area , bd=1, relief="sunken")
#         video_play_8 = tkinter.Canvas  (video_window_area , bd=1, relief="sunken")
#         video_play_9 = tkinter.Canvas  (video_window_area , bd=1, relief="sunken")
#
#         video_play_1.grid(row=0, column=0,sticky=tkinter.NSEW)
#
#         self.set_video_area(video_play_1,video_play_2,video_play_3,video_play_4,video_play_5,video_play_6,video_play_7,video_play_8,video_play_9)
#
#

