# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 680)
        Form.setMinimumSize(QtCore.QSize(480, 680))
        Form.setMaximumSize(QtCore.QSize(480, 680))
        self.groupBox_1 = QtWidgets.QGroupBox(Form)
        self.groupBox_1.setGeometry(QtCore.QRect(19, 79, 441, 111))
        self.groupBox_1.setObjectName("groupBox_1")
        self.pushButton_UpdateSerialPort = QtWidgets.QPushButton(self.groupBox_1)
        self.pushButton_UpdateSerialPort.setGeometry(QtCore.QRect(210, 30, 93, 61))
        self.pushButton_UpdateSerialPort.setObjectName("pushButton_UpdateSerialPort")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_1)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 141, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox_SerialPortName = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_SerialPortName.setObjectName("comboBox_SerialPortName")
        self.gridLayout.addWidget(self.comboBox_SerialPortName, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.comboBox_BaudRate = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_BaudRate.setObjectName("comboBox_BaudRate")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.gridLayout.addWidget(self.comboBox_BaudRate, 1, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_1)
        self.layoutWidget1.setGeometry(QtCore.QRect(330, 20, 95, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_Open = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.gridLayout_2.addWidget(self.pushButton_Open, 0, 0, 1, 1)
        self.pushButton_Close = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.gridLayout_2.addWidget(self.pushButton_Close, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(19, 199, 441, 401))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_TargetPosition = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_TargetPosition.setGeometry(QtCore.QRect(290, 360, 141, 31))
        self.lineEdit_TargetPosition.setObjectName("lineEdit_TargetPosition")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(220, 370, 60, 16))
        self.label_6.setObjectName("label_6")
        self.graphicsView_SystemDisplay = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView_SystemDisplay.setGeometry(QtCore.QRect(10, 30, 421, 321))
        self.graphicsView_SystemDisplay.setObjectName("graphicsView_SystemDisplay")
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(50, 20, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 610, 441, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_CurrentTime = QtWidgets.QLabel(self.groupBox_3)
        self.label_CurrentTime.setGeometry(QtCore.QRect(280, 30, 151, 21))
        self.label_CurrentTime.setText("")
        self.label_CurrentTime.setObjectName("label_CurrentTime")
        self.label_SerialPortStatement = QtWidgets.QLabel(self.groupBox_3)
        self.label_SerialPortStatement.setGeometry(QtCore.QRect(90, 30, 91, 21))
        self.label_SerialPortStatement.setText("")
        self.label_SerialPortStatement.setObjectName("label_SerialPortStatement")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 31, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(200, 31, 72, 15))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_1.setTitle(_translate("Form", "通信设置"))
        self.pushButton_UpdateSerialPort.setText(_translate("Form", "刷新"))
        self.label_2.setText(_translate("Form", "串口号"))
        self.label_3.setText(_translate("Form", "波特率"))
        self.comboBox_BaudRate.setItemText(0, _translate("Form", "9600"))
        self.comboBox_BaudRate.setItemText(1, _translate("Form", "115200"))
        self.pushButton_Open.setText(_translate("Form", "打开"))
        self.pushButton_Close.setText(_translate("Form", "关闭"))
        self.groupBox_2.setTitle(_translate("Form", "定位显示"))
        self.lineEdit_TargetPosition.setText(_translate("Form", "0,0"))
        self.label_6.setText(_translate("Form", "目标位置"))
        self.label_1.setText(_translate("Form", "基于超声波检测的目标定位系统"))
        self.groupBox_3.setTitle(_translate("Form", "状态栏"))
        self.label_4.setText(_translate("Form", "通信状态:"))
        self.label_5.setText(_translate("Form", "当前时间:"))
