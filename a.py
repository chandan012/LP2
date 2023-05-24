def aStarAlgo(start_node, stop_node, graph_nodes, heuristic_dist):
    open_set = set(start_node)  # Set to store nodes to be evaluated
    closed_set = set()  # Set to store evaluated nodes
    g = {}  # Dictionary to store g-score (cost from start to a node)
    parents = {}  # Dictionary to store parent nodes
    g[start_node] = 0  # Initialize g-score of start node as 0
    parents[start_node] = start_node  # Set parent of start node as itself

    while len(open_set) > 0:
        n = None

        # Find the node with the lowest f-score (g-score + heuristic)
        for v in open_set:
            if n == None or g[v] + heuristic_dist[v] < g[n] + heuristic_dist[n]:
                n = v

        if n == stop_node or graph_nodes[n] == None:
            pass
        else:
            # Explore neighbors of the current node
            for (m, weight) in get_neighbors(n, graph_nodes):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print('Path does not exist!')
            return None

        if n == stop_node:
            # Reconstruct the path from start to stop node
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)
            path.reverse()

            print('Path found: {}'.format(path))
            return path

        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None


def get_neighbors(v, graph_nodes):
    if v in graph_nodes:
        return graph_nodes[v]
    else:
        return None


def heuristic(n, heuristic_dist):
    return heuristic_dist[n]


# Get user input for graph and heuristic values
graph_nodes = {}
heuristic_dist = {}

num_nodes = int(input("Enter the number of nodes in the graph: "))
for _ in range(num_nodes):
    node = input("Enter the node: ")
    neighbors = input("Enter neighbors and their weights (comma-separated): ").split(',')
    neighbors = [(n.strip(), int(w.strip())) for n, w in map(lambda x: x.split(':'), neighbors)]
    graph_nodes[node] = neighbors

num_heuristics = int(input("Enter the number of heuristic values: "))
for _ in range(num_heuristics):
    node = input("Enter the node: ")
    value = int(input("Enter the heuristic value: "))
    heuristic_dist[node] = value

start_node = input("Enter the start node: ")
stop_node = input("Enter the stop node: ")

# Call the A* algorithm with user inputs
aStarAlgo(start_node, stop_node, graph_nodes, heuristic_dist)
