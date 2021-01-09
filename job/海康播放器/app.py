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
from my_tk_登陆修改密码 import tk_login
from threading import Thread


class my_app():
    HK_INI_PATH = './hk.ini'
    DAHUA_INI_PATH = './dahua.ini'
    REC_PATH = os.path.abspath('./rec')

    if not os.path.exists(REC_PATH):
        os.makedirs(REC_PATH)

    def __init__(self):
        self.root = Tk()
        self.root.title('dhplay')
        self.root['bg'] = '#bcbcbc'
        self.root.attributes("-alpha", 0.9)
        self.root.geometry("1080x720")
        self.window_des = [('单窗口', 1), ('四窗口', 4), ('九窗口', 9)]
        self.v_num = IntVar()
        self.v_num.set(1)
        self.is_single_playing = False
        self.now_hwnd = -1
        self.now_window_name = -1
        self.read_hk_servers = self.read_config(self.HK_INI_PATH)
        self.online_hk_servers = {}
        self.offline_hk_servers = {}
        self.read_dahua_servers = self.read_config(self.DAHUA_INI_PATH)
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

        self.list_area = tkinter.Frame(self.root, cursor='cross', bd=3, relief="sunken")

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
                                          class_='window_1', highlightthickness=2)
        self.video_play_2 = tkinter.Frame(self.video_play_area_1, cursor='plus', bd=2, relief="sunken",
                                          class_='window_2', highlightthickness=2)
        self.video_play_3 = tkinter.Frame(self.video_play_area_1, cursor='plus', bd=2, relief="sunken",
                                          class_='window_3', highlightthickness=2)
        self.video_play_4 = tkinter.Frame(self.video_play_area_2, cursor='plus', bd=2, relief="sunken",
                                          class_='window_4', highlightthickness=2)
        self.video_play_5 = tkinter.Frame(self.video_play_area_2, cursor='plus', bd=2, relief="sunken",
                                          class_='window_5', highlightthickness=2)
        self.video_play_6 = tkinter.Frame(self.video_play_area_2, cursor='plus', bd=2, relief="sunken",
                                          class_='window_6', highlightthickness=2)
        self.video_play_7 = tkinter.Frame(self.video_play_area_3, cursor='plus', bd=2, relief="sunken",
                                          class_='window_7', highlightthickness=2)
        self.video_play_8 = tkinter.Frame(self.video_play_area_3, cursor='plus', bd=2, relief="sunken",
                                          class_='window_8', highlightthickness=2)
        self.video_play_9 = tkinter.Frame(self.video_play_area_3, cursor='plus', bd=2, relief="sunken",
                                          class_='window_9', highlightthickness=2)

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
        self.cam_tree.pack(side='top', fill=tkinter.BOTH, expand=tkinter.YES)
        self.cam_tree_scb = ttk.Scrollbar(self.cam_tree, orient="vertical", command=self.cam_tree.yview)
        self.cam_tree_scb.pack(side='right', fill=tkinter.BOTH,expand=tkinter.NO)
        self.cam_tree.configure(yscrollcommand=self.cam_tree_scb.set)
        self.cam_tree.bind("<ButtonPress-1>", self.select_cam)
        self.cam_tree.bind("<Double-Button-1>", self.play_cam)

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

        self.show_cam_tree(event='')

        print('init finished')

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
        for select in self.cam_tree.selection():
            item = self.cam_tree.item(select, "values")
            print(item)  # 输出所选行的第一列的值
        if len(item) ==3 :
            return item
        else:
            return False

        statues,server_desc,channel=item

    def stop_play_cam(self, event):

        window = self.now_window_name
        print(self.window_status)
        if window in self.window_status.keys():
            if self.window_status[window] != 0:
                server, lRealHandle = self.window_status[window]
                server.Stop_Play_Cam(lRealHandle)
                self.window_status[window] = 0
        try:
            event.widget['bg'] = '#acbcbc'
        except:
            pass
        self.video_area.pack_forget()
        self.video_area.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

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
            showwarning(title='warning', message='该窗口已有视频播放,请先停止本窗口播放的视频')
            return

        if 'hk_' in statues:
            print('调用海康播放')
            print(self.online_hk_servers)
            server=self.online_hk_servers[server_desc]['instance']
            lRealHandle = server.Play_Cam(hwnd=self.now_hwnd, channel=int(channel))
            if lRealHandle:

                self.window_status[self.now_window_name] = ('hk',server,channel, lRealHandle)
            else:
                showwarning(message='播放异常，请检查')
            return


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
        try:
            event.widget['bg'] = '#acbcbc'
        except:
            pass
        self.video_area.pack_forget()
        self.video_area.pack(side=tkinter.LEFT, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)

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

    def get_hwnd(self, event):

        # 清除所有视频窗口的颜色
        self.clear_video_window_select_color()
        # 设置选中视频窗格的颜色,刚初始化
        print(self.window_status)
        if self.v_num.get() == 1:
            pass
        else:
            event.widget['highlightbackground'] = 'red'
        # 返回选中视频窗口的句柄
        hwnd = event.widget.winfo_id()
        name = event.widget.winfo_class()
        print('当前窗口的句柄为:', hwnd, name)
        self.now_hwnd = hwnd
        self.now_window_name = name
        return hwnd, name

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
                self.online_dahua_servers[server_desc] = server

    def show_hk_cam_tree(self):
        self.online_hk_tree = self.cam_tree.insert('', '1', text='海康在线', values='hk_online', open=True)
        self.offline_hk_tree = self.cam_tree.insert('', '3', text='海康离线', values='hk_offline', open=True)
        for key in self.online_hk_servers:

            server = self.online_hk_servers[key]
            tree = self.cam_tree.insert(self.online_hk_tree, '1',
                                        text=server['name'] + ' - ' + server['ip'] + ':' + server['port'],
                                        values=server['name'], open=True)

            for channel in server['channel'].keys():
                values = ['hk_online', key, channel]
                self.cam_tree.insert(tree, '1', text=str(str(channel) + ':' + server['channel'][channel]),
                                     values=values)

        for key in self.offline_hk_servers:
            server = self.offline_hk_servers[key]
            tree = self.cam_tree.insert(self.offline_hk_tree, '1',
                                        text=server['name'] + ' - ' + server['ip'] + ':' + server['port'],
                                        values=server['name'], open=True)

            for channel in server['channel'].keys():
                values = ['hk_offline', key, channel]
                self.cam_tree.insert(tree, '1', text=str(str(channel) + ':' + server['channel'][channel]),
                                     values=values)

    def show_dahua_cam_tree(self):
        self.online_dahua_tree = self.cam_tree.insert('', '2', text='大华在线', values='dahua_online', open=True)
        self.offline_dahua_tree = self.cam_tree.insert('', '4', text='大华离线', values='dahua_offline', open=True)
        for key in self.online_dahua_servers:
            server = self.online_dahua_servers[key]
            tree = self.cam_tree.insert(self.online_dahua_tree, '1',
                                        text=server['name'] + ' - ' + server['ip'] + ':' + server['port'],
                                        values=server['name'], open=True)

            for channel in server['channel'].keys():
                values = ['dahua_online', key, channel]
                self.cam_tree.insert(tree, '1', text=str(str(channel) + ':' + server['channel'][channel]),
                                     values=values)

        for key in self.offline_dahua_servers:
            server = self.offline_dahua_servers[key]
            tree = self.cam_tree.insert(self.offline_dahua_tree, '1',
                                        text=server['name'] + ' - ' + server['ip'] + ':' + server['port'],
                                        values=server['name'], open=True)

            for channel in server['channel'].keys():
                values = ['dahua_offline', key, channel]
                self.cam_tree.insert(tree, '1', text=str(str(channel) + ':' + server['channel'][channel]),
                                     values=values)

    def clean_cam_tree(self,event):
        for item in self.cam_tree.get_children():
            self.cam_tree.delete(item)

    def show_cam_tree(self,event):

        def show_hk():
            self.init_hk_dvr()
            self.show_hk_cam_tree()
        def show_dahua():
            self.init_dahua_dvr()
            self.show_dahua_cam_tree()

        self.clean_cam_tree(event='')

        t1=Thread(target=show_hk)
        t2=Thread(target=show_dahua)
        t1.setDaemon(True)
        t2.setDaemon(True)
        t1.start()
        t2.start()

    def check_hk_servers(self):
        new_online=[]
        for key in self.offline_hk_servers:
            server=self.offline_hk_servers[key]
            print(server)
            result=server['instance'].NET_DVR_Login()
            print(result)
            # if result==-1:
            #     continue
            if result>=-1:
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

        print(len(self.online_hk_servers),self.online_hk_servers)
        print(len(self.offline_hk_servers),self.offline_hk_servers)

    def check_servers(self,event):
        self.check_hk_servers()


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

