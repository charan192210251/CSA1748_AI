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

    # Read number of vertices
    num_vertices = int(input("Enter the number of vertices: "))

    # Read number of edges
    num_edges = int(input("Enter the number of edges: "))

    print("Enter the edges (u v):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        g.addEdge(u, v)

    # Read starting vertex for DFS
    start_vertex = int(input("Enter the starting vertex for DFS: "))

    print(f"Following is Depth First Traversal (starting from vertex {start_vertex})")
    g.DFS(start_vertex)
