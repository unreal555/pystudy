# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/2/7 0007 上午 9:42
# Tool ：PyCharm

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QLabel,QHBoxLayout,QVBoxLayout ,QDesktopWidget,QPushButton
import time
class my_win(QMainWindow):
    def __init__(self):
        super(my_win,self).__init__()

        w,h=QDesktopWidget().geometry().width(),QDesktopWidget().geometry().height()

        print(w,h)

        self.resize(400,300)

        w1,h1=self.geometry().width(),self.geometry().height()

        print(w1,h1)

        print(int((w-w1)/2),int((h-h1)/2))

        self.move(int((w-w1)/2),int((h-h1)/2))

        self.statusBar().showMessage('2222',2000)

        self.button=QPushButton()
        self.button.setText('退出')
        layout=QVBoxLayout()
        layout.addWidget(self.button)
        mainframe=QWidget()
        mainframe.setLayout(layout)

        self.setCentralWidget(mainframe)

        self.button.clicked.connect(self.close)




    def close(self):
        sender=self.sender()
        print(sender.enterEvent())
        QApplication.instance().quit()




if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=my_win()
    win.show()
    sys.exit(app.exec_())
