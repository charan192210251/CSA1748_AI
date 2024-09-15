def relu(n):
    return max(0, n)

def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

def feedforward(input_data, weights):
    # Compute activations for each layer
    node0 = relu(dot_product(input_data, weights[0]))
    node1 = relu(dot_product(input_data, weights[1]))
    node2 = relu(dot_product([node0, node1], weights[2]))
    node3 = relu(dot_product([node0, node1], weights[3]))
    output = relu(dot_product([node2, node3], weights[4]))
    return output

def main():
    # Hardcoded input samples
    inp = [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0]
    ]

    # Hardcoded weights for each layer
    weights = [
        [0.1, 0.2, 0.3],  # Weights for node0
        [0.4, 0.5, 0.6],  # Weights for node1
        [0.7, 0.8],       # Weights for node2
        [0.9, 1.0],       # Weights for node3
        [1.1, 1.2]        # Weights for output
    ]

    # Feedforward process
    print("\nFeed Forward Neural Network Output:")
    for x in inp:
        output = feedforward(x, weights)
        print(f"Input: {x}, Output: {output}")

if __name__ == "__main__":
    main()
