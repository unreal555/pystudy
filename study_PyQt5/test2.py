# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/2/8 0008 上午 9:46
# Tool ：PyCharm

'''
用掩码限制QLineEdit控件的输入

A    ASCII字母字符是必须输入的(A-Z、a-z)
a    ASCII字母字符是允许输入的,但不是必需的(A-Z、a-z)
N    ASCII字母字符是必须输入的(A-Z、a-z、0-9)
n    ASII字母字符是允许输入的,但不是必需的(A-Z、a-z、0-9)
X    任何字符都是必须输入的
x    任何字符都是允许输入的,但不是必需的
9    ASCII数字字符是必须输入的(0-9)
0    ASCII数字字符是允许输入的,但不是必需的(0-9)
D    ASCII数字字符是必须输入的(1-9)
d    ASCII数字字符是允许输入的,但不是必需的(1-9)
#    ASCI数字字符或加减符号是允许输入的,但不是必需的
H    十六进制格式字符是必须输入的(A-F、a-f、0-9)
h    十六进制格式字符是允许输入的,但不是必需的(A-F、a-f、0-9)
B    二进制格式字符是必须输入的(0,1)
b    二进制格式字符是允许输入的,但不是必需的(0,1)
>    所有的字母字符都大写
<    所有的字母字符都小写
!    关闭大小写转换
\    使用"\"转义上面列出的字符
'''

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QPushButton,QVBoxLayout,QGridLayout,QLabel,QLineEdit
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette,QPixmap,QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import Qt,QRegExp

class my(QWidget):
	def __init__(self):
		super(my, self).__init__()
		self.init(self)

	def init(self,argv):
		label1=QLabel()
		label1.setText("<font color=yellow>测试</font>")
		label1.setAutoFillBackground(True)
		palette=QPalette()
		palette.setColor(QPalette.Window,Qt.blue)
		label1.setPalette(palette)
		label1.setAlignment(Qt.AlignCenter)


		label2=QLabel()
		label2.setText("<a href=http://www.sohu.com>搜狐</a>")
		label2.setAutoFillBackground(True)
		label2.setOpenExternalLinks(True)
		palette.setColor(QPalette.Window,Qt.red)
		label2.setPalette(palette)

		label3=QLabel()
		label3.setAlignment(Qt.AlignCenter)
		label3.setToolTip('pic')
		label3.setPixmap(QPixmap('pic.png'))

		label1.linkHovered.connect(self.mouse_on)
		label2.linkHovered.connect(self.mouse_on)
		label3.linkHovered.connect(self.mouse_on)


		input1=QLineEdit()
		input1.setPlaceholderText('text')
		input1.setEchoMode(QLineEdit.Normal)
		input1.setInputMask('HH:HH:HH:HH:HH:HH;-')

		# reg=QRegExp('[-]{0,1}[a-zA-Z0-9]{1,3}')
		# validator = QRegExpValidator(reg)
		#
		# input1.setValidator(validator)

		vbox=QVBoxLayout()
		vbox.addWidget(label1)

		vbox.addWidget(label2)
		vbox.addWidget(label3)

		vbox.addWidget(input1)

		self.setLayout(vbox)
		self.setWindowTitle('text')



	def mouse_on(self):
		print(111)

if __name__ == '__main__':
	app=QApplication(sys.argv)
	window=my()
	window.show()
	app.exec_()