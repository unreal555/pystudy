# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/2/8 0008 上午 9:46
# Tool ：PyCharm

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QPushButton,QVBoxLayout,QGridLayout
from PyQt5 import QtCore

def on_click(window,app):

    print(window.sender().text())

    app.quit()

app=QApplication(sys.argv)

window=QWidget()

window.setGeometry(0,0,400,300)

button=QPushButton('退出')
bbutton=QPushButton('退出')

layout=QGridLayout()

layout.setGeometry(QtCore.QRect(0, 0, 400, 300))

layout.addWidget(button,1,2)
layout.addWidget(bbutton,4,3)

window.setLayout(layout)

button.clicked.connect(lambda :on_click(window,app))

button.setToolTip('测试')



window.show()
app.exec_()
              
