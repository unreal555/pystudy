# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/1/26 0026 上午 8:54
# Tool ：PyCharm

import base64
import os


for file in os.listdir('.'):
	file=str.lower(file)
	if  '.jpg' in file or '.bmp' in file or '.bmp' in file or '.png' in file:
		with open (file,'rb') as f:
			img=f.read()
		content=base64.b64encode(img).decode()
		print(file,content)

		with open('img.py','a',encoding='utf-8') as f:
			f.write(file.replace('.','_').replace('-','_')+'='+'b\''+content+'\'')
			f.write('\r\n')
                  
