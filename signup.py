# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Fallen\Documents\project\gui2\signup.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from dbconnections.DbCon import DbCon
from MySQLdb import Error
from login import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(592, 349)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 50, 71, 31))
        self.label.setObjectName("label")
        self.txt_userid = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_userid.setGeometry(QtCore.QRect(220, 50, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_userid.setFont(font)
        self.txt_userid.setObjectName("txt_userid")
        self.txt_username = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_username.setGeometry(QtCore.QRect(220, 120, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_username.setFont(font)
        self.txt_username.setObjectName("txt_username")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 190, 71, 31))
        self.label_2.setObjectName("label_2")
        self.txt_password = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_password.setGeometry(QtCore.QRect(220, 190, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_password.setFont(font)
        self.txt_password.setInputMask("")
        self.txt_password.setText("")
        self.txt_password.setObjectName("txt_password")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 120, 81, 31))
        self.label_3.setObjectName("label_3")
        self.btn_signup = QtWidgets.QPushButton(self.centralwidget)
        self.btn_signup.setGeometry(QtCore.QRect(254, 260, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_signup.setFont(font)
        self.btn_signup.setObjectName("btn_signup")
        self.btn_signup.clicked.connect(self.signup)

        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(360, 260, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.clicked.connect(self.cancel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 592, 21))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">User id</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Password</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">User Name</span></p></body></html>"))
        self.btn_signup.setText(_translate("MainWindow", "SignUp"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))

    def signup(self):
        dbcon = DbCon()
        status = dbcon.getConnection()
        if status:
            id = self.txt_userid.text()
            username = self.txt_username.text()
            password = self.txt_password.text()
            if id !="" and username !="" and password !="":
                if len(password)>=8:
                    try:
                        dbcon.adduser(id,username,password)
                        self.txt_userid.setText("")
                        self.txt_username.setText("")
                        self.txt_password.setText("")
                        try:
                            self.window = QtWidgets.QMainWindow()
                            self.ui = Ui_Login()
                            self.ui.setupLogin(self.window)
                            self.window.show()
                        except Exception as e:
                            print(e)
                    except Error as e:
                        print(e)
                else:
                    print("password must be 8 or more characters")
            else:
                print("Fill all the fields")
        else:
            print("No database Connection Established")
    def cancel(self):
        quit()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
