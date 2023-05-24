# Kruskal's algorithm for Minimum Spanning Tree
def kruskal(graph):
    graph = sorted(graph, key=lambda x: x[2])  # Sort edges based on weight
    parent = {}  # Parent dictionary for each node
    minimum_spanning_tree = []  # Resultant Minimum Spanning Tree

    # Function to find the parent of a node
    def find_parent(node):
        if parent[node] != node:
            parent[node] = find_parent(parent[node])
        return parent[node]

    # Function to union two sets
    def union_sets(node1, node2):
        parent[find_parent(node2)] = find_parent(node1)

    for u, v, weight in graph:
        parent[u] = u
        parent[v] = v

    for u, v, weight in graph:
        if find_parent(u) != find_parent(v):
            minimum_spanning_tree.append((u, v, weight))
            union_sets(u, v)

    return minimum_spanning_tree

# Taking user input for the graph
print("Enter the number of nodes in the graph:")
num_nodes = int(input())

graph = []

print("Enter node1 then its neighbour and then their weights (separated by spaces, use 'done' to finish):")
while True:
    input_str = input()
    if input_str == 'done':
        break
    u, v, weight = input_str.split()
    graph.append((u, v, int(weight)))

# Compute the Minimum Spanning Tree using Kruskal's algorithm
minimum_spanning_tree = kruskal(graph)

# Print the Minimum Spanning Tree
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge[0], "--", edge[1], ":", edge[2])

