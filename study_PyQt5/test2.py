# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/2/8 0008 上午 9:46
# Tool ：PyCharm

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QPushButton,QVBoxLayout

def on_click(window,app):

    print(window.sender().text())

    app.quit()

app=QApplication(sys.argv)

window=QWidget()

window.setGeometry(0,0,400,300)
button=QPushButton('退出')

layout=QVBoxLayout()

layout.addWidget(button)

window.setLayout(layout)

button.clicked.connect(lambda :on_click(window,app))

button.setToolTip('测试')



window.show()
app.exec_()
              
