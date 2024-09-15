from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

if __name__ == "__main__":
    g = Graph()

    # Hardcoded number of vertices
    num_vertices = 5

    # Hardcoded edges
    edges = [
        (0, 1),
        (0, 2),
        (1, 2),
        (2, 0),
        (2, 3),
        (3, 3)
    ]

    # Adding edges to the graph
    for u, v in edges:
        g.addEdge(u, v)

    # Hardcoded starting vertex for DFS
    start_vertex = 2

    print(f"Following is Depth First Traversal (starting from vertex {start_vertex}):")
    g.DFS(start_vertex)
