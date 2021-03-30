# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/3/30 0030 下午 3:23
# Tool ：PyCharm
import sys
from ui import Ui_Form
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
from PyQt5 import QtGui


class Moniter(QWidget,Ui_Form):

    def __init__(self):
        super(Moniter, self).__init__()
        self.setupUi(self)



    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if QMessageBox.question(self,'关闭','是否退出程序',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes) ==QMessageBox.Yes:
            a0.accept()
        else:
            a0.ignore()


app=QApplication(sys.argv)
window=Moniter()
window.show()
sys.exit(app.exec_())