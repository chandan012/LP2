def is_safe(vertex, graph, colors, color):
    # Check if it is safe to color the vertex with the given color
    for adjacent in graph[vertex]:
        if colors[adjacent] == color:
            return False
    return True

def m_coloring_util(vertex, m, graph, colors):
    # Base case: If all vertices are colored, return True
    if vertex == len(graph):
        return True

    for color in range(1, m+1):
        if is_safe(vertex, graph, colors, color):
            # Assign the color to the current vertex
            colors[vertex] = color

            # Recursive call to color the remaining vertices
            if m_coloring_util(vertex + 1, m, graph, colors):
                return True

            # If the recursive call does not lead to a solution, backtrack
            colors[vertex] = 0

    return False

def m_coloring():
    # Take user input for the graph
    graph = {}
    num_vertices = int(input("Enter the number of vertices in the graph: "))

    for vertex in range(num_vertices):
        adjacent_vertices = input("Enter the adjacent vertices for vertex {}: ".format(vertex)).split()
        graph[vertex] = [int(adjacent) for adjacent in adjacent_vertices]

    # Take user input for the number of colors
    m = int(input("Enter the number of colors: "))

    # Create a list to store the assigned colors for each vertex
    colors = [0] * num_vertices

    # Start coloring from the first vertex
    if m_coloring_util(0, m, graph, colors):
        # If a valid coloring is found, print the result
        print("Graph can be colored using", m, "colors.")
        for vertex, color in enumerate(colors):
            print("Vertex", vertex, ":", "Color", color)
    else:
        print("Graph cannot be colored using", m, "colors.")

# Test the m_coloring function
m_coloring()






# Enter the number of vertices in the graph: 4
# Enter the adjacent vertices for vertex 0: 1 2
# Enter the adjacent vertices for vertex 1: 0
# Enter the adjacent vertices for vertex 2: 1 0 3
# Enter the adjacent vertices for vertex 3: 2
# Enter the number of colors: 3
# Graph can be colored using 3 colors.
# Vertex 0 : Color 1
# Vertex 1 : Color 2
# Vertex 2 : Color 3
# Vertex 3 : Color 1