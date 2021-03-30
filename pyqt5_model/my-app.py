# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/3/30 0030 下午 4:38
# Tool ：PyCharm


import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget


class App(QWidget):
    def __init__(self):
        super(App,self).__init__()
        self.initUI()


    def initUI(self):
        self = QWidget()
        # self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('通用模型')
        # self.setGeometry(800,600,800,600)
        self.setWindowIcon(QIcon('ico.ico'))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    app = App()
    app.show()
    sys.exit(app.exec_())

              
