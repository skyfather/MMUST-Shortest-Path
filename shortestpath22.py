# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Fallen\Documents\project\gui2\shortestpath2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from dbconnections.DbCon import DbCon
from algorithms.Vertex import Vertex
import sys

class Ui_ShortestPath22(object):
    def __init__(self):
        self.dbcon = DbCon()
        self.status = self.dbcon.getConnection()

        self.msg_warning = QMessageBox()
        self.msg_warning.setIcon(QMessageBox.Warning)
        self.msg_warning.setWindowTitle("MMUST NAVIGATOR")

        self.textEdit = QtWidgets.QTextEdit()

    def setupShortestPath22(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 391, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 440, 75, 23))
        self.pushButton.setObjectName("pushButton")
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
        self.lblpath.setGeometry(QtCore.QRect(130, 270, 441, 91))
        self.lblpath.setObjectName("lblpath")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(560, 40, 181, 421))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.lbl_buildingcodes = QtWidgets.QLabel(self.centralwidget)
        self.lbl_buildingcodes.setGeometry(QtCore.QRect(580, 20, 121, 16))
        self.lbl_buildingcodes.setObjectName("lbl_buildingcodes")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        self.pushButton.clicked.connect(self.calculate2)

        # self.loadVerticies()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">SHORTEST PATH</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">From</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">To</span></p></body></html>"))
        self.lblpath.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\"><br/></span></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        MainWindow.setWindowIcon(QIcon("pics\\icon"))
        self.lbl_buildingcodes.setText(_translate("MainWindow", "Building Codes to use"))
        self.loadVerticies()

    def calculate2(self):
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
                    b = edge[5]
                    for n in vertlist2:
                        if sv == n.name:
                            sn = n
                    for nn in vertlist2:
                        if tv == nn.name:
                            tn = nn
                    # p = Edge(id,ename,w,sv,tv)
                    if b ==0:
                        edgelist.append(Edge(id, ename, w, sn, tn,b))

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
                                self.routes = "Traversing from {} to {}\n\tDistance ".format(self.start_vertex,self.target_vertex)+str(vert.minDistance)+"m\n\nPath is"
                                for nodes in path:
                                    self.routes += "-->"+nodes
                                self.lblpath.setText(self.routes)
                            else:
                                # self.lblpath.selectedText("")
                                self.lblpath.setText("There is no effective path from {} to {}".format(self.start_vertex,self.target_vertex))
                                self.msg_warning.setText("There is no effective path from {} to {}".format(self.start_vertex,self.target_vertex))
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

    def loadVerticies(self):
        if self.status:
            from algorithms.Edge import Edge

            verts = self.dbcon.get_vertices()
            for vert in verts:
                self.textEdit.append(vert[1]+"--->"+vert[2]+"\n")
            self.textEdit.append("*****Blocked Paths*****\n")

            edgelist = []
            vertlist = []
            for vert in verts:
                vertlist.append(Vertex(vert[1]))
            edges = self.dbcon.get_edges()
            for edge in edges:

                id = edge[0]
                ename = edge[1]
                w = edge[2]
                sv = edge[3]
                tv = edge[4]
                b = edge[5]
                for n in vertlist:
                    if sv == n.name:
                        sn = n
                for nn in vertlist:
                    if tv == nn.name:
                        tn = nn
                # p = Edge(id,ename,w,sv,tv)
                edgelist.append(Edge(id, ename, w, sn, tn, b))

            edgelist2 = set(edgelist)
            for edge in edgelist2:
                if edge.blocked == 1:
                    self.textEdit.append(edge.edgename)
        else:
            self.textEdit.setText("""The Network connection is Offline at the Momment\n
                                    Please try again sometimes later""")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ShortestPath22()
    ui.setupShortestPath22(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

