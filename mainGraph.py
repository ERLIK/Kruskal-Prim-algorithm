import matplotlib.pyplot as plt
import networkx as nx

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

D = nx.Graph()
D.add_nodes_from(['A','B','C','D','E','F','G','H','I','J','K','L'])
D.add_edge("A", "B", weight=3)
D.add_edge("B", "C", weight=1)
D.add_edge("C", "D", weight=1)
D.add_edge("A", "E", weight=2)
D.add_edge("A", "F", weight=4)
D.add_edge("B", "F", weight=2)
D.add_edge("C", "F", weight=4)
D.add_edge("C", "G", weight=1)
D.add_edge("D", "G", weight=1)
D.add_edge("D", "H", weight=5)
D.add_edge("E", "F", weight=5)
D.add_edge("F", "G", weight=3)
D.add_edge("G", "H", weight=5)
D.add_edge("E", "I", weight=1)
D.add_edge("F", "I", weight=6)
D.add_edge("F", "J", weight=3)
D.add_edge("I", "J", weight=2)
D.add_edge("G", "J", weight=3)
D.add_edge("G", "K", weight=3)
D.add_edge("J", "K", weight=3)
D.add_edge("G", "L", weight=2)
D.add_edge("G", "L", weight=2)
D.add_edge("K", "L", weight=4)
D.add_edge("H", "L", weight=2)

elarge = [(u, v) for (u, v, d) in D.edges(data=True)]
esmall = [(u, v) for (u, v, d) in D.edges(data=True)]

pos = nx.spring_layout(D, seed=7)
nx.draw_networkx_nodes(D, pos, node_size=700)
nx.draw_networkx_edges(D, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(D, pos, edgelist=esmall, width=6, alpha=0.5, edge_color='r', style="dashed")
nx.draw_networkx_labels(D, pos, font_size=20, font_family='sans-serif')
edge_labels = nx.get_edge_attributes(D, 'weight')
nx.draw_networkx_edge_labels(D, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()