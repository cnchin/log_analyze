# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 370, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(200, 110, 581, 231))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menu)
        self.menu_3.setObjectName("menu_3")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.cat_version = QtWidgets.QAction(MainWindow)
        self.cat_version.setObjectName("cat_version")
        self.cat_author = QtWidgets.QAction(MainWindow)
        self.cat_author.setObjectName("cat_author")
        self.open_file = QtWidgets.QAction(MainWindow)
        self.open_file.setObjectName("open_file")
        self.open_folder = QtWidgets.QAction(MainWindow)
        self.open_folder.setObjectName("open_folder")
        self.menu_3.addAction(self.open_file)
        self.menu_3.addAction(self.open_folder)
        self.menu.addAction(self.menu_3.menuAction())
        self.menu_2.addAction(self.cat_version)
        self.menu_2.addAction(self.cat_author)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "点他"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_3.setTitle(_translate("MainWindow", "打开"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))
        self.cat_version.setText(_translate("MainWindow", "版本"))
        self.cat_author.setText(_translate("MainWindow", "作者"))
        self.open_file.setText(_translate("MainWindow", "文件"))
        self.open_folder.setText(_translate("MainWindow", "文件夹"))
