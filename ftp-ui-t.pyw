# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\FTP\ftp.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,ftp

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 40, 331, 131))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(160, 200, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 200, 91, 20))
        self.label.setObjectName("label")
        #self.pushButton.clicked.connect(Dialog.PushButtonlClicked)
        self.pushButton.clicked.connect(self.buttonClicked)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "FTP"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "请在此输入要发布的信息。"))
        self.pushButton.setText(_translate("Dialog", "发送"))

        self.comboBox.setItemText(0, _translate("Dialog", "语文"))
        self.comboBox.setItemText(1, _translate("Dialog", "数学"))
        self.comboBox.setItemText(2, _translate("Dialog", "英语"))
        self.comboBox.setItemText(3, _translate("Dialog", "物理"))
        self.comboBox.setItemText(4, _translate("Dialog", "化学"))
        self.comboBox.setItemText(5, _translate("Dialog", "地理"))
        self.comboBox.setItemText(6, _translate("Dialog", "班务"))

        
        
        
        self.label.setText(_translate("Dialog", "信息类别："))

    def buttonClicked(self):
        t=self.plainTextEdit.toPlainText()
        n=self.comboBox.currentText()
        out=n+":"+t
        ftp.send(out)
        
        



if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    
    ui.setupUi(MainWindow) 
    MainWindow.show()
    sys.exit(app.exec_()) 
