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
    e3 = dbcon.get_edge(3)

    nv1 = Vertex(n1)
    # nv1 = Vertex(dbcon.get_vertex(svertex)[1])
    nv2 = Vertex(n2)
    nv3 = Vertex(n3)

    path1 = Edge(e1[0], e1[1], e1[2], nv1,nv2)
    path2 = Edge(e2[0], e2[1], e2[2], nv2,nv3)
    path3 = Edge(e3[0], e3[1], e3[2], nv1,nv3)
    # path1 = Edge(e1[0], e1[1], e1[2], Vertex(1), Vertex(2))
    # path2 = Edge(e2[0], e2[1], e2[2], Vertex(2), Vertex(3))
    # path3 = Edge(e3[0], e3[1], e3[2], Vertex(1), Vertex(3))

    nv1.adjacenciesList.append(path1)
    nv3.adjacenciesList.append(path3)
    nv2.adjacenciesList.append(path2)

    vertexList = {nv1,nv2,nv3}

    dijkistra = Dijkstra()

    # dijkistra.calculateShrtestPath(nv1)
    # dijkistra.getShortestPathTo(nv3)
    # print(nv2.predecessor)
    # print(nv3.visited)
    vertlist2 = []
    vertlist3 = []
    vertlist4 = []
    #
    # print("---------------")
    # print(nv1.adjacenciesList)
    # print(nv2.adjacenciesList)
    # print(nv3.adjacenciesList)
    # print("---------------")
    verts = dbcon.get_vertices()
    for vert in verts:
        vertlist2.append(Vertex(vert[1]))

    # print(type(vertlist2[1]))
    # vertlist2[1].adjacenciesList.append(12)
    # print(vertlist2[1].adjacenciesList)
    edgelist = []
    edges = dbcon.get_edges()
    for edge in edges:
        # edgelist.append(Edge(edge[0],edge[1],edge[2],vertlist2[0],vertlist2[1]))
        # edgelist.append(Edge(edge[0],edge[1],edge[2],Vertex(edge[3]),Vertex(edge[4])))
        # edgelist.append(Edge(edge[0],edge[1],edge[2],edge[3],edge[4]))
        id = edge[0]
        ename = edge[1]
        w = edge[2]
        # sv = Vertex(edge[3])
        # tv = Vertex(edge[4])
        sv = edge[3]
        tv = edge[4]
        if sv not in vertlist3:
            vertlist3.append(sv)
        if tv not in vertlist3:
            vertlist3.append(tv)
        sv = Vertex(edge[3])
        tv = Vertex(edge[4])
        print(id,ename,w,sv,tv)
        # p = Edge(id,ename,w,sv,tv)
        edgelist.append(Edge(id,ename,w,sv,tv))
        # edgelist.append(p)


    # for vert in vertlist2:
    #     print(vert)
    print()

    for vert in vertlist3:
        v = Vertex(vert)
        vertlist4.append(v)

    for v in vertlist4:
        print(v)
    for edge in edgelist:
        print(edge)

    # print("---------------")
    # print(edgelist[0].targetVertex)
    # print(vertlist2[0])

    # vertlist2[0].adjacenciesList.append(edgelist[0])
    # vertlist2[1].adjacenciesList.append(edgelist[1])
    # vertlist2[2].adjacenciesList.append(edgelist[2])
    vertlist4[0].adjacenciesList.append(edgelist[0])
    vertlist4[0].adjacenciesList.append(edgelist[2])
    vertlist4[1].adjacenciesList.append(edgelist[1])
    # vertlist4[2].adjacenciesList.append(edgelist[2])

    print(vertlist4[0].adjacenciesList)
    print(vertlist4[1].adjacenciesList)
    print(vertlist4[2].adjacenciesList)
    # print(vertlist2[0].minDistance)
    print()

    sv = vertlist4[0]
    tv = vertlist4[2]
    # # dijkistra.calculateShrtestPath(vertlist2[0])
    #
    dijkistra.calculateShrtestPath(vertlist2,vertlist4[0])
    # # print(sv.minDistance)
    # dijkistra.getShortestPathTo(vertlist2[2])

    dijkistra.getShortestPathTo(vertlist4[2])

    # print(tv.minDistance)
    # print(tv.predecessor)
    # print(edgelist[0].startVertex.name)
    # for verts in range(len(edgelist)):
    #     print(vert)
        # for mindist in edgelist[0].startVertex.name
    # for ed in edgelist:
    #     # print(ed,(type(ed.startVertex)))
    #     for s,t,v in ed:
    #         print(s,t,v)
    # print()
    # print(edgelist)
    # print(edgelist[0])
    # print(type(edgelist[1]))
    # print(edgelist[2])
    # print(len(edgelist))
else:
    print("No connection")

