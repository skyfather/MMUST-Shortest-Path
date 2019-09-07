# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Fallen\Documents\project\gui2\PathView.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from dbconnections.DbCon import DbCon


class Ui_PathView(object):
    def __init__(self):
        self.dbcon = DbCon()
        self.status = self.dbcon.getConnection()

    def setupPathView(self, PathView):
        PathView.setObjectName("PathView")
        PathView.resize(756, 533)
        self.centralwidget = QtWidgets.QWidget(PathView)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 10, 601, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 450, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.loadData)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 460, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.cancell)

        PathView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PathView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 21))
        self.menubar.setObjectName("menubar")
        PathView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PathView)
        self.statusbar.setObjectName("statusbar")
        PathView.setStatusBar(self.statusbar)

        self.retranslateUi(PathView)
        QtCore.QMetaObject.connectSlotsByName(PathView)

        self.loadData()

    def retranslateUi(self, PathView):
        _translate = QtCore.QCoreApplication.translate
        PathView.setWindowTitle(_translate("PathView", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("PathView", "Path Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("PathView", "Path name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("PathView", "Path length\n(metres)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("PathView", "To"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("PathView", "From"))
        self.pushButton.setText(_translate("PathView", "Load Paths"))
        self.pushButton_2.setText(_translate("PathView", "Exit"))

    def loadData(self):
        if self.status:
            rows = self.dbcon.get_edges()
            self.tableWidget.setRowCount(0)
            # horHeaders = ['ID','Name','Description']
            for row_number,row_data in enumerate(rows):
                self.tableWidget.insertRow(row_number)
                for column_number,column_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))
        else:
            print("No connection!")

    def cancell(self):
        try:
            app1.quit()
        except Exception as e:
            print(e)
if __name__ == "__main__":
    import sys
    app1 = QtWidgets.QApplication(sys.argv)
    PathView = QtWidgets.QMainWindow()
    ui = Ui_PathView()
    ui.setupPathView(PathView)
    PathView.show()
    sys.exit(app1.exec_())

