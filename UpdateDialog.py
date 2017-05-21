import sys
from  PyQt5 import QtWidgets,QtGui
from Ui_Update import Ui_Update

class UpdateDialog(QtWidgets.QDialog,Ui_Update):
    def __init__(self):
        super(UpdateDialog, self).__init__()
        self.setupUi(self)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = UpdateDialog()
    main.work()
    sys.exit(app.exec_())
