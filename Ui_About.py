# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(300, 400)
        About.setMinimumSize(QtCore.QSize(300, 400))
        About.setMaximumSize(QtCore.QSize(300, 400))
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(100, 100, 100, 100))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(About)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 340, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(About)
        self.pushButton_2.clicked.connect(About.close)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "关于"))
        self.label.setText(_translate("About", "相关作者:\n丁庆祝 花盛鋆"))
        self.pushButton_2.setText(_translate("About", "确定"))

