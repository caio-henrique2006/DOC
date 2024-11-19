import numpy as np

class MLP:
    def __init__(self, num_inputs=3, num_hidden=[3, 5], num_outputs=2):
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.num_outputs = num_outputs
        layers = [self.num_inputs] + self.num_hidden + [self.num_outputs]

        # initiate random weigths:
        self.weights = []
        for i in range(len(layers)-1):
            w = np.random.rand(layers[i], layers[i+1])
            self.weights.append(w)

        # Activations
        activations = []
        for i in range(len(layers)):
            a = np.zeros(layers[i])
            activations.append(a)
        self.activations = activations

        # Derivatives
        derivatives = []
        for i in range(len(layers)-1):
            d = np.zeros((layers[i], layers[i+1]))
            derivatives.append(d)
        self.derivatives = derivatives
    
    def forward_propagate(self, inputs):
        activations = inputs
        self.activations[0] = inputs
        for i, w in enumerate(self.weights):
            # calculate net inputs
            net_inputs = np.dot(activations, w)
            # calculate the activations
            activations = self._sigmoid(net_inputs)
            self.activations[i+1] = activations
        return activations
    
    def back_propagate(self, error, verbose=False):
        for i in reversed(range(len(self.derivatives))):
            activations = self.activations[i+1]
            delta = error * self._sigmoid_derivative(activations)
            delta_reshaped = delta.reshape(delta.shape[0], -1).T
            current_activations = self.activations[i] 
            current_activations_reshaped = current_activations.reshape(current_activations.shape[0], -1)
            self.derivatives[i] = np.dot(current_activations_reshaped, delta_reshaped)
            error = np.dot(delta, self.weights[i].T)
            if (verbose):
                print(print("Derivatives for W{}: {}".format(i, self.derivatives[i])))
        return error
    
    def gradient_descent(self, learning_rate):
        for i in range(len(self.weights)):
            weights = self.weights[i]
            print("Original W{} {}".format(i, weights))
            derivatives = self.derivatives[i]
            weights += derivatives * learning_rate
            print("Updated W{} {}".format(i, weights))


    def _sigmoid_derivative(self, x):
        return x * (1.0 * x)

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

if __name__ == "__main__":
    # create an MLP
    mlp = MLP(2, [5], 1)
    
    # create inputs
    input = np.array([0.1, 0.2])
    target = np.array([0.3])

    # perform forward propagation
    output = mlp.forward_propagate(input)

    # calculate the error
    error = target - output

    # back propagation
    mlp.back_propagate(error)

    # Apply gradient descent
    mlp.gradient_descent(learning_rate=1)