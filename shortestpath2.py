# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Fallen\Documents\project\gui2\shortestpath.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from dbconnections.DbCon import DbCon
import sys


class Ui_ShortestPath2(object):
    def __init__(self):
        self.dbcon = DbCon()
        self.status = self.dbcon.getConnection()

        self.msg_warning = QMessageBox()
        self.msg_warning.setIcon(QMessageBox.Warning)
        self.msg_warning.setWindowTitle("MMUST NAVIGATOR")

    def setupShortestPath2(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 391, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 440, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.calculate2)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 440, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.txt_from = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_from.setGeometry(QtCore.QRect(230, 110, 231, 20))
        self.txt_from.setObjectName("txt_from")
        self.txt_to = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_to.setGeometry(QtCore.QRect(230, 170, 231, 20))
        self.txt_to.setObjectName("txt_to")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 110, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 170, 51, 21))
        self.label_3.setObjectName("label_3")
        self.lblpath = QtWidgets.QLabel(self.centralwidget)
        self.lblpath.setGeometry(QtCore.QRect(130, 270, 511, 51))
        self.lblpath.setObjectName("lblpath")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">SHORTEST PATH</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">From</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">To</span></p></body></html>"))
        self.lblpath.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))

    def calculate(self):
        if self.status:
            self.start_vertex = self.txt_from.text()
            self.target_vertex = self.txt_to.text()
            vertex = self.dbcon.get_vertex(self.start_vertex)
            self.lblpath.setText(vertex[2])
            print(str(vertex))
        else:
            print("Not connected")
    def calculate2(self):
        try:
            if self.status:

                from algorithms.Vertex import Vertex
                from algorithms.Edge import Edge
                from algorithms.Dijkstra import Dijkstra

                # db staff
                dbcon = DbCon()
                status = dbcon.getConnection()
                if status:
                    dijkistra = Dijkstra()

                    vertlist2 = []

                    verts = dbcon.get_vertices()
                    for vert in verts:
                        vertlist2.append(Vertex(vert[1]))
                    edgelist = []
                    edges = dbcon.get_edges()
                    for edge in edges:

                        id = edge[0]
                        ename = edge[1]
                        w = edge[2]
                        sv = edge[3]
                        tv = edge[4]
                        for n in vertlist2:
                            if sv == n.name:
                                sn = n
                        for nn in vertlist2:
                            if tv == nn.name:
                                tn = nn
                        # p = Edge(id,ename,w,sv,tv)
                        edgelist.append(Edge(id, ename, w, sn, tn))

                    for edges in edgelist:
                        for sv in edges.startVertex:
                            # print(sv)
                            for n in vertlist2:
                                if sv == n.name:
                                    sn = n
                            sn.adjacenciesList.append(edges)
                    # print("--------------")
                    # for edges in edgelist:
                    #     for tv in edges.targetVertex:
                    #         # print(tv)
                    #         for nn in vertlist2:
                    #             if tv == nn.name:
                    #                 tn = nn
                    #         tn.adjacenciesList.append(edges)
                    # userinput1 = input("Enter startvertex: ").upper()
                    # userinput2 = input("Enter targetvertex: ").upper()
                    self.start_vertex = self.txt_from.text().upper()
                    self.target_vertex = self.txt_to.text().upper()
                    self.routes = ""
                    self.bool1 = False
                    self.bool2 = False

                    if self.start_vertex !="" and self.target_vertex !="":
                        for vert in vertlist2:
                            if self.start_vertex == vert.name:
                                dijkistra.calculateShrtestPath(vertlist2, vert)
                                self.bool1 = True
                            # else:
                            #     self.msg_warning.setText("Vertex {} does not exist on the graph".format(self.start_vertex))
                            #     self.msg_warning.setStandardButtons(QMessageBox.Ok)
                            #     self.msg_warning.exec_()
                        for vert in vertlist2:
                            if self.target_vertex == vert.name:
                                path = dijkistra.getShortestPathTo2(vert)
                                self.bool2 = True
                                path.reverse()
                                if vert.minDistance != sys.maxsize:
                                    self.routes = "Traversing from {} to {}\n\tDistance ".format(self.start_vertex,self.target_vertex)+str(vert.minDistance)+"\n\nPath is"
                                    for nodes in path:
                                        self.routes += " "+nodes
                                    self.lblpath.setText(self.routes)
                                else:
                                    # self.lblpath.selectedText("")
                                    self.msg_warning.setText("There is no effective path to {}".format(self.target_vertex))
                                    self.msg_warning.setStandardButtons(QMessageBox.Ok)
                                    self.msg_warning.exec_()
                            # else:
                            #     self.msg_warning.setText("Vertex {} does not exist on the graph".format(self.start_vertex))
                            #     self.msg_warning.setStandardButtons(QMessageBox.Ok)
                            #     self.msg_warning.exec_()
                        if self.bool1:
                            pass
                        else:
                            self.msg_warning.setText("Vertex {} does not exist on the graph".format(self.start_vertex))
                            self.msg_warning.setStandardButtons(QMessageBox.Ok)
                            self.msg_warning.exec_()
                        if self.bool2:
                            pass
                        else:
                            self.msg_warning.setText("Vertex {} does not exist on the graph".format(self.target_vertex))
                            self.msg_warning.setStandardButtons(QMessageBox.Ok)
                            self.msg_warning.exec_()
                    else:
                        self.msg_warning.setText("Fill all the input values")
                        self.msg_warning.setStandardButtons(QMessageBox.Ok)
                        self.msg_warning.exec_()

            else:
                self.msg_warning.setText("No database Connection")
                self.msg_warning.setStandardButtons(QMessageBox.Ok)
                self.msg_warning.exec_()
        except Exception as e:
            print(e)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ShortestPath2()
    ui.setupShortestPath2(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
