from algorithms.Vertex import Vertex
from algorithms.Edge import Edge
from algorithms.Dijkstra import Dijkstra
import MySQLdb
from _mysql_exceptions import Error
from dbconnections.DbCon import DbCon


#db staff
print("Attempting database connection ........")
dbcon = DbCon()
status = dbcon.getConnection()
if status:
    dijkistra = Dijkstra()

    # vertlist2 = []
    #
    # verts = dbcon.get_vertices()
    # for vert in verts:
    #     vertlist2.append(Vertex(vert[1]))
    # edgelist = []
    # edges = dbcon.get_edges()
    # for edge in edges:
    #     id = edge[0]
    #     ename = edge[1]
    #     w = edge[2]
    #     sv = edge[3]
    #     tv = edge[4]
    #     for n in vertlist2:
    #         if sv == n.name:
    #             sn = n
    #     for nn in vertlist2:
    #         if tv == nn.name:
    #             tn = nn
    #     # p = Edge(id,ename,w,sv,tv)
    #     edgelist.append(Edge(id,ename,w,sn,tn))
    #
    # for edges in edgelist:
    #     for sv in edges.startVertex:
    #         # print(sv)
    #         for n in vertlist2:
    #             if sv == n.name:
    #                 sn = n
    #         sn.adjacenciesList.append(edges)
    # # print("--------------")
    # # for edges in edgelist:
    # #     for tv in edges.targetVertex:
    # #         # print(tv)
    # #         for nn in vertlist2:
    # #             if tv == nn.name:
    # #                 tn = nn
    # #         tn.adjacenciesList.append(edges)
    # print("******NAVIGATE*********")
    # userinput1 = input("Enter startvertex: ").upper()
    # userinput2 = input("Enter targetvertex: ").upper()
    #
    # for vert in vertlist2:
    #     if userinput1 == vert.name:
    #         dijkistra.calculateShrtestPath(vertlist2, vert)
    # for vert in vertlist2:
    #     if userinput2 == vert.name:
    #         dijkistra.getShortestPathTo(vert)
    dbcon.add_edge(100,'e100',85,'MCU','H4')
    e = dbcon.get_edges()
    for edge in e:
        print(edge)

else:
    print("No connection")

