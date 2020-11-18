
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

class tk_nine_windows():


    def set_window_clolor(self,event):
        if self.is_single_playing==TRUE:
            return
        self.video_play_1['highlightbackground']= self.default_color
        self.video_play_2['highlightbackground']= self.default_color
        self.video_play_3['highlightbackground']= self.default_color
        self.video_play_4['highlightbackground']= self.default_color
        self.video_play_5['highlightbackground']= self.default_color
        self.video_play_6['highlightbackground']= self.default_color
        self.video_play_7['highlightbackground']= self.default_color
        self.video_play_8['highlightbackground']= self.default_color
        self.video_play_9['highlightbackground']= self.default_color
        #设置选中视频窗格的颜色,刚初始化
        print(self.window_status)
        if self.v_num.get()==1:
            pass
        else:
            event.widget['highlightbackground']='red'

    def get_hwnd(self,event):
        self.set_window_clolor(event)
        print(event.widget.winfo_id())
        print(event.widget.winfo_class())

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
        self.video_play_1['highlightbackground']= self.default_color
        self.video_play_2['highlightbackground']= self.default_color
        self.video_play_3['highlightbackground']= self.default_color
        self.video_play_4['highlightbackground']= self.default_color
        self.video_play_5['highlightbackground']= self.default_color
        self.video_play_6['highlightbackground']= self.default_color
        self.video_play_7['highlightbackground']= self.default_color
        self.video_play_8['highlightbackground']= self.default_color
        self.video_play_9['highlightbackground']= self.default_color
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

    def login(self):
        print(1)

        return False

    def __init__(self):
        self.default_color = '#acbcbc'
        self.root = Tk()
        self.root.title('test')
        self.root['bg'] = self.default_color
        self.root.attributes("-alpha", 0.9)
        self.root.geometry("1080x720")
        self.window_des = [('单窗口', 1), ('四窗口', 4), ('九窗口', 9)]
        self.v_num = ''
        self.is_single_playing = False

        self.window_status = {
            'window_1': '',
            'window_2': '',
            'window_3': '',
            'window_4': '',
            'window_5': '',
            'window_6': '',
            'window_7': '',
            'window_8': '',
            'window_9': '',
        }

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

        self.video_play_1 = tkinter.Frame(self.video_play_area_1 , cursor='plus',bd=2, relief="sunken",highlightthickness=1,takefocus=True,class_='window_1')
        self.video_play_2 = tkinter.Frame(self.video_play_area_1 , cursor='plus',bd=2, relief="sunken",highlightthickness=1,takefocus=True,class_='window_2')
        self.video_play_3 = tkinter.Frame(self.video_play_area_1 , cursor='plus',bd=2, relief="sunken",highlightthickness=1,takefocus=True,class_='window_3')
        self.video_play_4 = tkinter.Frame(self.video_play_area_2 , cursor='plus',bd=2, relief="sunken",highlightthickness=1,takefocus=True,class_='window_4')
        self.video_play_5 = tkinter.Frame(self.video_play_area_2 , cursor='plus',bd=2, relief="sunken",highlightthickness=1,takefocus=True,class_='window_5')
        self.video_play_6 = tkinter.Frame(self.video_play_area_2 , cursor='plus',bd=2, relief="sunken",highlightthickness=1,takefocus=True,class_='window_6')
        self.video_play_7 = tkinter.Frame(self.video_play_area_3 , cursor='plus',bd=2, relief="sunken",highlightthickness=1,takefocus=True,class_='window_7')
        self.video_play_8 = tkinter.Frame(self.video_play_area_3 , cursor='plus',bd=2, relief="sunken",highlightthickness=1,takefocus=True,class_='window_8')
        self.video_play_9 = tkinter.Frame(self.video_play_area_3 , cursor='plus',bd=2, relief="sunken",highlightthickness=1,takefocus=True,class_='window_9')
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

if __name__ == '__main__':
    app=tk_nine_windows()
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
#
#
# frame cursor style
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
#
