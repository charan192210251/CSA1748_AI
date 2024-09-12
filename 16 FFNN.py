import numpy as np

def relu(n):
    return max(0, n)

def feedforward(input_data, weights):
    node0 = relu(np.dot(input_data, weights[0]))
    node1 = relu(np.dot(input_data, weights[1]))
    node2 = relu(np.dot(np.array([node0, node1]), weights[2]))
    node3 = relu(np.dot(np.array([node0, node1]), weights[3]))
    output = relu(np.dot(np.array([node2, node3]), weights[4]))
    return output

# User input for the number of inputs and weights
num_inputs = int(input("Enter the number of input samples: "))
input_size = int(input("Enter the size of each input sample: "))

# Input data from user
inp = []
print("Enter the input samples (space-separated):")
for i in range(num_inputs):
    inp.append(list(map(float, input(f"Input {i+1}: ").split())))

inp = np.array(inp)

# Weights input
weights = []
print("\nEnter weights for each layer node (space-separated for each weight vector):")
for i in range(5):
    weights.append(np.array(list(map(float, input(f"Weights for node {i}: ").split()))))

# Feedforward process
print("\nFeed Forward Neural Network Output:")
for x in inp:
    output = feedforward(x, weights)
    print(f"Input: {x}, Output: {output}")
