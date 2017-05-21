import copy
import sys
from PyQt5 import QtWidgets
from Config import Config
from Ui_ShowSetting import Ui_ShowSetting

class ShowSettingDialog(QtWidgets.QDialog, Ui_ShowSetting):
    def __init__(self):
        super(ShowSettingDialog, self).__init__()
        self.setupUi(self)
        self.config = Config()
        self.data = self.config.data
        self.rawData = copy.deepcopy(self.data)
        self.checkBox.setChecked(self.data["Id"])
        self.checkBox_2.setChecked(self.data["name"])
        self.checkBox_3.setChecked(self.data["verified"])
        self.checkBox_4.setChecked(self.data["description"])
        self.checkBox_5.setChecked(self.data["gender"])
        self.checkBox_6.setChecked(self.data["fans"])
        self.checkBox_7.setChecked(self.data["follow"])

    def work(self):
        self.exec()

    def slotConfirm(self):
        self.data["Id"] = self.checkBox.isChecked()
        self.data["name"] = self.checkBox_2.isChecked()
        self.data["verified"] = self.checkBox_3.isChecked()
        self.data["description"] = self.checkBox_4.isChecked()
        self.data["gender"] = self.checkBox_5.isChecked()
        self.data["fans"] = self.checkBox_6.isChecked()
        self.data["follow"]=self.checkBox_7.isChecked()
        self.config.setConfig(self.data)
        self.close()

    def slotReset(self):
        self.data = copy.deepcopy(self.rawData)
        self.checkBox.setChecked(self.data["Id"])
        self.checkBox_2.setChecked(self.data["name"])
        self.checkBox_3.setChecked(self.data["verified"])
        self.checkBox_4.setChecked(self.data["description"])
        self.checkBox_5.setChecked(self.data["gender"])
        self.checkBox_6.setChecked(self.data["fans"])
        self.checkBox_7.setChecked(self.data["follow"])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = ShowSettingDialog()
    main.work()
    sys.exit(app.exec_())