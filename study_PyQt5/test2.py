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

label=QPushButton('退出')

layout=QVBoxLayout()

layout.addWidget(label)

window.setLayout(layout)

label.clicked.connect(lambda :on_click(window,app))



window.show()
app.exec_()
              
