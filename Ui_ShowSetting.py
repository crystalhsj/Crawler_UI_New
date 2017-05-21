# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowSetting.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ShowSetting(object):
    def setupUi(self, ShowSetting):
        ShowSetting.setObjectName("ShowSetting")
        ShowSetting.resize(400, 501)
        self.pushButton = QtWidgets.QPushButton(ShowSetting)
        self.pushButton.setGeometry(QtCore.QRect(60, 410, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(ShowSetting)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 410, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(ShowSetting)
        self.checkBox.setGeometry(QtCore.QRect(90, 50, 97, 22))
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(ShowSetting)
        self.checkBox_2.setGeometry(QtCore.QRect(90, 100, 97, 22))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(ShowSetting)
        self.checkBox_3.setGeometry(QtCore.QRect(90, 150, 97, 22))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(ShowSetting)
        self.checkBox_4.setGeometry(QtCore.QRect(90, 200, 97, 22))
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(ShowSetting)
        self.checkBox_5.setGeometry(QtCore.QRect(90, 250, 97, 22))
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(ShowSetting)
        self.checkBox_6.setGeometry(QtCore.QRect(90, 300, 97, 22))
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(ShowSetting)
        self.checkBox_7.setGeometry(QtCore.QRect(90, 350, 97, 22))
        self.checkBox_7.setChecked(True)
        self.checkBox_7.setObjectName("checkBox_7")

        self.retranslateUi(ShowSetting)
        self.pushButton.clicked.connect(ShowSetting.slotConfirm)
        self.pushButton_2.clicked.connect(ShowSetting.slotReset)
        QtCore.QMetaObject.connectSlotsByName(ShowSetting)

    def retranslateUi(self, ShowSetting):
        _translate = QtCore.QCoreApplication.translate
        ShowSetting.setWindowTitle(_translate("ShowSetting", "展示设置"))
        self.pushButton.setText(_translate("ShowSetting", "确定"))
        self.pushButton_2.setText(_translate("ShowSetting", "重置"))
        self.checkBox.setText(_translate("ShowSetting", "微博ID"))
        self.checkBox_2.setText(_translate("ShowSetting", "微博昵称"))
        self.checkBox_3.setText(_translate("ShowSetting", "是否认证"))
        self.checkBox_4.setText(_translate("ShowSetting", "描述"))
        self.checkBox_5.setText(_translate("ShowSetting", "性别"))
        self.checkBox_6.setText(_translate("ShowSetting", "粉丝"))
        self.checkBox_7.setText(_translate("ShowSetting", "关注"))

