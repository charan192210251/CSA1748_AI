from sys import maxsize
from itertools import permutations


def travellingSalesmanProblem(graph, s):
    V = len(graph)
    vertex = [i for i in range(V) if i != s]
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)
    return min_path


if __name__ == "__main__":
    # Read the number of vertices
    V = int(input("Enter the number of vertices: "))
    # Initialize the graph matrix
    graph = []
    print("Enter the adjacency matrix (one row per line, values separated by spaces):")
    for _ in range(V):
        row = list(map(int, input().split()))
        graph.append(row)

    # Read the starting vertex for TSP
    s = int(input("Enter the starting vertex for TSP: "))

    print("Minimum cost of visiting all vertices starting from vertex", s, "is:", travellingSalesmanProblem(graph, s))
