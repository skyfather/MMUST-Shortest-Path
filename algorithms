import heapq
from algorithms.Vertex import Vertex


class Dijkstra(object):
    def __init__(self):
        self.path = []
        self.pathname = []

    def calculateShrtestPath(self,vertList,startVertex):
        queue = []
        startVertex.minDistance = 0
        heapq.heappush(queue,startVertex)

        while len(queue)>0:
            actualVertex = heapq.heappop(queue)

            for edge in actualVertex.adjacenciesList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance+edge.weight

                if newDistance<v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(queue,v)

    def getShortestPathTo2(self,targetVertex):
        node = targetVertex
        while node is not None:
            self.path.append(node.name)
            node = node.predecessor
        return self.path
