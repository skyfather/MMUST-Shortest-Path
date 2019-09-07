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
    # print("Enter Start Vertex id: ")
    # svertex = int(input())
    # print("Enter Target Vertex id: ")
    # svertex = int(input())

    n1 = dbcon.get_vertex(1)[1]
    n2 = dbcon.get_vertex(2)[1]
    n3 = dbcon.get_vertex(3)[1]
    e1 = dbcon.get_edge(1)
    e2 = dbcon.get_edge(2)
    e3 = dbcon.get_edge(34)

    # nv1 = Vertex(n1)
    # nv2 = Vertex(n2)
    # nv3 = Vertex(n3)
    nv1 = Vertex('SPD')
    nv2 = Vertex('LBB')
    nv3 = Vertex('MCU')

    # path1 = Edge(e1[0], e1[1], e1[4], nv1,nv2)
    # path2 = Edge(e2[0], e2[1], e2[4], nv2,nv3)
    # path3 = Edge(e3[0], e3[1], e3[4], nv1,nv3)
    path1 = Edge(e1[0], e1[1], e1[4], nv1,nv2)
    path2 = Edge(e2[0], e2[1], e2[4], nv2,nv3)
    path3 = Edge(e3[0], e3[1], e3[4], nv1,nv3)

    nv1.adjacenciesList.append(path1)
    nv1.adjacenciesList.append(path3)
    nv2.adjacenciesList.append(path2)

    vertexList = {nv1,nv2,nv3}

    dijkistra = Dijkstra()

    dijkistra.calculateShrtestPath(vertexList, nv1)

    dijkistra.getShortestPathTo(nv3)

    # edges = dbcon.get_edges()
    # for i in range(len(edges)):
    #     print(i)
    # for i in edges:
    #     paths = Edge(i[0], i[1], i[4], nv1, nv2)
    #     print(paths)
else:
    print("No connection")

