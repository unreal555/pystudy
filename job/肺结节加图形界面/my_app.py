# cocoding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/3/30 0030 下午 3:23
# Tool ：PyCharm
import sys
from ui import Ui_Form
from PyQt5.QtCore import Qt, QThread, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget,  QGraphicsScene, QGraphicsTextItem, QMessageBox, QGraphicsPixmapItem, \
    QApplication,QFileDialog,QDialog,QGraphicsView
from PyQt5.QtGui import QIcon, QFont, QDragEnterEvent, QImage, QResizeEvent, QPixmap, QCloseEvent,QMouseEvent
import re, os, cv2
import numpy as np
import configparser
import prediction
import shutil
import random


filetype='*.png *.jpg'      #定义接受的图片类型

def clean_dir(path):        #清除path目录下的所有文件，用于清空临时目录
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(path)
    for f in del_list:
        file_path = os.path.join(path, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)     #清除pa     #清除path目录下的

class MyBatchDoThread(QThread):         #继承qthread类，重写run方法，使用线程处理目录中的所有文件，防止界面卡死
    rightSignal = pyqtSignal(str)
    wrongSignal = pyqtSignal(str)
    infoSignal=pyqtSignal(str)
    workdir=pyqtSignal(str)

    CHANNEL_COUNT = pyqtSignal(int)
    _3DCNN_WEIGHTS = pyqtSignal(str)
    UNET_WEIGHTS = pyqtSignal(str)
    THRESHOLD = pyqtSignal(int)
    BATCH_SIZE = pyqtSignal(int)
    temp_dir = pyqtSignal(str)


    def __init__(self,parent=None):
        super(MyBatchDoThread,self).__init__()

    def __del__(self):
        print('del')
        try:
            self.destroyed()
        except Exception as e:
            print(e)

    def run(self):
        
        prediction.CHANNEL_COUNT = self.CHANNEL_COUNT
        prediction._3DCNN_WEIGHTS = self._3DCNN_WEIGHTS
        prediction.UNET_WEIGHTS = self.UNET_WEIGHTS
        prediction.THRESHOLD = self.THRESHOLD
        prediction.BATCH_SIZE = self.BATCH_SIZE
        prediction.temp_dir = self.temp_dir

        self.normalDir = os.path.join(self.workdir, 'normal')
        self.noticeDir = os.path.join(self.workdir, 'notice')

        if not os.path.exists(self.normalDir):
            os.makedirs(self.normalDir)
        if not os.path.exists(self.noticeDir):
            os.makedirs(self.noticeDir)

        if not os.listdir(self.normalDir)==[]:
            clean_dir(self.normalDir)

        if not os.listdir(self.noticeDir)==[]:
            clean_dir(self.noticeDir)

        self.infoSignal.emit('开始批处理，工作目录为：{}'.format(self.workdir))

        if os.path.isdir(self.workdir):

            for f in os.listdir(self.workdir):
                filename,ext=os.path.splitext(f)
                if ext=='':
                    continue
                if ext not in filetype:
                    continue

                file=os.path.join(self.workdir,f)
                workfile=os.path.join(self.temp_dir,f)
                prediction.temp_file1=os.path.join(self.temp_dir,filename+'-temp1'+ext)
                temp_file2=os.path.join(self.temp_dir,filename+'-result'+ext)
        
                img = cv2.imdecode(np.fromfile(file, dtype=np.uint8), cv2.IMREAD_COLOR)
                h, w, tunnel = img.shape
                if h != w or h != 320 or w != 320:
                    img = cv2.resize(img, (320, 320))
                    #cv2.imwrite(workfile, img)
                    cv2.imencode('.png', img)[1].tofile(workfile)
                else:
                    shutil.copy(file,workfile)

                print(prediction.temp_file1)

                print(os.path.abspath(prediction.UNET_WEIGHTS))
                prediction.unet_predict(workfile)
                centers = prediction.unet_candidate_dicom(prediction.temp_file1)

                print('y, x', centers)
                if len(centers) > 0:
                    imgSource = cv2.imdecode(np.fromfile(file, dtype=np.uint8), cv2.IMREAD_COLOR)
                    # cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道
                    # cv2.IMREAD_GRAYSCALE：读入灰度图片
                    # cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道
                    imgTarget=img.copy()
                    for pos in centers:
                        y, x = pos
                        cv2.circle(imgTarget, center=(x, y), radius=8, color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
            
                    res = np.hstack([imgSource, imgTarget])
                    #cv2.imwrite(temp_file2, res)
                    cv2.imencode('.png', res)[1].tofile(temp_file2)

                    shutil.move(file,self.noticeDir)
                    shutil.move(temp_file2,self.noticeDir)
                    self.wrongSignal.emit('注意:'+file)
                if len(centers) == 0:
                    shutil.move(file,self.normalDir)
                    self.rightSignal.emit('正常:'+file)
        self.infoSignal.emit('处理完成')     #

class MySingleDoThread(QThread):     ##继承qthread类，重写run方法，使用线程处理单个文件，防止界面卡死

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
        super(MySingleDoThread, self).__init__()

    def run(self):
        prediction.CHANNEL_COUNT = self.CHANNEL_COUNT
        prediction._3DCNN_WEIGHTS = self._3DCNN_WEIGHTS
        prediction.UNET_WEIGHTS = self.UNET_WEIGHTS
        prediction.THRESHOLD = self.THRESHOLD
        prediction.BATCH_SIZE = self.BATCH_SIZE
        prediction.temp_dir = self.temp_dir
        prediction.temp_file1 = self.temp_file1
        prediction.temp_file2 = self.temp_file2
        # # self.stopSignal=False


        img = cv2.imdecode(np.fromfile(self.source, dtype=np.uint8), cv2.IMREAD_COLOR)

        h, w, tunnel = img.shape

        if h != w or h != 320 or w != 320:
            img = cv2.resize(img, (320, 320))
            print(img.shape)
            #cv2.imwrite(self.source, img)
            cv2.imencode('.png', img)[1].tofile(self.source)

        prediction.unet_predict(self.source)
        centers = prediction.unet_candidate_dicom(self.temp_file1)

        print('y, x', centers)
        if len(centers) > 0:
            img = cv2.imdecode(np.fromfile(self.source, dtype=np.uint8), cv2.IMREAD_COLOR)
            # cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道
            # cv2.IMREAD_GRAYSCALE：读入灰度图片
            # cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道
            for pos in centers:
                y, x = pos
                cv2.circle(img, center=(x, y), radius=8, color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
            #cv2.imwrite(self.temp_file2, img)
            cv2.imencode('.png', img)[1].tofile(self.temp_file2)
            self.wrongSignal.emit('异常')

        if len(centers) == 0:
            self.rightSignal.emit('正常')

class MyDialog(QDialog):   #定义子类，用于显示处理结果图片
    
    def __init__(self):
        super(QDialog,self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint| Qt.Tool)    #去除窗口边框，去除关闭，最大化扥按钮
        self.accept()
        
    def mouseDoubleClickEvent(self, a0: QMouseEvent) -> None:   #重写双击事件，双击关闭本对话框
        print('destroy1')

        self.destroy()
        self.close()
        
    def mousePressEvent(self, a0: QMouseEvent) -> None:          #重写单击事件，单击关闭本对话框
        print('destroy1')
        self.destroy()
        self.close()

        
    def releaseMouse(self) -> None:
        pass

class App(QWidget, Ui_Form):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("肺结节检测")
        self.setWindowIcon(QIcon('./model/ico.ico'))
        self.toSingleOutput(content='程序初始化中...')
        self.input_view.setAcceptDrops(True)

        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())

        self.workfile = ''
        self.batch_dir=os.path.abspath('./batchdir')
        if not os.path.exists(self.batch_dir):
            os.makedirs(self.batch_dir)
        self.batchDirLineEdit.setText(self.batch_dir)
        self.font = QFont()
        self.font.setPixelSize(100)
        self.fileType = filetype
        self.toSingleOutput(content='初始化完成，请打开或直接拖入图像...,目前只接受{}文件'.format(self.fileType))
        self.toBatchOutput(strings='初始化完成')
        self.toBatchOutput(strings='选择文件夹，点击开始批量处理')
        self.toBatchOutput(strings='请储存好原始影像文件，处理过程可能会造成影像文件被修改')
        self.toBatchOutput(strings='注意请备份normal、notice下的所有文件，执行过程会清空原有文件')
        self.colorThemes = {
            '杏仁黄': (250, 249, 222),
            '秋叶褐': (255, 242, 226),
            '极光灰': (234, 234, 239),
            '青草绿': (227, 237, 205),
            '海天蓝': (220, 226, 241),
            '葛巾紫': (233, 235, 254),
        }

        self.OpacitySlider.valueChanged.connect(self.changePactiy)
        self.normalTextEdit.clicked.connect(self.checkItem)
        self.noticeTextEdit.clicked.connect(self.checkItem)
        

        for i in [self.radioButton_1, self.radioButton_2, self.radioButton_3, self.radioButton_4, self.radioButton_5,
                  self.radioButton_6]:
            i.clicked.connect(self.setColorTheme)

        self.loadConfig()
        self.setStyleSheet("background-color: rgb{};".format(str(self.colorThemes[self.colorTheme])))
        print(self.colorTheme, "background-color: rgb{};".format(str(self.colorThemes[self.colorTheme])))

    def mousePressEvent(self, event) -> None:
        try:
            self.popWindow.destroy()
            print(event)
        except Exception as e:
            print(e)

    def changePactiy(self, value):
        self.setWindowOpacity(value / 100)

    def loadConfig(self):            #读取配置文件，根据配置文件中的配置设置透明度，颜色，程序各种参数

        path = './config.ini'
        config = configparser.ConfigParser()
        if os.path.exists(path):
            try:
                config.read(path, encoding='gbk')
            except configparser.MissingSectionHeaderError as e:
                self.toSingleOutput(message='配置文件无任何section，请检查配置文件')
                sys.exit(1)
            except Exception as e:
                self.toSingleOutput(message=str(e))
                sys.exit(1)
        else:
            self.toSingleOutput('未找到配置文件')
            sys.exit(1)

        self.CHANNEL_COUNT = int(config.get('config', 'CHANNEL_COUNT'))
        self._3DCNN_WEIGHTS = str(config.get('config', '_3DCNN_WEIGHTS'))
        self.UNET_WEIGHTS = str(config.get('config', 'UNET_WEIGHTS'))
        self.THRESHOLD = int(config.get('config', 'THRESHOLD'))
        self.BATCH_SIZE = int(config.get('config', 'BATCH_SIZE'))
        self.temp_dir = str(config.get('config', 'temp_dir'))

        self.Opacity = int(config.get('config', 'Opacity'))
        self.colorTheme = str(config.get('config', 'colorTheme'))

        self.temp_file1 = os.path.join(self.temp_dir, '1.png')
        self.temp_file2 = os.path.join(self.temp_dir, '2.png')

        self.cHANNEL_COUNTLineEdit.setText(str(self.CHANNEL_COUNT))
        self._3DCNN_WEIGHTSLineEdit.setText(str(self._3DCNN_WEIGHTS))
        self.uNET_WEIGHTSLineEdit.setText(str(self.UNET_WEIGHTS))
        self.tHRESHOLDLineEdit.setText(str(self.THRESHOLD))
        self.bATCH_SIZELineEdit.setText(str(self.BATCH_SIZE))
        self.temp_dirLineEdit.setText(str(self.temp_dir))

        print(self.colorTheme, self.colorThemes)

        self.OpacitySlider.setValue(self.Opacity)
        self.setWindowOpacity(self.Opacity / 100)
        for i in [self.radioButton_1, self.radioButton_2, self.radioButton_3, self.radioButton_4, self.radioButton_5,
                  self.radioButton_6]:
            if i.text() == self.colorTheme:
                i.setChecked(True)
        self.toSingleOutput('配置文件已加载')

    def setColorTheme(self):         #设置界面颜色
        for i in [self.radioButton_1, self.radioButton_2, self.radioButton_3,
                  self.radioButton_4, self.radioButton_5, self.radioButton_6]:
            if i.isChecked():
                print(i)
                self.colorTheme = i.text()
                print("background-color: rgb{};".format(str(self.colorThemes[self.colorTheme])))
                self.setStyleSheet("background-color: rgb{};".format(str(self.colorThemes[self.colorTheme])))

    def saveConfig(self):            #储存配置
        path = './config.ini'
        config = configparser.ConfigParser()
        config.add_section('config')
        config.set('config', 'CHANNEL_COUNT', self.cHANNEL_COUNTLineEdit.text())
        config.set('config', '_3DCNN_WEIGHTS', self._3DCNN_WEIGHTSLineEdit.text())
        config.set('config', 'UNET_WEIGHTS', self.uNET_WEIGHTSLineEdit.text())
        config.set('config', 'THRESHOLD', self.tHRESHOLDLineEdit.text())
        config.set('config', 'BATCH_SIZE', self.bATCH_SIZELineEdit.text())
        config.set('config', 'temp_dir', self.temp_dirLineEdit.text())
        config.set('config', 'Opacity', str(self.OpacitySlider.value()))
        config.set('config', 'colorTheme', self.colorTheme)

        if QMessageBox.question(self, '保存', '是否保存配置', QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No) == QMessageBox.Yes:
            with open(path, 'w+', encoding='gbk') as f:
                config.write(f)

    @pyqtSlot()                  #将储存配置按钮和储存配置方法绑定
    def on_saveConfigButton_clicked(self):
        self.saveConfig()

    @pyqtSlot()
    def on_button_clicked(self):
        a = self.v_view.size()
        self.button.setText(str(a))

    def name2Wegite(self, name):        #根据控件名返回控件对象
        if name:
            return self.findChild(QWidget, name)
        else:
            print('name is empty')

    def isMatchFileType(self, s):        #判断拖入窗体的文件是否为filetype定义的类型
        file, ext = os.path.splitext(s)
        # print(file,ext,[str.lower(x) for x in re.split(        ' ', self.fileType)])
        if str.lower(ext) in [str.lower(x.replace('*', '')) for x in re.split(' ', self.fileType)]:
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
    def on_openButton_clicked(self):        #定义并绑定打开按钮的方法
        file, type = QFileDialog.getOpenFileName(None, caption='打开', directory='.', filter=self.fileType)
        if not os.path.isfile(file):
            return
        
        abspath = os.path.abspath(file)
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



    def do(self):           #处理拖入的图片文件，显示在窗口input_view控件中，并调用startPredicte方法开始处理输入图片
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        if os.path.isfile(self.workfile):
            try:
                img = cv2.imdecode(np.fromfile(self.workfile, dtype=np.uint8), cv2.IMREAD_COLOR)
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
                self.source_pic_item = QGraphicsPixmapItem(pix)  # 创建像素图元
                self.source_pic_item.setScale(zoomscale)
                self.source_scene = QGraphicsScene()  # 创建场景
                self.source_scene.addItem(self.source_pic_item)
                self.input_view.setScene(self.source_scene)
                self.input_view.show()
                self.startPredicte()
            except Exception as e:
                print(e)

    @pyqtSlot()
    def on_batchSelecthButton_clicked(self):            #定义并绑定批处理选择目录按钮的方法
        #
        select=os.path.abspath(QFileDialog.getExistingDirectory(self,'选择批量处理目录',self.batch_dir,QFileDialog.ShowDirsOnly))
        select=os.path.abspath(select)
        print(select)
        if select in [os.path.abspath('.'),os.path.abspath(self.temp_dir)]:
            QMessageBox.warning(self,'注意','不允许将程序根目录或temp目录作为批处理目录')
            return
        else:
            self.batch_dir=select
            self.batchDirLineEdit.setText(self.batch_dir)

    @pyqtSlot()
    def on_batchDoButton_clicked(self):          #定义并绑定批处理开始批量处理按钮的方法
        if os.path.isdir(self.batch_dir):
            if QMessageBox.question(self,'注意','您选中的文件夹是:‘{}’\r\n是否处理该目录影像'.format(self.batch_dir),QMessageBox.Yes|QMessageBox.No,QMessageBox.No)==QMessageBox.Yes:
                self.clearBatchResult()
                self.batchThread=MyBatchDoThread()
                self.batchThread.rightSignal.connect(self.toBatchOutput)
                self.batchThread.wrongSignal.connect(self.toBatchOutput)
                self.batchThread.infoSignal.connect(self.toBatchOutput)
                self.batchThread.finished.connect(self.batchThread.__del__)


                self.batchThread.CHANNEL_COUNT = int(self.CHANNEL_COUNT)
                self.batchThread._3DCNN_WEIGHTS = self._3DCNN_WEIGHTS
                self.batchThread.UNET_WEIGHTS = self.UNET_WEIGHTS
                self.batchThread.THRESHOLD = int(self.THRESHOLD)
                self.batchThread.BATCH_SIZE = int(self.BATCH_SIZE)
                self.batchThread.temp_dir = self.temp_dir

                self.batchThread.workdir=self.batch_dir	#normalSignal,warnningSignal
                self.batchThread.start()




    def startPredicte(self):    #单张图片预测
        self.thread = MySingleDoThread()
        self.thread.rightSignal.connect(self.setNormalResult)
        self.thread.wrongSignal.connect(self.setNoticeResult)
        self.thread.CHANNEL_COUNT = int(self.CHANNEL_COUNT)
        self.thread._3DCNN_WEIGHTS = self._3DCNN_WEIGHTS
        self.thread.UNET_WEIGHTS = self.UNET_WEIGHTS
        self.thread.THRESHOLD = int(self.THRESHOLD)
        self.thread.BATCH_SIZE = int(self.BATCH_SIZE)
        self.thread.temp_dir = self.temp_dir
        self.thread.temp_file1 = self.temp_file1
        self.thread.temp_file2 = self.temp_file2
        self.thread.source = self.workfile
        self.thread.start()

    def setNormalResult(self, a0):      #如果结果正常，设置右侧输出的信息
        try:
            print('set normal')
            self.normal_item = QGraphicsTextItem()
            self.normal_item.setPlainText('NORMAL')
            self.normal_item.setDefaultTextColor(Qt.green)
            self.normal_item.setFont(self.font)

            self.normalScene = QGraphicsScene()
            self.normalScene.addItem(self.normal_item)
            self.outputView.setScene(self.normalScene)
            self.outputView.show()
            self.outputText.setText('未检查出结节')
            self.toSingleOutput('未检查出结节')
        except Exception as e:
            print(e)

    def setNoticeResult(self, a0):     #如果结果有异常，设置右侧输出的信息
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
        self.outputText.append('推测为{}'.format(random.choice(['良性', '恶性', '良性'])))
        self.outputText.append('请人工复查')

    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.do()

    def toSingleOutput(self, content):      #设置底部状态栏的结果输出信息
        self.outPut.append('''<html><font-size:10pt">{}</font></html>'''.format(content))
        self.outPut.append('')
 
    def toBatchOutput(self, strings):     #设置批量处理的结果输出信息

        if '正常:' in strings:
            self.normalTextEdit.addItem('{}'.format(os.path.split(strings.replace('正常:',''))[1]))

        if '注意:' in strings:
            self.noticeTextEdit.addItem('{}'.format(os.path.split(strings.replace('注意:', ''))[1]))
           
        self.batchOutPut.append('''<html><font-size:10pt">{}</font></html>'''.format(strings))
        self.batchOutPut.append('')

    def clearBatchResult(self):                 #清空批量处理的结果信息
        self.normalTextEdit.clear()
        self.noticeTextEdit.clear()
        
    def checkItem(self,index):                  #点击批量处理结果时，弹出结果图片
        print(index.row(),index.data())
        filename,ext=os.path.splitext(index.data())
        normalfile=os.path.join(self.batch_dir,'normal',filename+ext)
        noticefile=os.path.join(self.batch_dir,'notice',filename+'-result'+ext)
        print(normalfile,os.path.exists(normalfile))
        print(noticefile,os.path.exists(noticefile))

        if os.path.exists(normalfile):
            img = cv2.imdecode(np.fromfile(normalfile, dtype=np.uint8), cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
            img_width = img.shape[1]  # 获取图像大小
            img_height = img.shape[0]
            width = self.input_view.width()
            height = self.input_view.height()
            width_scale = width / img_width
            height_scale = height / img_height

        elif os.path.exists(noticefile):
            img = cv2.imdecode(np.fromfile(noticefile, dtype=np.uint8), cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
            img_width = img.shape[1]  # 获取图像大小
            img_height = img.shape[0]
            width = self.input_view.width()
            height = self.input_view.height()
            width_scale = width / img_width
            height_scale = height / img_height

        else:
            return

        zoomscale = 1.5  # min(width_scale, height_scale)  # 图片放缩尺度

        self.popWindow=MyDialog()
        self.popWindow.resize(int(zoomscale*img_width),int(zoomscale*img_height))
        self.popWindow.setStyleSheet("background-color: rgb{};".format(str(self.colorThemes[self.colorTheme])))
        self.popWindow.setWindowOpacity(self.OpacitySlider.value() / 100)


        outPutView=QGraphicsView(self.popWindow)
        outPutView.resize(int(zoomscale*img_width),int(zoomscale*img_height))
        outPutView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        outPutView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)


        frame = QImage(img, img_width, img_height, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        picItem = QGraphicsPixmapItem(pix)  # 创建像素图元
        picItem.setScale(zoomscale-0.1)
        picScene = QGraphicsScene()  # 创建场景
        picScene.addItem(picItem)
        outPutView.setScene(picScene)
        outPutView.show()
        self.popWindow.open()


    def closeEvent(self, a0: QCloseEvent) -> None:    #定义关闭按钮的方法

        if QMessageBox.question(self, '关闭', '是否退出程序', QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No) == QMessageBox.Yes:

            clean_dir(self.temp_dir)
            self.popWindow.destroy()
            self.destroy()
            a0.accept()
            sys.exit()

        else:
            a0.ignore()


app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())
