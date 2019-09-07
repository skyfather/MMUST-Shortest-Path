# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Fallen\Documents\project\gui2\MannageVertex.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from dbconnections.DbCon import DbCon


class Ui_ManageVertex(object):
    def __init__(self):
        self.dbcon = DbCon()
        self.status = self.dbcon.getConnection()
        self.msg_info = QMessageBox()
        self.msg_warning = QMessageBox()

        self.msg_info.setIcon(QMessageBox.Information)
        self.msg_info.setWindowTitle("MMUST NAVIGATOR")

        self.msg_warning.setWindowTitle("MMUST NAVIGATOR")
        self.msg_warning.setIcon(QMessageBox.Warning)
    def setupManageVertex(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 479)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(110, 30, 461, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(14, 40, 81, 23))
        self.btn_load.setObjectName("btn_load")
        self.txt_id = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_id.setGeometry(QtCore.QRect(600, 60, 201, 31))
        self.txt_id.setObjectName("txt_id")
        self.txt_name = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name.setGeometry(QtCore.QRect(600, 140, 201, 31))
        self.txt_name.setObjectName("txt_name")
        self.txt_description = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_description.setGeometry(QtCore.QRect(600, 220, 201, 31))
        self.txt_description.setObjectName("txt_description")
        self.btn_select = QtWidgets.QPushButton(self.centralwidget)
        self.btn_select.setGeometry(QtCore.QRect(10, 90, 81, 23))
        self.btn_select.setObjectName("btn_select")
        self.btn_edit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edit.setGeometry(QtCore.QRect(720, 300, 81, 23))
        self.btn_edit.setObjectName("btn_edit")
        self.btn_deleteAll = QtWidgets.QPushButton(self.centralwidget)
        self.btn_deleteAll.setGeometry(QtCore.QRect(700, 350, 101, 23))
        self.btn_deleteAll.setObjectName("btn_deleteAll")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(600, 300, 81, 23))
        self.btn_save.setObjectName("btn_save")
        self.btn_deleteOne = QtWidgets.QPushButton(self.centralwidget)
        self.btn_deleteOne.setGeometry(QtCore.QRect(600, 350, 81, 23))
        self.btn_deleteOne.setObjectName("btn_deleteOne")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btn_load.clicked.connect(self.loadData)
        self.btn_select.clicked.connect(self.selectData)
        self.btn_save.clicked.connect(self.saveVertex)
        self.btn_edit.clicked.connect(self.editVertex)
        self.btn_deleteOne.clicked.connect(self.deleteVertex)
        self.btn_deleteAll.clicked.connect(self.deleteAllVertex)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loadData()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Vertex ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vertex Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Vertex Description"))
        self.btn_load.setText(_translate("MainWindow", "Load Verticies"))
        self.txt_id.setPlaceholderText(_translate("MainWindow", "vertex id"))
        self.txt_name.setPlaceholderText(_translate("MainWindow", "vertex name"))
        self.txt_description.setPlaceholderText(_translate("MainWindow", "vertex description"))
        self.btn_select.setText(_translate("MainWindow", "Select >>"))
        self.btn_edit.setText(_translate("MainWindow", "Edit Vertex"))
        self.btn_deleteAll.setText(_translate("MainWindow", "Delete All Verticies"))
        self.btn_save.setText(_translate("MainWindow", "Add Vertex"))
        self.btn_deleteOne.setText(_translate("MainWindow", "Delete Vertex"))
        MainWindow.setWindowIcon(QIcon("pics\\icon"))

    def loadData(self):
        self.msg_info.setWindowTitle("Load Verticies")
        if self.status:
            rows = self.dbcon.get_vertices()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(rows):
                self.tableWidget.insertRow(row_number)
                for column_number, column_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))
            self.txt_id.setText("")
            self.txt_name.setText("")
            self.txt_description.setText("")
        else:
            self.msg_warning.setText("No database Connection")
            self.msg_warning.setStandardButtons(QMessageBox.Ok)
            self.msg_warning.exec_()

    def selectData(self):
        self.msg_info.setWindowTitle("Select Data")
        if self.status:
            indexes = self.tableWidget.selectionModel().selectedRows()
            for index in sorted(indexes):
                row = int(index.row())
                id = self.tableWidget.item(row, 0)
                name = self.tableWidget.item(row, 1)
                desc = self.tableWidget.item(row, 2)

                self.txt_id.setText(id.text())
                self.txt_name.setText(name.text())
                self.txt_description.setText(desc.text())
        else:
            self.msg_warning.setText("No database Connection")
            self.msg_warning.setStandardButtons(QMessageBox.Ok)
            self.msg_warning.exec_()

    def saveVertex(self):
        self.msg_info.setWindowTitle("Save Vertex")
        if self.status:
            id = self.txt_id.text()
            name = self.txt_name.text().upper()
            desc = self.txt_description.text()
            if id !="" and name !="" and desc !="":
                try:
                    self.dbcon.add_vertex(id,name,desc)
                    self.msg_info.setText("Vertex {} has been successfully added".format(name))
                    self.msg_info.setStandardButtons(QMessageBox.Ok)
                    self.msg_info.exec_()
                    self.loadData()
                except Exception as e:
                    self.msg_warning.setText(str(e).strip("()"))
                    self.msg_warning.setStandardButtons(QMessageBox.Ok)
                    self.msg_warning.exec_()
            else:
                self.msg_warning.setText("Fill all the values")
                self.msg_warning.setStandardButtons(QMessageBox.Ok)
                self.msg_warning.exec_()
        else:
            self.msg_warning.setText("No database Connection")
            self.msg_warning.setStandardButtons(QMessageBox.Ok)
            self.msg_warning.exec_()

    def editVertex(self):
        self.msg_info.setWindowTitle("Edit Vertex")
        if self.status:
            id = self.txt_id.text()
            name = self.txt_name.text()
            desc = self.txt_description.text()
            if id != "":
                self.msg_info.setText("Are you sure you want to update vertaex {}?".format(name))
                self.msg_info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

                retval = self.msg_info.exec_()
                if retval == 1024:
                    self.dbcon.update_vertex(id,name,desc)
            else:
                self.msg_warning.setText("Select a path to update it")
                self.msg_warning.setStandardButtons(QMessageBox.Ok)
                self.msg_warning.exec_()
            self.loadData()
        else:
            self.msg_warning.setText("No database Connection")
            self.msg_warning.setStandardButtons(QMessageBox.Ok)
            self.msg_warning.exec_()

    def deleteVertex(self):
        self.msg_info.setWindowTitle("Delete Vertex")
        if self.status:
            id = self.txt_id.text()
            if id !="":
                self.msg_info.setText("Do you want to delete vertex {}".format(id))
                self.msg_info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                retval = self.msg_info.exec_()
                if retval == 1024:
                    self.dbcon.delete_vertex(id)
                    self.txt_id.setText("")
                    self.txt_name.setText("")
                    self.txt_description.setText("")
            else:
                self.msg_warning.setText("Select a vertex or enter vertex id to delete it")
                self.msg_warning.setStandardButtons(QMessageBox.Ok)
                self.msg_warning.exec_()
            self.loadData()
        else:
            self.msg_warning.setText("No database Connection")
            self.msg_warning.setStandardButtons(QMessageBox.Ok)
            self.msg_warning.exec_()

    def deleteAllVertex(self):
        self.msg_info.setWindowTitle("Delete Verticies")
        if self.status:
            self.msg_info.setText("Are yousure you want to delete all verticies?")
            self.msg_info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = self.msg_info.exec_()
            if retval == 1024:
                # self.dbcon.delete_verticies()
                self.msg_warning.setText("Sorry mate! We cannot allow you to to mess\nthis up!!")
                self.msg_warning.setStandardButtons(QMessageBox.Ok)
                self.msg_warning.exec_()
            self.loadData()
        else:
            self.msg_warning.setText("No database Connection")
            self.msg_warning.setStandardButtons(QMessageBox.Ok)
            self.msg_warning.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ManageVertex()
    ui.setupManageVertex(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
