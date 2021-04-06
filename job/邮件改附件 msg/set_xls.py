# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/4/6 0006 下午 5:17
# Tool ：PyCharm

import xlrd
import xlwt


import win32com.client as wc  # wc这个别名好像不太好, 嘿嘿
from win32com.client import constants
import os

# file=os.path.abspath('./demo.xls')
# excel = wc.Dispatch("Excel.Application")
# excel.Visible=1
# x=excel.Workbooks.Open(file)
# print(x.author)
# x.Author = "Jean Selva"
# print(x.Author)
# print(x)
# x.Save()

a=xlrd.open_workbook('./demo.xls')

print(xlwt.Workbook.save(a))