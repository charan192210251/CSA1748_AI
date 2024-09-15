class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        self.colors_list = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink"]  # List of possible colors

    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    def graphColourUtil(self, m, colour, v):
        if v == self.V:
            return True
        for c in range(m):
            if self.isSafe(v, colour, c):
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1):
                    return True
                colour[v] = -1  # Reset the color if it doesn't work

    def graphColouring(self, m):
        colour = [-1] * self.V  # -1 indicates no color assigned yet
        if not self.graphColourUtil(m, colour, 0):
            print("Solution does not exist.")
            return False
        print("Solution exists and the following are the assigned colours:")
        for c in colour:
            print(self.colors_list[c], end=' ')
        print()
        return True

if __name__ == '__main__':
    # Hardcoded number of vertices
    vertices = 4
    g = Graph(vertices)

    # Hardcoded adjacency matrix
    g.graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]

    # Hardcoded number of colors (use as many colors as available in the colors_list)
    m = 3

    g.graphColouring(m)
