from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem
from Vertex_View import *
from dbconnections.DbCon import DbCon
from MainWindow2 import *

class Vertex_ViewController(QtWidgets.QMainWindow, Ui_VertexView):
    def __init__(self, parent=None):
        super(Vertex_ViewController, self).__init__(parent=parent)
        self.setupVertexView(self)

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

    def home(self):
        self.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.U(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    titleMain = Vertex_ViewController()
    titleMain.show()
    sys.exit(app.exec_())