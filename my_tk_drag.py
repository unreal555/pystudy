# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/1/15 0015 上午 10:03
# Tool ：PyCharm


import tkinter, os
from tkinter.messagebox import askokcancel, showinfo

import windnd
from my_icon import set_icon

import time

from threading import Thread

class drag_window():
	color='gray'#'#bcbcbc'
	pic_path = './pic/my-icon.png'
	print(os.path.abspath('.'))
	def __init__(self,size=50):
		self.size=size
		self.root = tkinter.Tk()
		self.root.title('测试工具')
		self.root['bd'] = 1
		self.root['bg'] = self.color
		self.root.attributes("-alpha", 0.5)
		self.root.resizable(0, 0)  # 设置窗口大小不可变
		self.root.overrideredirect(True)  #直接屏幕上绘图，不要按钮边框		self.float_window.attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
		self.root.attributes("-topmost", True)
		set_icon(self.root)

		self.float_window = tkinter.Toplevel()
		self.float_window.geometry('1x1')
		self.float_label=tkinter.Label(self.float_window,text='拖动文件到图标上松手执行\r左键三击或者右键退出')
		self.float_window.attributes("-alpha", 0.8)  # 透明度(0.0~1.0)
		self.float_window.overrideredirect(True)  # 去除窗口边框
		self.float_window.attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
		self.float_window.attributes("-topmost", True)


		self.max_x, self.max_y = self.root.maxsize()
		self.root.geometry("%sx%s+%s+%s"%(self.size,self.size,self.max_x-self.size,int(self.max_y*0.7)))

		self.img=tkinter.PhotoImage(file=self.pic_path)
		self.info_label=tkinter.Label(self.root,width=self.size,image=self.img,height=self.size)
		self.info_label.pack(side='bottom', fill=tkinter.BOTH, expand=tkinter.YES)

		self.menu = tkinter.Menu(self.root, tearoff=0,relief="groove")#"flat","sunken"，"raised"，"groove" 或 "ridge"
		self.menu.add_separator()
		self.menu.add_command(label="退出",command=self.on_click_exit)

		windnd.hook_dropfiles(self.root, func=self.drag_in_items)
		self.root.bind('<B1-Motion>',self.on_mouse_drag_window)
		self.root.bind('<ButtonPress-1>', self.on_mouse_left_button_press)
		self.root.bind('<Button-3>',self.on_mouse_right_button_press)
		self.root.bind(('<Double-Button-3>',self.on_mouse_right_button_press))

		self.root.bind('<Enter>',self.on_mouse_enter_area_and_show_help)
		self.root.bind('<Leave>', self.on_mouse_leave_area_and_hide_help)


	def drag_in_items(self,items):
		files=[]
		folders=[]
		for item in items:
			item=item.decode('gbk')
			print(items)
			if os.path.isfile(item):
				print('file')
				files.append(item)
			if os.path.isdir(item):
				print('folder')
				folders.append(item)
		print(files+folders)
		showinfo('info:%s files,%s folders'%(len(files),len(folders)),'\r'.join(files+folders))

	def on_mouse_left_button_press(self,event):
		self.x=event.x
		self.y=event.y

	def on_mouse_drag_window(self,event):
		x=event.x_root-self.x
		y=event.y_root-self.y
		print(x,y)
		print(self.size)
		self.root.geometry("%sx%s+%s+%s"%(self.size,self.size,x,y))

	def on_mouse_right_button_press(self,event):
		self.menu.post(event.x_root,event.y_root)


	def __del__(self):
		self.root.destroy()

	def on_mouse_enter_area_and_show_help(self,event):

		def do():
			time.sleep(1)
			self.float_label.pack()
			self.float_window.geometry('%sx%s+%s+%s' % (150, 30, event.x_root,event.y_root))
			return

		t=Thread(target=do)
		t.setDaemon(True)
		t.start()

	def on_mouse_leave_area_and_hide_help(self,event):
		self.float_window.geometry('%sx%s+%s+%s' % (0, 0, 0, 0))
		self.float_label.pack_forget()



	def on_click_exit(self):
		self.__del__()






if __name__ == '__main__':
	win=drag_window(size=50)
	win.root.mainloop()



'''
#<B1-Motion> 拖动左键触发事件
#<B2-Motion> 拖动中键触发事件
#<B3-Motion> 拖动右键触发事件
'''


