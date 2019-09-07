# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Fallen\Documents\project\gui2\ManagePaths.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from dbconnections.DbCon import DbCon
# from PyQt4 import QtGui
from MySQLdb import Error
from AddPath import *


class Ui_ManagePaths(object):
    def __init__(self):
        self.dbcon = DbCon()
        self.status = self.dbcon.getConnection()

        self.msg_info = QMessageBox()
        self.msg_info.setIcon(QMessageBox.Information)
        self.msg_info.setWindowTitle("MMUST NAVIGATOR")

        self.msg_warning = QMessageBox()
        self.msg_warning.setIcon(QMessageBox.Warning)
        self.msg_warning.setWindowTitle("MMUST NAVIGATOR")

    def loadData(self):

        if self.status:
            rows = self.dbcon.get_edges()
            self.tableWidget.setRowCount(0)
            # horHeaders = ['ID','Name','Description']
            for row_number,row_data in enumerate(rows):
                self.tableWidget.insertRow(row_number)
                for column_number,column_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))

            # self.tableWidget.setHorizontalHeaderLabels(horHeaders)
        else:
            print("No connection!")

    def setupManagePaths(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1007, 462)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.btn_load.setObjectName("btn_load")

        self.btn_load.clicked.connect(self.loadData)

        self.btn_select = QtWidgets.QPushButton(self.centralwidget)
        self.btn_select.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.btn_select.setObjectName("btn_select")

        self.btn_select.clicked.connect(self.tableSelection)

        self.btn_addPath = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addPath.setGeometry(QtCore.QRect(10, 150, 75, 23))
        self.btn_addPath.setObjectName("btn_addPath")

        self.btn_addPath.clicked.connect(self.open_addPath)

        #-------------------------------------------------
        self.btn_blockPath = QtWidgets.QPushButton(self.centralwidget)
        self.btn_blockPath.setGeometry(QtCore.QRect(790, 370, 75, 23))
        self.btn_blockPath.setObjectName("btn_blockPath")

        self.btn_blockPath.clicked.connect(self.blockPath)
        #---------------------------------------------------

        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(910, 370, 75, 23))
        self.btn_delete.setObjectName("btn_delete")

        self.btn_delete.clicked.connect(self.delete_one)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 5, 281, 31))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(640, 0, 20, 461))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 40, 531, 291))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.txt_id = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_id.setGeometry(QtCore.QRect(780, 50, 201, 31))
        self.txt_id.setObjectName("txt_id")
        self.txt_weight = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_weight.setGeometry(QtCore.QRect(780, 170, 201, 31))
        self.txt_weight.setObjectName("txt_weight")
        self.txt_name = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name.setGeometry(QtCore.QRect(780, 110, 201, 31))
        self.txt_name.setObjectName("txt_name")
        self.txt_startv = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_startv.setGeometry(QtCore.QRect(780, 230, 201, 31))
        self.txt_startv.setObjectName("txt_startv")
        self.btn_editPath = QtWidgets.QPushButton(self.centralwidget)
        self.btn_editPath.setGeometry(QtCore.QRect(670, 370, 75, 23))
        self.btn_editPath.setObjectName("btn_editPath")

        self.btn_editPath.clicked.connect(self.update_path)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(670, 52, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(670, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(670, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(670, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txt_targetv = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_targetv.setGeometry(QtCore.QRect(780, 290, 201, 31))
        self.txt_targetv.setObjectName("txt_targetv")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(670, 290, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1007, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        try:
            self.loadData()
        except Error as e:
            self.msg_warning.setText("The database is offline")
            self.msg_warning.setStandardButtons(QMessageBox.Ok)
            self.msg_warning.exec_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manage Paths"))
        self.btn_load.setText(_translate("MainWindow", "Load Paths"))
        self.btn_select.setText(_translate("MainWindow", "Select>>"))
        self.btn_addPath.setText(_translate("MainWindow", "Add Path"))
        #--------------------------------------------------------------
        self.btn_blockPath.setText(_translate("MainWindow", "Block Path"))
        #---------------------------------------------------------------
        self.btn_delete.setText(_translate("MainWindow", "Delete Path"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">PATHS PANEL</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "LENGTH\n(metres)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "START VERTEX"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TARGET VERTEX"))
        self.btn_editPath.setText(_translate("MainWindow", "Edit Path"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">ID</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "NAME"))
        self.label_4.setText(_translate("MainWindow", "WEIGHT"))
        self.label_5.setText(_translate("MainWindow", "START VERTEX"))
        self.label_6.setText(_translate("MainWindow", "TARGET VERTEX"))
        MainWindow.setWindowIcon(QIcon('pics\\icon.png'))

    def open_addPath(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def tableSelection(self):
        indexes = self.tableWidget.selectionModel().selectedRows()
        for index in sorted(indexes):
            # print('Row %d is selected' % index.row())
            row = int(index.row())
            id = self.tableWidget.item(row, 0)
            name = self.tableWidget.item(row, 1)
            weight = self.tableWidget.item(row, 2)
            startv = self.tableWidget.item(row, 3)
            targetv = self.tableWidget.item(row, 4)

            self.txt_id.setText(id.text())
            self.txt_name.setText(name.text())
            self.txt_weight.setText(weight.text())
            self.txt_startv.setText(startv.text())
            self.txt_targetv.setText(targetv.text())
    def update_path(self):
        if self.status:
            id = self.txt_id.text()
            name = self.txt_name.text()
            weight = self.txt_weight.text()
            startv = self.txt_startv.text().upper()
            targetv = self.txt_targetv.text().upper()
            if id !="":
                # msg = QMessageBox()
                # msg.setIcon(QMessageBox.Warning)

                self.msg_info.setText("Are you sure you want to update path {}?".format(name))
                # msg.setInformativeText("Are you sure you want to block path? ")
                self.msg_info.setWindowTitle("Path Update")
                # msg.setDetailedText("The details are as follows:")
                self.msg_info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                # msg.buttonClicked.connect(self.msgbtn)

                retval = self.msg_info.exec_()
                # print("value of pressed message box button:", retval)
                if retval == 1024:
                    self.dbcon.update_edge(id,name,weight,startv,targetv)
                    self.msg_info.setText("Path {} successfully updated!".format(id))
                    self.msg_info.setStandardButtons(QMessageBox.Ok)
                    self.msg_info.exec_()

                    self.txt_id.setText("")
                    self.txt_name.setText("")
                    self.txt_weight.setText("")
                    self.txt_startv.setText("")
                    self.txt_targetv.setText("")
            else:
                self.msg_warning.setText("Select a path to update it")
                self.msg_warning.setStandardButtons(QMessageBox.Ok)
                self.msg_warning.exec_()
        else:
            self.msg_warning.setText("No database connection")
            self.msg_warning.setStandardButtons(QMessageBox.Ok)
            self.msg_warning.exec_()

    def delete_one(self):
        if self.status:
            id = self.txt_id.text()
            # edgename = self.txt_name.text()
            if id !="":
                # msg = QMessageBox()
                # msg.setIcon(QMessageBox.Warning)

                self.msg_info.setText("Are you sure want to delete path: {}?".format(id))
                # msg.setInformativeText("Are you sure want to delete path?")
                self.msg_info.setWindowTitle("Delete")
                # msg.setDetailedText("The details are as follows:")
                self.msg_info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                # msg.buttonClicked.connect(self.msgbtn)

                retval = self.msg_info.exec_()
                # print("value of pressed message box button:", retval)
                if retval == 1024:
                    self.dbcon.delete_edge(id)

                    self.msg_info.setText("Edge {} successfully deleted!".format(id))
                    self.msg_info.setStandardButtons(QMessageBox.Ok)
                    self.msg_info.exec_()

                    self.txt_id.setText("")
                    self.txt_name.setText("")
                    self.txt_weight.setText("")
                    self.txt_startv.setText("")
                    self.txt_targetv.setText("")
            else:
                self.msg_warning.setText("Select a path first delete it")
                self.msg_warning.setStandardButtons(QMessageBox.Ok)
                self.msg_warning.exec_()
        else:
            self.msg_warning.setText("No database connection")
            self.msg_warning.setStandardButtons(QMessageBox.Ok)
            self.msg_warning.exec_()
    def delete_all(self):
        if self.status:
            # msg = QMessageBox()
            # msg.setIcon(QMessageBox.Warning)

            self.msg_info.setText("Are you sure you want to delete all the paths?")
            # msg.setInformativeText("Are you sure you want to delete all the paths?")
            self.msg_info.setWindowTitle("Delete All")
            # msg.setDetailedText("The details are as follows:")
            self.msg_info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            # msg.buttonClicked.connect(self.msgbtn)

            retval = self.msg_info.exec_()
            # print("value of pressed message box button:", retval)
            if retval == 1024:
                self.dbcon.delete_edges()
                self.msg_info.setText("All the edges have been deleted!")
                self.msg_info.setStandardButtons(QMessageBox.Ok)
                self.msg_info.exec_()
        else:
            self.msg_warning.setText("No database connection")
            self.msg_warning.setStandardButtons(QMessageBox.Ok)
            self.msg_warning.exec_()

    def blockPath(self):
        pathid = self.txt_id.text()
        pathname = self.txt_name.text()
        sv = self.txt_startv.text()
        tv = self.txt_targetv.text()
        print(pathid,pathname,sv,tv)
        pathid = int(pathid)
        try:
            if pathid !="":
                self.dbcon.block_path(pathname,sv,tv)
            else:
                self.msg_warning.setText("Path id must have an input value")
                self.msg_warning.setStandardButtons(QMessageBox.Ok)
                self.msg_warning.exec_()
        except Error as e:
            self.msg_warning.setText(str(e))
            self.msg_warning.setStandardButtons(QMessageBox.Ok)
            self.msg_warning.exec_()
    def get_PathId(self):
        self.pathid = self.txt_id.text()
        return self.pathid
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ManagePaths()
    ui.setupManagePaths(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
