# cocoding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/3/30 0030 下午 3:23
# Tool ：PyCharm
import sys
from ui import Ui_Form
from PyQt5.QtCore import Qt,QThread,pyqtSlot,pyqtSignal
from PyQt5.QtWidgets import QWidget,QFileDialog,QGraphicsScene,QGraphicsTextItem,QMessageBox,QGraphicsPixmapItem,QApplication
from PyQt5.QtGui import QIcon,QFont,QDragEnterEvent,QImage,QResizeEvent,QPixmap,QCloseEvent
import re,os,cv2
import numpy as np
import time
import configparser
import prediction

from concurrent.futures import ThreadPoolExecutor


class Mythread(QThread):
    rightSignal = pyqtSignal(str)
    wrongSignal = pyqtSignal(str)
    
    CHANNEL_COUNT = pyqtSignal(int)
    _3DCNN_WEIGHTS = pyqtSignal(str)
    UNET_WEIGHTS = pyqtSignal(str)
    THRESHOLD = pyqtSignal(int)
    BATCH_SIZE = pyqtSignal(int)
    temp_dir = pyqtSignal(str)
    temp_file1 = pyqtSignal(str)
    temp_file2 = pyqtSignal(str)
    source = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(Mythread, self).__init__()

    def run(self):
        prediction.CHANNEL_COUNT = self.CHANNEL_COUNT
        prediction._3DCNN_WEIGHTS = self._3DCNN_WEIGHTS
        prediction.UNET_WEIGHTS = self.UNET_WEIGHTS
        prediction.THRESHOLD =self.THRESHOLD
        prediction.BATCH_SIZE = self.BATCH_SIZE
        prediction.temp_dir = self.temp_dir
        prediction.temp_file1 = self.temp_file1
        prediction.temp_file2 = self.temp_file2
        # # self.stopSignal=False
        print(self.source)
        prediction.unet_predict(self.source)
        centers = prediction.unet_candidate_dicom(self.temp_file1)
        print(66666)
        print('y, x', centers)
        if len(centers) > 0:
            img=cv2.imdecode(np.fromfile(self.source, dtype=np.uint8), cv2.IMREAD_COLOR)
            # cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道
            # cv2.IMREAD_GRAYSCALE：读入灰度图片
            # cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道
            for pos in centers:
                y, x = pos
                cv2.circle(img, center=(x, y), radius=8, color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
            cv2.imwrite(self.temp_file2, img)
            self.wrongSignal.emit('异常')

        
        if len(centers) == 0:
            self.rightSignal.emit('正常')

class App(QWidget,Ui_Form):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("肺结节检测")
        self.setWindowIcon(QIcon('ico.ico'))
        self.toOutput(content='程序初始化中...')
        self.input_view.setAcceptDrops(True)
        self.workfile=''
        self.font=QFont()
        self.font.setPixelSize(100)
        self.fileType='*.png *.jpg'
        self.toOutput(content='初始化完成，请打开或直接拖入图像...,目前只接受{}文件'.format(self.fileType))
        self.colorThemes={
            '杏仁黄': (250, 249, 222),
            '秋叶褐': (255, 242, 226),
            '极光灰':(234, 234, 239),
            '青草绿':(227, 237, 205),
            '海天蓝':(220, 226, 241),
            '葛巾紫':(233, 235, 254),
        }

        self.OpacitySlider.valueChanged.connect(self.changePactiy)

        for i in [self.radioButton_1, self.radioButton_2, self.radioButton_3,self.radioButton_4, self.radioButton_5, self.radioButton_6]:
            i.clicked.connect(self.setColorTheme)
            
        
        self.loadConfig()
        self.setStyleSheet("background-color: rgb{};".format(str(self.colorThemes[self.colorTheme])))
        print(self.colorTheme,"background-color: rgb{};".format(str(self.colorThemes[self.colorTheme])))

    def changePactiy(self,value):
        self.setWindowOpacity(value/100)


    def loadConfig(self):
    
        path='./config.ini'
        config = configparser.ConfigParser()
        if os.path.exists(path):
            try:
                config.read(path, encoding='gbk')
            except configparser.MissingSectionHeaderError as e:
                self.toOutput(message='配置文件无任何section，请检查配置文件')
                sys.exit(1)
            except Exception as e:
                self.toOutput(message=str(e))
                sys.exit(1)
        else:
            self.toOutput('未找到配置文件')
            sys.exit(1)

        self.CHANNEL_COUNT = int(config.get('config','CHANNEL_COUNT'))
        self._3DCNN_WEIGHTS = str(config.get('config','_3DCNN_WEIGHTS'))
        self.UNET_WEIGHTS = str(config.get('config','UNET_WEIGHTS'))
        self.THRESHOLD = int(config.get('config','THRESHOLD'))
        self.BATCH_SIZE = int(config.get('config','BATCH_SIZE'))
        self.temp_dir = str(config.get('config','temp_dir'))
        
        self.Opacity=int(config.get('config','Opacity'))
        self.colorTheme=str(config.get('config','colorTheme'))
        
        self.temp_file1 = os.path.join(self.temp_dir, '1.png')
        self.temp_file2 = os.path.join(self.temp_dir, '2.png')

        self.cHANNEL_COUNTLineEdit.setText(str(self.CHANNEL_COUNT))
        self._3DCNN_WEIGHTSLineEdit.setText(str(self._3DCNN_WEIGHTS))
        self.uNET_WEIGHTSLineEdit.setText(str(self.UNET_WEIGHTS))
        self.tHRESHOLDLineEdit.setText(str(self.THRESHOLD))
        self.bATCH_SIZELineEdit.setText(str(self.BATCH_SIZE))
        self.temp_dirLineEdit.setText(str(self.temp_dir))
        
        print(self.colorTheme,self.colorThemes)
        
        self.OpacitySlider.setValue(self.Opacity)
        self.setWindowOpacity(self.Opacity / 100)
        for i in [self.radioButton_1, self.radioButton_2, self.radioButton_3,self.radioButton_4, self.radioButton_5, self.radioButton_6]:
            if i.text()==self.colorTheme:
                i.setChecked(True)
                
        
    def setColorTheme(self):
        for i in [self.radioButton_1,self.radioButton_2 ,self.radioButton_3 ,
                  self.radioButton_4 ,self.radioButton_5 ,self.radioButton_6  ]:
            if i.isChecked():
                print(i)
                self.colorTheme=i.text()
                print("background-color: rgb{};".format(str(self.colorThemes[self.colorTheme])))
                self.setStyleSheet("background-color: rgb{};".format(str(self.colorThemes[self.colorTheme])))

        
    def saveConfig(self):
        path = './config.ini'
        config = configparser.ConfigParser()
        config.add_section('config')
        config.set('config','CHANNEL_COUNT',self.cHANNEL_COUNTLineEdit.text())
        config.set('config','_3DCNN_WEIGHTS',self._3DCNN_WEIGHTSLineEdit.text())
        config.set('config', 'UNET_WEIGHTS',self.uNET_WEIGHTSLineEdit.text())
        config.set('config','THRESHOLD',self.tHRESHOLDLineEdit.text())
        config.set('config','BATCH_SIZE',self.bATCH_SIZELineEdit.text())
        config.set('config','temp_dir',self.temp_dirLineEdit.text())
        config.set('config', 'Opacity', str(self.OpacitySlider.value()))
        config.set('config', 'colorTheme', self.colorTheme)

        with open(path, 'w+', encoding='gbk') as f:
            config.write(f)

    @pyqtSlot()
    
    def on_saveConfigButton_clicked(self):
        self.saveConfig()
        
        
    @pyqtSlot()
    def on_button_clicked(self):
        a=self.v_view.size()
        self.button.setText(str(a))

    def name2Wegite(self,name):
        if name:
            return self.findChild(QWidget, name)
        else:
            print('name is empty')

    def isMatchFileType(self,s):
        file,ext=os.path.splitext(s)
        #print(file,ext,[str.lower(x) for x in re.split(        ' ', self.fileType)])
        if str.lower(ext) in [str.lower(x.replace('*','')) for x in re.split(' ',self.fileType)]:
            return True
        else:
            return False

    def dragEnterEvent(self, e:QDragEnterEvent):
        print('enter')
        if e.mimeData().hasText():
            txt = e.mimeData().text()
            print(txt)
            if self.isMatchFileType(txt):
                print('accept')
                e.accept()
        print('ww')
        #     else:
        #         e.ignore()
        # else:
        #     e.ignore()

    def dropEvent(self, e):
        print('drop')
        txt=e.mimeData().text()
        txt=re.sub('file:[/]+','',txt)
        abspath=os.path.abspath(txt)
        self.workfile=abspath
        self.resizeEvent(QResizeEvent)
        self.toOutput(content='检测到文件输入:{},处理'.format(abspath))

    @pyqtSlot()
    def on_openButton_clicked(self):
        file,type=QFileDialog.getOpenFileName(None,caption='打开',directory='.',filter='*.png *.jpg')
        abspath=os.path.abspath(file)
        self.workfile=abspath
        self.load_pic()
        self.toOutput(content='检测到文件输入:{},处理'.format(abspath))

    def load_pic(self):
        if os.path.isfile(self.workfile):
            try:
                img = cv2.imdecode(np.fromfile(self.workfile, dtype=np.uint8), cv2.IMREAD_COLOR)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
                img_width = img.shape[1]  # 获取图像大小
                img_height = img.shape[0]
                width = self.input_view.width()
                height = self.input_view.height()
                width_scale=width / img_width
                height_scale=height / img_height
                zoomscale = min(width_scale,height_scale )  # 图片放缩尺度
                frame = QImage(img, img_width, img_height, QImage.Format_RGB888)
                pix = QPixmap.fromImage(frame)
                self.source_pic_item = QGraphicsPixmapItem(pix)  # 创建像素图元
                self.source_pic_item.setScale(zoomscale)
                self.source_scene = QGraphicsScene()  # 创建场景
                self.source_scene.addItem(self.source_pic_item)
                self.input_view.setScene(self.source_scene)
                self.input_view.show()
                self.start()
            except Exception as e:
                print(e)

    def start(self):
        
            self.thread=Mythread()
            self.thread.rightSignal.connect(self.setNormalResult)
            self.thread.wrongSignal.connect(self.setNoticeResult)
            
            self.thread.CHANNEL_COUNT=int(self.CHANNEL_COUNT)
            self.thread._3DCNN_WEIGHTS=self._3DCNN_WEIGHTS
            self.thread.UNET_WEIGHTS=self.UNET_WEIGHTS
            self.thread.THRESHOLD=int(self.THRESHOLD)
            self.thread.BATCH_SIZE=int(self.BATCH_SIZE)
            self.thread.temp_dir=self.temp_dir
            self.thread.temp_file1=self.temp_file1
            self.thread.temp_file2=self.temp_file2
            self.thread.source=self.workfile
            self.thread.run()
            return


    def setNormalResult(self,a0):
        try:
            print('set normal')
            self.normal_item=QGraphicsTextItem()
            self.normal_item.setPlainText('NORMAL')
            self.normal_item.setDefaultTextColor(Qt.green)
            self.normal_item.setFont(self.font)

            self.normalScene=QGraphicsScene()
            self.normalScene.addItem(self.normal_item)
            self.outputView.setScene(self.normalScene)
            self.outputView.show()
            self.outputText.setText('未检查出结节')
            self.toOutput('yes')
        except Exception as e:
            print(e)


    def setNoticeResult(self,a0):
        
        self.outputText.setText('')
        img = cv2.imdecode(np.fromfile(self.temp_file2, dtype=np.uint8), cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        img_width = img.shape[1]  # 获取图像大小
        img_height = img.shape[0]
        width = self.input_view.width()
        height = self.input_view.height()
        width_scale = width / img_width
        height_scale = height / img_height
        zoomscale = min(width_scale, height_scale)  # 图片放缩尺度
        frame = QImage(img, img_width, img_height, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.notice_item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.notice_item.setScale(zoomscale)
        self.notice_scene = QGraphicsScene()  # 创建场景
        self.notice_scene.addItem(self.notice_item)
        self.outputView.setScene(self.notice_scene)
        self.outputView.show()
        
        
        self.outputText.append('检查出结节')
        self.outputText.append('推测为良性')
        self.outputText.append('请人工复查')


    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.load_pic()

    def toOutput(self,content):
        self.outPut.append('''<html><font-size:10pt">{}</font></html>'''.format(content))
        self.outPut.append('')

    def closeEvent(self, a0: QCloseEvent) -> None:
        if self.doButton.text()=='STOP':
            QMessageBox.warning(self, '警告', '图像处理中，请先停止', QMessageBox.Ok)
            a0.ignore()
            return

        if QMessageBox.question(self,'关闭','是否退出程序',QMessageBox.Yes|QMessageBox.No,QMessageBox.No) ==QMessageBox.Yes:
            a0.accept()
        else:
            a0.ignore()


app=QApplication(sys.argv)
window=App()
window.show()
sys.exit(app.exec_())
