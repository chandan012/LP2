def dfs(visited,graph,node):
    if node not in visited:
        print(node,end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited,graph,node,queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s,end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    visited1 = set() # TO keep track of DFS visited nodes
    visited2 = set() # TO keep track of BFS visited nodes
    queue = []       # For BFS
    n = int(input("Enter number of nodes : "))
    graph = dict()

    for i in range(1,n+1):
        edges = int(input("Enter number of edges for node {} : ".format(i)))
        graph[i] = list()
        for j in range(1,edges+1):
            node = int(input("Enter edge {} for node {} : ".format(j,i)))
            graph[i].append(node)
    print(graph)


    while (1):
        print("1.BFS")
        print("2.DFS")
        print("3.EXIT")
        print("enter choise")
        choise = int(input())

        if choise == 2:
            print("The following is DFS","\n")
            dfs(visited1, graph, 1)
            print()
            print()

        elif choise == 1:
            print("The following is BFS","\n")
            bfs(visited2, graph, 1, queue)
            print()
            print()
        elif choise == 3:
            break
        else:

            print("invalid choise")

if __name__=="__main__":
    main()


