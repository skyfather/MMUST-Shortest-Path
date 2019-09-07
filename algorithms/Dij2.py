import sys

with open('graph.txt','r') as f:
    lines =f.readlines()

lines = [x.strip() for x in lines]
for x in lines:
    print("line is ->",x,"<-")

print()
it = iter(lines)
edges = zip(it,it,it)
contain = []
for (a,w,b) in edges:
    print("edge is: ",a,w,b)
    contain.append(a)
    contain.append(b)

print()

# vertices = set([a for (a,w,b) in edges]+[b for (a,w,b) in edges])
vertices = set(contain)
for v in vertices:
    print("Vertices is: ",v)

INFINITY = sys.maxsize
UNDEFINED = "?"
dist = {}
prev = {}
source = "A"
target = "C"

for v in vertices:
    dist[v] = INFINITY
    prev[v] = UNDEFINED

dist[source] = 0
Q = vertices

print(dist)

while Q !=[]:
    for candidate in Q:
        min_dist_sofar = INFINITY
        if dist[candidate]<=min_dist_sofar:
            u = candidate
            min_dist_sofar = dist[candidate]

    print("u = ",u)
    Q.remove(u)
    if u == target:
        print("vertex found")
        s = []
        u = target
        while prev[v]!=UNDEFINED:
            s = [u]+s
            u = prev[u]
        s = [u]+s
        print("Shortest path is: ",s)
        exit(0)

    for (a,w,v) in edges:
        if a==u:
            alt = dist[u]+int(w)
            if alt<dist[v]:
                dist[v] = alt
                prev[v] = u


print(len(Q))
for elem in Q:
    print(elem)
