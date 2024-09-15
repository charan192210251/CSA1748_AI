from collections import deque


def is_valid_state(m, c, b, m_total, c_total):
    """ Check if the state is valid """
    if m < 0 or c < 0 or m > m_total or c > c_total:
        return False
    if m > 0 and m < c:
        return False
    if (m_total - m) > 0 and (m_total - m) < (c_total - c):
        return False
    return True


def get_possible_moves(state, m_total, c_total):
    """ Generate possible moves from the current state """
    m, c, b = state
    if b == 1:  # Boat on the left side
        moves = [
            (m - 2, c, 0),  # 2 missionaries
            (m - 1, c - 1, 0),  # 1 missionary and 1 cannibal
            (m, c - 2, 0),  # 2 cannibals
            (m - 1, c, 0),  # 1 missionary
            (m, c - 1, 0)  # 1 cannibal
        ]
    else:  # Boat on the right side
        moves = [
            (m + 2, c, 1),  # 2 missionaries
            (m + 1, c + 1, 1),  # 1 missionary and 1 cannibal
            (m, c + 2, 1),  # 2 cannibals
            (m + 1, c, 1),  # 1 missionary
            (m, c + 1, 1)  # 1 cannibal
        ]
    return [(new_m, new_c, new_b) for new_m, new_c, new_b in moves if
            is_valid_state(new_m, new_c, new_b, m_total, c_total)]


def bfs(m_total, c_total):
    """ Breadth-First Search to solve the Missionaries and Cannibals problem """
    initial_state = (m_total, c_total, 1)
    goal_state = (0, 0, 0)
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        (state, path) = queue.popleft()
        if state == goal_state:
            print("You Win!")
            return path + [state]

        if state in visited:
            continue

        visited.add(state)
        for move in get_possible_moves(state, m_total, c_total):
            queue.append((move, path + [state]))

    return None


def main():
    m_total = int(input("Enter the number of missionaries: "))
    c_total = int(input("Enter the number of cannibals: "))

    if m_total < 1 or c_total < 1:
        print("The number of missionaries and cannibals must be at least 1.")
        return

    solution = bfs(m_total, c_total)
    if solution:
        print("Solution found:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
print("You win the game !!!")
