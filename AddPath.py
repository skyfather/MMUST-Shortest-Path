# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Fallen\Documents\project\gui2\addPath.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from dbconnections.DbCon import DbCon


class Ui_MainWindow(object):
    def __init__(self):
        self.dbcon = DbCon()
        self.status = self.dbcon.getConnection()
        self.msg_warning = QMessageBox()
        self.msg_warning.setIcon(QMessageBox.Warning)
        self.msg_warning.setWindowTitle("MMUST NAVIGATOR")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(734, 523)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 251, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 110, 81, 21))
        self.label_2.setObjectName("label_2")
        self.txtid = QtWidgets.QLineEdit(self.centralwidget)
        self.txtid.setGeometry(QtCore.QRect(270, 110, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtid.setFont(font)
        self.txtid.setObjectName("txtid")
        self.txtname = QtWidgets.QLineEdit(self.centralwidget)
        self.txtname.setGeometry(QtCore.QRect(270, 169, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtname.setFont(font)
        self.txtname.setObjectName("txtname")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 180, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 300, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 240, 111, 21))
        self.label_5.setObjectName("label_5")
        self.txtweight = QtWidgets.QLineEdit(self.centralwidget)
        self.txtweight.setGeometry(QtCore.QRect(270, 229, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtweight.setFont(font)
        self.txtweight.setObjectName("txtweight")
        self.txtfrom = QtWidgets.QLineEdit(self.centralwidget)
        self.txtfrom.setGeometry(QtCore.QRect(270, 289, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtfrom.setFont(font)
        self.txtfrom.setObjectName("txtfrom")
        self.txtto = QtWidgets.QLineEdit(self.centralwidget)
        self.txtto.setGeometry(QtCore.QRect(270, 349, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtto.setFont(font)
        self.txtto.setObjectName("txtto")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 360, 81, 21))
        self.label_6.setObjectName("label_6")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(500, 450, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(610, 450, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #event actions
        self.btnSave.clicked.connect(self.addPath)
        self.btnCancel.clicked.connect(self.cancel)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Create Path</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Path id</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Path name</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">From</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">weight(length)</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">To</span></p></body></html>"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))
        MainWindow.setWindowIcon(QIcon('pics\\icon.png'))

    def addPath(self):
        if self.status:
            self.pathid = self.txtid.text()
            self.pathname = self.txtname.text()
            self.weight = self.txtweight.text()
            self.startVertex = self.txtfrom.text().upper()
            self.targetVertex = self.txtto.text().upper()

            vertList = []
            verticies = self.dbcon.get_vertices()
            if self.pathid !="":
                for vert in verticies:
                    vertList.append(vert[1])
                if self.startVertex not in vertList:
                    print("The vertex {} does not exist on the graph".format(self.startVertex))
                    self.msg_warning.setText("The vertex {} does not exist on the graph".format(self.startVertex))
                    self.msg.setStandardButtons(QMessageBox.Ok)
                    self.msg_warning.exec_()
                elif self.targetVertex not in vertList:
                    print("The vertex {} does not exist on the graph".format(self.startVertex))
                    self.msg_warning.setText("The vertex {} does not exist on the graph".format(self.startVertex))
                    self.msg_warning.setStandardButtons(QMessageBox.Ok)
                    self.msg_warning.exec_()
                else:
                    try:
                        self.dbcon.add_edge(self.pathid,self.pathname,self.weight,self.startVertex,self.targetVertex)
                    except Exception as ex:
                        print(ex)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Path {} {} has been added to the databse".format(self.pathid,self.pathname))
                    # msg.setInformativeText("Are you sure want to delete path?")
                    msg.setWindowTitle("Delete")
                    # msg.setDetailedText("The details are as follows:")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    # msg.buttonClicked.connect(self.msgbtn)

                    retval = msg.exec_()

                    print("Path {} {} has been added to the databse".format(self.pathid,self.pathname))
                    self.txtid.setText('')
                    self.txtname.setText('')
                    self.txtweight.setText("")
                    self.txtfrom.setText("")
                    self.txtto.setText("")
            else:
                self.msg_warning.setText("The path id cannot be empty")
                self.msg_warning.setStandardButtons(QMessageBox.Ok)
                self.msg_warning.exec_()
        else:
            print('Path not saved')
            self.msg_warning.setText("Path has not been saved")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg_warning.exec_()

    def cancel(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)

        self.msg.setText("This is a message box")
        self.msg.setInformativeText("This is additional information")
        self.msg.setWindowTitle("MessageBox demo")
        self.msg.setDetailedText("The details are as follows:")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

