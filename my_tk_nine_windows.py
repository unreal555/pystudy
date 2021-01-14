# coding:utf-8
# ﻿ Team : JiaLiDun University
# Author：zl
# Date ：2020/9/30 0030 上午 9:39
# Tool ：PyCharm

import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

default_color = '#bcbcbc'
VIDEO_DEFAULT_COLOR = '#acbcbc'

from my_icon import set_icon



class my_app():

	def __init__(self):
		self.root = Tk()

		set_icon(self.root)

		self.root.title('Player')
		self.root['bd']=0
		self.root['bg'] = default_color
		self.root.attributes("-alpha", 0.9)
		#self.root.resizable(0, 0)  # 设置窗口大小不可变
		self.root.overrideredirect(False)
		max_x,max_y=self.root.maxsize()
		self.root.geometry("%sx%s+%s+%s"%(int(max_x*0.9),int(max_y*0.9),int(max_x*0.05),int(max_y*0.02)))

		self.float_window = tk.Toplevel()
		self.float_window.geometry('1x1')
		self.float_label=Label(self.float_window)
		self.float_window.attributes("-alpha", 0.5)  # 透明度(0.0~1.0)
		self.float_window.overrideredirect(True)  # 去除窗口边框
		self.float_window.attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
		self.float_window.attributes("-topmost", True)

		self.window_des = [('单窗口', 1), ('四窗口', 4), ('九窗口', 9)]

		self.v_num = IntVar()
		self.v_num.set(9)

		self.info = StringVar()
		self.info.set('初始化中......')

		self.is_single_playing = False

		self.now_hwnd = -1
		self.now_window_name = -1
		self.now_window_widget = -1

		self.closing_flag = False

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
	#	self.refresh_button.bind("<ButtonPress-1>", self.check_servers)

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

		self.image = tk.PhotoImage(file="./pic/fenge_line.png")
		self.hide_button= tk.Button(self.hide_area,width=5,text='showing',bg='gray',image=self.image)
		self.hide_button.pack(side=tk.LEFT, anchor=tk.S, expand=tk.NO, fill=tk.BOTH)
		self.hide_button.bind("<ButtonPress-1>",self.on_click_hide_cam_tree_area)
		self.hide_button.bind("<Enter>",self.on_mouse_enter_hidden_button)
		self.hide_button.bind("<Leave>", self.on_mouse_leave_hidden_button)
		self.hide_button.bind("<Enter>", self.on_mouse_enter_hidden_button)

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

		self.show_window()

		self.root.bind('<KeyPress-Escape>',self.on_click_esc)

		self.now_hwnd = self.video_play_1.winfo_id()

		self.now_window_name = self.video_play_1.winfo_class()

		self.now_window_widget = self.video_play_1

		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

		self.last_init(event='')


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
		x=event.x_root
		y=event.y_root
		self.float_label['text']='隐藏左侧'
		self.float_label.pack()
		self.float_window.geometry('%sx%s+%s+%s'%(50,15,x,y))
		#self.hide_button['bg']='black'

	def on_mouse_leave_hidden_button(self,event):
		self.hide_button['bg'] = 'white'
		self.float_label['text'] = ''
		self.float_window.geometry('%sx%s+%s+%s' % (0, 0, 0, 0))
		#self.float_label.pack_forget()




	def on_closing(self):
		if askokcancel("Quit", "Do you want to quit?"):
			self.__del__()


	def scale_mouse_click(self, event):
		x = event.x_root
		y = event.y_root
		self.root.attributes("-alpha", self.scale_bar.get() / 100)

	def get_time(self):
		return time.strftime('%Y-%m-%d %H:%M:%S')


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

		pass


	def on_click_play_cam(self, event):
		pass


	def rec_cam(self):
		pass

	def stop_rec_cam(self):
		pass

	def capture_cam(self, event):
		pass

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

		state = self.window_status[self.now_window_name]

		if state == 0:
			self.info.set('当前窗口为 {} ,空闲中'.format(self.now_window_name))
		else:
			pass


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




	def last_init(self, event):

		pass


	def show_cam_tree(self):

		pass


	def auto_check_servers(self):
		print('11111')


	def check_hk_servers(self):
		pass



	def __del__(self):
		print('程序退出,销毁')


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

