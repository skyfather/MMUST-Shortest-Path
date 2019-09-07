# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Fallen\Documents\project\gui2\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

from dbconnections.DbCon import DbCon
# from dbconnections.Dbtest2 import Dbtest2
from dbconnections.DbCon import DbCon
from AdminPanel import *
from MainWindow import *
import sys

class Ui_Login(object):
    def __init__(self):
        self.msg_warning = QMessageBox()
        self.msg_warning.setIcon(QMessageBox.Warning)
        self.msg_warning.setWindowTitle("MMUST NAVIGATOR")

    def setupLogin(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 407)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(290, 10, 20, 421))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lblUsername = QtWidgets.QLabel(self.centralwidget)
        self.lblUsername.setGeometry(QtCore.QRect(330, 90, 51, 21))
        self.lblUsername.setObjectName("lblUsername")
        self.lblPassword = QtWidgets.QLabel(self.centralwidget)
        self.lblPassword.setGeometry(QtCore.QRect(330, 210, 61, 21))
        self.lblPassword.setObjectName("lblPassword")
        self.btnlogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnlogin.setGeometry(QtCore.QRect(430, 320, 75, 23))
        self.btnlogin.setObjectName("btnlogin")
        self.txtusername = QtWidgets.QLineEdit(self.centralwidget)
        self.txtusername.setGeometry(QtCore.QRect(430, 90, 171, 20))
        self.txtusername.setObjectName("txtusername")
        self.txtpassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtpassword.setGeometry(QtCore.QRect(430, 210, 171, 20))
        self.txtpassword.setObjectName("txtpassword")
        self.btncancel = QtWidgets.QPushButton(self.centralwidget)
        self.btncancel.setGeometry(QtCore.QRect(530, 320, 75, 23))
        self.btncancel.setObjectName("btncancel")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(330, 10, 311, 41))
        self.lblTitle.setObjectName("lblTitle")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.txtpassword.setEchoMode(QLineEdit.Password)
        self.btnlogin.clicked.connect(self.login)
        self.btncancel.clicked.connect(self.cancell)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.lblUsername.setText(_translate("MainWindow", "Username"))
        self.lblPassword.setText(_translate("MainWindow", "Password"))
        self.btnlogin.setText(_translate("MainWindow", "Login"))
        self.btncancel.setText(_translate("MainWindow", "Exit"))
        self.lblTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">MMUST NAVIGATOR LOGIN</span></p></body></html>"))
        MainWindow.setWindowIcon(QIcon('pics\\icon.png'))

    def login(self):
        # self.hide()
        dbcon = DbCon()
        status = dbcon.getConnection()
        if status:
            username = self.txtusername.text()
            password = self.txtpassword.text()
            if username !='' and password!='':
                users = dbcon.authenticate_user(username,password)
                if users is not None:
                    # self.hide()
                    self.window = QtWidgets.QMainWindow()
                    self.ui = AdminPanel()
                    self.ui.AdminUi(self.window)
                    self.window.show()
                else:
                    self.msg_warning.setText("Invalid username or Password")
                    self.msg_warning.setStandardButtons(QMessageBox.Ok)
                    self.msg_warning.exec_()
                    self.txtusername.setText("")
                    self.txtpassword.setText("")
            else:
                self.msg_warning.setText("Fill all the values")
                self.msg_warning.setStandardButtons(QMessageBox.Ok)
                self.msg_warning.exec_()
                self.txtusername.setText("")
                self.txtpassword.setText("")
        else:
            self.msg_warning.setText("Database Communication not established! ")
            self.msg_warning.setStandardButtons(QMessageBox.Ok)
            self.msg_warning.exec_()

    def cancell(self):
        try:
            self.hide()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupAccount(self.window)
            self.window.show()
        except Exception as e:
            print(e)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupLogin(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())