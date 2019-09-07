import sys


class Vertex(object):
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacenciesList = []
        self.minDistance = sys.maxsize

    def __cmp__(self, otherVertex):
        return self.__cmp__(self.minDistance,otherVertex.minDistance)

    def __lt__(self, other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority<otherPriority

    def get_minDistance(self):
        return self.minDistance

    def __iter__(self):
        yield self.name

    def __repr__(self):
        return '{self.name}'.format(self=self)