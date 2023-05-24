# Function to add edges to the graph
def add_edge(graph, node1, node2, weight):
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append((node2, weight))
    graph[node2].append((node1, weight))

# Prim's algorithm for Minimum Spanning Tree
def prim(graph):
    # Initialize the minimum spanning tree and visited nodes
    mst = []
    visited = set()

    # Start from an arbitrary node
    start_node = list(graph.keys())[0]
    visited.add(start_node)

    while len(visited) < len(graph):
        min_edge = None

        # Find the minimum-weight edge connecting a visited node to an unvisited node
        for node in visited:
            for neighbour, weight in graph[node]:
                if neighbour not in visited:
                    if min_edge is None or weight < min_edge[2]:
                        min_edge = (node, neighbour, weight)

        if min_edge is not None:
            # Add the minimum-weight edge to the minimum spanning tree
            mst.append(min_edge)
            visited.add(min_edge[1])

    return mst

# Taking user input for the graph
print("Enter the number of nodes in the graph:")
num_nodes = int(input())

graph = {}

print("Enter node1 then its neighbour and then their weights (separated by spaces, use 'done' to finish):")
while True:
    input_str = input()
    if input_str == 'done':
        break
    node1, node2, weight = input_str.split()
    add_edge(graph, node1, node2, int(weight))

# Compute the minimum spanning tree using Prim's algorithm
minimum_spanning_tree = prim(graph)

# Calculate the total cost of the minimum spanning tree
total_cost = sum(edge[2] for edge in minimum_spanning_tree)

# Print the minimum spanning tree
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge[0], "--", edge[1], ":", edge[2])

# Print the total cost of the spanning tree
print("Total Cost of the Minimum Spanning Tree:", total_cost)
