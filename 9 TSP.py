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
    # Hardcoded number of vertices
    V = 4

    # Hardcoded adjacency matrix (graph)
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    # Hardcoded starting vertex for TSP
    s = 0

    print("Minimum cost of visiting all vertices starting from vertex", s, "is:", travellingSalesmanProblem(graph, s))
