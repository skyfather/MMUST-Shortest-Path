from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem

from dbconnections.DbCon import DbCon


class Ui_VertexView(object):
    def loadData(self):
        dbcon = DbCon()
        status = dbcon.getConnection()
        if status:
            rows = dbcon.get_vertices()
            self.tableWidget.setRowCount(0)
            horHeaders = ['ID','Name','Description']
            for row_number,row_data in enumerate(rows):
                self.tableWidget.insertRow(row_number)
                for column_number,column_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))

            self.tableWidget.setHorizontalHeaderLabels(horHeaders)
        else:
            print("No connection!")
    def setupVertexView(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 536)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setGeometry(QtCore.QRect(420, 460, 75, 23))
        self.btnOk.setObjectName("btnOk")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(540, 460, 75, 23))
        self.btnCancel.setObjectName("btnCancel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 281, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 0, 51, 41))
        self.label_2.setStyleSheet("border-image: url(:/new_icons/icons8-home-26.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 0, 51, 41))
        self.label_4.setStyleSheet("border-image: url(:/new_icons/icons8-user-40.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 51, 41))
        self.label_3.setStyleSheet("border-image: url(:/new_icons/icons8-go-back-40.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(70, 80, 401, 331))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(12)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btnOk.clicked.connect(self.loadData)
        # self.btnCancel.clicked.connect(self.home)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loadData()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vertex View"))
        self.btnOk.setText(_translate("MainWindow", "Ok"))
        self.btnCancel.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">MMUST BUILDINGS</span></p></body></html>"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        MainWindow.setWindowIcon(QIcon('pics\\icon.png'))

import new_icons_rc
#
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_VertexView()
    ui.setupVertexView(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

