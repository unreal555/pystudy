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
import ctypes
import tkinter as tk
import re
import configparser
from my_dvr import DVR
from tkinter import ttk
from my_tk_登陆修改密码 import tk_login

    
class my_app():
    REC_PATH=os.path.abspath('./rec')
    if not os.path.exists(REC_PATH):
        os.makedirs(REC_PATH)

    def get_time(self):
        return time.strftime('%Y-%m-%d %H:%M:%S')



    def read_config(self, path=os.path.join('.', 'config.ini')):
        '''
        读取path指定的配置文件，默认为本目录config.ini
        读取section指定的配置段，以字典的形式返回该section的key，value
        '''

        config = configparser.ConfigParser()

        if os.path.exists(path):
            try:
                config.read(path, encoding='gbk')

            except configparser.MissingSectionHeaderError as e:
                print('配置文件无任何section，请检查配置文件')
                return (1)
            except Exception as e:
                print(e)
                print('读取配置文件错误，请检查配置文件')
                return (1)
        else:
            print('未找到配置文件')
            return (1)

        servers = []
        for section in config.sections():
            server = {}
            server['name'] = section
            for item in config.items(section):
                server[item[0]] = item[1]
            servers.append(server)
        print(servers)
        return servers

    def select_cam(self, event):
        print('点击选中cam')
        for item in self.cam_tree.selection():
            item_text = self.cam_tree.item(item, "values")
            print(item_text)  # 输出所选行的第一列的值

    def stop_play_cam(self,event):

        window=self.now_window_name
        print(self.window_status)
        if window in self.window_status.keys():
            if self.window_status[window] != 0:
                server, lRealHandle = self.window_status[window]
                server.Stop_Play_Cam(lRealHandle)
                self.window_status[window]=0
        try:
            event.widget['bg'] = '#acbcbc'
        except:
            pass
        self.video_area.pack_forget()
        self.video_area.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

    def play_cam(self, event):

        print('播放选中cam')
        print(self.window_status)
        for item in self.cam_tree.selection():
            item_text = self.cam_tree.item(item, "values")
            print(item_text)  # 输出所选行的第一列的值
        if len(item_text) == 1:
            print('主机无法播放,请选择通道')
            return
        print('播放', item_text)
        server_ip=item_text[0]
        server_port = item_text[1]
        server_username = item_text[2]
        server_pwd = item_text[3]
        server_channle = int(re.findall('\d+',item_text[4])[0])
        print(server_ip,server_port,server_username,server_pwd,server_channle)

        if len(self.login_servers)==0:
            server = DVR(sDVRIP=server_ip, sDVRPort=server_port, sUserName=server_username,
                         sPassword=server_pwd)
            self.login_servers.append(server)
        else:
            for server in self.login_servers:
                info=server.GetServerInfo()
                if server_ip in info and server_username in info and server_port in info:
                   # print(server_ip,server_username,server_port in info)
                    server=server
                else:
                    server = DVR(sDVRIP=server_ip, sDVRPort=server_port, sUserName=server_username,
                                 sPassword=server_pwd)
                    self.login_servers.append(server)

        print(self.window_status[self.now_window_name]==0)

        if self.window_status[self.now_window_name]==0:

            lRealHandle=server.Play_Cam(hwnd=self.now_hwnd,channle=server_channle)
            self.window_status[self.now_window_name]=(server,lRealHandle)
            return True

        if askokcancel(title='warning',message='该窗口已有视频播放,确定要在该窗口播放吗?'):
            self.stop_play_cam(event=None)
            lRealHandle=server.Play_Cam(hwnd=self.now_hwnd,channle=server_channle)
            self.window_status[self.now_window_name]=(server,lRealHandle)
            return True
        else:
            pass

    def rec_cam(self):
        pass

    def stop_rec_cam(self):
        pass

    def capture_cam(self,event):
        window=self.now_window_name
        print(self.window_status)
        if window in self.window_status.keys():
            if self.window_status[window] != 0:
                server, lRealHandle = self.window_status[window]
                server.Capture_Cam(lRealHandle,os.path.join(self.REC_PATH,self.get_time()+'.bmp'))
                self.window_status[window]=0
        try:
            event.widget['bg'] = '#acbcbc'
        except:
            pass
        self.video_area.pack_forget()
        self.video_area.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

    def clear_video_window_select_color(self):
        self.video_play_1['highlightbackground']= '#bcbcbc'
        self.video_play_2['highlightbackground']= '#bcbcbc'
        self.video_play_3['highlightbackground']= '#bcbcbc'
        self.video_play_4['highlightbackground']= '#bcbcbc'
        self.video_play_5['highlightbackground']= '#bcbcbc'
        self.video_play_6['highlightbackground']= '#bcbcbc'
        self.video_play_7['highlightbackground']= '#bcbcbc'
        self.video_play_8['highlightbackground']= '#bcbcbc'
        self.video_play_9['highlightbackground']= '#bcbcbc'



    def get_hwnd(self,event):

        #清除所有视频窗口的颜色
        self.clear_video_window_select_color()
        #设置选中视频窗格的颜色,刚初始化
        print(self.window_status)
        if self.v_num.get()==1:
            pass
        else:
            event.widget['highlightbackground']='red'
        #返回选中视频窗口的句柄
        hwnd=event.widget.winfo_id()
        name=event.widget.winfo_class()
        print('当前窗口的句柄为:',hwnd,name)
        self.now_hwnd=hwnd
        self.now_window_name=name
        return hwnd,name

    def get_father_widget(self,event):
        return event.widget.nametowidget(event.widget.winfo_parent())

    def show_nine_play(self):



        self.video_play_1['highlightthickness']= 2
        self.video_play_2['highlightthickness']= 2
        self.video_play_3['highlightthickness']= 2
        self.video_play_4['highlightthickness']= 2
        self.video_play_5['highlightthickness']= 2
        self.video_play_6['highlightthickness']= 2
        self.video_play_7['highlightthickness']= 2
        self.video_play_8['highlightthickness']= 2
        self.video_play_9['highlightthickness']= 2

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
        self.video_play_1['highlightthickness'] = 2
        self.video_play_2['highlightthickness'] = 2
        self.video_play_3['highlightthickness'] = 2
        self.video_play_4['highlightthickness'] = 2
        self.video_play_5['highlightthickness'] = 2
        self.video_play_6['highlightthickness'] = 2
        self.video_play_7['highlightthickness'] = 2
        self.video_play_8['highlightthickness'] = 2
        self.video_play_9['highlightthickness'] = 2
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

            event.widget['highlightthickness']=0
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

      #  print(self.v_num.get(),self.is_single_playing)

        if self.v_num.get()==9:

            self.show_nine_play()

        if self.v_num.get() == 4:

            self.show_four_play()

        if self.v_num.get() == 1:

            self.show_single_play(event=None)


    def __init__(self):
        self.root = Tk()
        self.root.title('dhplay')
        self.root['bg'] = '#bcbcbc'
        self.root.attributes("-alpha", 0.9)
        self.root.geometry("1080x720")
        self.window_des = [('单窗口', 1), ('四窗口', 4), ('九窗口', 9)]
        self.v_num = ''
        self.is_single_playing = False
        self.now_hwnd = -1
        self.now_window_name = -1
        self.login_servers = []
        self.window_status = {
            'window_1': 0,
            'window_2': 0,
            'window_3': 0,
            'window_4': 0,
            'window_5': 0,
            'window_6': 0,
            'window_7': 0,
            'window_8': 0,
            'window_9': 0,
        }
        self.rec_status = []
        self.list_area=tkinter.Frame(self.root,cursor='cross' ,bd=3, relief="sunken")

        self.video_area=tkinter.Frame(self.root ,bd=1, relief="sunken")

        self.list_area.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.video_area.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)


        self.video_play_area=tkinter.Frame(self.video_area ,bd=1, relief="sunken")

        self.video_control_area=tkinter.Frame(self.video_area, bd=1, relief="sunken")

        self.video_play_area.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

        self.video_control_area.pack(side=tkinter.BOTTOM, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.video_play_area_1=tkinter.Frame(self.video_play_area ,bd=1, relief="sunken")
        self.video_play_area_2=tkinter.Frame(self.video_play_area ,bd=1, relief="sunken")
        self.video_play_area_3=tkinter.Frame(self.video_play_area ,bd=1, relief="sunken")

        self.video_play_1 = tkinter.Frame(self.video_play_area_1 , cursor='plus',bd=2, relief="sunken",class_='window_1',highlightthickness=2)
        self.video_play_2 = tkinter.Frame(self.video_play_area_1 , cursor='plus',bd=2, relief="sunken",class_='window_2',highlightthickness=2)
        self.video_play_3 = tkinter.Frame(self.video_play_area_1 , cursor='plus',bd=2, relief="sunken",class_='window_3',highlightthickness=2)
        self.video_play_4 = tkinter.Frame(self.video_play_area_2 , cursor='plus',bd=2, relief="sunken",class_='window_4',highlightthickness=2)
        self.video_play_5 = tkinter.Frame(self.video_play_area_2 , cursor='plus',bd=2, relief="sunken",class_='window_5',highlightthickness=2)
        self.video_play_6 = tkinter.Frame(self.video_play_area_2 , cursor='plus',bd=2, relief="sunken",class_='window_6',highlightthickness=2)
        self.video_play_7 = tkinter.Frame(self.video_play_area_3 , cursor='plus',bd=2, relief="sunken",class_='window_7',highlightthickness=2)
        self.video_play_8 = tkinter.Frame(self.video_play_area_3 , cursor='plus',bd=2, relief="sunken",class_='window_8',highlightthickness=2)
        self.video_play_9 = tkinter.Frame(self.video_play_area_3 , cursor='plus',bd=2, relief="sunken",class_='window_9',highlightthickness=2)

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

        self.cam_tree = ttk.Treeview(self.list_area, selectmode='browse')
        self.cam_tree.pack(side='left',fill=tkinter.BOTH)
        self.cam_tree_scb = ttk.Scrollbar(self.list_area, orient="vertical", command=self.cam_tree.yview)
        self.cam_tree_scb.pack(side='right', fill=tkinter.BOTH)
        self.cam_tree.configure(yscrollcommand=self.cam_tree_scb.set)

        for server in self.read_config():
            tree = self.cam_tree.insert('', '1', text=server['name'] + ' - ' + server['ip'] + ':' + server['port'],values=server['name'])
            for key in server.keys():
                if 'channle' in key:
                    values = (server['ip'], server['port'], server['user_name'], server['pwd'], key)
                    self.cam_tree.insert(tree, '1', text=key.replace('channle_', '') + server[key], values=values)
        self.cam_tree.bind("<ButtonPress-1>", self.select_cam)
        self.cam_tree.bind("<Double-Button-1>", self.play_cam)

        self.v_num = IntVar()
        self.v_num.set(1)

        for lang, num in self.window_des:
            self.b = Radiobutton(self.video_control_area, text=lang, variable=self.v_num, value=num,indicatoron=False,command=self.show_window)
            self.b.pack(side=tkinter.RIGHT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.show_window()

        self.stop_button=tkinter.Button(self.video_control_area,text='停止')
        self.stop_button.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
        self.stop_button.bind("<ButtonPress-1>", self.stop_play_cam)

        self.capture_button=tkinter.Button(self.video_control_area,text='截图')
        self.capture_button.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
        self.capture_button.bind("<ButtonPress-1>", self.capture_cam)
        # self.play_button=tkinter.Button(self.video_control_area,text='播放')
        # self.play_button.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
        #
        # self.speedup_button=tkinter.Button(self.video_control_area,text='加速')
        # self.speedup_button.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
        #
        # self.pause_button=tkinter.Button(self.video_control_area,text='暂停')
        # self.pause_button.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)


        self.now_hwnd = self.video_play_1.winfo_id()

        self.now_window_name=self.video_play_1.winfo_class()

        print('init finished')

    def __del__(self):
        print('程序退出,销毁')

        for server in self.login_servers:
            server.Close()
        self.window_des=0
        self.v_num=0
        self.is_single_playing=0
        self.now_hwnd=0
        self.login_servers=0
        self.root=0



def start():

    app=my_app()
    app.root.mainloop()

login=tk_login(my_func=start)
login.main_window.mainloop()



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

