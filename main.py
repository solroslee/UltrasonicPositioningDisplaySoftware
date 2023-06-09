"""
# File       : main.py
# Encoding   : utf-8
# Date       ：2023/3/30
# Author     ：LiFZ
# Email      ：lifzcn@gmail.com
# Version    ：python 3.9
# Description：
"""

import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from interface import Ui_Form
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class mainWindow(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        self.createItems()
        self.createSignalSlot()
        self.systemInterface()

    def createItems(self):
        self.com = QSerialPort()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(100)

    def createSignalSlot(self):
        self.pushButton_Open.clicked.connect(self.comOpen)
        self.pushButton_Close.clicked.connect(self.comClose)
        self.pushButton_UpdateSerialPort.clicked.connect(self.comRefresh)
        self.com.readyRead.connect(self.receiveData)

    def showTime(self):
        self.label_CurrentTime.setText(time.strftime("%B %d, %H:%M:%S", time.localtime()))

    def receiveData(self):
        try:
            rxData = bytes(self.com.readAll())
            self.lineEdit_TargetPosition.setText(rxData.decode("utf-8"))
            infoList = rxData.decode("utf-8").split(',')
            targetAngle = int(infoList[0])
            targetDistance = float(infoList[1])
            if targetAngle >= 0 and targetAngle < 45:
                self.lineEdit_TargetPosition.setText("E→N:" + str(targetAngle) + '°' + ',' + str(targetDistance) + 'm')
            elif targetAngle >= 45 and targetAngle < 90:
                self.lineEdit_TargetPosition.setText(
                    "N→E:" + str(90 - targetAngle) + '°' + ',' + str(targetDistance) + 'm')
            elif targetAngle >= 90 and targetAngle < 135:
                self.lineEdit_TargetPosition.setText(
                    "N→W:" + str(135 - targetAngle) + '°' + ',' + str(targetDistance) + 'm')
            else:
                self.lineEdit_TargetPosition.setText(
                    "W→N:" + str(180 - targetAngle) + '°' + ',' + str(targetDistance) + 'm')
            self.updateDisplay(targetAngle, targetDistance)
        except Exception as e:
            QMessageBox.critical(self, "严重错误", "串口接收数据错误!\n" + str(e))

    def comRefresh(self):
        self.comboBox_SerialPortName.clear()
        com = QSerialPort()
        com_list = QSerialPortInfo.availablePorts()
        for info in com_list:
            com.setPort(info)
            if com.open(QSerialPort.ReadWrite):
                self.comboBox_SerialPortName.addItem(info.portName())
                com.close()

    def comOpen(self):
        serialPortName = self.comboBox_SerialPortName.currentText()
        baudRate = int(self.comboBox_BaudRate.currentText())
        self.com.setPortName(serialPortName)
        try:
            if self.com.open(QSerialPort.ReadWrite) == False:
                QMessageBox.critical(self, "严重错误", "串口打开失败!")
                return
        except Exception as e:
            QMessageBox.critical(self, "严重错误", "串口打开失败!\n" + str(e))
            return
        self.pushButton_Close.setEnabled(True)
        self.pushButton_Open.setEnabled(False)
        self.pushButton_UpdateSerialPort.setEnabled(False)
        self.comboBox_SerialPortName.setEnabled(False)
        self.comboBox_BaudRate.setEnabled(False)
        self.label_SerialPortStatement.setText("通信已建立!")
        self.com.setBaudRate(baudRate)

    def comClose(self):
        self.com.close()
        self.pushButton_Close.setEnabled(False)
        self.pushButton_Open.setEnabled(True)
        self.pushButton_UpdateSerialPort.setEnabled(True)
        self.comboBox_SerialPortName.setEnabled(True)
        self.comboBox_BaudRate.setEnabled(True)
        self.label_SerialPortStatement.setText("通信已断开!")

    def close(self):
        sys.exit(app.exec_())

    def systemInterface(self):
        fig = Figure(figsize=(4, 3), dpi=100)
        self.canvas = FigureCanvas(fig)
        self.canvas.setParent(self.graphicsView_SystemDisplay)
        ax = fig.add_subplot(111, polar=True)
        ax.scatter(0, 0, color='r')
        ax.set_rmax(50)
        ax.set_autoscale_on(False)
        scene = QGraphicsScene(self)
        scene.addWidget(self.canvas)
        self.graphicsView_SystemDisplay.setScene(scene)

    def updateDisplay(self, targetAngle, targetDistance):
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111, polar=True)
        ax.scatter(np.pi * targetAngle / 180, targetDistance, color='r')
        ax.set_rmax(50)
        ax.set_autoscale_on(False)
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = mainWindow()
    myWin.show()
    sys.exit(app.exec_())
