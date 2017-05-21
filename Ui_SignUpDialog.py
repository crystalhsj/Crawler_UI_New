import sys
from UserList import UserList
from  PyQt5 import QtWidgets
from Ui_SignUp import Ui_SignUp

class SignUpDialog(QtWidgets.QDialog, Ui_SignUp):
    def __init__(self):
        super(SignUpDialog, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.onClick);

    def onClick(self):
        name=self.lineEdit.text()
        passwd=self.lineEdit_2.text()
        confirm=self.lineEdit_3.text()
        if passwd!=confirm:
            QtWidgets.QMessageBox.warning(self,"密码错误","请输入同样的密码！！！",QtWidgets.QMessageBox.Yes)
        elif passwd=="":
            QtWidgets.QMessageBox.warning(self, "密码错误", "密码不能为空！！！", QtWidgets.QMessageBox.Yes)
        elif UserList().addUser(name,passwd):
            QtWidgets.QMessageBox.information(self, "注册成功", "恭喜您注册成功！！！", QtWidgets.QMessageBox.Yes)
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "用户已存在", "该用户名已被使用，请重试！！！", QtWidgets.QMessageBox.Yes)

    def work(self):
        self.exec()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = SignUpDialog()
    main.work()

