import sys
from  PyQt5 import QtWidgets,QtGui
from Ui_Help import Ui_Help

class HelpDialog(QtWidgets.QDialog,Ui_Help):
    def __init__(self):
        super(HelpDialog, self).__init__()
        self.setupUi(self)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = HelpDialog()
    main.work()
    sys.exit(app.exec_())
