import math

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def activate(self, inputs):
        z = sum(w * i for w, i in zip(self.weights, inputs)) + self.bias
        return 1 / (1 + math.exp(-z))  # Sigmoid activation
        
class NeuralNetwork:
    def __init__(self):
        self.layers = []

    def add_layer(self, neurons):
        self.layers.append(neurons)

    def forward(self, inputs):
        for layer in self.layers:
            outputs = []
            for neuron in layer:
                output = neuron.activate(inputs)
                outputs.append(output)
            inputs = outputs
        return inputs
    
# Example usage:
if __name__ == "__main__":
    nn = NeuralNetwork()
    nn.add_layer([Neuron([0.2, 0.8], 0.5), Neuron([0.5, 0.1], -0.3)])
    nn.add_layer([Neuron([0.3, 0.7], 0.1)])

    input_data = [1.0, 0.5]
    output = nn.forward(input_data)
    print("Network output:", output)