import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from ui.main import Ui_MainWindow

if __name__ == '__main__':
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui=Ui_MainWindow()
    #向主窗口上创建控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
