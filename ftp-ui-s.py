# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\FTP\ftp-s.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

import sys,ftp

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(609, 296)
        self.textBrowser = QtWidgets.QTextEdit(Dialog)
        self.textBrowser.setReadOnly(True)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        
        
        self.timer = QTimer(Dialog)
        self.timer.timeout.connect(self.buttonClicked) 
        self.timer.start(10000) 
        self.textBrowser.setGeometry(QtCore.QRect(10, 21, 591, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.buttonClicked)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 200, 91, 20))
        self.label.setObjectName("label")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "FTP"))
        
        self.pushButton.setText(_translate("Dialog", "刷新"))


    def buttonClicked(self):
        t=ftp.ftp('r')
        if t=='err':
            self.label.setText(_translate("Dialog", "连接失败"))
        else:
            t=t.split('%')[1:]
            #t.reverse()
            self.textBrowser.clear()
            for i in t:
                i=i.split(':')
                a=i[0]+':'
                b='  '+i[1]
                self.textBrowser.append(a)
                self.textBrowser.append(b)
        
        



if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow) 
    MainWindow.show()
    sys.exit(app.exec_()) 
