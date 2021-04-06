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

file=os.path.abspath('./demo.xls')
excel = wc.Dispatch("Excel.Application")
# excel.Visible=1
x=excel.Workbooks.Open(file)
print(x.author)
sht = x.Worksheets('Sheet1')
x.Author = "Jean Selva"
print(x.BuiltinDocumentProperties("Last author").value)
print(x.BuiltinDocumentProperties("Last save time").value)
print(x.BuiltinDocumentProperties("Creation date").value)

x.Save()

