# Implement a perceptron to learn the AND logic gate. 
# ( AND gate is Linearly separable and  Perfect for single layer perceptron)

import numpy as np

# Training data for AND gate
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 0, 0, 1])  # AND output

# Initialize weights and bias
weights = np.zeros(2)
bias = 0
learning_rate = 0.1

# Activation function
def step_function(x):
    return 1 if x >= 0 else 0

# Training
for epoch in range(10):
    for i in range(len(X)):
        linear_output = np.dot(X[i], weights) + bias
        y_pred = step_function(linear_output)
        error = y[i] - y_pred

        # Update rule
        weights += learning_rate * error * X[i]
        bias += learning_rate * error

print("Trained weights:", weights)
print("Trained bias:", bias)

# Testing
print("\nTesting AND gate:")
for i in range(len(X)):
    output = step_function(np.dot(X[i], weights) + bias)
    print(X[i], "->", output)
