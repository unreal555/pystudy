# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(800, 500)
        Form.setAcceptDrops(True)
        Form.setStyleSheet("")
        self.gridLayout_6 = QtWidgets.QGridLayout(Form)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Pages = QtWidgets.QTabWidget(Form)
        self.Pages.setStyleSheet("font: 12pt \"宋体\";")
        self.Pages.setTabPosition(QtWidgets.QTabWidget.North)
        self.Pages.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.Pages.setElideMode(QtCore.Qt.ElideLeft)
        self.Pages.setUsesScrollButtons(False)
        self.Pages.setDocumentMode(False)
        self.Pages.setTabsClosable(False)
        self.Pages.setMovable(True)
        self.Pages.setObjectName("Pages")
        self.diagnose = QtWidgets.QWidget()
        self.diagnose.setObjectName("diagnose")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.diagnose)
        self.gridLayout_9.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_9.setSpacing(2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.diagnose)
        self.frame.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.input_view = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.input_view.sizePolicy().hasHeightForWidth())
        self.input_view.setSizePolicy(sizePolicy)
        self.input_view.setFrameShape(QtWidgets.QFrame.Box)
        self.input_view.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.input_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.input_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.input_view.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.input_view.setObjectName("input_view")
        self.verticalLayout_4.addWidget(self.input_view)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.outPut = QtWidgets.QTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outPut.sizePolicy().hasHeightForWidth())
        self.outPut.setSizePolicy(sizePolicy)
        self.outPut.setAcceptDrops(False)
        self.outPut.setFrameShape(QtWidgets.QFrame.Box)
        self.outPut.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outPut.setReadOnly(True)
        self.outPut.setObjectName("outPut")
        self.verticalLayout_4.addWidget(self.outPut)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setStyleSheet("border-color: rgb(132, 132, 132);\n"
"border-color: rgb(25, 25, 25);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.openButton = QtWidgets.QPushButton(self.frame)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout_2.addWidget(self.openButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.diagnose)
        self.frame_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.outputText = QtWidgets.QTextEdit(self.frame_2)
        self.outputText.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputText.sizePolicy().hasHeightForWidth())
        self.outputText.setSizePolicy(sizePolicy)
        self.outputText.setStyleSheet("text-decoration: underline;\n"
"font: 20pt \"仿宋\";")
        self.outputText.setFrameShape(QtWidgets.QFrame.Box)
        self.outputText.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputText.setObjectName("outputText")
        self.gridLayout_2.addWidget(self.outputText, 3, 0, 1, 1)
        self.outputView = QtWidgets.QGraphicsView(self.frame_2)
        self.outputView.setFrameShape(QtWidgets.QFrame.Box)
        self.outputView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputView.setObjectName("outputView")
        self.gridLayout_2.addWidget(self.outputView, 1, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_2)
        self.gridLayout_4.addWidget(self.frame_2, 1, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.diagnose)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_7.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_7.setSpacing(1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.diagnose)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_8.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_8.setSpacing(1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.gridLayout_8.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_4, 0, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.Pages.addTab(self.diagnose, "")
        self.batch = QtWidgets.QWidget()
        self.batch.setObjectName("batch")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.batch)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.groupBox_3 = QtWidgets.QGroupBox(self.batch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.batchDirLineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.batchDirLineEdit.setEnabled(False)
        self.batchDirLineEdit.setObjectName("batchDirLineEdit")
        self.gridLayout_11.addWidget(self.batchDirLineEdit, 0, 0, 1, 1)
        self.batchSelecthButton = QtWidgets.QPushButton(self.groupBox_3)
        self.batchSelecthButton.setObjectName("batchSelecthButton")
        self.gridLayout_11.addWidget(self.batchSelecthButton, 0, 1, 1, 1)
        self.batchDoButton = QtWidgets.QPushButton(self.groupBox_3)
        self.batchDoButton.setObjectName("batchDoButton")
        self.gridLayout_11.addWidget(self.batchDoButton, 0, 2, 1, 1)
        self.horizontalLayout_8.addLayout(self.gridLayout_11)
        self.gridLayout_12.addWidget(self.groupBox_3, 0, 1, 1, 2)
        self.groupBox_6 = QtWidgets.QGroupBox(self.batch)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.batchOutPut = QtWidgets.QTextBrowser(self.groupBox_6)
        self.batchOutPut.setEnabled(True)
        self.batchOutPut.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.batchOutPut.setReadOnly(True)
        self.batchOutPut.setObjectName("batchOutPut")
        self.gridLayout_15.addWidget(self.batchOutPut, 0, 0, 1, 1)
        self.horizontalLayout_11.addLayout(self.gridLayout_15)
        self.gridLayout_12.addWidget(self.groupBox_6, 3, 1, 1, 2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.batch)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.noticeTextEdit = QtWidgets.QListWidget(self.groupBox_5)
        self.noticeTextEdit.setObjectName("noticeTextEdit")
        self.gridLayout_14.addWidget(self.noticeTextEdit, 0, 0, 1, 1)
        self.horizontalLayout_12.addLayout(self.gridLayout_14)
        self.gridLayout_12.addWidget(self.groupBox_5, 1, 2, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.batch)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.normalTextEdit = QtWidgets.QListWidget(self.groupBox_4)
        self.normalTextEdit.setObjectName("normalTextEdit")
        self.gridLayout_13.addWidget(self.normalTextEdit, 0, 0, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_13)
        self.gridLayout_12.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.horizontalLayout_9.addLayout(self.gridLayout_12)
        self.Pages.addTab(self.batch, "")
        self.configure = QtWidgets.QWidget()
        self.configure.setObjectName("configure")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.configure)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.configure)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.cHANNEL_COUNTLabel = QtWidgets.QLabel(self.groupBox)
        self.cHANNEL_COUNTLabel.setObjectName("cHANNEL_COUNTLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.cHANNEL_COUNTLabel)
        self.cHANNEL_COUNTLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.cHANNEL_COUNTLineEdit.setObjectName("cHANNEL_COUNTLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cHANNEL_COUNTLineEdit)
        self._3DCNN_WEIGHTSLabel = QtWidgets.QLabel(self.groupBox)
        self._3DCNN_WEIGHTSLabel.setObjectName("_3DCNN_WEIGHTSLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self._3DCNN_WEIGHTSLabel)
        self._3DCNN_WEIGHTSLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self._3DCNN_WEIGHTSLineEdit.setObjectName("_3DCNN_WEIGHTSLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self._3DCNN_WEIGHTSLineEdit)
        self.uNET_WEIGHTSLabel = QtWidgets.QLabel(self.groupBox)
        self.uNET_WEIGHTSLabel.setObjectName("uNET_WEIGHTSLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.uNET_WEIGHTSLabel)
        self.uNET_WEIGHTSLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.uNET_WEIGHTSLineEdit.setObjectName("uNET_WEIGHTSLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.uNET_WEIGHTSLineEdit)
        self.tHRESHOLDLabel = QtWidgets.QLabel(self.groupBox)
        self.tHRESHOLDLabel.setObjectName("tHRESHOLDLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.tHRESHOLDLabel)
        self.tHRESHOLDLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.tHRESHOLDLineEdit.setObjectName("tHRESHOLDLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tHRESHOLDLineEdit)
        self.bATCH_SIZELabel = QtWidgets.QLabel(self.groupBox)
        self.bATCH_SIZELabel.setObjectName("bATCH_SIZELabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.bATCH_SIZELabel)
        self.bATCH_SIZELineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.bATCH_SIZELineEdit.setObjectName("bATCH_SIZELineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.bATCH_SIZELineEdit)
        self.temp_dirLabel = QtWidgets.QLabel(self.groupBox)
        self.temp_dirLabel.setObjectName("temp_dirLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.temp_dirLabel)
        self.temp_dirLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.temp_dirLineEdit.setObjectName("temp_dirLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.temp_dirLineEdit)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.configure)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.OpacitySlider = QtWidgets.QSlider(self.frame_5)
        self.OpacitySlider.setMinimum(60)
        self.OpacitySlider.setMaximum(100)
        self.OpacitySlider.setProperty("value", 60)
        self.OpacitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.OpacitySlider.setInvertedAppearance(False)
        self.OpacitySlider.setInvertedControls(False)
        self.OpacitySlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.OpacitySlider.setTickInterval(10)
        self.OpacitySlider.setObjectName("OpacitySlider")
        self.horizontalLayout_6.addWidget(self.OpacitySlider)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_6)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_10.addWidget(self.radioButton_2, 0, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_6)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_10.addWidget(self.radioButton_3, 0, 1, 1, 1)
        self.radioButton_1 = QtWidgets.QRadioButton(self.frame_6)
        self.radioButton_1.setObjectName("radioButton_1")
        self.gridLayout_10.addWidget(self.radioButton_1, 0, 2, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_6)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_10.addWidget(self.radioButton_4, 1, 0, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame_6)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_10.addWidget(self.radioButton_5, 1, 1, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.frame_6)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout_10.addWidget(self.radioButton_6, 1, 2, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_10)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.saveConfigButton = QtWidgets.QPushButton(self.configure)
        self.saveConfigButton.setObjectName("saveConfigButton")
        self.verticalLayout_5.addWidget(self.saveConfigButton)
        self.Pages.addTab(self.configure, "")
        self.horizontalLayout.addWidget(self.Pages)
        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.Pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "肺结节预测"))
        self.label_5.setText(_translate("Form", "运行日志"))
        self.outPut.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
        self.openButton.setText(_translate("Form", "选择影像"))
        self.label_4.setText(_translate("Form", "肿瘤预测"))
        self.label_3.setText(_translate("Form", "影像分析"))
        self.label.setText(_translate("Form", "输入"))
        self.label_2.setText(_translate("Form", "结论"))
        self.Pages.setTabText(self.Pages.indexOf(self.diagnose), _translate("Form", "诊断"))
        self.groupBox_3.setTitle(_translate("Form", "批量处理"))
        self.batchSelecthButton.setText(_translate("Form", "选择目录"))
        self.batchDoButton.setText(_translate("Form", "开始批量处理"))
        self.groupBox_6.setTitle(_translate("Form", "运行日志"))
        self.groupBox_5.setTitle(_translate("Form", "疑似结节"))
        self.groupBox_4.setTitle(_translate("Form", "正常"))
        self.Pages.setTabText(self.Pages.indexOf(self.batch), _translate("Form", "批量处理"))
        self.groupBox.setTitle(_translate("Form", "参数设置"))
        self.cHANNEL_COUNTLabel.setText(_translate("Form", "CHANNEL_COUNT"))
        self._3DCNN_WEIGHTSLabel.setText(_translate("Form", "_3DCNN_WEIGHTS"))
        self.uNET_WEIGHTSLabel.setText(_translate("Form", "UNET_WEIGHTS"))
        self.tHRESHOLDLabel.setText(_translate("Form", "THRESHOLD"))
        self.bATCH_SIZELabel.setText(_translate("Form", "BATCH_SIZE"))
        self.temp_dirLabel.setText(_translate("Form", "temp_dir"))
        self.label_8.setText(_translate("Form", "TextLabel"))
        self.comboBox.setItemText(0, _translate("Form", "CNN卷积"))
        self.comboBox.setItemText(1, _translate("Form", "循环网络"))
        self.comboBox.setItemText(2, _translate("Form", "深度生成"))
        self.comboBox.setItemText(3, _translate("Form", "K-means"))
        self.comboBox.setItemText(4, _translate("Form", "SVM"))
        self.groupBox_2.setTitle(_translate("Form", "系统设置"))
        self.label_7.setText(_translate("Form", "透明度："))
        self.label_6.setText(_translate("Form", "色彩主题"))
        self.radioButton_2.setText(_translate("Form", "秋叶褐"))
        self.radioButton_3.setText(_translate("Form", "极光灰"))
        self.radioButton_1.setText(_translate("Form", "杏仁黄"))
        self.radioButton_4.setText(_translate("Form", "青草绿"))
        self.radioButton_5.setText(_translate("Form", "海天蓝"))
        self.radioButton_6.setText(_translate("Form", "葛巾紫"))
        self.saveConfigButton.setText(_translate("Form", "储存配置"))
        self.Pages.setTabText(self.Pages.indexOf(self.configure), _translate("Form", "配置"))