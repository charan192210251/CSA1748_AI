import numpy as np


def create_board():
    return np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])


def place_player(board, player, row, col):
    if board[row, col] == 0:
        board[row, col] = player
        return True
    else:
        print("That position is already taken. Try again.")
        return False


def row_win(board, player):
    for row in board:
        if np.all(row == player):
            return True
    return False


def col_win(board, player):
    for col in range(len(board)):
        if np.all(board[:, col] == player):
            return True
    return False


def diag_win(board, player):
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1  # Tie game
    return winner


def play_game():
    board, winner, counter = create_board(), 0, 1
    print("Initial board:")
    print(board)

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
            print(board)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break

    return winner


if __name__ == '__main__':
    print("Welcome to the Tic-Tac-Toe game!")
    result = play_game()

    if result == -1:
        print("It's a tie!")
    else:
        print(f"Winner is Player {result}!")
