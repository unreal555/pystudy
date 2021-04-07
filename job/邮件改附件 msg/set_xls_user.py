# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/4/6 0006 下午 5:17
# Tool ：PyCharm

import win32com.client as wc  # wc这个别名好像不太好, 嘿嘿
import os
import re
import my_system_tools


def do(file):
	file=os.path.abspath(file)
	excel = wc.Dispatch("Excel.Application")
	excel.Visible=1
	x=excel.Workbooks.Open(file)
	# print(x.Author)
	# sht = x.Worksheets('Sheet1')
	author=x.BuiltinDocumentProperties("author").value
	last_author=x.BuiltinDocumentProperties("Last author").value
	create_date=x.BuiltinDocumentProperties("Creation date").value
	last_save_date=x.BuiltinDocumentProperties("Last save time").value
	print(author)
	print(last_author)
	print(create_date)
	print(last_save_date)

	if not author=='':
		x.BuiltinDocumentProperties("author").value='Administraotor'

	if not last_author=='':
		x.BuiltinDocumentProperties("Last author").value = 'Administraotor'

	#my_system_tools.set_time()
	print(type(last_save_date))
	year,month,day,hour,min,sec,aaa,aaa=re.split(r'[ \:\-\+]',str(last_save_date))
	my_system_tools.set_date(year,month,day)
	my_system_tools.set_time(hour,min,sec)
	x.Save()
	x.Close()
	my_system_tools.auto_set_date_time()

if __name__ == '__main__':
	file = os.path.abspath(r'C:\Users\Administrator\Desktop\新建文件夹/demo.xls')
	do(file=file)