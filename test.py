# 导入库
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui.mainWindowLayout import Ui_MainWindow
import inspect


class UiMainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(UiMainWindow, self).__init__(parent)
        self.setupUi(self)
        print("UiMainWindow init success")
        self.pushButton.clicked.connect(self.display)
        self.open_file.triggered.connect(self.open_file_slot)

    def display(self):
        print("Func={0}() start".format(inspect.stack()[0][3]))
        self.textBrowser.setText("hello world")

    def open_file_slot(self):
        print("Func={0}() start".format(inspect.stack()[0][3]))
        path = QFileDialog.getOpenFileName(self, "open")
        print(path)


if __name__ == '__main__':
    # 创建一个应用程序
    app = QApplication(sys.argv)
    # 实例化UiMainWindow类
    ui = UiMainWindow()
    # 显示该窗口
    ui.show()
    sys.exit(app.exec_())
