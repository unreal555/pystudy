# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/3/31 0031 上午 9:46
# Tool ：PyCharm

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from ui import Ui_Form
import re

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
    filetype = '*.mp4 *.avi'
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ico.ico'))
        self.setWindowOpacity(0.8)
        self.tray = TrayIcon(self)
    
        self.PlayArea=QVideoWidget(self.PlayAreaGroupBox)
        self.horizontalLayout.addWidget(self.PlayArea)

        self.player=QMediaPlayer()
        self.player.setVideoOutput(self.PlayArea)
        self.moviePath=''
        self.movie=''
        self.movieDuration=''
        self.vol=100
        self.mousePos=''

        self.OnTopCheckBox.toggled.connect(self.setStayOnTop)
        self.FrameLessCheckBox.toggled.connect(self.setFrameLess)
        self.player.durationChanged.connect(self.getDuration)
        
        self.show()
    
    
    def setFrameLess(self):
        self.hide()
        if  self.FrameLessCheckBox.isChecked():
            self.setWindowFlags(Qt.FramelessWindowHint) #无边框
        else:
            self.setWindowFlag(Qt.Window)
        self.show()
        # self.tray.hide()
        
    def loadFlie(self):
        pass

    def ms2HMS(self, ms):
        playtime = ms / 1000
        h = int(playtime // 3600)
        m = int((playtime - h * 3600) // 60)
        s = int(playtime - h * 3600 - m * 60)
        return ms, h, m, s

    def getDuration(self):
        '''
		QT中，使用QMediaplayer类可以很方便地实现视频的播放，而在QMediaplayer类中有个duration函数可以直接获取所打开视频的总时间长度。但使用后你会发现duration（）返回的居然是个0。
        在初始回放开始时可能不可用，请连接durationChanged()信号以接收状态通知。
		即我们只需要写个槽函数，在槽函数里面调用duration（）就可以接收到正确的时间
		'''
        ms = self.player.duration()
        ms, h, m, s = self.ms2HMS(ms=ms)
        print(ms, h, m, s)
        return ms, h, m, s
    
    def isMatchFileType(self, s):        #判断拖入窗体的文件是否为filetype定义的类型
        file, ext = os.path.splitext(s)
        # print(file,ext,[str.lower(x) for x in re.split(        ' ', self.fileType)])
        if str.lower(ext) in [str.lower(x.replace('*', '')) for x in re.split(' ',self.fileType)]:
            return True
        else:
            return False

    def dragEnterEvent(self, e: QDragEnterEvent):      #接受，或拒绝拖入窗体的文件
        if self.Pages.currentIndex() != 0:
            e.ignore()
            return

        if e.mimeData().hasText():
            txt = e.mimeData().text()
            print(txt)
            if self.isMatchFileType(txt):
                print('accept')
                e.accept()

    def dropEvent(self, e):       #处理拖入窗体的文件
        print('drop')
        txt = e.mimeData().text()
        txt = re.sub('file:[/]+', '', txt)
        abspath = os.path.abspath(txt)
        path, file = os.path.split(abspath)
        filename, ext = os.path.splitext(file)
        self.workfile = os.path.join(self.temp_dir, file)
        self.temp_file1 = os.path.join(self.temp_dir, filename + '-temp1' + ext)
        self.temp_file2 = os.path.join(self.temp_dir, filename + '-temp2' + ext)
        shutil.copy(abspath, self.workfile)
        self.lineEdit.setText(abspath)
        self.lineEdit.setDisabled(True)
        self.do()
        self.toSingleOutput(content='检测到文件输入:{},处理'.format(abspath))
        
    @pyqtSlot()
    def on_OpenPushButton_clicked(self):
        path,_=QFileDialog.getOpenFileName(None, caption='打开', directory='c:/', filter=self.filetype)
        self.moviePath=QUrl.fromLocalFile(path)
        self.movie = QMediaContent(self.moviePath)
        self.player.setMedia(self.movie)
        self.play()
        
    def mousePressEvent(self, a0: QMouseEvent) -> None:
        print('press')
        print(a0.globalPos())
        print(a0.pos())
        print(a0.screenPos())
        self.mousePos=a0.screenPos()
        
    def on_VolPushButton_released(self):
        
        x=self.VolPushButton.pos().x()
        y=self.VolPushButton.pos().y()
        print(self.groupBox.geometry())
        pos=QPoint(x+30,self.groupBox.geometry().y()+y-100+15)

        OpacitySlider = QSlider(self)
        OpacitySlider.resize(20,100)
        OpacitySlider.move(pos)
        OpacitySlider.setMinimum(0)
        OpacitySlider.setMaximum(100)
        OpacitySlider.setProperty("value", self.vol)
        OpacitySlider.setOrientation(Qt.Vertical)
        OpacitySlider.setInvertedAppearance(False)
        OpacitySlider.setInvertedControls(False)
        OpacitySlider.setTickPosition(QSlider.TickPosition.TicksRight)
        OpacitySlider.setTickInterval(10)
        OpacitySlider.show()
        
    
    def play(self,pos=0):
        self.player.setPosition(pos) # to start at the beginning of the video every time)
        self.player.play()


    def setStayOnTop(self,f=True):
        self.hide()
        if self.OnTopCheckBox.isChecked():
            print('置顶')
            self.setWindowFlags(Qt.WindowStaysOnTopHint) #置顶
        else:
            print('取消置顶')
            self.setWindowFlag(Qt.Widget)
        self.show()

    def hideEvent(self, a0:QHideEvent):
        print(a0)
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