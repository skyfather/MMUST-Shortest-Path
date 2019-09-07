from algorithms.Vertex import Vertex


class Edge(object):
    def __init__(self,id,edgename,weight,startVertex,targetVertex,blocked=0):
        self.id =id
        self.edgename = edgename
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex
        # self.startVertex = Vertex(targetVertex)
        # self.targetVertex = Vertex(targetVertex)
        self.blocked = blocked

    def __iter__(self):
        # yield (self.id,self.edgename,self.weight,self.startVertex,self.targetVertex)
        yield self.startVertex,self.targetVertex,self.weight

    def getName(self):
        return self.edgename()
    def setBlocked(self,block):
        self.blocked = block
    def unblock(self):
        self.blocked = 0

    def __repr__(self):
        return '{self.edgename}, {self.weight}, {self.startVertex}, {self.targetVertex}'.format(self=self)