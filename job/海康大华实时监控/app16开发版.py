# coding：utf8
# ﻿Team  JiaLiDun University
# Author：zl
# Date ：2020/9/30 0030 上午 9:39
# Tool ：PyCharm
import time
import os
import pickle
from concurrent.futures import ThreadPoolExecutor

import configparser

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

from my_hk_dvr import HK_DVR
from my_dh_dvr import DAHUA_DVR
import my_icon

from my_tk_login import tk_login


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
		my_icon.set_icon(self.root,my_icon.USER_ICON)
		self.root.title('现场可视化管理平台')
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


		self.window_des = [('单窗口', 1), ('四窗口', 4), ('九窗口', 9),('老多窗口', 16)]

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
			'window_10': 0,
			'window_11': 0,
			'window_12': 0,
			'window_13': 0,
			'window_14': 0,
			'window_15': 0,
			'window_16': 0
		}
		self.win_all=['window_1','window_2','window_3','window_4',
		              'window_5','window_6','window_7','window_8',
		              'window_9','window_10','window_11','window_12',
		              'window_13','window_14','window_15','window_16',]

		self.rec_status = {}

		self.list_area = tk.Frame(self.root, bd=0, relief="sunken")

		self.hide_area = tk.Frame(self.root, bd=0, relief="sunken")

		self.video_area = tk.Frame(self.root, bd=0, relief="sunken")

		self.video_area.pack(side=tk.RIGHT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)

		self.hide_area.pack(side=tk.RIGHT, anchor=tk.S, expand=tk.NO, fill=tk.Y)

		self.list_area.pack(side=tk.RIGHT, anchor=tk.S, expand=tk.NO, fill=tk.Y)

		self.video_play_area = tk.Frame(self.video_area, bd=0, relief="sunken")
		self.video_play_area.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)

		self.video_play_bottom_area = tk.Frame(self.video_area, bd=0, relief="sunken")
		self.video_play_bottom_area.pack(side=tk.TOP, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

		self.video_control_hide_area= tk.Frame(self.video_play_bottom_area, bd=0, relief="sunken",height=10)
		self.video_control_hide_area.pack(side=tk.TOP, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

		self.video_control_area = tk.Frame(self.video_play_bottom_area, bd=0, relief="sunken")
		self.video_control_area.pack(side=tk.BOTTOM, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

		self.video_play_area_1 = tk.Frame(self.video_play_area, bd=0, relief="sunken")
		self.video_play_area_2 = tk.Frame(self.video_play_area, bd=0, relief="sunken")
		self.video_play_area_3 = tk.Frame(self.video_play_area, bd=0, relief="sunken")
		self.video_play_area_4 = tk.Frame(self.video_play_area, bd=0, relief="sunken")

		self.video_play_1 = tk.Frame(self.video_play_area_1, cursor='plus', bd=1, relief="sunken",
		                             class_='window_1', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_2 = tk.Frame(self.video_play_area_1, cursor='plus', bd=1, relief="sunken",
		                             class_='window_2', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_3 = tk.Frame(self.video_play_area_1, cursor='plus', bd=1, relief="sunken",
		                             class_='window_3', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_4 = tk.Frame(self.video_play_area_1, cursor='plus', bd=1, relief="sunken",
		                             class_='window_4', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_5 = tk.Frame(self.video_play_area_2, cursor='plus', bd=1, relief="sunken",
		                             class_='window_5', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_6 = tk.Frame(self.video_play_area_2, cursor='plus', bd=1, relief="sunken",
		                             class_='window_6', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_7 = tk.Frame(self.video_play_area_2, cursor='plus', bd=1, relief="sunken",
		                             class_='window_7', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_8 = tk.Frame(self.video_play_area_2, cursor='plus', bd=1, relief="sunken",
		                             class_='window_8', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_9 = tk.Frame(self.video_play_area_3, cursor='plus', bd=1, relief="sunken",
		                             class_='window_9', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_10 = tk.Frame(self.video_play_area_3, cursor='plus', bd=1, relief="sunken",
		                             class_='window_10', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_11 = tk.Frame(self.video_play_area_3, cursor='plus', bd=1, relief="sunken",
		                             class_='window_11', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_12 = tk.Frame(self.video_play_area_3, cursor='plus', bd=1, relief="sunken",
		                             class_='window_12', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_13 = tk.Frame(self.video_play_area_4, cursor='plus', bd=1, relief="sunken",
		                             class_='window_13', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_14 = tk.Frame(self.video_play_area_4, cursor='plus', bd=1, relief="sunken",
		                             class_='window_14', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_15 = tk.Frame(self.video_play_area_4, cursor='plus', bd=1, relief="sunken",
		                             class_='window_15', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_16 = tk.Frame(self.video_play_area_4, cursor='plus', bd=1, relief="sunken",
		                             class_='window_16', highlightthickness=2, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_1_state=tk.Label(self.video_play_1,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_2_state=tk.Label(self.video_play_2,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_3_state=tk.Label(self.video_play_3,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_4_state=tk.Label(self.video_play_4,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_5_state=tk.Label(self.video_play_5,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_6_state=tk.Label(self.video_play_6,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_7_state=tk.Label(self.video_play_7,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_8_state=tk.Label(self.video_play_8,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_9_state=tk.Label(self.video_play_9,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_10_state=tk.Label(self.video_play_10,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_11_state=tk.Label(self.video_play_11,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_12_state=tk.Label(self.video_play_12,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_13_state=tk.Label(self.video_play_13,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_14_state=tk.Label(self.video_play_14,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_15_state=tk.Label(self.video_play_15,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)
		self.video_play_16_state=tk.Label(self.video_play_16,cursor='plus', bd=1,relief="sunken",
		                              highlightthickness=0, bg=VIDEO_DEFAULT_COLOR)

		self.video_play_states=[self.video_play_1_state,self.video_play_2_state,self.video_play_3_state,self.video_play_4_state,
		                  self.video_play_5_state,self.video_play_6_state,self.video_play_7_state,self.video_play_8_state,
		                  self.video_play_9_state,self.video_play_10_state,self.video_play_11_state,self.video_play_12_state,
		                  self.video_play_13_state,self.video_play_14_state,self.video_play_15_state,self.video_play_16_state,]

		self.video_plays=[self.video_play_1,self.video_play_2,self.video_play_3,self.video_play_4,
		                  self.video_play_5,self.video_play_6,self.video_play_7,self.video_play_8,
		                  self.video_play_9,self.video_play_10,self.video_play_11,self.video_play_12,
		                  self.video_play_13,self.video_play_14,self.video_play_15,self.video_play_16,]

		for v_play in self.video_plays:
			v_play.bind('<Motion>',self.on_mouse_move_in_video_play_area)
			v_play.bind('<Leave>', self.on_mouse_move_out_video_play_area)
			v_play.bind("<ButtonPress-1>", self.set_select_window_info)
			v_play.bind("<Double-Button-1>", self.change_window)

		style = ttk.Style()
		# style_head.configure("Treeview.Heading", font=('', 65))
		style.configure("Treeview", font=('', 15))

		self.cam_tree = ttk.Treeview(self.list_area, selectmode='browse')
		self.cam_tree.pack(side='top', fill=tk.BOTH, expand=tk.YES)

		self.cam_tree.bind("<ButtonPress-1>", self.select_cam)
		self.cam_tree.bind("<Double-Button-1>", self.on_click_play_cam)

		self.cam_tree_scb_y = Scrollbar(self.cam_tree, orient='vertical',command=self.cam_tree.yview,width=10)
		self.cam_tree_scb_y.pack(side='right', fill=tk.BOTH, expand=tk.NO)
		self.cam_tree.configure(yscrollcommand=self.cam_tree_scb_y.set)

		self.cam_tree_scb_x = Scrollbar(self.cam_tree, orient='horizontal',command=self.cam_tree.xview,width=10)
		self.cam_tree_scb_x.pack(side='bottom', fill=tk.BOTH, expand=tk.NO)
		self.cam_tree.configure(xscrollcommand=self.cam_tree_scb_x.set)

		self.refresh_button = tk.Button(self.list_area, text='刷新服务器',width=30)
		self.refresh_button.pack(side='bottom', fill=tk.BOTH, expand=tk.NO)
		self.refresh_button.bind("<ButtonPress-1>", self.check_servers)
		# refresh button 的disablede 状态在手动刷新时设置，使按钮不可用，防止连续点击重复刷新服务器状态，影响性能
		# 同时作为自动刷新，关机时检测刷新服务器状态的标志，自动刷新前若检测到该状态为disabled，则推迟一个刷新周期
		# 自动刷新中若检测到关闭信号，则中断刷新服务器，并将disabled状态设置为正常，作为on_closing方法关机是否等待还是继续关机的标志位

		self.stop_button = tk.Button(self.video_control_area, text='停止')
		self.stop_button.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)
		self.stop_button.bind("<ButtonPress-1>", self.on_click_stop_play_cam)

		self.capture_button = tk.Button(self.video_control_area, text='截图')
		self.capture_button.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)
		self.capture_button.bind("<ButtonPress-1>", self.capture_cam)

		self.rec_button = tk.Button(self.video_control_area, text='录像/停止')
		self.rec_button.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)
		self.rec_button.bind('<Button-1>',self.on_click_rec_button)

		# self.speedup_button = tk.Button(self.video_control_area, text='加速')
		# self.speedup_button.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)
		#
		# self.pause_button = tk.Button(self.video_control_area, text='暂停')
		# self.pause_button.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

		self.image = tk.PhotoImage(file="./dat/fenge_line.png")
		self.left_hide_button= tk.Button(self.hide_area,width=5,text='showing',bg='gray',image=self.image)
		self.left_hide_button.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)
		self.left_hide_button.bind("<ButtonPress-1>",self.on_click_hide_cam_tree_area)
		self.left_hide_button.bind("<Enter>",self.on_mouse_enter_hidden_button)
		self.left_hide_button.bind("<Leave>", self.on_mouse_leave_hidden_button)

		self.video_play_bottom_area.bind('<Enter>',self.on_mouse_enter_control_area)
		self.video_play_bottom_area.bind('<Leave>', self.mouse_move_leave_control_area)

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

		self.show_win_info_checkbutton_flag= StringVar()
		self.show_win_info_checkbutton_flag.set('show')
		self.show_win_info_checkbutton=tk.Checkbutton(self.video_control_area, variable=self.show_win_info_checkbutton_flag,onvalue='show',offvalue='hide',text='显示窗格信息',
													  command=self.on_click_show_win_info_checkbutton)
		self.show_win_info_checkbutton.pack(side=tk.RIGHT, anchor=tk.S)
		self.refresh_video_states()


		self.label_blank = tk.Label(self.video_control_area, text='   ', anchor='e', justify='right')
		self.label_blank.pack(side=tk.RIGHT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

		self.root.bind('<KeyPress-Escape>',self.on_click_esc)

		self.now_hwnd = self.video_play_1.winfo_id()

		self.now_window_name = self.video_play_1.winfo_class()

		self.now_window_widget = self.video_play_1

		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

		self.last_init(event='')
		# self.v_num.set(9)
		# self.show_window()

	def refresh_video_states(self):
		self.on_click_show_win_info_checkbutton()

	def on_click_show_win_info_checkbutton(self):

		if self.show_win_info_checkbutton_flag.get()=='hide':
			for label in self.video_play_states:
				label['text']=''
				label.place_forget()
			return

		for win_desc,label in zip(self.win_all,self.video_play_states):
			print(win_desc)
			info=self.window_status[win_desc]
			if info==0:
				show_info='窗口：%s，No Singal'%win_desc
			else:
				server_desc,ip,port,user=info[0].split(':')
				channel=info[2]
				if server_desc=='dahua':
					server_desc='大华'
				if server_desc=='haikang':
					server_desc='海康'
				if info[3]=='playback':
					state='回放'
				else:
					state='实时播放'
				show_info = '%s %s \r %s@%s:%s channel %s' % (win_desc, state,server_desc, ip, port, channel)
				#show_info='窗口：%s，正在播放%s@%s:%s channel %s %s'%(win_desc,server_desc,ip,port,channel,state)
			label['text']=show_info
			label.place(rely=0.9, relx=0.5,anchor=CENTER)
			label['bg']=DEFAULT_COLOR

	def show_rec_state(self):
		def do():
			while self.closing_flag==False:
				print('show rec')
				for label in self.video_play_states:
						label['bg']=DEFAULT_COLOR
				time.sleep(1)
				for win,label in zip(self.win_all,self.video_play_states):
					if win in self.rec_status.keys():
						label['bg']='green'
				time.sleep(1)
		ThreadPoolExecutor().submit(do)

	def on_click_esc(self,event):
		'''
		若检测到esc键被按下，则判断是全屏还是正常播放状态，若是全屏状态则退出全屏，若是正常播放则调用on_closing关闭
		'''
		self.video_control_area.pack(side=tk.BOTTOM, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)
		if self.full_screen_button['text']=='退出全屏':
			self.root.attributes("-fullscreen", False)
			self.root.attributes("-topmost", False)
			self.full_screen_button['text'] = '全屏'
			return
		if self.full_screen_button['text'] == '全屏':
			self.on_closing()
			return

	def on_click_hide_cam_tree_area(self,event):
		'''
		隐藏\打开摄像头列表
		'''
		if self.left_hide_button['text']=='showing':
			self.list_area.pack_forget()
			self.left_hide_button['text'] = 'hidding'
			return

		if self.left_hide_button['text']=='hidding':
			self.list_area.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)
			self.left_hide_button['text'] = 'showing'
			return

	def on_mouse_enter_hidden_button(self,event):
		self.left_hide_button['bg']='black'

	def on_mouse_leave_hidden_button(self,event):
		self.left_hide_button['bg'] = 'white'

	def on_mouse_enter_control_area(self,event):
		if self.full_screen_button['text']=='退出全屏':
			self.video_control_area.pack(side=tk.BOTTOM, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)

	def mouse_move_leave_control_area(self,event):
		if self.full_screen_button['text'] == '退出全屏':
			self.video_control_area.pack_forget()

	def on_mouse_move_in_video_play_area(self,event):
		if self.show_win_info_checkbutton_flag.get()=='show':
			return
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
			if info[3] == 'playback':
				state = '回放'
			else:
				state = '实时播放'
			show_info = '%s %s\r%s@%s:%s channel %s' % (win_desc, state, server_desc, ip, port, channel)
			size_x=8*(len(show_info)-18)
			size_y=40

		self.float_label['text']=show_info
		self.float_label.pack(side=tk.RIGHT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.float_window.geometry('%sx%s+%s+%s'%(size_x,size_y,event.x_root+5,event.y_root+5))
		self.float_window.attributes("-topmost", True)
		#self.float_label.after(10000,self.on_mouse_stop_move_three_second)

	def on_mouse_move_out_video_play_area(self,event):
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
		ThreadPoolExecutor(max_workers=1).submit(do)

	def scale_mouse_click(self, event):
		self.root.attributes("-alpha", self.scale_bar.get() / 100)

	def get_time(self):
		return time.strftime('%Y-%m-%d-%H-%M-%S')

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

	def on_click_stop_play_cam(self, event):

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
				if self.now_window_name in self.rec_status.keys():
					self.rec_status.pop(self.now_window_name)
				self.now_window_widget['bg'] = VIDEO_DEFAULT_COLOR
				self.info.set('当前窗口为 {} ,空闲中'.format(self.now_window_name))
			self.refresh_video_states()
		ThreadPoolExecutor(max_workers=1).submit(do)

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
		self.refresh_video_states()

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

	def on_click_rec_button(self,event):
		def do():
			info=self.window_status[self.now_window_name]

			if info==0:
				showinfo('','请先选中一个正在播放的窗口')
				return

			desc, server, channel, handel = info
			if self.now_window_name in self.rec_status.keys():
				print('停止录像')
				if askokcancel(message='是否停止{} channel:{}录像'.format(desc,channel)):
					ThreadPoolExecutor().submit(self.stop_rec_cam)
			else:
				print('开始录像')
				if askokcancel(message='是否开始{} channel:{}录像'.format(desc, channel)):
					ThreadPoolExecutor().submit(self.rec_cam)
		ThreadPoolExecutor().submit(do)

	def rec_cam(self):
		if self.window_status[self.now_window_name]==0:
			return
		desc,server,channel,handel=self.window_status[self.now_window_name]
		if 'dahua' in desc:
			print('调用大华录像')
		if 'haikang' in desc:
			print('调用海康录像')
			file_path = os.path.join(REC_PATH, desc.replace(':', '-') + '-' + self.get_time() + '.mp4')
			server.Rec_Cam(handel,file_path)
		self.rec_status.update({self.now_window_name:self.window_status[self.now_window_name]})
		print(self.rec_status)
			
	def stop_rec_cam(self):
		if self.window_status[self.now_window_name]==0:
			return
		desc, server, channel, handel = self.window_status[self.now_window_name]
		if 'dahua' in desc:
			print('调用大华停止录像')
		if 'haikang' in desc:
			print('调用海康停止录像')
			server.Stop_Rec_Cam(handel)
		self.rec_status.pop(self.now_window_name)
		print(self.rec_status)

	def capture_cam(self, event):
		'''
		大华截图回调函数无法传入储存地址，只能使用时间作为文件名，参数是通道号，
		海康截图可以直接传入文件地址，参数是是视频播放句柄号，和文件地址
		'''
		def do():
			info = self.window_status[self.now_window_name]

			if info == 0:
				showwarning(message='当前窗口没有视频播放')
				return

			server_desc, server, channel, handel = info

			if 'haikang:' in server_desc:

				file_path=os.path.join(REC_PATH,server_desc.replace(':','-')+'-'+self.get_time()+'.jpg')
				print('调用海康截图')
				print(file_path)
				server.Capture_Cam(int(handel),file_path)

			if 'dahua:' in server_desc:
				print('调用大华截图')
				server.Capture_Cam(int(channel))
		ThreadPoolExecutor().submit(do)

	def on_click_full_screen_button(self,event):
		self.list_area.pack_forget()
		self.left_hide_button['text'] = 'hidding'
		if self.full_screen_button['text']=='全屏':
			self.root.attributes("-fullscreen", True)
			self.root.attributes("-topmost",True)
			self.full_screen_button['text'] = '退出全屏'
			return
		if self.full_screen_button['text']=='退出全屏':
			self.root.attributes("-fullscreen", False)
			self.root.attributes("-topmost", False)
			self.video_control_area.pack(side=tk.BOTTOM, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)
			self.full_screen_button['text'] = '全屏'
			return

	def clear_video_window_select_color(self):
		for player in self.video_plays:
			player['highlightbackground'] = '#bcbcbc'

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
		if name == 'window_10':
			return self.video_play_10.winfo_id()
		if name == 'window_11':
			return self.video_play_11.winfo_id()
		if name == 'window_12':
			return self.video_play_12.winfo_id()
		if name == 'window_13':
			return self.video_play_13.winfo_id()
		if name == 'window_14':
			return self.video_play_14.winfo_id()
		if name == 'window_15':
			return self.video_play_15.winfo_id()
		if name == 'window_16':
			return self.video_play_16.winfo_id()
		if name == 'window_17':
			return self.video_play_17.winfo_id()
		if name == 'window_18':
			return self.video_play_18.winfo_id()

	def get_window_wdiget(self, name):
		if name == 'window_1':
			return self.video_play_1
		if name == 'window_2':
			return self.video_play_2
		if name == 'window_3':
			return self.video_play_3
		if name == 'window_4':
			return self.video_play_4
		if name == 'window_5':
			return self.video_play_5
		if name == 'window_6':
			return self.video_play_6
		if name == 'window_7':
			return self.video_play_7
		if name == 'window_8':
			return self.video_play_8
		if name == 'window_9':
			return self.video_play_9
		if name == 'window_10':
			return self.video_play_10
		if name == 'window_11':
			return self.video_play_11
		if name == 'window_12':
			return self.video_play_12
		if name == 'window_13':
			return self.video_play_13
		if name == 'window_14':
			return self.video_play_14
		if name == 'window_15':
			return self.video_play_15
		if name == 'window_16':
			return self.video_play_16

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
				self.refresh_video_states()

	def get_father_widget(self, event):
		return event.widget.nametowidget(event.widget.winfo_parent())

	def get_childen_widget(self, event):
		child=event.widget.winfo_children()
		return [event.widget.nametowidget(x) for x in child]

	def show_sixteen_play(self):
		for play in self.video_plays:
			play['highlightthickness'] = 2
			play.pack_forget()
		self.video_play_area_1.pack_forget()
		self.video_play_area_2.pack_forget()
		self.video_play_area_3.pack_forget()
		self.video_play_area_4.pack_forget()
		self.video_play_area_1.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_area_2.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_area_3.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_area_4.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		for play in self.video_plays:
			play.pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.is_single_playing = False

	def show_nine_play(self):

		for play in self.video_plays:
			play['highlightthickness'] = 2
			play.pack_forget()
		self.video_play_area_1.pack_forget()
		self.video_play_area_2.pack_forget()
		self.video_play_area_3.pack_forget()
		self.video_play_area_4.pack_forget()
		self.video_play_area_1.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_area_2.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_area_3.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		for n in [0,1,2,4,5,6,8,9,10,13,14,15]:
			self.video_plays[n].pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.is_single_playing = False

	def show_four_play(self):
		for play in self.video_plays:
			play['highlightthickness'] = 2
			play.pack_forget()
		self.video_play_area_1.pack_forget()
		self.video_play_area_2.pack_forget()
		self.video_play_area_3.pack_forget()
		self.video_play_area_4.pack_forget()
		self.video_play_area_1.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.video_play_area_2.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		for n in [0,1,4,5]:
			self.video_plays[n].pack(side=tk.LEFT, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)
		self.is_single_playing = False

	def show_single_play(self, event):
		for play in self.video_plays:
			play['highlightthickness'] = 2
			play.pack_forget()

		self.video_play_area_1.pack_forget()
		self.video_play_area_2.pack_forget()
		self.video_play_area_3.pack_forget()
		self.video_play_area_4.pack_forget()
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
			return

		if self.is_single_playing== True and self.v_num.get() == 9:
			self.show_nine_play()
			return

		if self.is_single_playing == False and self.v_num.get() == 4:
			self.show_single_play(event)
			return

		if self.is_single_playing == True and self.v_num.get() == 4:
			self.show_four_play()
			return

		if self.is_single_playing == False and self.v_num.get() == 16:
			self.show_single_play(event)
			return

		if self.is_single_playing == True and self.v_num.get() == 16:
			self.show_sixteen_play()
			return

	def show_window(self):

		#  print(self.v_num.get(),self.is_single_playing)
		if self.v_num.get() == 16:
			self.show_sixteen_play()


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
		pool=ThreadPoolExecutor(max_workers=2)
		self.info.set('初始化视频服务器中......')
		hk = pool.submit(self.init_hk_dvr)
		dahua = pool.submit(self.init_dahua_dvr)

		while (not hk.done()) or (not dahua.done()):
			time.sleep(1)
			continue
		self.info.set('初始化视频服务器完毕')
		return True

	def check_playing_viedeo_status(self):
		print('检查视频播放状态')
		cams = {}
		playbacks = {}

		for win in self.window_status.keys():
			info=self.window_status[win]
			if info==0:
				continue
			win_desc,server, channel, handel=info

			if handel=='playback':
				print(win,'is playback rec')
				playbacks[win]=info
			if isinstance(handel,int):
				print(win,'is palying cam')
				cams[win]=info
		return cams,playbacks

	def last_init(self, event):

		def do():
			if self.closing_flag == False:
				self.refresh_button['state'] = tk.DISABLED
				self.refresh_button.unbind("<ButtonPress-1>")
				#刷新按钮禁用，防止在初始化过程中重复点击按钮刷新服务器
				self.init_dvr()
				#初始登录视频服务器，
				self.show_cam_tree()
				#根据登陆情况初始化服务器列表
				self.refresh_button['state'] = tk.NORMAL
				self.refresh_button.bind("<ButtonPress-1>", self.check_servers)
				#允许点击刷新按钮
				self.load_windows_states()
				#加载上回的视频和窗口状态
				self.auto_check_servers()
				#启动定时刷新
				self.show_rec_state()
				#开始正在录像的显示rec标志

			if self.closing_flag == True:
				print(self.refresh_button)
				self.refresh_button['state'] = tk.NORMAL

		ThreadPoolExecutor(max_workers=1).submit(do)

	def show_cam_tree(self):

		self.clean_cam_tree(event='')

		if len(self.online_hk_servers) != 0:
			self.online_hk_tree = self.cam_tree.insert('', '0', text='海康在线', values='haikang:online', open=True,)
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
				for i in range(REFRESH_TIME,0,-1):
					if i%60==0:   print(i,'后刷新服务器')
					if i%60==0:  self.info.set('计划在%s秒后自动刷新服务器...'%(i))
					#60刷新一次状态t标签
					time.sleep(1)

					if self.closing_flag==True:
						exit()
					#检测到程序关闭信号，直接退出自动检查循环

					if self.refresh_button['state'] == tk.DISABLED:
						break
					#等待周期中，如果refresh__button不可用，说明在手动刷新或者正在初始化，结束本次等待周期

				if self.refresh_button['state'] == tk.DISABLED:
					continue
				# 等待周期中，如果refresh__button不可用，说明在手动刷新或者正在初始化，结束本次等待周期，进入下次等待

				self.refresh_button['state'] = tk.DISABLED
				self.refresh_button.unbind("<ButtonPress-1>")
				self.info.set('自动刷新服务器状态......')
				dh_check = pool.submit(self.check_dh_servers)
				hk_check = pool.submit(self.check_hk_servers)

				while (not dh_check.done()) or (not hk_check.done()):
					print(dh_check.done(), hk_check.done(), not (dh_check.done() and hk_check.done()))
					time.sleep(1)
					if self.closing_flag == True:
						print('检测到关机')
						self.refresh_button['state'] = tk.NORMAL
						self.video_play_area.forget()
						break
					else:
						continue
					#检测服务器过程中若发现关机信号，则把刷新按钮状态更新为正常，结束刷新服务器的检测过程，同时把刷新按钮设为正常，作为刷新结束的标志
				print('没有检测到关机')
				pool.submit(self.show_cam_tree)
				self.info.set('刷新服务器成功')
				self.refresh_button['state'] = tk.NORMAL
				self.refresh_button.bind("<ButtonPress-1>", self.check_servers)


				dh_new_online,dh_new_offline=dh_check.result()
				hk_new_online,hk_new_offline=hk_check.result()

				cams,playbacks=self.check_playing_viedeo_status()

				print('dh_new_online',dh_new_online)
				print('dh_new_offline',dh_new_offline)

				print('hk_new_online',hk_new_online)
				print('hk_new_offline',hk_new_offline)
				print(cams,playbacks)

				for win in cams.keys():
					desc,server,channel,handel=cams[win]
					if (desc in dh_new_offline) or (desc in hk_new_offline):
						print('检测到服务器掉线，准备播放录像')
						server.Stop_Play_Cam(handel)
						self.window_status[win] = [desc,server,channel,'playback']
						self.get_window_wdiget(win)['bg'] = VIDEO_DEFAULT_COLOR
						self.refresh_video_states()

				for win in playbacks.keys():
					desc,server,channel,handel=playbacks[win]
					if (desc in dh_new_online) or (desc in hk_new_online):
						print('检测服务器上线，并准备播放实时摄像头')
						if 'haikang' in desc:
							self.play_hk_cam(desc, server, channel, win, self.get_window_hwnd(win))
							self.refresh_video_states()
						if 'dahua' in desc:
							self.play_dh_cam(desc, server, channel, win, self.get_window_hwnd(win))
							self.refresh_video_states()


		pool=ThreadPoolExecutor(max_workers=4)
		pool.submit(do)


	def check_hk_servers(self):
		print(self.online_hk_servers)
		print(self.offline_hk_servers)
		new_online = {}
		new_offline={}
		for desc in self.offline_hk_servers.keys():
			server = self.offline_hk_servers[desc]
			result = server['instance'].NET_DVR_Login()
			print(desc)
			if result == None:
				continue
			if result != None:
				new_online[desc]=server
		for desc in new_online.keys():
			self.online_hk_servers.update({desc:new_online[desc]})
			self.offline_hk_servers.pop(desc)
		print('hk2')
		for desc in self.online_hk_servers.keys():
			print(desc)
			server = self.online_hk_servers[desc]
			if server['instance'].check_device_online() == False:
				new_offline[desc]=server
		for desc in new_offline.keys():
			self.offline_hk_servers.update({desc:new_offline[desc]})
			self.online_hk_servers.pop(desc)

		return new_online,new_offline


	def check_dh_servers(self):
		new_online = {}
		new_offline = {}

		print('dahua1')
		for desc in self.offline_dahua_servers.keys():
			server = self.offline_dahua_servers[desc]
			result = server['instance'].NET_DVR_Login()
			if result == None:
				continue
			if result != None:
				new_online[desc]=server
		for desc in new_online.keys():
			self.online_dahua_servers.update({desc:new_online[desc]})
			self.offline_dahua_servers.pop(desc)

		print('dahua 2')
		for desc in self.online_dahua_servers.keys():
			server = self.online_dahua_servers[desc]
			if server['instance'].check_device_online() == False:
				new_offline[desc]=server
		for desc in new_offline.keys():
			self.offline_dahua_servers.update({desc:new_offline[desc]})
			self.online_dahua_servers.pop(desc)

		return new_online,new_offline

	def check_servers(self, event):
		def do():
			self.info.set('刷新服务器状态......')
			self.refresh_button['state'] = tk.DISABLED
			self.refresh_button.unbind("<ButtonPress-1>")
			dh_check = pool.submit(self.check_dh_servers)
			hk_check = pool.submit(self.check_hk_servers)
			while (not dh_check.done()) or (not hk_check.done()) :
				print(dh_check.done(), hk_check.done(), not(dh_check.done() and hk_check.done()))
				time.sleep(1)
				if self.closing_flag == True:
					self.refresh_button['state'] = tk.NORMAL
					break
			if self.closing_flag == False:
				pool.submit(self.show_cam_tree)
				self.info.set('刷新服务器成功')
				self.refresh_button['state'] = tk.NORMAL
				self.refresh_button.bind("<ButtonPress-1>", self.check_servers)

			dh_new_online, dh_new_offline = dh_check.result()
			hk_new_online, hk_new_offline = hk_check.result()

			cams, playbacks = self.check_playing_viedeo_status()

			print('dh_new_online', dh_new_online)
			print('dh_new_offline', dh_new_offline)

			print('hk_new_online', hk_new_online)
			print('hk_new_offline', hk_new_offline)
			print(cams, playbacks)

			for win in cams.keys():
				desc, server, channel, handel = cams[win]
				if (desc in dh_new_offline) or (desc in hk_new_offline):
					print('检测到服务器掉线，准备播放录像')
					server.Stop_Play_Cam(handel)
					self.window_status[win] = [desc, server, channel, 'playback']
					self.get_window_wdiget(win)['bg'] = VIDEO_DEFAULT_COLOR
					self.refresh_video_states()

			for win in playbacks.keys():
				desc, server, channel, handel = playbacks[win]
				if (desc in dh_new_online) or (desc in hk_new_online):
					print('检测服务器上线，并准备播放实时摄像头')
					if 'haikang' in desc:
						self.play_hk_cam(desc, server, channel, win, self.get_window_hwnd(win))
						self.refresh_video_states()
					if 'dahua' in desc:
						self.play_dh_cam(desc, server, channel, win, self.get_window_hwnd(win))
						self.refresh_video_states()

		pool = ThreadPoolExecutor(max_workers=3)
		pool.submit(do)

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

		print(login)
		self.float_window.quit()
		self.root.quit()
		try:
            exit()
        except Exception as e
            pass
                
		print('destory')


def start():
	app = my_app()
	app.root.mainloop()

login=tk_login(my_func=start)
login.main_window.mainloop()


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

