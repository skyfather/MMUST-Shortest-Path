from algorithms.Vertex import Vertex
from algorithms.Edge2 import Edge2
from algorithms.Dijkstra import Dijkstra
import MySQLdb
from _mysql_exceptions import Error
from dbconnections.DbCon import DbCon


#db staff
print("Attempting database connection ........")
dbcon = DbCon()
status = dbcon.getConnection()
if status:
    # print("Enter Start Vertex id: ")
    # svertex = int(input())
    # print("Enter Target Vertex id: ")
    # svertex = int(input())

    dijkistra = Dijkstra()

    vertlist2 = []

    verts = dbcon.get_vertices()
    for vert in verts:
        vertlist2.append(Vertex(vert[1]))
    edgelist = []
    edges = dbcon.get_edges()
    for edge in edges:
        # id = edge[0]
        ename = edge[0]
        w = edge[1]
        sv = edge[2]
        tv = edge[3]
        for n in vertlist2:
            if sv == n.name:
                sn = n
        for nn in vertlist2:
            if tv == nn.name:
                tn = nn
        # p = Edge(id,ename,w,sv,tv)
        edgelist.append(Edge2(ename,w,sn,tn))

    print("------------------")
    for edge in edgelist:
        print(edge)
    print("------------------")
    #
    # vertlist2[0].adjacenciesList.append(edgelist[0])
    # vertlist2[1].adjacenciesList.append(edgelist[1])
    # vertlist2[2].adjacenciesList.append(edgelist[2])
    #
    # dijkistra.calculateShrtestPath(vertlist2,vertlist2[0])
    # dijkistra.getShortestPathTo(vertlist2[2])

    for edges in edgelist:
        for sv in edges.startVertex:
            print(sv)
            for n in vertlist2:
                if sv == n.name:
                    sn = n
            sn.adjacenciesList.append(edges)
    print("--------------")
    for edges in edgelist:
        for tv in edges.targetVertex:
            print(tv)
            for nn in vertlist2:
                if tv == nn.name:
                    tn = nn

            tn.adjacenciesList.append(edges)

    print("Ajacencies lists")
    print(vertlist2[0].adjacenciesList)
    print(vertlist2[1].adjacenciesList)
    print(vertlist2[2].adjacenciesList)

    print("******NAVIGATE*********")
    dijkistra.calculateShrtestPath(vertlist2,vertlist2[2])
    dijkistra.getShortestPathTo(vertlist2[1])
else:
    print("No connection")

