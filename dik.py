def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # Initialize all distances as infinity
    distances[start] = 0  # Set the distance of the start node to 0
    visited = set()  # Set to store visited nodes

    while True:
        min_node = None
        min_distance = float('inf')

        # Find the unvisited node with the minimum distance
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_node = node
                min_distance = distances[node]

        if min_node is None:
            break

        visited.add(min_node)

        # Update distances to the neighboring nodes
        for neighbor, distance in graph[min_node].items():
            new_distance = distances[min_node] + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances

# Take graph input from the user
graph = {}
num_nodes = int(input("Enter the number of nodes in the graph: "))

# Iterate over each node to input its neighbors and distances
for i in range(num_nodes):
    node = input(f"Enter the name of node {i+1}: ")
    graph[node] = {}

    num_neighbors = int(input(f"Enter the number of neighbors for node {node}: "))

    # Iterate over each neighbor of the current node
    for j in range(num_neighbors):
        neighbor = input(f"Enter the name of neighbor {j+1}: ")
        distance = int(input(f"Enter the distance from node {node} to neighbor {neighbor}: "))
        graph[node][neighbor] = distance

start_node = input("Enter the starting node: ")
distances = dijkstra(graph, start_node)

# Print the shortest distances from the start node to all other nodes
for node, distance in distances.items():
    print(f"Shortest distance from {start_node} to {node}: {distance}")
