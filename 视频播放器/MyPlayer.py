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
import re,os


class TrayIcon(QSystemTrayIcon):
	def __init__(self, parent=None):
		super(TrayIcon, self).__init__(parent)
		self.activated.connect(self.iconClicked)
		# 把鼠标点击图标的信号和槽连接
		self.messageClicked.connect(self.mClicked)
		# 把鼠标点击弹出消息的信号和槽连接
		self.setIcon(QIcon("ico.ico"))
		self.icon = self.MessageIcon()
		# 设置图标
		self.showMenu()
	
	def showMenu(self):
		"设计托盘的菜单，这里我实现了一个二级菜单"
		self.menu = QMenu()
		self.menu1 = QMenu()
		self.showAction1 = QAction("显示消息1", self, triggered=self.showM)
		self.showAction2 = QAction("显示消息2", self, triggered=self.showM)
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


class window(QWidget, Ui_Form):
	fileType = '*.mp4 *.avi'
	
	def __init__(self, parent=None):
		super(window, self).__init__(parent)
		self.setupUi(self)
		self.setWindowIcon(QIcon('ico.ico'))
		self.setWindowOpacity(0.8)
		self.tray = TrayIcon(self)
		self.resize(800,500)
		self.op = QGraphicsOpacityEffect()
		self.op.setOpacity(0.5)
		
		self.PlayArea = QVideoWidget(self.PlayAreaGroupBox)
		self.horizontalLayout.addWidget(self.PlayArea)
		self.PlayArea.enterEvent = self.showProcessSlider
		self.PlayArea.mousePressEvent = self.showProcessSlider
		self.PlayArea.setAcceptDrops(True)
		self.PlayArea.dragEnterEvent=self.dragEnterEvent
		self.PlayArea.dropEvent=self.dropEvent
		self.PlayArea.wheelEvent = self.mouseSetVol

		
		self.player = QMediaPlayer()
		self.player.setVideoOutput(self.PlayArea)
		self.moviePath = ''
		self.movie = ''
		self.movieDuration = 1
		self.vol = 100
		self.mousePos = ''
		
		self.VolSlider = QSlider(self)
		self.VolSlider.resize(20, 120)
		self.VolSlider.hide()
		self.VolSlider.leaveEvent = self.leaveVolPushButtonEvent
		self.VolSlider.valueChanged.connect(self.setVol)
		self.VolSlider.setGraphicsEffect(self.op)
		self.VolSlider.setAutoFillBackground(True)
		
		self.ProcessSlider = QSlider(self)
		self.ProcessSlider.setOrientation(Qt.Horizontal)
		self.ProcessSlider.hide()
		self.ProcessSlider.leaveEvent = self.hideProcessSlider
		self.ProcessSlider.valueChanged.connect(self.move2Position)
		self.ProcessSlider.setGraphicsEffect(self.op)
		self.ProcessSlider.setAutoFillBackground(True)
		
		self.OnTopCheckBox.toggled.connect(self.setStayOnTop)
		self.FrameLessCheckBox.toggled.connect(self.setFrameLess)
		self.player.durationChanged.connect(self.getDuration)
		self.player.positionChanged.connect(self.setPosition)
		
		self.show()

	def move2Position(self):
		print(self.ProcessSlider.value())
		self.player.setPosition(self.ProcessSlider.value())
		if self.player.state()==2:
			return
		if self.player.state()==0:
			self.player.play()
	
	def setPosition(self):
		if not self.ProcessSlider.isHidden():
			self.ProcessSlider.setValue(self.player.position())
			
	@pyqtSlot()
	def on_StopPushButton_clicked(self):
		self.player.stop()
	
	@pyqtSlot()
	def on_PausePushButton_clicked(self):
		if self.player.state()==1 :
			print('暂停')
			self.player.pause()
			return
		if self.player.state()==2:
			print('恢复播放')
			self.player.play()
			return
	
	def showProcessSlider(self, event):
		print('enter PlayArea')
		width = self.PlayArea.rect().width()
		height = self.PlayArea.rect().height()
		print(width, height, event.x(), event.y())
		print(event.y() <= 0.4 * height and self.ProcessSlider.isHidden())
		if event.y() > 0.6 * height and self.ProcessSlider.isHidden():
			size = (width, 20)
			pos = QPoint(0, int(0.95 * height))
			self.ProcessSlider.resize(*size)
			self.ProcessSlider.move(pos)
			self.ProcessSlider.setMinimum(0)
			self.ProcessSlider.setMaximum(self.movieDuration)
			self.ProcessSlider.setPageStep(self.movieDuration / 100)
			self.ProcessSlider.setValue(self.player.position())
			self.ProcessSlider.setGraphicsEffect(self.op)
			self.ProcessSlider.setAutoFillBackground(True)
			self.ProcessSlider.show()
		else:
			self.ProcessSlider.hide()
	
	def hideProcessSlider(self, event):
		print('hide ProcessSlider')
		self.ProcessSlider.hide()


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
		self.movieDuration = ms
	
	def isMatchFileType(self, s):  # 判断拖入窗体的文件是否为filetype定义的类型
		file, ext = os.path.splitext(s)
		# print(file,ext,[str.lower(x) for x in re.split(        ' ', self.fileType)])
		if str.lower(ext) in [str.lower(x.replace('*', '')) for x in re.split(' ', self.fileType)]:
			return True
		else:
			return False
	
	def dragEnterEvent(self, e: QDragEnterEvent):  # 接受，或拒绝拖入窗体的文件
		print(111)
		
		if e.mimeData().hasText():
			txt = e.mimeData().text()
			print(txt)
			if self.isMatchFileType(txt):
				print('accept')
				e.accept()
	
	def dropEvent(self, e):  # 处理拖入窗体的文件
		print('drop')
		txt = e.mimeData().text()
		txt = re.sub('file:[/]+', '', txt)
		abspath = os.path.abspath(txt)

		self.moviePath = QUrl.fromLocalFile(abspath)
		self.movie = QMediaContent(self.moviePath)
		self.player.setMedia(self.movie)
		self.play()
	
	@pyqtSlot()
	def on_OpenPushButton_clicked(self):
		# path,_=QFileDialog.getOpenFileName(None, caption='打开', directory='c:/', filter=self.filetype)
		path = 'c://01.mp4'
		self.moviePath = QUrl.fromLocalFile(path)
		self.movie = QMediaContent(self.moviePath)
		self.player.setMedia(self.movie)
		self.play()
	
	def mousePressEvent(self, a0: QMouseEvent) -> None:
		self.mousePos = a0.screenPos()
	
	def on_VolPushButton_released(self):
		x = self.VolPushButton.pos().x()
		y = self.VolPushButton.pos().y()
		pos = QPoint(x + 30, self.groupBox.geometry().y() + y - 120 + 30)
		print(pos)
		
		self.VolSlider.move(pos)
		self.VolSlider.setMinimum(0)
		self.VolSlider.setMaximum(100)
		self.VolSlider.setProperty("value", self.vol)
		self.VolSlider.setOrientation(Qt.Vertical)
		self.VolSlider.setInvertedAppearance(False)
		self.VolSlider.setInvertedControls(False)
		self.VolSlider.setTickPosition(QSlider.TickPosition.TicksRight)
		self.VolSlider.setTickInterval(10)
		self.VolSlider.setValue(self.vol)
		self.VolSlider.show()
	
	def setVol(self):
		print(self.VolSlider.value())
		self.vol = self.VolSlider.value()
		self.player.setVolume(self.vol)
	
	def mouseSetVol(self, a0: QWheelEvent) -> None:
		value=self.vol+float(a0.angleDelta().y()/120)
		if 0<=value<=100:
			self.vol=value
			self.player.setVolume(self.vol)

	
	def leaveVolPushButtonEvent(self, event: QEvent):
		self.VolSlider.hide()
	
	def play(self, pos=0):
		self.player.setPosition(pos)  # to start at the beginning of the video every time)
		self.player.play()
	
	def setStayOnTop(self, f=True):

		if self.OnTopCheckBox.isChecked():
			print('置顶')
			self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 置顶
		else:
			print('取消置顶')
			self.setWindowFlag(Qt.Widget)

		self.showNormal()
		self.tray.hide()
	
	def setFrameLess(self):
		if self.FrameLessCheckBox.isChecked():
			self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
		else:
			self.setWindowFlags(Qt.WindowStaysOnTopHint)
			self.setWindowFlag(Qt.Widget)
		self.showNormal()
		self.tray.hide()


	
	# self.tray.hide()
	
	def hideEvent(self, a0: QHideEvent):
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
