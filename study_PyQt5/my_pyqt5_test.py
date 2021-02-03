# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/2/2 0002 上午 9:23
# Tool ：PyCharm

import sys
from frist import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
	app=QApplication(sys.argv)
	mainwindow=QMainWindow()
	ui= Ui_MainWindow()
	ui.setupUi(mainwindow)
	mainwindow.show()
	sys.exit(app.exec_())
