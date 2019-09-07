# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addpath2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

from dbconnections.DbCon import DbCon
from MySQLdb import Error


class Ui_AddPath2(object):
    def setupAddPath2(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(611, 424)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 5, 231, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 110, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 160, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 210, 71, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 260, 71, 21))
        self.label_6.setObjectName("label_6")
        self.txtname = QtWidgets.QLineEdit(self.centralwidget)
        self.txtname.setGeometry(QtCore.QRect(200, 100, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtname.setFont(font)
        self.txtname.setObjectName("txtname")
        self.txt_length = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_length.setGeometry(QtCore.QRect(200, 150, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_length.setFont(font)
        self.txt_length.setObjectName("txt_length")
        self.txt_from = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_from.setGeometry(QtCore.QRect(200, 200, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_from.setFont(font)
        self.txt_from.setObjectName("txt_from")
        self.txt_to = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_to.setGeometry(QtCore.QRect(200, 250, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_to.setFont(font)
        self.txt_to.setObjectName("txt_to")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(404, 352, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(510, 350, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName("btn_exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 611, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_save.clicked.connect(self.addPath)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Create Path</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Path Name</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Path Length</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">From</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">To</span></p></body></html>"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))
        MainWindow.setWindowIcon(QIcon('pics\\icon.png'))

    def addPath(self):
        self.dbcon = DbCon()
        self.status = self.dbcon.getConnection()
        if self.status:
            name = self.txtname.text()
            length = self.txt_length.text()
            startv = self.txt_from.text().upper()
            targetv = self.txt_to.text().upper()
            if name !="" and(startv !="" and targetv !=""):
                try:
                    length = int(length)
                    self.dbcon.add_edge(name,length,startv,targetv)
                    self.dbcon.add_edge(name,length,targetv,startv)
                    print("Path {} successfully added".format(name))
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Path {} has been added to the databse".format(name))
                    msg.setWindowTitle("MMUST Navigator")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.exec()
                    self.txtname.setText("")
                    self.txt_length.setText("")
                    self.txt_from.setText("")
                    self.txt_to.setText("")
                except Error as e:
                    print(e)
                    msg.setIcon(QMessageBox.Information)
                    msg.setText(str(e))
                    msg.setWindowTitle("MMUST Navigator")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.exec()
                except Exception as ex:
                    print(ex)
                    msg.setIcon(QMessageBox.Information)
                    msg.setText(str(ex))
                    msg.setWindowTitle("MMUST Navigator")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.exec()
            else:
                print("fill all the values")
        else:
            print("No database connection")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AddPath2()
    ui.setupAddPath2(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

