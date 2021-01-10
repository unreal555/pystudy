# Team : JiaLiDun University
# Author：zl
# Date ：2020/9/30 0030 上午 9:39
# Tool ：PyCharm


from tkinter import *
from tkinter.messagebox import *
import tkinter
import time
import os
from tkinter.filedialog import askopenfilename
import ctypes
import tkinter as tk
import re
import configparser
from my_hk_dvr import HK_DVR
from tkinter import ttk
from my_tk_login import tk_login
from threading import Thread

HK_INI_PATH = './hk.ini'
DAHUA_INI_PATH = './dahua.ini'
REC_PATH = os.path.abspath('./rec')
default_color = '#bcbcbc'
video_default_color='#acbcbc'


class my_app():


    if not os.path.exists(REC_PATH):
        os.makedirs(REC_PATH)

    def __init__(self):
        self.root = Tk()
        self.root.title('Player')


        self.root['bg'] = default_color
        self.root.attributes("-alpha", 0.9)

        #self.root.overrideredirect(True)
        self.root.geometry("1080x720")
        self.root.state("zoomed")


        self.window_des = [('单窗口', 1), ('四窗口', 4), ('九窗口', 9)]

        self.v_num = IntVar()
        self.v_num.set(1)

        self.info=StringVar()
        self.info.set('初始化中......')

        self.is_single_playing = False

        self.now_hwnd = -1
        self.now_window_name = -1
        self.now_window_widget=-1

        self.read_hk_servers = self.read_config(HK_INI_PATH)
        self.online_hk_servers = {}
        self.offline_hk_servers = {}
        self.read_dahua_servers = self.read_config(DAHUA_INI_PATH)
        self.online_dahua_servers = {}
        self.offline_dahua_servers = {}

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

        self.list_area = tkinter.Frame(self.root,  bd=3, relief="sunken")

        self.video_area = tkinter.Frame(self.root, bd=1, relief="sunken")

        self.list_area.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.video_area.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

        self.video_play_area = tkinter.Frame(self.video_area, bd=1, relief="sunken")

        self.video_control_area = tkinter.Frame(self.video_area, bd=1, relief="sunken")

        self.video_play_area.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

        self.video_control_area.pack(side=tkinter.BOTTOM, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.video_play_area_1 = tkinter.Frame(self.video_play_area, bd=1, relief="sunken")
        self.video_play_area_2 = tkinter.Frame(self.video_play_area, bd=1, relief="sunken")
        self.video_play_area_3 = tkinter.Frame(self.video_play_area, bd=1, relief="sunken")

        self.video_play_1 = tkinter.Frame(self.video_play_area_1, cursor='plus', bd=2, relief="sunken",
                                          class_='window_1', highlightthickness=2,bg=video_default_color)
        self.video_play_2 = tkinter.Frame(self.video_play_area_1, cursor='plus', bd=2, relief="sunken",
                                          class_='window_2', highlightthickness=2,bg=video_default_color)
        self.video_play_3 = tkinter.Frame(self.video_play_area_1, cursor='plus', bd=2, relief="sunken",
                                          class_='window_3', highlightthickness=2,bg=video_default_color)
        self.video_play_4 = tkinter.Frame(self.video_play_area_2, cursor='plus', bd=2, relief="sunken",
                                          class_='window_4', highlightthickness=2,bg=video_default_color)
        self.video_play_5 = tkinter.Frame(self.video_play_area_2, cursor='plus', bd=2, relief="sunken",
                                          class_='window_5', highlightthickness=2,bg=video_default_color)
        self.video_play_6 = tkinter.Frame(self.video_play_area_2, cursor='plus', bd=2, relief="sunken",
                                          class_='window_6', highlightthickness=2,bg=video_default_color)
        self.video_play_7 = tkinter.Frame(self.video_play_area_3, cursor='plus', bd=2, relief="sunken",
                                          class_='window_7', highlightthickness=2,bg=video_default_color)
        self.video_play_8 = tkinter.Frame(self.video_play_area_3, cursor='plus', bd=2, relief="sunken",
                                          class_='window_8', highlightthickness=2,bg=video_default_color)
        self.video_play_9 = tkinter.Frame(self.video_play_area_3, cursor='plus', bd=2, relief="sunken",
                                          class_='window_9', highlightthickness=2,bg=video_default_color)

        self.video_play_1.bind("<ButtonPress-1>", self.set_select_window_info)
        self.video_play_2.bind("<ButtonPress-1>", self.set_select_window_info)
        self.video_play_3.bind("<ButtonPress-1>", self.set_select_window_info)
        self.video_play_4.bind("<ButtonPress-1>", self.set_select_window_info)
        self.video_play_5.bind("<ButtonPress-1>", self.set_select_window_info)
        self.video_play_6.bind("<ButtonPress-1>", self.set_select_window_info)
        self.video_play_7.bind("<ButtonPress-1>", self.set_select_window_info)
        self.video_play_8.bind("<ButtonPress-1>", self.set_select_window_info)
        self.video_play_9.bind("<ButtonPress-1>", self.set_select_window_info)
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
        self.cam_tree.pack(side='top', fill=tkinter.BOTH, expand=tkinter.YES)


        self.cam_tree.bind("<ButtonPress-1>", self.select_cam)
        self.cam_tree.bind("<Double-Button-1>", self.play_cam)

        self.cam_tree_scb_y = ttk.Scrollbar(self.cam_tree, orient='vertical', command=self.cam_tree.yview)
        self.cam_tree_scb_y.pack(side='right', fill=tkinter.BOTH,expand=tkinter.NO)
        self.cam_tree.configure(yscrollcommand=self.cam_tree_scb_y.set,)

        self.cam_tree_scb_x = ttk.Scrollbar(self.cam_tree, orient=str.lower('HORIZONTAL'), command=self.cam_tree.xview)
        self.cam_tree_scb_x.pack(side='bottom', fill=tkinter.BOTH,expand=tkinter.NO)
        self.cam_tree.configure(yscrollcommand=self.cam_tree_scb_x.set)

        self.refresh_button = tkinter.Button(self.list_area, width=20,text='刷新服务器')
        self.refresh_button.pack(side='bottom', fill=tkinter.BOTH, expand=tkinter.NO)
        self.refresh_button.bind("<ButtonPress-1>", self.check_servers)

        for lang, num in self.window_des:
            self.b = Radiobutton(self.video_control_area, text=lang, variable=self.v_num, value=num, indicatoron=False,
                                 command=self.show_window)
            self.b.pack(side=tkinter.RIGHT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.show_window()

        self.stop_button = tkinter.Button(self.video_control_area, text='停止')
        self.stop_button.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
        self.stop_button.bind("<ButtonPress-1>", self.stop_play_cam)

        self.capture_button = tkinter.Button(self.video_control_area, text='截图')
        self.capture_button.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
        self.capture_button.bind("<ButtonPress-1>", self.capture_cam)

        self.play_button = tkinter.Button(self.video_control_area, text='播放')
        self.play_button.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.speedup_button = tkinter.Button(self.video_control_area, text='加速')
        self.speedup_button.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.pause_button = tkinter.Button(self.video_control_area, text='暂停')
        self.pause_button.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)

        self.now_hwnd = self.video_play_1.winfo_id()

        self.now_window_name = self.video_play_1.winfo_class()

        self.now_window_widget = self.video_play_1

        self.init_cam_tree(event='')

        self.scale_bar = tkinter.Scale(self.video_control_area, from_=20 ,to=100, orient=tkinter.HORIZONTAL, showvalue=0, borderwidth=0.01,
                                 repeatinterval=5, font=('宋体', 8),
                                 sliderlength=10,resolution=0.1)#tickinterval=5  刻度


        self.label_info= tk.Label(self.video_control_area,textvariable=self.info,width=60)  #anchor='w' ,justify='left',
        self.label_info.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)



        self.scale_bar.set(90)
        self.scale_bar.bind("<ButtonPress-1>", self.scale_mouse_move)
        self.scale_bar.bind("<ButtonRelease-1>", self.scale_mouse_move)
        self.scale_bar.bind('<B1-Motion> ', self.scale_mouse_move)
        self.scale_bar.pack(side=tkinter.BOTTOM, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

        print('init finished')

    def scale_mouse_move(self,event):
        print(event.x_root,event.y_root)
        # print(self.scale_bar.location())
        self.root.attributes("-alpha", self.scale_bar.get()/100)

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
                showwarning(message='配置文件无任何section，请检查配置文件')
                return []

            except Exception as e:
                showwarning(message=str(e))
                return []


        else:
            print('未找到配置文件')
            return []

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
        print('鼠标单击选中cam')
        print(self.window_status)
        if self.cam_tree.selection()==():
            return
        for select in self.cam_tree.selection():
            item = self.cam_tree.item(select, "values")
            print(item)  # 输出所选行的第一列的值

        if len(item) ==3:
            return item




    def stop_play_cam(self, event):

        def do():

            if self.now_window_name==-1 or self.now_window_name==-1 or self.now_window_widget==-1:
                showwarning(message='请先选择一个播放窗口')
                return

            if self.window_status[self.now_window_name]==0:
                showwarning(message='窗口空闲，没有可停止的对象')
                return


            if self.window_status[self.now_window_name] != 0:
                server_type,server,channel,cam_handle = self.window_status[self.now_window_name]
                print(server)
                server.Stop_Play_Cam(cam_handle)
                self.window_status[self.now_window_name] = 0
                self.now_window_widget['bg']=video_default_color

        t=Thread(target=do)
        t.setDaemon(True)
        t.start()



    def play_cam(self, event):

        print('播放选中cam')
        print(self.window_status)
        for select in self.cam_tree.selection():
            item = self.cam_tree.item(select, "values")
            print(item)  # 输出所选行的第一列的值
        if len(item) == 1:
            print('主机无法播放,请选择通道')
            return
        print('播放', item)

        statues,server_desc,channel=item

        if 'offline' in statues:
            showwarning(message='服务器不在线，请刷新服务器')
            return

        if self.window_status[self.now_window_name]!=0:
            print(self.window_status[self.now_window_name])
            showwarning(title='warning', message='该窗口已有视频播放,请先停止本窗口播放的视频')
            return

        if 'hk_' in statues:
            print('调用海康播放')
            print(self.online_hk_servers)
            server=self.online_hk_servers[server_desc]['instance']

            for  window_name  in self.window_status.keys():
                value=self.window_status[window_name]
                if isinstance(value,int):
                    continue
                if server in value  and 'hk' in value  and channel in value:
                    showwarning(message='本cam已在 {} 中播放'.format(window_name))
                    return

            lRealHandle = server.Play_Cam(hwnd=self.now_hwnd, channel=int(channel))
            if lRealHandle==-1:
                showwarning(message='播放异常，请检查')
                return
            if lRealHandle>=0:
                self.window_status[self.now_window_name] = ('hk',server,channel, lRealHandle)


        if 'dahua_' in statues:
            print('调用大华播放')
            return

    def rec_cam(self):
        pass

    def stop_rec_cam(self):
        pass

    def capture_cam(self, event):
        window = self.now_window_name
        print(self.window_status)
        if window in self.window_status.keys():
            if self.window_status[window] != 0:
                server, lRealHandle = self.window_status[window]
                server.Capture_Cam(lRealHandle, os.path.join(self.REC_PATH, self.get_time() + '.bmp'))
                self.window_status[window] = 0
        # try:
        #     event.widget['bg'] = '#acbcbc'
        # except:
        #     pass
        # self.video_area.pack_forget()
        # self.video_area.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

    def clear_video_window_select_color(self):
        self.video_play_1['highlightbackground'] = '#bcbcbc'
        self.video_play_2['highlightbackground'] = '#bcbcbc'
        self.video_play_3['highlightbackground'] = '#bcbcbc'
        self.video_play_4['highlightbackground'] = '#bcbcbc'
        self.video_play_5['highlightbackground'] = '#bcbcbc'
        self.video_play_6['highlightbackground'] = '#bcbcbc'
        self.video_play_7['highlightbackground'] = '#bcbcbc'
        self.video_play_8['highlightbackground'] = '#bcbcbc'
        self.video_play_9['highlightbackground'] = '#bcbcbc'

    def set_select_window_info(self, event):

        # 清除所有视频窗口的颜色
        self.clear_video_window_select_color()
        # 设置选中视频窗格的颜色,刚初始化
        if self.v_num.get() == 1:
            pass
        else:
            event.widget['highlightbackground'] = 'red'
        # 设置选中视频窗口的句柄
        self.now_hwnd = event.widget.winfo_id()
        self.now_window_name  = event.widget.winfo_class()
        self.now_window_widget=event.widget

        print('当前窗口的句柄,name,widget:', self.now_hwnd,self.now_window_name,self.now_window_widget)
        print('当前窗口的状态为：',self.window_status[self.now_window_name])
        
        self.info.set('当前窗口为 {} {}'.format(self.now_window_name,self.window_status[self.now_window_name]))

    def get_father_widget(self, event):
        return event.widget.nametowidget(event.widget.winfo_parent())

    def show_nine_play(self):

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

    def show_single_play(self, event):
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
        if event == None:
            self.video_play_area_1.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
            self.video_play_1.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        else:

            event.widget['highlightthickness'] = 0
            father_frame = event.widget.nametowidget(event.widget.winfo_parent())
            father_frame.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
            event.widget.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        self.is_single_playing = True

    def change_window(self, event):
        print(event, self.v_num.get(), self.is_single_playing)
        if self.v_num.get == 1:
            pass
        if self.is_single_playing == False and self.v_num.get() == 9:
            self.show_single_play(event)
        elif self.is_single_playing == True and self.v_num.get() == 9:
            self.show_nine_play()
        elif self.is_single_playing == False and self.v_num.get() == 4:
            self.show_single_play(event)
        elif self.is_single_playing == True and self.v_num.get() == 4:
            self.show_four_play()

    def show_window(self):

        #  print(self.v_num.get(),self.is_single_playing)

        if self.v_num.get() == 9:
            self.show_nine_play()

        if self.v_num.get() == 4:
            self.show_four_play()

        if self.v_num.get() == 1:
            self.show_single_play(event=None)

    def init_hk_dvr(self):
        for item in self.read_hk_servers:
            print('登陆海康{}'.format(item))
            server = {}
            server['name'] = item['name']
            server['ip'] = item['ip']
            server['port'] = item['port']
            server['user_name'] = item['user_name']
            server['pwd'] = item['pwd']
            server['type']='hk'
            server['channel'] = {}
            for key in item.keys():
                result = re.findall('channel_(\d+)', str.lower(key.replace(' ', '')))
                if len(result) == 1:
                    result = result[0]
                    server['channel'][result] = item[key]
            server_desc = server['ip'] + ':' + server['port'] + ':' + server['user_name']

            if (server_desc in self.online_hk_servers.keys()) or (server_desc in self.offline_hk_servers.keys()):
                showwarning(message='大华配置文件中存在重复的主机，请检查配置文件，将同一主机的cam放在一起')
                return


            instance = HK_DVR(sDVRIP=server['ip'], sDVRPort=server['port'], sUserName=server['user_name'],
                           sPassword=server["pwd"])
            if instance.lUserID == -1:
                server['instance'] = instance
                self.offline_hk_servers[server_desc] = server
            if instance.lUserID >= 0:
                server['instance'] = instance
                self.online_hk_servers[server_desc] = server


    def init_dahua_dvr(self):

        for item in self.read_dahua_servers:
            print('登陆大华{}'.format(item))
            server = {}
            server['name'] = item['name']
            server['ip'] = item['ip']
            server['port'] = item['port']
            server['user_name'] = item['user_name']
            server['pwd'] = item['pwd']
            server['type']='dahua'
            server['channel'] = {}
            for key in item.keys():
                result = re.findall('channel_(\d+)', str.lower(key.replace(' ', '')))

                if len(result) == 1:
                    result = result[0]
                    server['channel'][result] = item[key]
            server_desc = server['ip'] + ':' + server['port'] + ':' + server['user_name']
            instance =HK_DVR(sDVRIP=server['ip'], sDVRPort=server['port'], sUserName=server['user_name'],
                           sPassword=server["pwd"])
            if instance.lUserID == -1:
                server['instance'] = instance
                self.offline_dahua_servers[server_desc] = server
            if instance.lUserID >= 0:
                server['instance'] = instance
                self.online_dahua_servers[server_desc] = server


    def show_cam_tree(self):

        self.clean_cam_tree(event='')

        if len(self.online_hk_servers)!=0:
            self.online_hk_tree = self.cam_tree.insert('', '0', text='海康在线', values='hk_online', open=True)
            for key in self.online_hk_servers:
                server = self.online_hk_servers[key]
                tree = self.cam_tree.insert(self.online_hk_tree, '1',
                                            text=server['name'] + ' - ' + server['ip'] + ':' + server['port'],
                                            values=server['name'], open=True)
                for channel in server['channel'].keys():
                    values = ['hk_online', key, channel]
                    self.cam_tree.insert(tree, '1', text=str(str(channel) + ':' + server['channel'][channel]),
                                         values=values)

        if len(self.online_dahua_servers)!=0:
            self.online_dahua_tree = self.cam_tree.insert('', '1', text='大华在线', values='dahua_online', open=True)
            for key in self.online_dahua_servers:
                server = self.online_dahua_servers[key]
                tree = self.cam_tree.insert(self.online_dahua_tree, '1',
                                            text=server['name'] + ' - ' + server['ip'] + ':' + server['port'],
                                            values=server['name'], open=True)
                for channel in server['channel'].keys():
                    values = ['dahua_online', key, channel]
                    self.cam_tree.insert(tree, '1', text=str(str(channel) + ':' + server['channel'][channel]),
                                         values=values)

        self.fengexian = self.cam_tree.insert('', '2', text=' '*20, values='fengge', open=True)
        self.fengexian = self.cam_tree.insert('', '3', text='*'*20, values='fengge', open=True)
        self.fengexian = self.cam_tree.insert('', '4', text=' '*20, values='fengge', open=True)

        if len(self.offline_hk_servers)!=0:
            self.offline_hk_tree = self.cam_tree.insert('', '7', text='海康离线', values='hk_offline', open=True)
            for key in self.offline_hk_servers:
                server = self.offline_hk_servers[key]
                tree = self.cam_tree.insert(self.offline_hk_tree, '1',
                                            text=server['name'] + ' - ' + server['ip'] + ':' + server['port'],
                                            values=server['name'], open=False)
                for channel in server['channel'].keys():
                    values = ['hk_offline', key, channel]
                    self.cam_tree.insert(tree, '1', text=str(str(channel) + ':' + server['channel'][channel]),
                                         values=values)

        if len(self.offline_dahua_servers)!=0:
            self.offline_dahua_tree = self.cam_tree.insert('', '8', text='大华离线', values='dahua_offline', open=True)
            for key in self.offline_dahua_servers:
                server = self.offline_dahua_servers[key]
                tree = self.cam_tree.insert(self.offline_dahua_tree, '1',
                                            text=server['name'] + ' - ' + server['ip'] + ':' + server['port'],
                                            values=server['name'], open=False)
                for channel in server['channel'].keys():
                    values = ['dahua_offline', key, channel]
                    self.cam_tree.insert(tree, '1', text=str(str(channel) + ':' + server['channel'][channel]),
                                         values=values)



    def clean_cam_tree(self,event):
        for item in self.cam_tree.get_children():
            self.cam_tree.delete(item)

    def init_cam_tree(self,event):

        def do():
            self.info.set('连接视频服务器中......')
            t1 = Thread(target=self.init_hk_dvr)
            t2 = Thread(target=self.init_dahua_dvr)
            t3 = Thread(target=self.show_cam_tree)
            t1.setDaemon(True)
            t2.setDaemon(True)
            t1.start()
            t2.start()
            while 1:
                if t1.is_alive() or t2.is_alive():
                    pass
                else:
                    t3.start()
                    self.info.set('初始化完毕')
                    break


        t=Thread(target=do)
        t.start()



    def check_hk_servers(self):
        new_online=[]
        for key in self.offline_hk_servers:
            server=self.offline_hk_servers[key]
            result=server['instance'].NET_DVR_Login()
            if result==-1:
                continue
            if result>=0:
                new_online.append([key,{key:server}])
        for key,item in new_online:
            self.online_hk_servers.update(item)
            self.offline_hk_servers.pop(key)

        print(len(self.online_hk_servers),self.online_hk_servers)
        print(len(self.offline_hk_servers),self.offline_hk_servers)

        new_offline=[]
        for key in self.online_hk_servers:
            server=self.online_hk_servers[key]
            if server['instance'].check_device_online()==False:
                new_offline.append([key,{key:server}])
        for key,server in new_offline:
            self.offline_hk_servers.update(server)
            self.online_hk_servers.pop(key)

        if new_offline!=[] or new_online!=[]:
            self.show_cam_tree()


        print(len(self.online_hk_servers),self.online_hk_servers)
        print(len(self.offline_hk_servers),self.offline_hk_servers)



    def check_servers(self,event):
        t1=Thread(target=self.check_hk_servers)
        t1.setDaemon(True)
        t1.start()

    def __del__(self):
        print('程序退出,销毁')
        for key in self.online_hk_servers:
            self.online_hk_servers[key]['instance'].Close()
        for key in self.offline_hk_servers:
            self.offline_hk_servers[key]['instance'].Close()

        for key in self.online_dahua_servers:
            self.online_dahua_servers[key]['instance'].Close()
        for key in self.offline_dahua_servers:
            self.offline_dahua_servers[key]['instance'].Close()

        self.window_des = 0
        self.v_num = 0
        self.is_single_playing = 0
        self.now_hwnd = 0
        self.login_servers = 0
        self.root = 0


def start():
    app = my_app()
    app.root.mainloop()


# login=tk_login(my_func=start)
# login.main_window.mainloop()
start()



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

