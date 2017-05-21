# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Help.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(300, 400)
        Help.setMinimumSize(QtCore.QSize(300, 400))
        Help.setMaximumSize(QtCore.QSize(300, 400))
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Help)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 301, 341))
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(Help)
        self.pushButton.setGeometry(QtCore.QRect(100, 360, 99, 27))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Help)
        self.pushButton.clicked.connect(Help.close)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "帮助"))
        self.plainTextEdit.setPlainText(_translate("Help", "这里是产品的帮助文档。\n"
"微博爬虫程序使用说明：\n1. 初始用户及任务名请根据需要进行设置，若为空则默认是初始值\n2. 点击'测试用户'可以查看初始用户的各项信息\n"
                       "3. 点击'开始爬取'进行爬虫,中途可以点击'暂停'或'停止爬虫'\n4. 爬虫模块右侧的文本框显示剩余的时间，若在规定时间内完成爬虫所设置的其他条件则显示结束\n"
                       "5. 同一个初始用户不能多次爬取，每次更换\n6. 可以在'爬虫设置'中进行相关设置"))
        self.pushButton.setText(_translate("Help", "确定"))

