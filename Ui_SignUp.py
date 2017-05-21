# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignUp.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignUp(object):
    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.resize(300, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SignUp.sizePolicy().hasHeightForWidth())
        SignUp.setSizePolicy(sizePolicy)
        SignUp.setMinimumSize(QtCore.QSize(300, 400))
        SignUp.setMaximumSize(QtCore.QSize(300, 400))
        self.lineEdit = QtWidgets.QLineEdit(SignUp)
        self.lineEdit.setGeometry(QtCore.QRect(122, 100, 151, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(SignUp)
        self.lineEdit_2.setGeometry(QtCore.QRect(122, 160, 151, 27))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(SignUp)
        self.lineEdit_3.setGeometry(QtCore.QRect(122, 220, 151, 27))
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(SignUp)
        self.label.setGeometry(QtCore.QRect(30, 100, 68, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(SignUp)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 68, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(SignUp)
        self.label_3.setGeometry(QtCore.QRect(30, 230, 68, 17))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(SignUp)
        self.pushButton.setGeometry(QtCore.QRect(100, 320, 99, 27))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "注册用户"))
        self.label.setText(_translate("SignUp", "用户名："))
        self.label_2.setText(_translate("SignUp", "密码："))
        self.label_3.setText(_translate("SignUp", "确认密码："))
        self.pushButton.setText(_translate("SignUp", "注册"))

