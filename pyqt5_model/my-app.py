# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/3/30 0030 下午 4:38
# Tool ：PyCharm


import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QMessageBox


class App(QWidget):
    def __init__(self):
        super(App,self).__init__()
        self.initUI()

    def initUI(self):
        # self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('通用模型')
        self.setWindowIcon(QtGui.QIcon('ico.ico'))
        self.resize(400,300)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if QMessageBox.question(self,'关闭','确定要退出吗',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)==QMessageBox.Yes:
            a0.accept()
        else:
            a0.ignore()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

              
