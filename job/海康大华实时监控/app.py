
# ﻿ Team : JiaLiDun University
# Author：zl
# Date ：2020/9/30 0030 上午 9:39
# Tool ：PyCharm
import time
import os
import pickle
from threading import Thread

import configparser

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

from my_hk_dvr import HK_DVR
from my_dh_dvr import DAHUA_DVR
from my_icon import set_icon

# from my_tk_login import tk_login


HK_INI_PATH = './hk.ini'
DAHUA_INI_PATH = './dahua.ini'
REC_PATH = './rec'
DAT_PATH = './dat'
DEFAULT_COLOR = '#bcbcbc'
VIDEO_DEFAULT_COLOR = '#acbcbc'
FONT_COLOR='black'
REFRESH_TIME=600


class my_app():
	if not os.path.exists(DAT_PATH):
		os.makedirs(DAT_PATH)

	if not os.path.exists(REC_PATH):
		os.makedirs(REC_PATH)

	def __init__(self):
		self.root = Tk()
		set_icon(self.root)
		self.root.title('Player')
		self.root['bd']=0
		self.root['bg'] = DEFAULT_COLOR
		self.root.attributes("-alpha", 0.9)
		#self.root.resizable(0, 0)  # 设置窗口大小不可变
		self.root.overrideredirect()
		max_x,max_y=self.root.maxsize()
		self.root.geometry("%sx%s+%s+%s"%(int(max_x*0.9),int(max_y*0.9),int(max_x*0.05),int(max_y*0.02)))

		self.float_window = tk.Toplevel(self.root)
		self.float_window.geometry('1x1')
		self.float_label=tk.Label(self.float_window,text='')
		self.float_window.attributes("-alpha", 0.7)  # 透明度(0.0~1.0)
		self.float_window.overrideredirect(True)  # 去除窗口边框
		self.float_window.attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
		self.float_window.attributes("-topmost", True)


		self.window_des = [('单窗口', 1), ('四窗口', 4), ('九窗口', 9)]

		self.v_num = IntVar()

		self.info = StringVar()
		self.info.set('初始化中......')

		self.is_single_playing = False

		self.now_hwnd = -1
		self.now_window_name = -1
		self.now_window_widget = -1

		self.closing_flag = False

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

		self.list_area = tk.Frame(self.root, bd=0, relief="sunken")

		self.hide_area = tk.Frame(self.root, bd=0, relief="sunken")

		self.video_area = tk.Frame(self.root, bd=0, relief="sunken")

		self.video_area.pack(side=tk.RIGHT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)

		self.hide_area.pack(side=tk.RIGHT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

		self.list_area.pack(side=tk.RIGHT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

		self.video_play_area = tk.Frame(self.video_area, bd=0, relief="sunken")

		self.video_control_area = tk.Frame(self.video_area, bd=0, relief="sunken")

		self.video_play_area.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)

		self.video_control_area.pack(side=tk.BOTTOM, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

		self.video_play_area_1 = tk.Frame(self.video_play_area, bd=0, relief="sunken")
		self.video_play_area_2 = tk.Frame(self.video_play_area, bd=0, relief="sunken")
		self.video_play_area_3 = tk.Frame(self.video_play_area, bd=0, relief="sunken")

		self.video_play_1 = tk.Frame(self.video_play_area_1, cursor='plus', bd=1, relief="sunken",
		                             class_='window_1', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_2 = tk.Frame(self.video_play_area_1, cursor='plus', bd=1, relief="sunken",
		                             class_='window_2', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_3 = tk.Frame(self.video_play_area_1, cursor='plus', bd=1, relief="sunken",
		                             class_='window_3', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_4 = tk.Frame(self.video_play_area_2, cursor='plus', bd=1, relief="sunken",
		                             class_='window_4', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_5 = tk.Frame(self.video_play_area_2, cursor='plus', bd=1, relief="sunken",
		                             class_='window_5', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_6 = tk.Frame(self.video_play_area_2, cursor='plus', bd=1, relief="sunken",
		                             class_='window_6', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_7 = tk.Frame(self.video_play_area_3, cursor='plus', bd=1, relief="sunken",
		                             class_='window_7', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_8 = tk.Frame(self.video_play_area_3, cursor='plus', bd=1, relief="sunken",
		                             class_='window_8', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_9 = tk.Frame(self.video_play_area_3, cursor='plus', bd=1, relief="sunken",
		                             class_='window_9', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)


		self.video_play_1.bind('<Motion>',self.on_mouse_move_in_area)
		self.video_play_1.bind('<Leave>', self.on_mouse_move_out_area)

		self.video_play_2.bind('<Motion>',self.on_mouse_move_in_area)
		self.video_play_2.bind('<Leave>', self.on_mouse_move_out_area)

		self.video_play_3.bind('<Motion>',self.on_mouse_move_in_area)
		self.video_play_3.bind('<Leave>', self.on_mouse_move_out_area)

		self.video_play_4.bind('<Motion>',self.on_mouse_move_in_area)
		self.video_play_4.bind('<Leave>', self.on_mouse_move_out_area)

		self.video_play_5.bind('<Motion>',self.on_mouse_move_in_area)
		self.video_play_5.bind('<Leave>', self.on_mouse_move_out_area)

		self.video_play_6.bind('<Motion>',self.on_mouse_move_in_area)
		self.video_play_6.bind('<Leave>', self.on_mouse_move_out_area)

		self.video_play_7.bind('<Motion>',self.on_mouse_move_in_area)
		self.video_play_7.bind('<Leave>', self.on_mouse_move_out_area)

		self.video_play_8.bind('<Motion>',self.on_mouse_move_in_area)
		self.video_play_8.bind('<Leave>', self.on_mouse_move_out_area)

		self.video_play_9.bind('<Motion>',self.on_mouse_move_in_area)
		self.video_play_9.bind('<Leave>', self.on_mouse_move_out_area)

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
		self.cam_tree.pack(side='top', fill=tk.BOTH, expand=tk.YES)

		self.cam_tree.bind("<ButtonPress-1>", self.select_cam)
		self.cam_tree.bind("<Double-Button-1>", self.on_click_play_cam)

		self.cam_tree_scb_y = Scrollbar(self.cam_tree, orient='vertical',command=self.cam_tree.yview,width=15)
		self.cam_tree_scb_y.pack(side='right', fill=tk.BOTH, expand=tk.NO)
		self.cam_tree.configure(yscrollcommand=self.cam_tree_scb_y.set)

		self.cam_tree_scb_x = Scrollbar(self.cam_tree, orient='horizontal',command=self.cam_tree.xview,width=15)
		self.cam_tree_scb_x.pack(side='bottom', fill=tk.BOTH, expand=tk.NO)
		self.cam_tree.configure(xscrollcommand=self.cam_tree_scb_x.set)

		self.refresh_button = tk.Button(self.list_area, width=18, text='刷新服务器')
		self.refresh_button.pack(side='bottom', fill=tk.BOTH, expand=tk.NO)
		self.refresh_button.bind("<ButtonPress-1>", self.check_servers)

		self.stop_button = tk.Button(self.video_control_area, text='停止')
		self.stop_button.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)
		self.stop_button.bind("<ButtonPress-1>", self.stop_play_cam)

		self.capture_button = tk.Button(self.video_control_area, text='截图')
		self.capture_button.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)
		self.capture_button.bind("<ButtonPress-1>", self.capture_cam)

		self.play_button = tk.Button(self.video_control_area, text='播放')
		self.play_button.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

		self.speedup_button = tk.Button(self.video_control_area, text='加速')
		self.speedup_button.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

		self.pause_button = tk.Button(self.video_control_area, text='暂停')
		self.pause_button.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

		self.image = tk.PhotoImage(file="./dat/fenge_line.png")
		self.hide_button= tk.Button(self.hide_area,width=5,text='showing',bg='gray',image=self.image)
		self.hide_button.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)
		self.hide_button.bind("<ButtonPress-1>",self.on_click_hide_cam_tree_area)
		self.hide_button.bind("<Enter>",self.on_mouse_enter_hidden_button)
		self.hide_button.bind("<Leave>", self.on_mouse_leave_hidden_button)

		self.label_info = tk.Label(self.video_control_area, textvariable=self.info,width=60)  # anchor='w' ,justify='left',
		self.label_info.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

		self.full_screen_button = tk.Button(self.video_control_area,  text='全屏')#width=3,
		self.full_screen_button.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.NO)
		self.full_screen_button.bind("<ButtonPress-1>", self.on_click_full_screen_button)

		for lang, num in self.window_des:
			self.b = Radiobutton(self.video_control_area, text=lang, variable=self.v_num, value=num, indicatoron=False,
			                     command=self.show_window)
			self.b.pack(side=tk.RIGHT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

		self.scale_bar = tk.Scale(self.video_control_area, from_=50, to=100, orient=tk.HORIZONTAL, showvalue=0,
		                          borderwidth=0.01,
		                          repeatinterval=1, repeatdelay=100, sliderlength=15,
		                          resolution=0.1)  # tickinterval=5  刻度
		self.scale_bar.set(95)
		self.scale_bar.bind("<ButtonPress-1>", self.scale_mouse_click)
		self.scale_bar.bind("<ButtonRelease-1>", self.scale_mouse_click)
		self.scale_bar.bind('<B1-Motion> ', self.scale_mouse_click)
		self.scale_bar.pack(side=tk.RIGHT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)

		self.label_scale_name = tk.Label(self.video_control_area, text='透明度', anchor='e', justify='right')
		self.label_scale_name.pack(side=tk.RIGHT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

		self.label_blank = tk.Label(self.video_control_area, text='   ', anchor='e', justify='right')
		self.label_blank.pack(side=tk.RIGHT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

		self.root.bind('<KeyPress-Escape>',self.on_click_esc)

		self.now_hwnd = self.video_play_1.winfo_id()

		self.now_window_name = self.video_play_1.winfo_class()

		self.now_window_widget = self.video_play_1

		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

		self.last_init(event='')
		# self.v_num.set(4)
		# self.show_window()

	def on_click_esc(self,event):

		print(event)
		if self.full_screen_button['text']=='退出全屏':
			self.root.attributes("-fullscreen", False)
			self.root.attributes("-topmost", False)
			self.full_screen_button['text'] = '全屏'
			return
		if self.full_screen_button['text'] == '全屏':
			self.on_closing()
			return

	def on_click_hide_cam_tree_area(self,event):
		if self.hide_button['text']=='showing':
			self.list_area.pack_forget()
			self.hide_button['text'] = 'hidding'
			return

		if self.hide_button['text']=='hidding':
			self.list_area.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)
			self.hide_button['text'] = 'showing'
			return

		self.list_area.pack_forget()
		print(self.list_area.winfo_exists())

	def on_mouse_enter_hidden_button(self,event):
		self.hide_button['bg']='black'

	def on_mouse_leave_hidden_button(self,event):
		self.hide_button['bg'] = 'white'

	def on_mouse_move_in_area(self,event):
		win_desc=event.widget.winfo_class()
		info=self.window_status[event.widget.winfo_class()]
		if info==0:
			show_info='窗口：%s，No Singal'%win_desc
			size_x=8*len(show_info)
			size_y=20
		else:
			server_desc,ip,port,user=info[0].split(':')
			channel=info[2]
			if server_desc=='dahua':
				server_desc='大华'
			if server_desc=='haikang':
				server_desc='海康'
			show_info='窗口：%s，正在播放%s@%s:%s channel %s'%(win_desc,server_desc,ip,port,channel)
			size_x=8*len(show_info)
			size_y=20
		self.float_label['text']=show_info
		self.float_label.pack(side=tk.RIGHT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.float_window.geometry('%sx%s+%s+%s'%(size_x,size_y,event.x_root+5,event.y_root+5))
		#self.float_label.after(10000,self.on_mouse_stop_move_three_second)


	def on_mouse_move_out_area(self,event):

		self.float_label['text']=0
		self.float_label.pack_forget()
		self.float_window.geometry('1x1')


	def on_mouse_stop_move_three_second(self):
		try:
			self.float_label['text']=0
			self.float_label.pack_forget()
			self.float_window.geometry('1x1')
			self.float_label.after(10000, self.on_mouse_stop_move_three_second)
		except Exception as e:
			print(e)


	def on_closing(self):
		def do():
			if askokcancel("Quit", "Do you want to quit?"):
				self.save_windows_states()
				self.closing_flag = True
				while self.refresh_button['state'] == tk.DISABLED:
					print(self.refresh_button['state'], self.refresh_button['state'] == tk.DISABLED)
					self.info.set('正在关闭，请等待...')
					time.sleep(1)
				self.__del__()

		t = Thread(target=do)
		t.setDaemon(True)
		t.start()

	def scale_mouse_click(self, event):
		x = event.x_root
		y = event.y_root
		self.root.attributes("-alpha", self.scale_bar.get() / 100)

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
		item = ''
		for select in self.cam_tree.selection():
			item = self.cam_tree.item(select, "values")
			print(item)  # 输出所选行的第一列的值
		if len(item) > 2:
			return item

	def stop_play_cam(self, event):

		def do():

			if self.now_window_name == -1 or self.now_hwnd == -1 or self.now_window_widget == -1:
				showwarning(message='请先选择一个播放窗口')
				return

			if self.window_status[self.now_window_name] == 0:
				showwarning(message='窗口空闲，没有可停止的对象')
				return

			if self.window_status[self.now_window_name] != 0:
				server_type, server, channel, cam_handle = self.window_status[self.now_window_name]
				print(server)
				server.Stop_Play_Cam(cam_handle)
				self.window_status[self.now_window_name] = 0
				self.now_window_widget['bg'] = VIDEO_DEFAULT_COLOR
				self.info.set('当前窗口为 {} ,空闲中'.format(self.now_window_name))

		t = Thread(target=do)
		t.setDaemon(True)
		t.start()

	def on_click_play_cam(self, event):
		print('播放菜单选中cam')
		print(self.window_status)
		item=''
		for select in self.cam_tree.selection():
			item = self.cam_tree.item(select, "values")
			print(item)  # 输出所选行的第一列的值
		if len(item) in (0,1):
			print('主机无法播放,请选择通道')
			return
		print('播放', item)
		statues, server_desc, channel = item
		channel = int(channel)

		if ':offline' in statues:
			showwarning(message='服务器不在线，请刷新服务器')
			return

		if self.window_status[self.now_window_name] != 0:
			print(self.window_status[self.now_window_name])
			showwarning(title='warning', message='该窗口已有视频播放,请先停止本窗口播放的视频')
			return

		if 'haikang:' in statues:
			print('调用海康播放')
			server = self.online_hk_servers[server_desc]['instance']

			for window_name in self.window_status.keys():
				value = self.window_status[window_name]

				if isinstance(value, int):
					continue
				# if server in value and 'haikang:' in value[0] and channel in value:
				# 	showwarning(message='本cam已在 {} 中播放'.format(window_name))
				# 	return

			self.play_hk_cam(server_desc, server, channel, self.now_window_name, self.now_hwnd)

		if 'dahua:' in statues:
			print('调用大华播放')
			server = self.online_dahua_servers[server_desc]['instance']

			for window_name in self.window_status.keys():
				value = self.window_status[window_name]

				if isinstance(value, int):
					continue
				# if server in value and 'dahua:' in value[0] and channel in value:
				# 	showwarning(message='本cam已在 {} 中播放'.format(window_name))
				# 	return

			self.play_dh_cam(server_desc, server, channel, self.now_window_name, self.now_hwnd)

	def play_dh_cam(self, server_desc, server, channel, window_name, hwnd):
		channel = int(channel)
		lRealHandle = server.Play_Cam(hwnd, channel)
		if lRealHandle == 'shibai':
			showwarning(message='播放异常，请检查')
			return
		if isinstance(lRealHandle, int):
			self.window_status[window_name] = (server_desc, server, channel, lRealHandle)

	def play_hk_cam(self, server_desc, server, channel, window_name, hwnd):
		channel = int(channel)
		lRealHandle = server.Play_Cam(hwnd, channel)
		if lRealHandle == 'shibai':
			showwarning(message='播放异常，请检查')
			return
		if isinstance(lRealHandle, int):
			self.window_status[window_name] = (server_desc, server, channel, lRealHandle)

	def rec_cam(self):
		pass

	def stop_rec_cam(self):
		pass

	def capture_cam(self, event):
		# dahua:47.92.89.1:8101:admin', <my_dh_dvr.DAHUA_DVR object at 0x000000000BCBA340>, 0, 410118320)

		info = self.window_status[self.now_window_name]

		if len(info) == 0:
			showwarning(message='当前窗口没有视频播放')
			return

		server_desc, server, channel, lUrseID = info

		if 'haikang:' in server_desc:
			print('调用海康截图')
			#self.play_hk_cam(server_desc, server, channel, self.now_window_name, self.now_hwnd)

		if 'dahua:' in server_desc:
			print('调用大华截图')

			#self._dh_cam(server_desc, server, channel, self.now_window_name, self.now_hwnd)

	def on_click_full_screen_button(self,event):
		if self.full_screen_button['text']=='全屏':
			self.root.attributes("-fullscreen", True)
			self.root.attributes("-topmost",True)
			self.full_screen_button['text'] = '退出全屏'
			return
		if self.full_screen_button['text']=='退出全屏':
			self.root.attributes("-fullscreen", False)
			self.root.attributes("-topmost", False)
			self.full_screen_button['text'] = '全屏'
			return

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
		if self.v_num.get() != 1:
			event.widget['highlightbackground'] = 'red'
		# 设置选中视频窗口的句柄
		self.now_hwnd = event.widget.winfo_id()
		self.now_window_name = event.widget.winfo_class()
		self.now_window_widget = event.widget

		print('当前窗口的句柄,name,widget:', self.now_hwnd, self.now_window_name, self.now_window_widget)
		print('当前窗口的状态为：', self.window_status[self.now_window_name])

		win_desc=event.widget.winfo_class()
		info=self.window_status[event.widget.winfo_class()]
		print(info)
		if info==0:
			show_info='窗口：%s，No Singal'%win_desc
		else:
			server_desc,ip,port,user=info[0].split(':')
			channel=info[2]
			if server_desc=='dahua':
				server_desc='大华'
			if server_desc=='haikang':
				server_desc='海康'
			show_info='窗口：%s，正在播放%s@%s:%s channel %s'%(win_desc,server_desc,ip,port,channel)
		self.info.set(show_info)




	def save_windows_states(self):
		states = {}
		v_num=self.v_num.get()
		if v_num not in [1,4,9,16]:
			v_num=9
		states['v_num']=v_num
		for win_name in self.window_status:
			if self.window_status[win_name] == 0:
				continue
			else:
				desc, dvr, channel, handle = self.window_status[win_name]
				states[win_name] = [desc, channel]
		print(states)
		with open(os.path.join(DAT_PATH, 'state.dat'), 'wb') as f:
			pickle.dump(states, f)

	def get_window_hwnd(self, name):
		if name == 'window_1':
			return self.video_play_1.winfo_id()
		if name == 'window_2':
			return self.video_play_2.winfo_id()
		if name == 'window_3':
			return self.video_play_3.winfo_id()
		if name == 'window_4':
			return self.video_play_4.winfo_id()
		if name == 'window_5':
			return self.video_play_5.winfo_id()
		if name == 'window_6':
			return self.video_play_6.winfo_id()
		if name == 'window_7':
			return self.video_play_7.winfo_id()
		if name == 'window_8':
			return self.video_play_8.winfo_id()
		if name == 'window_9':
			return self.video_play_9.winfo_id()

	def load_windows_states(self):
		states = {}
		if os.path.exists(os.path.join(DAT_PATH, 'state.dat')) and os.path.isfile(os.path.join(DAT_PATH, 'state.dat')):
			with open(os.path.join(DAT_PATH, 'state.dat'), 'rb') as f:
				try:
					states = pickle.load(f)
					print('加载的上次的配置', states)
				except:
					self.v_num.set(9)
					self.show_window()
					return

		print('load',states)

		if states=={}:
			self.v_num.set(9)
			self.show_window()
			return


		v_num=states['v_num']
		if v_num not in [1,4,9,16]:
			v_num=9
		self.v_num.set(v_num)
		self.show_window()

		if len(states)==1:
			return

		if askokcancel('提示', '是否载入上次的视频窗口') == True:
			for window_name in states.keys():
				if window_name=='v_num':
					continue
				server_desc, channel = states[window_name]
				print(server_desc, window_name, channel)
				hwnd = self.get_window_hwnd(window_name)
				server = ''
				print(server_desc, self.online_hk_servers.keys())
				if server_desc in self.online_hk_servers.keys():
					server = self.online_hk_servers[server_desc]['instance']
				if server_desc in self.online_dahua_servers.keys():
					server = self.online_dahua_servers[server_desc]['instance']
				print(server_desc, server, channel, window_name, channel, hwnd)
				if server == '':
					continue
				else:
					self.play_hk_cam(server_desc, server, channel, window_name, hwnd)


	def get_father_widget(self, event):

		return event.widget.nametowidget(event.widget.winfo_parent())

	def get_childen_widget(self, event):
		child=event.widget.winfo_children()
		return [event.widget.nametowidget(x) for x in child]

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
		self.video_play_area_1.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_area_2.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_area_3.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_1.pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_2.pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_3.pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_4.pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_5.pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_6.pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_7.pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_8.pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_9.pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
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
		self.video_play_area_1.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_area_2.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_1.pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_2.pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_4.pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_5.pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
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
			self.video_play_area_1.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
			self.video_play_1.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		else:

			event.widget['highlightthickness'] = 0
			father_frame = event.widget.nametowidget(event.widget.winfo_parent())
			father_frame.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
			event.widget.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
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
			server['type'] = 'hk'
			server['channel'] = {}
			for key in item.keys():
				result = re.findall('channel_(\d+)', str.lower(key.replace(' ', '')))
				if len(result) == 1:
					result = int(result[0])
					server['channel'][result] = item[key]
			server_desc = 'haikang:' + server['ip'] + ':' + server['port'] + ':' + server['user_name']

			if (server_desc in self.online_hk_servers.keys()) or (server_desc in self.offline_hk_servers.keys()):
				showwarning(message='大华配置文件中存在重复的主机，请检查配置文件，将同一主机的cam放在一起')
				return

			instance = HK_DVR(sDVRIP=server['ip'], sDVRPort=server['port'], sUserName=server['user_name'],
			                  sPassword=server["pwd"])
			if instance.lUserID == None:
				server['instance'] = instance
				self.offline_hk_servers[server_desc] = server
			if instance.lUserID != None:
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
			server['type'] = 'dahua'
			server['channel'] = {}
			for key in item.keys():
				result = re.findall('channel_(\d+)', str.lower(key.replace(' ', '')))

				if len(result) == 1:
					result = int(result[0])
					server['channel'][result] = item[key]
			server_desc = 'dahua:' + server['ip'] + ':' + server['port'] + ':' + server['user_name']
			instance = DAHUA_DVR(sDVRIP=server['ip'], sDVRPort=server['port'], sUserName=server['user_name'],
			                     sPassword=server["pwd"])
			if instance.lUserID == None:
				server['instance'] = instance
				self.offline_dahua_servers[server_desc] = server
			if instance.lUserID != None:
				server['instance'] = instance
				self.online_dahua_servers[server_desc] = server

	def init_dvr(self):

		self.info.set('初始化视频服务器中......')
		t1 = Thread(target=self.init_hk_dvr)
		t2 = Thread(target=self.init_dahua_dvr)
		t1.setDaemon(True)
		t2.setDaemon(True)
		t1.start()
		t2.start()
		while t1.is_alive() or t2.is_alive():
			time.sleep(1)
			continue
		self.info.set('初始化视频服务器完毕')
		return True

	def last_init(self, event):

		def do():
			self.refresh_button['state'] = tk.DISABLED
			self.refresh_button.unbind("<ButtonPress-1>")
			self.init_dvr()
			if self.closing_flag == False:
				# t = Thread(target=self.show_cam_tree)
				# t.setDaemon(True)
				# t.start()
				self.show_cam_tree()
				self.refresh_button['state'] = tk.NORMAL
				self.refresh_button.bind("<ButtonPress-1>", self.check_servers)
				self.load_windows_states()
				self.auto_check_servers()

			if self.closing_flag == True:
				print(self.refresh_button)
				self.refresh_button['state'] = tk.NORMAL


		t = Thread(target=do)
		t.setDaemon(True)
		t.start()

	def show_cam_tree(self):

		self.clean_cam_tree(event='')

		if len(self.online_hk_servers) != 0:
			self.online_hk_tree = self.cam_tree.insert('', '0', text='海康在线', values='haikang:online', open=True)
			for key in self.online_hk_servers:
				server = self.online_hk_servers[key]
				tree = self.cam_tree.insert(self.online_hk_tree, '1',
				                            text=server['name'] + ' - ' + server['ip'] + ':' + server['port'],
				                            values=server['name'], open=True)
				for channel in sorted(server['channel'].keys(),reverse = False):
					values = ['haikang:online', key, channel]
					self.cam_tree.insert(tree, '1', text=str(str(channel) + ':' + server['channel'][channel]),
					                     values=values)

		if len(self.online_dahua_servers) != 0:
			self.online_dahua_tree = self.cam_tree.insert('', '1', text='大华在线', values='dahua:online', open=True)
			for key in self.online_dahua_servers:
				server = self.online_dahua_servers[key]
				tree = self.cam_tree.insert(self.online_dahua_tree, '1',
				                            text=server['name'] + ' - ' + server['ip'] + ':' + server['port'],
				                            values=server['name'], open=True)
				for channel in sorted(server['channel'].keys(),reverse = False):
					values = ['dahua:online', key, channel]
					self.cam_tree.insert(tree, '1', text=str(str(channel) + ':' + server['channel'][channel]),
					                     values=values)

		self.fengexian = self.cam_tree.insert('', '2', text=' ' * 20, values='fengge', open=True)
		self.fengexian = self.cam_tree.insert('', '3', text='*' * 5 + '我是分割线' + '*' * 5, values='fengge', open=True)
		self.fengexian = self.cam_tree.insert('', '4', text=' ' * 20, values='fengge', open=True)

		if len(self.offline_hk_servers) != 0:
			self.offline_hk_tree = self.cam_tree.insert('', '7', text='海康离线', values='haikang:offline', open=True)
			for key in self.offline_hk_servers:
				server = self.offline_hk_servers[key]
				tree = self.cam_tree.insert(self.offline_hk_tree, '1',
				                            text=server['name'] + ' - ' + server['ip'] + ':' + server['port'],
				                            values=server['name'], open=False)
				for channel in sorted(server['channel'].keys(),reverse = False):
					values = ['haikang:offline', key, channel]
					self.cam_tree.insert(tree, '1', text=str(str(channel) + ':' + server['channel'][channel]),
					                     values=values)

		if len(self.offline_dahua_servers) != 0:
			self.offline_dahua_tree = self.cam_tree.insert('', '8', text='大华离线', values='dahua:offline', open=True)
			for key in self.offline_dahua_servers:
				server = self.offline_dahua_servers[key]
				tree = self.cam_tree.insert(self.offline_dahua_tree, '1',
				                            text=server['name'] + ' - ' + server['ip'] + ':' + server['port'],
				                            values=server['name'], open=False)
				for channel in sorted(server['channel'].keys(),reverse = False):
					values = ['dahua:offline', key, channel]
					self.cam_tree.insert(tree, '1', text=str(str(channel) + ':' + server['channel'][channel]),
					                     values=values)

	def clean_cam_tree(self, event):
		for item in self.cam_tree.get_children():
			self.cam_tree.delete(item)


	def auto_check_servers(self):

		def do():

			while self.closing_flag == False:
				for i in range(REFRESH_TIME//10,0,-1):
					self.info.set('计划在%s秒后自动刷新服务器...'%(i*10))
					time.sleep(10)
					if self.closing_flag==True:
						exit()
				print('自动刷新服务器')
				if self.refresh_button['state'] == tk.DISABLED:
					time.sleep(3)
					continue

				self.refresh_button['state'] = tk.DISABLED
				self.refresh_button.unbind("<ButtonPress-1>")
				self.info.set('自动刷新服务器状态......')
				check1 = Thread(target=self.check_dh_servers)
				check2 = Thread(target=self.check_hk_servers)

				check1.setDaemon(True)
				check2.setDaemon(True)

				check1.start()
				check2.start()

				while check1.is_alive() or check2.is_alive():
					time.sleep(2)
					continue
				if self.closing_flag == False:
					show1 = Thread(target=self.show_cam_tree)
					show1.setDaemon(True)
					show1.start()
					self.info.set('自动刷新服务器成功')
					self.refresh_button['state'] = tk.NORMAL
					self.refresh_button.bind("<ButtonPress-1>", self.check_servers)
				if self.closing_flag == True:
					print(self.refresh_button)
					self.refresh_button['state'] = tk.NORMAL
					break

		t = Thread(target=do)
		t.setDaemon(True)
		t.start()

	def check_hk_servers(self):
		new_online = []
		for key in self.offline_hk_servers:
			server = self.offline_hk_servers[key]
			result = server['instance'].NET_DVR_Login()
			if result == None:
				continue
			if result != None:
				new_online.append([key, {key: server}])
		for key, item in new_online:
			self.online_hk_servers.update(item)
			self.offline_hk_servers.pop(key)

		new_offline = []
		for key in self.online_hk_servers:
			server = self.online_hk_servers[key]
			if server['instance'].check_device_online() == False:
				new_offline.append([key, {key: server}])
		for key, item in new_offline:
			self.offline_hk_servers.update(item)
			self.online_hk_servers.pop(key)

		print(len(self.online_hk_servers), self.online_hk_servers)
		print(len(self.offline_hk_servers), self.offline_hk_servers)

	def check_dh_servers(self):
		new_online = []
		for key in self.offline_dahua_servers:
			server = self.offline_dahua_servers[key]
			result = server['instance'].NET_DVR_Login()
			if result == None:
				continue
			if result != None:
				new_online.append([key, {key: server}])
		for key, item in new_online:
			self.online_dahua_servers.update(item)
			self.offline_dahua_servers.pop(key)

		new_offline = []
		for key in self.online_dahua_servers:
			server = self.online_dahua_servers[key]
			if server['instance'].check_device_online() == False:
				new_offline.append([key, {key: server}])
		for key, item in new_offline:
			self.offline_dahua_servers.update(item)
			self.online_dahua_servers.pop(key)

		print(len(self.online_dahua_servers), self.online_dahua_servers)
		print(len(self.offline_dahua_servers), self.offline_dahua_servers)

	def check_servers(self, event):
		self.refresh_button['state'] = tk.DISABLED
		self.refresh_button.unbind("<ButtonPress-1>")

		def do():
			self.info.set('刷新服务器状态......')
			check1 = Thread(target=self.check_dh_servers)
			check2 = Thread(target=self.check_hk_servers)

			check1.setDaemon(True)
			check2.setDaemon(True)

			check1.start()
			check2.start()

			while 1:
				if check1.is_alive() or check2.is_alive():
					time.sleep(1)
					continue
				if self.closing_flag == False:
					show1 = Thread(target=self.show_cam_tree)
					show1.setDaemon(True)
					show1.start()
					self.info.set('刷新服务器成功')
					self.refresh_button['state'] = tk.NORMAL
					self.refresh_button.bind("<ButtonPress-1>", self.check_servers)
					break
				if self.closing_flag == True:
					print(self.refresh_button)
					self.refresh_button['state'] = tk.NORMAL
					break

		t = Thread(target=do)
		t.setDaemon(True)
		t.start()

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
		self.root.destroy()


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

