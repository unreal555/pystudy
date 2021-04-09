# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/4/6 0006 上午 9:37
# Tool ：PyCharm

import win32com.client as wc
import os,shutil
import set_xlsx_user
import set_xls_user
from stupid_set_xlsx_username import clean_dir

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
		print('共有',msg.Attachments.Count,'个附件')
		xls_count=0
		xlsx_count=0
		count=0
		all={}
		for att in msg.Attachments:
			fujian_dir = os.path.join(tempdir, str(att.Index))
			fujian=os.path.join(fujian_dir, att.FileName)
			if not os.path.exists(fujian_dir):
				os.makedirs(fujian_dir)
			print('储存', att.Index, att.FileName, fujian)
			all[att.Index]=fujian
			att.SaveAsFile(fujian)
		print(all)

		for index in range(msg.Attachments.Count,0,-1):
			print('删除附件',index)
			msg.Attachments.Remove(index)

		for index in all.keys():
			file=all[index]
			if str.lower(file[-5:])=='.xlsx':
				set_xlsx_user.do(file)
				msg.Attachments.Add(file)
				xlsx_count+=1
				print('添加修改完的附件',file)

			elif str.lower(file[-4:])=='.xls':
				set_xls_user.do(file)
				msg.Attachments.Add(file)
				xls_count += 1
				print('添加修改完的附件', file)
			else:
				print('添加不需要处理的附件', file)
				msg.Attachments.Add(file)

			print('删除temp目录缓存的附件',file)
			os.remove(file)

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
		print('处理完邮件',infile,'\r\n')

del outlook
try:
	clean_dir((tempdir))
except Exception as e:
	print(e)




