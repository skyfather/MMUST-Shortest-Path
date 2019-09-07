# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Fallen\Documents\project\gui2\administration.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from AddVertex import Ui_AddVertex
from Managepaths import *
from ManagePaths2 import *
from manageUsers import *
from login import *
from MainWindow import *
from ManageVertex import *
from Account import *
import sys

class AdminPanel(object):
    def AdminUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 399)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(110, 10, 341, 31))
        self.lblTitle.setObjectName("lblTitle")
        self.btnLogout = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogout.setGeometry(QtCore.QRect(540, 330, 91, 23))
        self.btnLogout.setObjectName("btnLogout")

        self.btnLogout.clicked.connect(self.logout)

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 90, 441, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnPaths = QtWidgets.QPushButton(self.layoutWidget)
        self.btnPaths.setObjectName("btnPaths")

        self.btnPaths.clicked.connect(self.managePaths)

        self.gridLayout.addWidget(self.btnPaths, 2, 1, 1, 1)
        self.btnGraph = QtWidgets.QPushButton(self.layoutWidget)
        self.btnGraph.setObjectName("btnGraph")

        self.btnGraph.clicked.connect(self.manageGraph)

        self.gridLayout.addWidget(self.btnGraph, 1, 1, 1, 1)
        self.btnUsers = QtWidgets.QPushButton(self.layoutWidget)
        self.btnUsers.setObjectName("btnUsers")

        self.btnUsers.clicked.connect(self.manageAccount)

        self.gridLayout.addWidget(self.btnUsers, 4, 1, 1, 1)
        self.btnVertex = QtWidgets.QPushButton(self.layoutWidget)
        self.btnVertex.setObjectName("btnVertex")
        self.gridLayout.addWidget(self.btnVertex, 3, 1, 1, 1)

        self.btnVertex.clicked.connect(self.manageVertex)

        self.lblIcon = QtWidgets.QLabel(self.centralwidget)
        self.lblIcon.setGeometry(QtCore.QRect(590, 0, 41, 31))
        self.lblIcon.setStyleSheet("border-image: url(:/new_icons/icons8-administrator-male-26.png);")
        self.lblIcon.setObjectName("lblIcon")
        self.lblUser = QtWidgets.QLabel(self.centralwidget)
        self.lblUser.setGeometry(QtCore.QRect(510, 30, 141, 21))
        self.lblUser.setObjectName("lblUser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Administration Panel</span></p></body></html>"))
        self.btnLogout.setText(_translate("MainWindow", "Logout"))
        self.btnPaths.setText(_translate("MainWindow", "Manage Paths"))
        self.btnGraph.setText(_translate("MainWindow", "Home"))
        self.btnUsers.setText(_translate("MainWindow", "Manage Account"))
        self.btnVertex.setText(_translate("MainWindow", "Manage Buildings"))
        self.lblIcon.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lblUser.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Logged in as: Admin</p></body></html>"))
        MainWindow.setWindowIcon(QIcon("pics\\icon"))
    #
    def manageVertex(self):
        try:
            self.addVertex = QtWidgets.QMainWindow()
            self.ui = Ui_ManageVertex()
            self.ui.setupManageVertex(self.addVertex)
            self.addVertex.show()
        except :
            print("Unable to open the Manage Vertex window")
    def managePaths(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ManagePaths2()
            self.ui.setupManagePaths2(self.window)
            self.window.show()
        except Exception as e:
            print(e)
    def manageGraph(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def manageAccount(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Account()
        self.ui.setupAccount(self.window)
        self.window.show()
    def logout(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupLogin(self.window)
        self.window.show()

import new_icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AdminPanel()
    ui.AdminUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

