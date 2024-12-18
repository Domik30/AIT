def is_eulerian(graph):
    odd_degree_count = 0
    print("\nDegrees of each node:")
    for node in graph:
        degree = len(graph[node])
        print(f"Node {node}: Degree {degree}")
        if degree % 2 != 0:
            odd_degree_count += 1
    print(f"Total nodes with odd degree: {odd_degree_count}")

    # Eulerian cycle: all degrees are even
    if odd_degree_count == 0:
        return "Graph has an Eulerian cycle (can be traversed in a closed loop)."
    # Eulerian path: exactly two vertices with odd degree
    elif odd_degree_count == 2:
        return "Graph has an Eulerian path (can be traversed from one point to another)."
    # Not Eulerian
    else:
        return "Graph is not Eulerian (cannot be traversed in a single path or cycle)."


def build_graph():
    print("Let's build a graph!")

    # Step 1: Enter nodes
    nodes = input("Enter nodes separated by spaces (e.g., 'A B C D'): ").split()
    graph = {node: [] for node in nodes}
    print(f"Nodes added: {nodes}")

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
                print(f"Edge added: {node1} <-> {node2}")
            else:
                print("One or both of the nodes do not exist. Try again.")
        except ValueError:
            print("Invalid edge format. Use 'A-B'. Try again.")
    print("Graph construction completed.")
    return graph


def main():
    print("Welcome to the Eulerian graph checker!")
    graph = build_graph()
    print("\nConstructed graph (adjacency list):")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")
    result = is_eulerian(graph)
    print(f"\nResult: {result}")


if __name__ == "__main__":
    main()



