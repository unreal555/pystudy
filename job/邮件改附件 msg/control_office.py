# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/4/6 0006 上午 9:37
# Tool ：PyCharm

import win32com.client as win32
import os,shutil
import set_xlsx_user


# file=r'C:\Users\Administrator\Desktop\新建文件夹\demo.xls'
#
# excel = win32.gencache.EnsureDispatch('Excel.Application')
# wb = excel.Workbooks.Open(file)
#
# wb.SaveAs(file+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
# wb.Close()                               #FileFormat = 56 is for .xls extension
# excel.Application.Quit()

basedir=r'.\source'

basedir=os.path.abspath(basedir)

tempdir=os.path.join(basedir,'tempd')

finisheddir=os.path.join(basedir,'finished')

tododir=os.path.join(basedir,'tododir')

if not os.path.exists(tempdir):
	os.makedirs(tempdir)

if not os.path.exists(finisheddir):
	os.makedirs(finisheddir)

if not os.path.exists(tododir):
	os.makedirs(tododir)

n=10000
for infile in os.listdir(basedir):

	if str.lower(os.path.splitext(infile)[1]) in ['.msg']:
		print('开始处理',infile)
		outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")
		workfile=os.path.join(tempdir,'demo{}.msg'.format(n))
		shutil.copy(os.path.join(basedir,infile),workfile)
		msg = outlook.OpenSharedItem(workfile)
		print(msg.Attachments.Count)
		flag=0

		for att in msg.Attachments:
			print(att.FileName,att.Index)

			if str.lower(att.FileName[-5:])=='.xlsx':
				fujian=os.path.join(tempdir,att.FileName)
				print(fujian)
				att.SaveAsFile(fujian)
				set_xlsx_user.do(fujian)
				print('删除附件',att.Index,att.FileName)
				msg.Attachments.Remove(att.Index)
				msg.Attachments.Add(fujian)
				flag+=1



		if flag>0:
			msg.SaveAs(os.path.join(finisheddir, infile))
			os.remove(fujian)
		if flag==0:
			shutil.copy(workfile,os.path.join(tododir,infile))
		msg.Close(1)
		del msg
		del outlook
		n+=1


	print('\r\n')



