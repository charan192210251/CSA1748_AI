def create_board():
    return [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]


def place_player(board, player, row, col):
    if board[row][col] == 0:
        board[row][col] = player
        return True
    else:
        print("That position is already taken. Try again.")
        return False


def row_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    return False


def col_win(board, player):
    for col in range(len(board)):
        if all([board[row][col] == player for row in range(len(board))]):
            return True
    return False


def diag_win(board, player):
    if all([board[i][i] == player for i in range(len(board))]) or all([board[i][len(board) - 1 - i] == player for i in range(len(board))]):
        return True
    return False


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if all([cell != 0 for row in board for cell in row]) and winner == 0:
        winner = -1  # Tie game
    return winner


def play_game():
    board, winner, counter = create_board(), 0, 1
    print("Initial board:")
    for row in board:
        print(row)

    while winner == 0:
        for player in [1, 2]:
            valid_move = False
            while not valid_move:
                try:
                    print(f"\nPlayer {player}'s turn")
                    row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
                    col = int(input(f"Player {player}, enter column (0, 1, or 2): "))

                    if row not in range(3) or col not in range(3):
                        print("Invalid input. Please enter numbers between 0 and 2.")
                    else:
                        valid_move = place_player(board, player, row, col)

                except ValueError:
                    print("Invalid input. Please enter numbers only.")

            print(f"\nBoard after move {counter}:")
            for row in board:
                print(row)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break

    return winner


if __name__ == "__main__":
    print("Welcome to the Tic-Tac-Toe game!")
    result = play_game()

    if result == -1:
        print("It's a tie!")
    else:
        print(f"Winner is Player {result}!")
