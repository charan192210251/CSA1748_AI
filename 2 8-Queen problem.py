def attack(i, j, N, board):
    for k in range(0, N):
        if board[i][k] == 'Q' or board[k][j] == 'Q':
            return True
    # Checking diagonally
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 'Q':
                    return True
    return False


def N_queens(n, N, board):
    if n == 0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            if (not attack(i, j, N, board)) and (board[i][j] != 'Q'):
                board[i][j] = 'Q'
                if N_queens(n - 1, N, board):
                    return True
                board[i][j] = 0
    return False


def user_input():
    N = int(input("Enter the size of the board (N x N): "))
    board = [[0] * N for _ in range(N)]

    print(f"Placing {N} queens on the {N}x{N} board...\n")

    if N_queens(N, N, board):
        print("Solution found:")
        for row in board:
            print(' '.join(['Q' if cell == 'Q' else '.' for cell in row]))
    else:
        print("No solution exists.")


# Call the function to take user input and solve the problem
user_input()
