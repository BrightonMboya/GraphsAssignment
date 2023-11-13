class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def kruskal(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((vertex, neighbor, weight))

    edges.sort(key=lambda x: x[2])  # Sort edges by weight

    minimum_spanning_tree = []
    disjoint_set = DisjointSet(graph.keys())

    for edge in edges:
        vertex1, vertex2, weight = edge
        if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
            disjoint_set.union(vertex1, vertex2)
            minimum_spanning_tree.append(edge)

    return minimum_spanning_tree

# Example graph representation: {node: [(neighbor, weight), ...]}
graph = {
    'A': [('L', 14), ('F', 5), ('C', 8)],
    'F': [('D', 14), ('B', 20), ('K', 16), ('A', 5), ('I', 8)],
    'C': [('I', 10), ('L', 8), ('G', 12), ('A', 8)],
    'D': [('G', 22), ('B', 8), ('F', 14)],
    'B': [('H', 12), ('F', 20), ('D', 8), ('K', 47)],
    'K': [('B', 47), ('J', 5), ('F', 16)],
    'I': [('F', 8), ('E', 16), ('C', 10)],
    'G': [('L', 13), ('J', 5), ('C', 12), ('D', 22)],
    'J': [('H', 16), ('K', 5), ('G', 5)],
    'L': [('E', 15), ('H', 15), ('A', 14), ('C', 8), ('G', 13)],
    'E': [('H', 8), ('I', 16), ('L', 15)],
    'H': [('E', 8), ('B', 12), ('J', 16), ('L', 15)]
}

minimum_spanning_tree = kruskal(graph)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
