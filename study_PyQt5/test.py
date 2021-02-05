# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/2/5 0005 上午 9:27
# Tool ：PyCharm

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QPushButton,QHBoxLayout
from PyQt5.QtGui import QIcon

class my_test(QMainWindow):
    print(0)
    def __init__(self):

        super(my_test,self).__init__()
        self.setWindowTitle('test')
        self.resize(400,300)
        self.button=QPushButton()
        self.button.setText('退出')
        self.setMouseTracking(True)

        self.button.clicked.connect(self.OnClickButton)

        Hlayout=QHBoxLayout()
        Hlayout.addWidget(self.button)

        centerframe=QWidget()
        centerframe.setLayout(Hlayout)
        centerframe.setMouseTracking(True)

        self.setCentralWidget(centerframe)

    def OnClickButton(self):
        sender=self.sender()
        print(sender.text(),'click')
        instance=QApplication.instance()
        instance.quit()

    def mouseEnter(self,event):
        print('进入')

    def mouseMoveEvent(self,e):


        print(e.x(),e.y())


if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('my-icon.ico'))
    win=my_test()
    win.show()
    sys.exit(app.exec_())
