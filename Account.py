# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Fallen\Documents\project\gui2\Account.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from  PyQt5.QtWidgets import QMessageBox
from dbconnections.DbCon import DbCon
from MySQLdb import Error


class Ui_Account(object):
    def __init__(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Login")

    def setupAccount(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 396)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_username = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_username.setGeometry(QtCore.QRect(130, 50, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_username.setFont(font)
        self.txt_username.setObjectName("txt_username")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 151, 21))
        self.label.setObjectName("label")
        self.txt_oldPass = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_oldPass.setGeometry(QtCore.QRect(130, 110, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_oldPass.setFont(font)
        self.txt_oldPass.setObjectName("txt_oldPass")
        self.txt_newPass = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_newPass.setGeometry(QtCore.QRect(130, 170, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_newPass.setFont(font)
        self.txt_newPass.setObjectName("txt_newPass")
        self.txt_confirmPass = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_confirmPass.setGeometry(QtCore.QRect(130, 240, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_confirmPass.setFont(font)
        self.txt_confirmPass.setObjectName("txt_confirmPass")
        self.btn_Save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Save.setGeometry(QtCore.QRect(300, 300, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Save.setFont(font)
        self.btn_Save.setObjectName("btn_Save")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(410, 300, 81, 31))
        self.btn_exit.setObjectName("btn_exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btn_Save.clicked.connect(self.changeLoginDetails)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txt_username.setPlaceholderText(_translate("MainWindow", "username"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Login Details</span></p></body></html>"))
        self.txt_oldPass.setPlaceholderText(_translate("MainWindow", "old_password"))
        self.txt_newPass.setPlaceholderText(_translate("MainWindow", "new_password"))
        self.txt_confirmPass.setPlaceholderText(_translate("MainWindow", "confirm_password"))
        self.btn_Save.setText(_translate("MainWindow", "Save"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))
        MainWindow.setWindowIcon(QIcon("pics\\icon"))

    def changeLoginDetails(self):
        username = self.txt_username.text()
        oldpass = self.txt_oldPass.text()
        newpass = self.txt_newPass.text()
        confirmpass = self.txt_confirmPass.text()
        try:
            self.dbcon = DbCon()
            self.status = self.dbcon.getConnection()
            if self.status:
                if username !="":
                    if newpass !="" and confirmpass !="":
                        if newpass == confirmpass:
                            try:
                                self.admin = self.dbcon.get_user(username)
                            except Error as e:
                                print(e)
                            print(self.admin[2])
                            if self.admin is not None:
                                if oldpass == self.admin[2]:
                                    print("Yes")
                                else:
                                    self.msg.setIcon(QMessageBox.Warning)
                                    self.msg.setText("The oldpassword does not match")
                                    self.msg.setStandardButtons(QMessageBox.Ok)
                                    self.msg.exec_()
                            else:
                                self.msg.setIcon(QMessageBox.Warning)
                                self.msg.setText("The user does not exist")
                                self.msg.setStandardButtons(QMessageBox.Ok)
                                self.msg.exec_()
                        else:
                            self.msg.setIcon(QMessageBox.Warning)
                            self.msg.setText("Unmarching new password")
                            self.msg.setStandardButtons(QMessageBox.Ok)
                            self.msg.exec_()
                    else:
                        self.msg.setIcon(QMessageBox.Warning)
                        self.msg.setText("Ensure new password and confirm password are not empty")
                        self.msg.setStandardButtons(QMessageBox.Ok)
                        self.msg.exec_()
                else:
                    self.msg.setIcon(QMessageBox.Warning)
                    self.msg.setText("Please input the username")
                    self.msg.setStandardButtons(QMessageBox.Ok)
                    self.msg.exec_()
            else:
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.setText("Database connection not established")
                self.msg.setStandardButtons(QMessageBox.Ok)
                self.msg.exec_()

        except Error as e:
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText(str(e))
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Account()
    ui.setupAccount(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

