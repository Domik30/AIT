def is_connected(graph):
    visited = set()

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

    start_node = next(iter(graph))
    dfs(start_node)

    return len(visited) == len(graph)


def is_eulerian(graph):
    if not is_connected(graph):
        return "Graph is not Eulerian (it is not connected)."

    odd_degree_count = 0
    print("Degrees of each node:")
    for node in graph:
        degree = len(graph[node])
        print("Node", node, ": Degree", degree)
        if degree % 2 != 0:
            odd_degree_count += 1
    print("Total nodes with odd degree:", odd_degree_count)

    if odd_degree_count == 0:
        return "Graph has an Eulerian cycle (can be traversed in a closed loop)."
    elif odd_degree_count == 2:
        return "Graph has an Eulerian path (can be traversed from one point to another)."
    else:
        return "Graph is not Eulerian (cannot be traversed in a single path or cycle)."


def build_graph():
    nodes = input("Enter nodes separated by spaces (e.g., 'A B C D'): ").split()
    graph = dict((node, []) for node in nodes)
    print("Nodes added:", " ".join(nodes))
    print("Now, enter edges one by one in the format 'A-B' (or just press Enter to finish):")
    while True:
        edge = input("Edge: ").strip()
        if not edge:
            break
        try:
            node1, node2 = edge.split('-')
            if node1 in graph and node2 in graph:
                graph[node1].append(node2)
                graph[node2].append(node1)
                print("Edge added:", node1, "<->", node2)
            else:
                print("One or both of the nodes do not exist. Try again.")
        except ValueError:
            print("Invalid edge format. Use 'A-B'. Try again.")
    return graph


def main():
    graph = build_graph()
    for node, neighbors in graph.items():
        print(node, ":", " ".join(neighbors))
    result = is_eulerian(graph)
    print("Result:", result)


if __name__ == "__main__":
    main()
