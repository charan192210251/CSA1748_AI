import heapq

class Graph:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.costs = [[1] * width for _ in range(height)]
        self.start = None
        self.goal = None

    def set_cost(self, x, y, cost):
        self.costs[y][x] = cost

    def set_start(self, x, y):
        self.start = (x, y)

    def set_goal(self, x, y):
        self.goal = (x, y)

    def heuristic(self, a, b):
        # Manhattan distance
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def neighbors(self, x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                yield (nx, ny)

    def a_star(self):
        start = self.start
        goal = self.goal

        open_set = []
        heapq.heappush(open_set, (0 + self.heuristic(start, goal), 0, start))
        came_from = {}
        cost_so_far = {start: 0}

        while open_set:
            _, current_cost, current = heapq.heappop(open_set)

            if current == goal:
                break

            for neighbor in self.neighbors(*current):
                new_cost = cost_so_far[current] + self.costs[neighbor[1]][neighbor[0]]
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (priority, new_cost, neighbor))
                    came_from[neighbor] = current

        path = []
        step = goal
        while step != start:
            path.append(step)
            step = came_from[step]
        path.append(start)
        path.reverse()
        return path

def main():
    # Hardcoded grid size
    width = 5
    height = 5

    g = Graph(width, height)

    # Hardcoded costs for each cell in the grid
    costs = [
        [1, 3, 1, 5, 2],
        [1, 1, 1, 1, 1],
        [4, 3, 1, 3, 4],
        [2, 1, 2, 1, 2],
        [3, 1, 1, 1, 1]
    ]

    # Set costs in the graph
    for y in range(height):
        for x in range(width):
            g.set_cost(x, y, costs[y][x])

    # Hardcoded start and goal coordinates
    start_x, start_y = 0, 0
    goal_x, goal_y = 4, 4

    g.set_start(start_x, start_y)
    g.set_goal(goal_x, goal_y)

    # Run A* algorithm
    path = g.a_star()

    print("Path found:")
    print(path)

if __name__ == '__main__':
    main()
