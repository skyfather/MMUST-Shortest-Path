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
from manageUsers import *
from login import *
from MainWindow import *
from ManageVertex import *
from AdminPanel import *


class AdminPanelController(QtWidgets.QMainWindow, AdminPanel):
    def __init__(self, parent=None):
        super(AdminPanelController, self).__init__(parent=parent)
        self.AdminUi(self)

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
            self.hide()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ManagePaths()
            self.ui.setupManagePaths(self.window)
            self.window.show()
        except Exception as e:
            print(e)
    def manageGraph(self):
        self.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def manageUsers(self):
        self.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ManageUsers()
        self.ui.setupManageUsers(self.window)
        self.window.show()
    def logout(self):
        self.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupLogin(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    titleMain = AdminPanelController()
    titleMain.show()
    sys.exit(app.exec_())

