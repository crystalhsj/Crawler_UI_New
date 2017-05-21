import sys
from  PyQt5 import QtWidgets,QtGui
from Ui_About import Ui_About

class AboutDialog(QtWidgets.QDialog,Ui_About):
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.setupUi(self)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = AboutDialog()
    main.work()
    sys.exit(app.exec_())
