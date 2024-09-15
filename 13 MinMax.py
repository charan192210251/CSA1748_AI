import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # Base case: if the current depth is the target depth, return the score at this node
    if curDepth == targetDepth:
        return scores[nodeIndex]

    # If it's the maximizing player's turn
    if maxTurn:
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    # If it's the minimizing player's turn
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))

def main():
    # Hardcoded leaf node scores
    scores = [3, 5, 6,9,1,2,0,4]  # Example leaf scores

    # Calculate the depth of the game tree
    treeDepth = int(math.log(len(scores), 2))

    # Start the minimax algorithm from depth 0 and index 0 with maximizing player's turn
    optimal_value = minimax(0, 0, True, scores, treeDepth)

    # Print the result
    print("The optimal value is:", optimal_value)

if __name__ == "__main__":
    main()
