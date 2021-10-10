# 导入库
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow

# 导入自定义类
from ui.mainWindowLayout import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
