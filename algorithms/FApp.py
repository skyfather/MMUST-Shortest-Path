from algorithms.Vertex import Vertex
from algorithms.Edge import Edge
from algorithms.Dijkstra import Dijkstra


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
gate = Vertex('GATE')

# edge1 = Edge(id=1,weight=1,startVertex=spd,targetVertex=lbb,edgename="edge1")
# edge2 = Edge(id=2,weight=13,startVertex=lbb,targetVertex=med,edgename="edge2")
# edge3 = Edge(id=3,weight=10.1,startVertex=spd,targetVertex=med, edgename="edge3")
# edge4 = Edge(4,'edge4',4,'spd','lbb')
edge1 = Edge(1,'edge1',12,spd,mea)#spd
edge11 = Edge(11,'edge11',12,mea,spd)#mea
edge2 = Edge(2,'edge2',200,spd,h4)#spd
edge22 = Edge(22,'edge22',200,h4,spd)#h4
edge3 = Edge(3,'edge3',3,spd,lbb)#spd
edge33 = Edge(33,'edge33',3,lbb,spd)#lbb
edge4 = Edge(4,'edge4',20,spd,med)#spd
edge44 = Edge(44,'edge44',20,med,spd)#med
edge5 = Edge(5,'edge5',100,spd,mcu)#mcu
edge55 = Edge(55,'edge55',100,mcu,spd)#mcu
edge6 = Edge(6,'edge6',5,lbb,mea)#lbb
edge66 = Edge(66,'edge66',5,mea,lbb)#mea

edge7 = Edge(7,'edge7',65,med,gate)#med
edge77 = Edge(77,'edge77',65,gate,med)#gate
edge8 = Edge(8,'edge8',60,mea,gate)#mea
edge88 = Edge(88,'edge88',60,gate,mea)#gate
edge10 = Edge(10,'edge10',5,mea,med)#mea
edge1010 = Edge(1010,'edge1010',5,med,mea)#med
edge11 = Edge(11,'edge11',55,lib,gate)#lib
edge1111 = Edge(1111,'edge1111',55,gate,lib)#gate
edge12 = Edge(12,'edge12',4,mcu,h1)#mcu
edge1212 = Edge(1212,'edge1212',4,h1,mcu)#h1
edge13 = Edge(13,'edge13',7,mcu,h3)#mcu
edge1313 = Edge(1313,'edge1313',7,h3,mcu)#h3
edge14 = Edge(14,'edge14',3,h1,h2)#h1
edge1414 = Edge(1414,'edge1414',3,h2,h1)#h2
edge15 = Edge(15,'edge15',3,h2,h3)#h2
edge1515 = Edge(1515,'edge1515',3,h3,h2)#h3

edge16 = Edge(16,'edge16',70,h2,gate)#h2
edge1616 = Edge(16,'edge1616',70,gate,h2)#gate
edge17 = Edge(17,'edge17',150,gate,spd)#gate
edge1717 = Edge(1717,'edge1717',150,spd,gate)#spd



#db staff
print("Attempting database connection ........\n")

print(type(edge3))

spd.adjacenciesList.append(edge1)
spd.adjacenciesList.append(edge2)
spd.adjacenciesList.append(edge3)
spd.adjacenciesList.append(edge4)
spd.adjacenciesList.append(edge5)
spd.adjacenciesList.append(edge1717)

lbb.adjacenciesList.append(edge33)
lbb.adjacenciesList.append(edge6)

med.adjacenciesList.append(edge44)
med.adjacenciesList.append(edge7)
med.adjacenciesList.append(edge1010)


mea.adjacenciesList.append(edge11)
mea.adjacenciesList.append(edge8)
mea.adjacenciesList.append(edge10)
mea.adjacenciesList.append(edge66)

lib.adjacenciesList.append(edge11)

mcu.adjacenciesList.append(edge12)
mcu.adjacenciesList.append(edge13)
mcu.adjacenciesList.append(edge55)

h1.adjacenciesList.append(edge1212)
h1.adjacenciesList.append(edge14)

h2.adjacenciesList.append(edge1414)
h2.adjacenciesList.append(edge15)
h2.adjacenciesList.append(edge16)

h3.adjacenciesList.append(edge1515)
h3.adjacenciesList.append(edge1313)

h4.adjacenciesList.append(edge22)

gate.adjacenciesList.append(edge1616)
gate.adjacenciesList.append(edge17)
gate.adjacenciesList.append(edge1111)
gate.adjacenciesList.append(edge88)
gate.adjacenciesList.append(edge77)




# spd.adjacenciesList.append(edge4)
# spd.adjacenciesList.append(edge6)
# lbb.adjacenciesList.append(edge5)

vertexList = {spd,lbb,med,mea,lib,mcu,h1,h2,h3,h4,gate}
vertexList2 = [spd,lbb,med]

dijkistra = Dijkstra()

# userinput1 = 'LIB'
# userinput2 = 'MEA'

userinput1 = input("Start Vertex: ").upper()
userinput2 = input("Target Vertex: ").upper()
print(type(vertexList))
for sv in vertexList:

    if userinput1==sv.name:

        dijkistra.calculateShrtestPath(vertexList,sv)
        print(sv.name)
        print(sv.minDistance)

for tv in vertexList:
    if userinput2==tv.name:
        temp = dijkistra.getShortestPathTo2(tv)
        print(tv.name)
        print(tv.minDistance)
        print(temp)
print("---------------------")
