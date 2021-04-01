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
        self.parent().exit()
        sys.exit()

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window,self).__init__(parent)

        self.setWindowIcon(QIcon('ico.ico'))
        self.tray = TrayIcon(self)
        self.setWindowOpacity(0.9)
        self.setWindowFlags(Qt.FramelessWindowHint) #无边框
        self.setWindowFlags(Qt.WindowStaysOnTopHint) #置顶
        #self.setAttribute(Qt.WA_TranslucentBackground)  #彻底透明

        palette1 = QPalette()
        palette1.setColor(palette1.Background,QColor(0,0,0))
        self.setPalette(palette1)

        layout=QHBoxLayout()
        self.setLayout(layout)

        sd = QSlider(self)
        self.sd = sd
        sd.setMaximum(200)
        sd.setMinimum(100)

        sd.setSingleStep(2)  # 设置步长
        sd.setPageStep(5)  # 设置翻页步长，使用PageUp PageDown
        sd.setTracking(True)
        # sd.setValue(101)  # 设置数值
        sd.setSliderPosition(199)  # 设置滑块位置
        # sd.setInvertedAppearance(True)  # 反转外观
        # sd.setInvertedControls(True)  # 反转操作，
        sd.setOrientation(Qt.Horizontal)
        self.sd.setTickPosition(QSlider.TicksBothSides)
        self.sd.setTickInterval(5)
        self.sd.setPageStep(5)  # 设置翻页步长，也会顺带调整刻度线密度


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