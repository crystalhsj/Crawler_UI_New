import sys
from UserList import UserList
from  PyQt5 import QtWidgets,QtGui
from Ui_Login import Ui_Login

class LoginDialog(QtWidgets.QDialog,Ui_Login):
    def __init__(self):
        super(LoginDialog, self).__init__()
        self.setupUi(self)
        self.name=""
        self.pushButton.clicked.connect(self.onClick)

    def onClick(self):
        name=self.lineEdit.text()
        passwd=self.lineEdit_2.text()
        if UserList().checkUser(name,passwd):
            QtWidgets.QMessageBox.information(self, "登陆成功", "恭喜您登陆成功！！！", QtWidgets.QMessageBox.Yes)
            self.name=name
            self.close()

        else:
            QtWidgets.QMessageBox.warning(self, "登陆失败", "不存在帐号或帐号密码不正确！！！", QtWidgets.QMessageBox.Yes)

    def work(self):
        self.exec()
        return self.name

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = LoginDialog()
    main.work()
    sys.exit(app.exec_())
