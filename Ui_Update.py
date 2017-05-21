# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Update.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Update(object):
    def setupUi(self, Update):
        Update.setObjectName("Update")
        Update.resize(300, 400)
        Update.setMinimumSize(QtCore.QSize(300, 400))
        Update.setMaximumSize(QtCore.QSize(300, 400))
        self.label = QtWidgets.QLabel(Update)
        self.label.setGeometry(QtCore.QRect(80, 170, 141, 41))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Update)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 320, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Update)
        self.pushButton_2.clicked.connect(Update.close)
        QtCore.QMetaObject.connectSlotsByName(Update)

    def retranslateUi(self, Update):
        _translate = QtCore.QCoreApplication.translate
        Update.setWindowTitle(_translate("Update", "更新"))
        self.label.setText(_translate("Update", "软件已经是最新状态"))
        self.pushButton_2.setText(_translate("Update", "确定"))

