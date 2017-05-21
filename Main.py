import sys
from  PyQt5 import QtWidgets,QtGui
from Ui_Window import Ui_MainWindow
from LoginDialog import LoginDialog
from Ui_SignUpDialog import SignUpDialog
from HelpDialog import HelpDialog
from AboutDialog import AboutDialog
from UpdateDialog import UpdateDialog
from SpiderSettingDialog import SpiderSettingDialog
from ShowSettingDialog import ShowSettingDialog
from Spider import *
from Config import Config
from Window import Ui_MainWindow
from PyQt5 import QtCore


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    _signal = QtCore.pyqtSignal(str)
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.label_2.setText("请登录。。。")
        self.tabWidget.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.lineEdit.setText("5822209475")
        self.lineEdit_4.setText("test")
        self.action_login.triggered.connect(self.loginSlot)
        self.action_signin.triggered.connect(self.signUpSlot)
        self.action_help.triggered.connect(self.helpSlot)
        self.action_about.triggered.connect(self.aboutSlot)
        self.action_update.triggered.connect(self.updateSlot)
        self.action_8.triggered.connect(self.spiderSettingSlot)
        self.action_10.triggered.connect(self.showSettingSlot)
        self.pushButton_8.clicked.connect(self.test)
        self.pushButton.clicked.connect(self.startSpiderSlot)
        self.pushButton_2.clicked.connect(self.pauseSpiderSlot)
        self.pauseflag=False
        self.pushButton_3.clicked.connect(self.stopSpiderSlot)
        self.pushButton_4.clicked.connect(self.showContentSlot)
        self.show()
        self.SW=None
        self._signal.connect(self.textEditSlot)

    def showContentSlot(self):
        filename=self.comboBox.currentText()
        data=Config().getConfig()
        try:
            self.textEdit_2.clear()
            list_show=[data["Id"],data["name"],data["verified"],data["description"],data["gender"],data["fans"],data["follow"]]
            with open(filename+".csv",'r')as r:
                rr=csv.reader(r)
                for i in rr:
                    lis=[]
                    for j in range(0,len(list_show)):
                        if list_show[j]:
                            lis.append(i[j])
                    self.textEdit_2.append(reduce(lambda x,y:str(x)+" "+str(y),lis)+"\n")
            r.close()
        except:
            self.textEdit_2.setText("未找到该文件!")

    def textEditEmit(self,s):
        self._signal.emit(s)

    def textEditSlot(self,s):
        self.textEdit.append(s+"\n")


    def test(self):
        #uid=self.lineEdit.text()
        #testName=self.lineEdit_4.text()
        info=SpiderWb(start_user=self.lineEdit.text(), task_name=self.lineEdit_4.text(),threads=1,show=self).test()
        for i in range(0,len(info)):
            try:
                self.treeWidget.topLevelItem(i).setText(1,str(info[i]))
            except:
                continue

    def spiderSettingSlot(self):
        SpiderSettingDialog().exec()

    def showSettingSlot(self):
        ShowSettingDialog().exec()

    def updateSlot(self):
        UpdateDialog().exec()

    def aboutSlot(self):
        AboutDialog().exec()

    def helpSlot(self):
        HelpDialog().exec()

    def loginSlot(self):
        res=LoginDialog().work()
        if res :
            self.tabWidget.setEnabled(True)
            self.label_2.setText("欢迎登陆，"+res)

    def signUpSlot(self):
        res=SignUpDialog().work()

    def startSpiderSlot(self):
        if self.lineEdit.text()=="" or self.lineEdit.text()==None:
            self.lineEdit.setText("5822209475")
        if self.lineEdit_4.text()=="" or self.lineEdit_4.text()==None:
            self.lineEdit_4.setText("test")
        data=Config().getConfig()
        direction=["followers","fans","likes"]
        self.SW=SpiderWb(start_user=self.lineEdit.text(), task_name=self.lineEdit_4.text(),
                         threads=data["threadNum"],direction=direction[int(data["direction"])],
                         spider_depth=data["depth"],spider_width=data["width"],
                         spider_people=data["number"], spider_time=data["time"]*60,show=self)
        self.SW.start()
        self.SW.time_over()
        flag=False
        for i in range(0,self.comboBox.count()):
            if self.comboBox.itemText(i)==self.lineEdit_4.text():
                flag=True
                break
        if not flag:
            self.comboBox.insertItem(0, self.lineEdit_4.text())
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)


    def pauseSpiderSlot(self):
        if self.SW!= None:
            if self.pauseflag==False:
                self.SW.parse()
                self.pauseflag=True
            else:
                self.SW.resume()
                self.pauseflag=False

    def stopSpiderSlot(self):
        if self.SW!=None:
            if self.SW.thread.running:
                self.SW.stop()
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(False)



app = QtWidgets.QApplication(sys.argv)
main = Main()
sys.exit(app.exec_())

