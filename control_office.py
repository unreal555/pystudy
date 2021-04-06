# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/4/6 0006 上午 9:37
# Tool ：PyCharm

import win32com.client as win32

# file=r'C:\Users\Administrator\Desktop\新建文件夹\demo.xls'
#
# excel = win32.gencache.EnsureDispatch('Excel.Application')
# wb = excel.Workbooks.Open(file)
#
# wb.SaveAs(file+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
# wb.Close()                               #FileFormat = 56 is for .xls extension
# excel.Application.Quit()

file=r'C:/Users/Administrator/Desktop/新建文件夹/demo.msg'

fujian=r'C:/Users/Administrator/Desktop/新建文件夹/demo.xlsx'

outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")
msg = outlook.OpenSharedItem(file)

print(msg.Attachments.Count)
for att in msg.Attachments:
	print(att.FileName,att.Index)
	if '.xlsx' in att.FileName:
		print('删除附件',att.Index,att.FileName)
		msg.Attachments.Remove(att.Index)

msg.Attachments.Add(fujian)

print(msg.Attachments.Count)
for att in msg.Attachments:
	print(att.FileName)


msg.SaveAs(r'd:/test.msg')
# print(msg.)
# msg.close()
# outlook.close()