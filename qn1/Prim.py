from collections import defaultdict
import heapq

def prim(graph):
    min_spanning_tree = []
    visited = set()
    start_node = list(graph.keys())[0]  # Choosing the starting node arbitrarily

    priority_queue = [(0, None, start_node)]  # (weight, parent, node)

    while priority_queue:
        weight, parent, node = heapq.heappop(priority_queue)

        if node not in visited:
            visited.add(node)

            if parent is not None:
                min_spanning_tree.append((parent, node, weight))

            for neighbor, neighbor_weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (neighbor_weight, node, neighbor))

    return min_spanning_tree

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

minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
