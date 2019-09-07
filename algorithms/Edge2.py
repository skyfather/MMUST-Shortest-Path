from algorithms.Vertex import Vertex


class Edge2(object):
    def __init__(self,edgename,weight,startVertex,targetVertex):
        # self.id =id
        self.edgename = edgename
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex
        # self.startVertex = Vertex(targetVertex)
        # self.targetVertex = Vertex(targetVertex)
        self.blocked = 0

    def __iter__(self):
        # yield (self.id,self.edgename,self.weight,self.startVertex,self.targetVertex)
        yield self.startVertex,self.targetVertex,self.weight

    def setBlocked(self):
        self.blocked = 1
    def __repr__(self):
        return '{self.edgename}, {self.weight}, {self.startVertex}, {self.targetVertex}'.format(self=self)