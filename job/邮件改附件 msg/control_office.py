# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/4/6 0006 上午 9:37
# Tool ：PyCharm

import win32com.client as wc
import os,shutil
import set_xlsx_user
import set_xls_user

basedir=r'C:\Users\Administrator\Desktop\source'

basedir=os.path.abspath(basedir)

tempdir=os.path.join(basedir,'tempd')

bothdir=os.path.join(basedir,'bothdir')

xlsxdir=os.path.join(basedir,'xlsxdir')

xlsdir=os.path.join(basedir,'xlsdir')

if not os.path.exists(tempdir):
	os.makedirs(tempdir)

if not os.path.exists(xlsxdir):
	os.makedirs(xlsxdir)

if not os.path.exists(xlsdir):
	os.makedirs(xlsdir)

if not os.path.exists(bothdir):
	os.makedirs(bothdir)

outlook = wc.Dispatch("Outlook.Application").GetNamespace("MAPI")

n=10000

for infile in os.listdir(basedir):

	if str.lower(os.path.splitext(infile)[1]) in ['.msg']:
		print('开始处理',infile)
		workfile=os.path.join(tempdir,'demo{}.msg'.format(n))
		shutil.move(os.path.join(basedir,infile),workfile)
		msg = outlook.OpenSharedItem(workfile)
		print(msg.Attachments.Count)
		xls_count=0
		xlsx_count=0
		for att in msg.Attachments:
			print(att.FileName,att.Index)
			fujian=''
			if str.lower(att.FileName[-5:])=='.xlsx':
				fujian=os.path.join(tempdir,att.FileName)
				print(fujian)
				att.SaveAsFile(fujian)
				set_xlsx_user.do(fujian)
				print('删除附件',att.Index,att.FileName)
				msg.Attachments.Remove(att.Index)
				msg.Attachments.Add(fujian)
				xlsx_count+=1

				if os.path.isfile(fujian):
					os.remove(fujian)

			elif str.lower(att.FileName[-4:])=='.xls':
				fujian=os.path.join(tempdir,att.FileName)
				print(fujian)
				att.SaveAsFile(fujian)
				set_xls_user.do(fujian)
				print('删除附件',att.Index,att.FileName)
				msg.Attachments.Remove(att.Index)
				msg.Attachments.Add(fujian)
				xls_count += 1

				if os.path.isfile(fujian):
					os.remove(fujian)

			print('\r\n')

		if xlsx_count>0 and xls_count>0:
			msg.SaveAs(os.path.join(bothdir, infile))

		elif xlsx_count>0:
			msg.SaveAs(os.path.join(xlsxdir, infile))

		elif xls_count>0:
			msg.SaveAs(os.path.join(xlsdir, infile))

		elif xls_count==0 and xlsx_count==0:
			msg.SaveAs(os.path.join(basedir, infile))

		msg.Close(1)

		del msg

		n+=1
		print('\r\n')

del outlook





