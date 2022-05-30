import sys
import string
import matplotlib.pyplot as plt
import networkx as nx

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):

        self.way = list()
        alphabet = string.ascii_uppercase
        totalWeight = 0
        nodeNames = ''
        for i in range(self.V):
            nodeNames += alphabet[i]
        self.nodes = list(nodeNames)

        print("Edge \tWeight")
        for i in range(1, self.V):
            print(alphabet[parent[i]], "-", alphabet[i], "\t", self.graph[i][parent[i]])
            self.way.append([alphabet[parent[i]], alphabet[i], self.graph[i][parent[i]]])
            totalWeight += self.graph[i][parent[i]]
        print(f'Minimum yayılan ağacın toplam ağırlığı: {totalWeight}')

    def minKey(self, key, mstSet):

        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def primMST(self):

        key = [sys.maxsize] * self.V
        parent = [None] * self.V

        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1
        alphabet = string.ascii_uppercase

        for cout in range(self.V):

            u = self.minKey(key, mstSet)

            mstSet[u] = True

            for v in range(self.V):

                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        print(f'Başlangıç Node: {alphabet[key[0]]}\n')

        self.printMST(parent)

g = Graph(12)
          # a  b  c  d  e  f  g  h  i  j  k  l
g.graph = [[0, 3, 0, 0, 2, 4, 0, 0, 0, 0, 0, 0],  #a
           [3, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0],  #b
           [0, 1, 0, 1, 0, 4, 1, 0, 0, 0, 0, 0],  #c
           [0, 0, 1, 0, 0, 0, 1, 5, 0, 0, 0, 0],  #d
           [2, 0, 0, 0, 0, 5, 0, 0, 1, 0, 0, 0],  #e
           [4, 2, 4, 0, 5, 0, 3, 0, 6, 3, 0, 0],  #f
           [0, 0, 1, 1, 0, 3, 0, 5, 0, 3, 3, 2],  #g
           [0, 0, 0, 5, 0, 0, 5, 0, 0, 0, 0, 2],  #h
           [0, 0, 0, 0, 1, 6, 0, 0, 0, 2, 0, 0],  #i
           [0, 0, 0, 0, 0, 3, 3, 0, 2, 0, 3, 0],  #j
           [0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 4],  #k
           [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 4, 0]]  #l

class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

g.primMST()

D = nx.Graph()
D.add_nodes_from(g.nodes)

for i in g.way:
    D.add_edge(i[0], i[1], weight = i[2])

elarge = [(u, v) for (u, v, d) in D.edges(data=True)]
esmall = [(u, v) for (u, v, d) in D.edges(data=True)]

pos = nx.spring_layout(D, seed=700)

# nodes
nx.draw_networkx_nodes(D, pos, node_size=400)

# edges
nx.draw_networkx_edges(D, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(D, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed")

# node labels
nx.draw_networkx_labels(D, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(D, "weight")
nx.draw_networkx_edge_labels(D, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()