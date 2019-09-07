
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from dbconnections.DbCon import DbCon
from shortestpath2 import *

class ShortestPathController(QtWidgets.QMainWindow, Ui_ShortestPath2):
    def __init__(self, parent=None):
        super(ShortestPathController, self).__init__(parent=parent)
        self.setupShortestPath2(self)

        self.dbcon = DbCon()
        self.status = self.dbcon.getConnection()

        self.msg_warning = QMessageBox()
        self.msg_warning.setIcon(QMessageBox.Warning)
        self.msg_warning.setWindowTitle("MMUST NAVIGATOR")

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    titleMain = ShortestPathController()
    titleMain.show()
    sys.exit(app.exec_())
