# 导入库
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from ui.mainWindowLayout import Ui_MainWindow
import inspect


class UiMainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(UiMainWindow, self).__init__(parent)
        self.setupUi(self)
        print("UiMainWindow init success")
        self.pushButton.clicked.connect(self.display)
        self.open_file.triggered.connect(self.open_file_slot)
        self.cat_version.triggered.connect(self.cat_version_slot)
        self.cat_author.triggered.connect(self.cat_author_slot)

    def display(self):  # test operation
        print("Func={0}() start".format(inspect.stack()[0][3]))
        self.textBrowser.setText("hello world")

    def open_file_slot(self):  # 打开 文件，并将内容显示到text控件上
        print("Func={0}() start".format(inspect.stack()[0][3]))
        filePath = QFileDialog.getOpenFileName(self)
        filePath = str(filePath[0])
        print(filePath)
        try:
            with open(filePath, "r") as f:
                readlines = f.readlines()
            for readline in readlines:
                self.textBrowser.append(readline)
        except Exception:
            print("open file error")

    def cat_version_slot(self):  # 查看版本信息
        QMessageBox.information(
            self,
            '版本信息',
            'version = 0.01')

    def cat_author_slot(self):  # 查看作者信息
        QMessageBox.information(
            self,
            '作者信息',
            'author = chin')


if __name__ == '__main__':
    # 创建一个应用程序
    app = QApplication(sys.argv)
    # 实例化UiMainWindow类
    ui = UiMainWindow()
    # 显示该窗口
    ui.show()
    sys.exit(app.exec_())
