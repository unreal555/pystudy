# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(802, 612)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.n_view = QtWidgets.QGraphicsView(Form)
        self.n_view.setEnabled(True)
        self.n_view.setObjectName("n_view")
        self.verticalLayout.addWidget(self.n_view)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.z_view = QtWidgets.QGraphicsView(Form)
        self.z_view.setObjectName("z_view")
        self.verticalLayout_3.addWidget(self.z_view)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.v_label = QtWidgets.QLabel(Form)
        self.v_label.setTextFormat(QtCore.Qt.AutoText)
        self.v_label.setAlignment(QtCore.Qt.AlignCenter)
        self.v_label.setObjectName("v_label")
        self.verticalLayout_4.addWidget(self.v_label)
        self.v_view = QtWidgets.QGraphicsView(Form)
        self.v_view.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_view.setObjectName("v_view")
        self.verticalLayout_4.addWidget(self.v_view)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.a_label = QtWidgets.QLabel(Form)
        self.a_label.setAlignment(QtCore.Qt.AlignCenter)
        self.a_label.setObjectName("a_label")
        self.verticalLayout_2.addWidget(self.a_label)
        self.a_view = QtWidgets.QGraphicsView(Form)
        self.a_view.setObjectName("a_view")
        self.verticalLayout_2.addWidget(self.a_view)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.button = QtWidgets.QPushButton(Form)
        self.button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy)
        self.button.setObjectName("button")
        self.gridLayout.addWidget(self.button, 2, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "压力曲线"))
        self.label_3.setText(_translate("Form", "电阻曲线"))
        self.v_label.setText(_translate("Form", "电压曲线"))
        self.a_label.setText(_translate("Form", "电流曲线"))
        self.button.setText(_translate("Form", "PushButton"))