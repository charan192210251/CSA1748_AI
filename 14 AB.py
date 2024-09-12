MAX, MIN = 1000, -1000


def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Base case: return the value at the leaf node
    if depth == 3:
        return values[nodeIndex]

        # Maximizing player's turn
    if maximizingPlayer:
        best = MIN
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

        # Minimizing player's turn
    else:
        best = MAX
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


if __name__ == "__main__":
    # Taking user input for the leaf node values
    values_input = input("Enter the leaf node values separated by spaces: ")

    # Convert the input string into a list of integers
    values = list(map(int, values_input.split()))

    # Ensure the user entered 8 values (for a depth-3 binary tree)
    if len(values) != 8:
        print("Please enter exactly 8 values.")
    else:
        # Calculate the optimal value using the minimax algorithm with alpha-beta pruning
        print("The optimal value is:", minimax(0, 0, True, values, MIN, MAX))
