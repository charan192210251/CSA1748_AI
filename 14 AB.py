MAX, MIN = 1000, -1000

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Base case: return the value at the leaf node
    if depth == 3:
        return values[nodeIndex]

    # Maximizing player's turn
    if maximizingPlayer:
        best = MIN
        for i in range(2):  # Iterate over 0 and 1
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    # Minimizing player's turn
    else:
        best = MAX
        for i in range(2):  # Iterate over 0 and 1
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

def main():
    # Hardcoded leaf node values
    values = [3, 5, 6,9,1,2,0,4]  # Example leaf values

    # Ensure there are exactly 8 values (for a depth-3 binary tree)
    if len(values) != 8:
        print("Please provide exactly 8 values.")
    else:
        # Calculate the optimal value using the minimax algorithm with alpha-beta pruning
        optimal_value = minimax(0, 0, True, values, MIN, MAX)
        print("The optimal value is:", optimal_value)

if __name__ == "__main__":
    main()
