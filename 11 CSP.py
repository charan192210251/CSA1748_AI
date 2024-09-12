class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    def graphColourUtil(self, m, colour, v):
        if v == self.V:
            return True
        for c in range(1, m + 1):
            if self.isSafe(v, colour, c):
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1):
                    return True
                colour[v] = 0

    def graphColouring(self, m):
        colour = [0] * self.V
        if not self.graphColourUtil(m, colour, 0):
            return False
        print("Solution exists and the following are the assigned colours:")
        for c in colour:
            print(c, end=' ')
        return True


if __name__ == '__main__':
    vertices = int(input("Enter number of vertices: "))
    g = Graph(vertices)

    print("Enter the adjacency matrix row by row:")
    for i in range(vertices):
        g.graph[i] = list(map(int, input().split()))

    m = int(input("Enter number of colors: "))

    g.graphColouring(m)
