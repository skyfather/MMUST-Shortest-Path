# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Fallen\Documents\project\gui2\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from  Vertex_View import *
from shortestpath2 import *
from login import *
from PathView import *
from About import *
from shortestpathController import *

class Ui_MainWindow2(object):

    def setupMainWin2(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 524)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.viewMap = QtWidgets.QPushButton(self.centralwidget)
        self.viewMap.setGeometry(QtCore.QRect(80, 430, 91, 23))
        self.viewMap.setObjectName("viewMap")
        #open a new window
        self.viewMap.clicked.connect(self.about)

        self.paths = QtWidgets.QPushButton(self.centralwidget)
        self.paths.setGeometry(QtCore.QRect(370, 230, 111, 23))
        self.paths.setObjectName("paths")
        self.paths.clicked.connect(self.open_paths)

        self.travel = QtWidgets.QPushButton(self.centralwidget)
        self.travel.setGeometry(QtCore.QRect(80, 230, 111, 23))
        self.travel.setObjectName("travel")
        #open the navigate window
        # self.travel.clicked.connect(self.openNavigate)
        self.travel.clicked.connect(self.navigate)

        self.buildings = QtWidgets.QPushButton(self.centralwidget)
        self.buildings.setGeometry(QtCore.QRect(364, 430, 101, 23))
        self.buildings.setObjectName("buildings")

        #open a new window
        self.buildings.clicked.connect(self.viewVertex)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 120, 111, 91))
        self.label.setStyleSheet("border-image: url(:/newPrefix/if_user_walk_63071.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 303, 101, 101))
        self.label_2.setStyleSheet("border-image: url(:/newPrefix/if_Rounded_-_High_Ultra_Colour02_-_Maps_2250024.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(357, 300, 111, 111))
        self.label_3.setStyleSheet("border-image: url(:/newPrefix/if_12_2302937.ico);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 110, 111, 101))
        self.label_4.setStyleSheet("border-image: url(:/newPrefix/if_path_2969396.ico);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 20, 421, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(620, 0, 31, 31))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/new_icons/icons8-administrator-male-26.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(550, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        try:
            self.label_7.mousePressEvent = self.login
        except Exception as e:
            print(e)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 21))
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
        self.viewMap.setText(_translate("MainWindow", "About"))
        self.paths.setText(_translate("MainWindow", "Paths"))
        self.travel.setText(_translate("MainWindow", "Travel"))
        self.buildings.setText(_translate("MainWindow", "Buildings"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#55557f;\">MMUST NAVIGATOR APPLICATION</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#0000ff;\">Log in</span></p></body></html>"))
        MainWindow.setWindowIcon(QIcon('pics\\icon.png'))

    # def __init__(self, parent=None):
    #     super(MainWindow, self).__init__(parent=parent)
    #     self.setupMainWin2(self)
    #     # self.beginButton.clicked.connect(self.openLogin)
    #     # self.vleMedRevButton.clicked.connect(self.openVleSite)
    #     # self.quitButton.clicked.connect(self.quitProgram)

    def navigate(self):
        self.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ShortestPath2()
        self.ui.setupShortestPath2(self.window)
        self.window.show()

    def open_paths(self):
        self.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PathView()
        self.ui.setupPathView(self.window)
        self.window.show()

    def viewVertex(self):
        # self.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_VertexView()
        self.ui.setupVertexView(self.window)
        self.window.show()
    def about(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_About()
        self.ui.setupAbout(self.window)
        self.window.show()

    def login(self,event):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupLogin(self.window)
        self.window.show()

    def cancel(self):
        self.QMessageBox.about(self,'Vertex','Exit')
        self.exit(1)


import imgs_rc
import new_icons_rc

# class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow2):
    # def __init__(self, parent=None):
    #     super(MainWindow, self).__init__(parent=parent)
    #     self.setupMainWin2(self)
    #     # self.beginButton.clicked.connect(self.openLogin)
    #     # self.vleMedRevButton.clicked.connect(self.openVleSite)
    #     # self.quitButton.clicked.connect(self.quitProgram)
    #
    # def navigate(self):
    #     self.hide()
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_ShortestPath2()
    #     self.ui.setupShortestPath2(self.window)
    #     self.window.show()
    #
    # def open_paths(self):
    #     self.hide()
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_PathView()
    #     self.ui.setupPathView(self.window)
    #     self.window.show()
    #
    # def viewVertex(self):
    #     # self.hide()
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_VertexView()
    #     self.ui.setupVertexView(self.window)
    #     self.window.show()
    # def about(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_About()
    #     self.ui.setupAbout(self.window)
    #     self.window.show()
    #
    # def login(self,event):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_Login()
    #     self.ui.setupLogin(self.window)
    #     self.window.show()
    #
    # def cancel(self):
    #     self.QMessageBox.about(self,'Vertex','Exit')
    #     self.exit(1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupMainWin2(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # titleMain = MainWindow()
    # titleMain.show()
    # sys.exit(app.exec_())
