import matplotlib.pyplot as plt
import networkx as nx
import string

class Graph:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_graph = []
        self.final_graph = []
    def add_edge(self, node1, node2, weight):
        alphabet = string.ascii_uppercase
        self.m_graph.append([alphabet.index(node1), alphabet.index(node2), weight])

    def find_subtree(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_subtree(parent, parent[i])

    def connect_subtrees(self, parent, subtree_sizes, x, y):
        xroot = self.find_subtree(parent, x)
        yroot = self.find_subtree(parent, y)
        if subtree_sizes[xroot] < subtree_sizes[yroot]:
            parent[xroot] = yroot
        elif subtree_sizes[xroot] > subtree_sizes[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
        subtree_sizes[xroot] += 1

    def kruskals_mst(self):
        result = []
        
        i = 0
        e = 0

        self.m_graph = sorted(self.m_graph, key=lambda item: item[2])
        
        parent = []
        subtree_sizes = []

        for node in range(self.m_num_of_nodes):
            parent.append(node)
            subtree_sizes.append(0)

        while e < (self.m_num_of_nodes - 1):
            node1, node2, weight = self.m_graph[i]
            i = i + 1

            x = self.find_subtree(parent, node1)
            y = self.find_subtree(parent, node2)

            if x != y:
                e = e + 1
                result.append([node1, node2, weight])
                self.connect_subtrees(parent, subtree_sizes, x, y)
        self.final_graph = result

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

G = Graph(12)
G.add_edge("A", "B", 3)
G.add_edge("B", "C", 1)
G.add_edge("C", "D", 1)
G.add_edge("A", "E", 2)
G.add_edge("A", "F", 4)
G.add_edge("B", "F", 2)
G.add_edge("C", "F", 4)
G.add_edge("C", "G", 1)
G.add_edge("D", "G", 1)
G.add_edge("D", "H", 5)
G.add_edge("E", "F", 5)
G.add_edge("F", "G", 3)
G.add_edge("G", "H", 5)
G.add_edge("E", "I", 1)
G.add_edge("F", "I", 6)
G.add_edge("F", "J", 3)
G.add_edge("I", "J", 2)
G.add_edge("G", "J", 3)
G.add_edge("G", "K", 3)
G.add_edge("J", "K", 3)
G.add_edge("G", "L", 2)
G.add_edge("G", "L", 2)
G.add_edge("K", "L", 4)
G.add_edge("H", "L", 2)
G.kruskals_mst()

alphabet = string.ascii_uppercase
D = nx.Graph()
for edge in G.final_graph:
    D.add_edge(alphabet[edge[0]], alphabet[edge[1]], weight = edge[2])

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
plt.title('KRUSKAL ALGORİTMASI')
plt.tight_layout()
plt.show()