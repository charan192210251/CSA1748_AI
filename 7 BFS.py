from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

if __name__ == '__main__':
    g = Graph()

    # Define the edges manually
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

    # Define the starting vertex for BFS
    start_vertex = 2

    print("Following is Breadth First Traversal (starting from vertex {})".format(start_vertex))
    g.BFS(start_vertex)
