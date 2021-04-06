# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/4/6 0006 下午 5:17
# Tool ：PyCharm

import win32com.client as win32
import os

file=os.path.abspath('./demo.xls')
excel = win32.Dispatch("Excel.Application")
excel.Visible=1
x=excel.Workbooks.Open(file)

print(x)


