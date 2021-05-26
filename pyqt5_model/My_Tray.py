# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/3/31 0031 上午 9:46
# Tool ：PyCharm

import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui import Ui_Form

class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.showMenu()
        self.other()

    def showMenu(self):
        "设计托盘的菜单，这里我实现了一个二级菜单"
        self.menu = QMenu()
        self.menu1 = QMenu()
        self.showAction1 = QAction("显示消息1", self, triggered=self.showM)
        self.showAction2 = QAction("显示消息2", self,triggered=self.showM)
        self.quitAction = QAction("退出", self, triggered=self.quit)

        self.menu1.addAction(self.showAction1)
        self.menu1.addAction(self.showAction2)
        self.menu.addMenu(self.menu1, )

        self.menu.addAction(self.showAction1)
        self.menu.addAction(self.showAction2)
        self.menu.addAction(self.quitAction)
        self.menu1.setTitle("二级菜单")
        self.setContextMenu(self.menu)

    def other(self):
        self.activated.connect(self.iconClied)
        #把鼠标点击图标的信号和槽连接
        self.messageClicked.connect(self.mClied)
        #把鼠标点击弹出消息的信号和槽连接
        self.setIcon(QIcon("ico.ico"))
        self.icon = self.MessageIcon()
        #设置图标

    def iconClied(self, reason):
        "鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        if reason == 2 or reason == 3:

            self.setVisible(False)
            self.parent().setVisible(True)
            self.parent().showNormal()
        print(reason)

    def mClied(self):
        self.showMessage("提示", "你点了消息", self.icon)

    def showM(self):

        self.showMessage("测试", "我是消息", self.icon)

    def quit(self):
        "保险起见，为了完整的退出"
        self.setVisible(False)
        self.destroy()
        self.parent().destroy()

class Window(QWidget,Ui_Form):
    def __init__(self, parent=None):
        super(Window,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ico.ico'))
        self.tray = TrayIcon(self)
        self.setWindowOpacity(0.8)
        self.setWindowFlags(Qt.FramelessWindowHint) #无边框
        self.setWindowFlags(Qt.WindowStaysOnTopHint) #置顶
        #self.setAttribute(Qt.WA_TranslucentBackground)  #彻底透明
        self.setWindowTitle('图形界面范例')
        self.resize(1024,768)


        self.horizontalScrollBar.setMaximum(100)
        self.horizontalScrollBar.setMinimum(40)
        self.horizontalScrollBar.setValue(80)

        self.horizontalScrollBar.valueChanged.connect(self.changePactiy)

    def changePactiy(self,value):

        self.setWindowOpacity(value/100)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.palette = QPalette()
        self.pix = QPixmap("./resource/beauty.jpg")
        self.palette.setBrush(QPalette.Background, QBrush(self.pix.scaled(self.width(),self.height())))
        self.setPalette(self.palette)


    def paintEvent(self, event):  # set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./img/1.jpg")  # 换成自己的图片的相对路径
        painter.drawPixmap(self.rect(), pixmap)


    def hideEvent(self, QHideEvent):
        self.setVisible(False)
        self.tray.setVisible(True)

    def closeEvent(self, a0: QCloseEvent) -> None:
        if QMessageBox.warning(self,'关闭','Yes关闭，No最小化',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)==QMessageBox.Yes:
            a0.accept()
            self.children().exit()
        else:
            a0.ignore()
            self.hideEvent(QHideEvent)



class RunThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(1,1000):
            time.sleep(1)
            print(i,)




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main = Window()
    main.showNormal()
    print(main)
    sys.exit(app.exec_())