# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/3/31 0031 上午 9:46
# Tool ：PyCharm

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui import Ui_Form

class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.activated.connect(self.iconClicked)
        #把鼠标点击图标的信号和槽连接
        self.messageClicked.connect(self.mClicked)
        #把鼠标点击弹出消息的信号和槽连接
        self.setIcon(QIcon("ico.ico"))
        self.icon = self.MessageIcon()
        #设置图标
        self.showMenu()

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


    def iconClicked(self, reason):
        "鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        if reason == 2 or reason == 3:
            self.setVisible(False)
            self.parent().setVisible(True)
            self.parent().showNormal()

    def mClicked(self):
        self.showMessage("提示", "你点了消息", self.icon)

    def showM(self):
        self.showMessage("测试", "我是消息", self.icon)

    def quit(self):
        "保险起见，为了完整的退出"
        self.setVisible(False)
        self.destroy()
        self.parent().destroy()


class window(QWidget,Ui_Form):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ico.ico'))
        self.setWindowOpacity(0.8)
        self.setWindowFlags(Qt.FramelessWindowHint) #无边框
        self.setWindowFlags(Qt.WindowStaysOnTopHint) #置顶
        self.show()
        self.tray = TrayIcon(self)

    def hideEvent(self, QHideEvent):
        self.setVisible(False)
        self.tray.setVisible(True)
        
    def closeEvent(self, a0: QCloseEvent) -> None:
        self.destroy()
        self.tray.destroy()
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main = window()


    sys.exit(app.exec_())