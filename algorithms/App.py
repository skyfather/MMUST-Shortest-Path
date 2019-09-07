from algorithms.Vertex import Vertex
from algorithms.Edge import Edge
from algorithms.Dijkstra import Dijkstra
import MySQLdb
from _mysql_exceptions import Error


spd = Vertex("SPD")
lbb = Vertex("LBB")
med = Vertex("MED")
mea = Vertex("MEA")
lib = Vertex("LIB")
mcu = Vertex("MCU")
h1 = Vertex("H1")
h2 = Vertex("H2")
h3 = Vertex("H3")
h4 = Vertex("H4")


# edge1 = Edge(id=1,weight=1,startVertex=spd,targetVertex=lbb,edgename="edge1")
# edge2 = Edge(id=2,weight=13,startVertex=lbb,targetVertex=med,edgename="edge2")
# edge3 = Edge(id=3,weight=10.1,startVertex=spd,targetVertex=med, edgename="edge3")
# edge4 = Edge(4,'edge4',4,'spd','lbb')
edge1 = Edge(1,'edge1',3,spd,lbb)
edge2 = Edge(2,'edge2',2,lbb,med)
edge3 = Edge(3,'edge3',6,spd,med)

edge4 = Edge(4,'edge4',3,lbb,spd)
edge5 = Edge(5,'edge5',2,med,lbb)
edge6 = Edge(6,'edge6',6,med,spd)


#db staff
print("Attempting database connection ........\n")

print(type(edge3))

spd.adjacenciesList.append(edge1)
spd.adjacenciesList.append(edge3)

lbb.adjacenciesList.append(edge2)
lbb.adjacenciesList.append(edge4)

med.adjacenciesList.append(edge6)
med.adjacenciesList.append(edge5)


# spd.adjacenciesList.append(edge4)
# spd.adjacenciesList.append(edge6)
# lbb.adjacenciesList.append(edge5)

vertexList = {spd,lbb,med}
vertexList2 = [spd,lbb,med]

dijkistra = Dijkstra()

# userinput1 = 'MED'
# userinput2 = 'SPD'
userinput1 = input("Start Vertex: ")
userinput2 = input("Target Vertex: ")
# print(type(vertexList2))
for sv in vertexList2:

    if userinput1==sv.name:

        dijkistra.calculateShrtestPath(vertexList,sv)
        print(sv.name)
        print(sv.minDistance)

    else:
        print("Node not found")
for tv in vertexList2:
    if userinput2==tv.name:
        dijkistra.getShortestPathTo(tv)
        print(tv.name)
        print(tv.minDistance)

#
# for n in vertexList:
#     for nn in n:
#         if userinput1==nn:
#             dijkistra.calculateShrtestPath(vertexList, n)
#
# dijkistra.calculateShrtestPath(vertexList,userinput1)
# dijkistra.getShortestPathTo(userinput2)
# print(lbb.adjacenciesList)
print("---------------------")
