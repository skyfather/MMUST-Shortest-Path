from PyQt5.QtWidgets import *
import sys
import MySQLdb
from MySQLdb import Error


class TabbleApp(QWidget):
    def __init__(self):
        super(TabbleApp,self).__init__()
        self.myInit()

    def myInit(self):
        self.setWindowTitle("QTable Widget")
        self.setGeometry(200,300,400,350)
        self.layout = QVBoxLayout()
        self.createTable()
        self.setLayout(self.layout)
        self.show()
    def createTable(self):
        try:
            db = MySQLdb.connect("localhost", "root", "", "proj1")
            cur = db.cursor()
            sql = "SELECT * FROM users"
            cur.execute(sql)
        except Error as e:
            print(e)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setItem(0, 0, QTableWidgetItem(cur.fetchone()[1]))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(cur.fetchone()[1]))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Am first"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Second"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Third here"))
        self.tableWidget.move(5, 5)
        self.layout.addWidget(self.tableWidget)

if __name__ == '__main__':
     app = QApplication(sys.argv)
     win = TabbleApp()
     sys.exit(app.exec_())
