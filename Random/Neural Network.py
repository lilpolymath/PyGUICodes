"""
Teaching Math Using Neural Network
This program teaches a computer to predict the output
of a mathematical expression, without knowing
the exact formula.
The Formula is 2(a + b)
"""

from numpy import random, dot, array

class neural_network:
    def __init__(self):
        random.seed(1)
        # We model a single neuron, with 3 inputs and 1 output
        # and assign random weight
        self.weights = 2 * random.random((2, 1)) - 1

    def train(self, inputs, outputs, num):
        for iteration in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = 0.01*dot(inputs.T, error)
            self.weights += adjustment

    def think(self, inputs):
        return dot(inputs, self.weights)


neural_network = neural_network()

# The Training Set
inputs = array([[2, 3], [1, 1], [5, 2], [12, 3]])
outputs = array([[10, 4, 14, 30]]).T

# Training the Neural Network using the Training Set
neural_network.train(inputs, outputs, 1000)

# Ask the Neural Network the Output
print(neural_network.think(array([99, 1])))

