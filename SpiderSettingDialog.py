import copy
import sys
from PyQt5 import QtWidgets
from Config import Config
from Ui_SpiderSetting import Ui_SpiderSetting


class SpiderSettingDialog(QtWidgets.QDialog, Ui_SpiderSetting):
    def __init__(self):
        super(SpiderSettingDialog, self).__init__()
        self.setupUi(self)
        self.config = Config()
        self.data = self.config.data
        self.rawData = copy.deepcopy(self.data)
        self.spinBox.setValue(self.data["threadNum"])
        self.comboBox.setCurrentIndex(self.data["direction"])
        self.spinBox_2.setValue(self.data["depth"])
        self.spinBox_3.setValue(self.data["width"])
        self.spinBox_4.setValue(self.data["number"])
        self.spinBox_5.setValue(self.data["time"])

    def work(self):
        self.exec()

    def slotConfirm(self):
        self.data["threadNum"] = self.spinBox.value()
        self.data["direction"] = self.comboBox.currentIndex()
        self.data["depth"] = self.spinBox_2.value()
        self.data["width"] = self.spinBox_3.value()
        self.data["number"] = self.spinBox_4.value()
        self.data["time"] = self.spinBox_5.value()
        self.config.setConfig(self.data)
        self.close()

    def slotReset(self):
        self.data = copy.deepcopy(self.rawData)
        self.spinBox.setValue(self.data["threadNum"])
        self.comboBox.setCurrentIndex(self.data["direction"])
        self.spinBox_2.setValue(self.data["depth"])
        self.spinBox_3.setValue(self.data["width"])
        self.spinBox_4.setValue(self.data["number"])
        self.spinBox_5.setValue(self.data["time"])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = SpiderSettingDialog()
    main.work()
    sys.exit(app.exec_())
