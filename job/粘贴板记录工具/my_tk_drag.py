# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/1/15 0015 上午 10:03
# Tool ：PyCharm
import os
import windnd

import tkinter
from tkinter.messagebox import askokcancel, showinfo

from my_img import my_icon_png
import base64
import my_icon

class drag_window():
	color='gray'#'#bcbcbc'

	def __init__(self,size=50):
		self.temp_dir = os.getenv('temp')
		self.icon_path = os.path.join(self.temp_dir, 'my_icon.png')
		with open(self.icon_path, 'wb') as f:
			f.write(base64.b64decode(my_icon_png))
		self.is_closing=False
		self.size=size
		self.root = tkinter.Tk()
		self.root.title('测试工具')
		self.root['bd'] = 1
		self.root['bg'] = self.color
		self.root.attributes("-alpha", 0.5)
		self.root.resizable(0, 0)  # 设置窗口大小不可变
		self.root.overrideredirect(True)  #直接屏幕上绘图，不要按钮边框		self.float_window.attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
		self.root.attributes("-topmost", True)
		my_icon.set_icon(self.root,my_icon.MY_PERSON_ICON)

		self.float_window = tkinter.Toplevel()
		self.float_window.geometry('1x1')
		self.float_label=tkinter.Label(self.float_window,text='拖动文件到图标\r右键退出')
		self.float_window.attributes("-alpha", 0.8)  # 透明度(0.0~1.0)
		self.float_window.overrideredirect(True)  # 去除窗口边框
		self.float_window.attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
		self.float_window.attributes("-topmost", True)

		self.max_x, self.max_y = self.root.maxsize()
		self.root.geometry("%sx%s+%s+%s"%(self.size,self.size,self.max_x-self.size,int(self.max_y*0.7)))

		self.img=tkinter.PhotoImage(file=self.icon_path)
		self.info_label=tkinter.Label(self.root,image=self.img,width=self.size,height=self.size,compound='center',font=('微软雅黑',16)
		                             ,fg='white')
		self.info_label.pack(side='bottom', fill=tkinter.BOTH, expand=tkinter.YES)

		self.menu = tkinter.Menu(self.root, tearoff=0,relief="groove")#"flat","sunken"，"raised"，"groove" 或 "ridge"
		self.menu.add_separator()
		self.menu.add_command(label="退出",command=self.on_click_exit)

		windnd.hook_dropfiles(self.root, func=self.drag_in_items)
		self.root.bind('<B1-Motion>',self.on_mouse_drag_window)
		self.root.bind('<ButtonPress-1>', self.on_mouse_left_button_press)
		self.root.bind('<Button-3>',self.on_mouse_right_button_press)
		#self.root.bind('<Enter>',self.on_mouse_enter_area_and_show_help)
		#self.root.bind('<Leave>', self.on_mouse_leave_area_and_hide_help)

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
		self.on_mouse_leave_area_and_hide_help(event)
		x=event.x_root-self.x
		y=event.y_root-self.y
		self.root.geometry("%sx%s+%s+%s"%(self.size,self.size,x,y))

	def on_mouse_right_button_press(self,event):
		self.menu.post(event.x_root,event.y_root)


	def __del__(self):
		self.root.quit()

	def on_mouse_enter_area_and_show_help(self,event):
		self.float_window.geometry('%sx%s+%s+%s' % (100, 30, event.x_root + 5, event.y_root + 5))
		self.float_label.pack()

	def on_mouse_leave_area_and_hide_help(self,event):
		self.float_window.geometry('%sx%s+%s+%s' % (0, 0, 0, 0))
		self.float_label.pack_forget()

	def on_click_exit(self):
		self.is_closing=True
		self.__del__()

if __name__ == '__main__':
	win=drag_window(size=50)
	win.root.mainloop()


'''
#<B1-Motion> 拖动左键触发事件
#<B2-Motion> 拖动中键触发事件
#<B3-Motion> 拖动右键触发事件
'''


