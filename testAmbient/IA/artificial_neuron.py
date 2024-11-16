import math

def sigmoid(x):
    y = 1.0 / (1 + math.exp(-x))
    return y

def activate(inputs, weigths):
    # perform net input
    h = 0
    for x, w in zip(inputs, weigths):
        h += x*w
    
    # Activation
    return sigmoid(h)

if __name__ == "__main__":
    inputs = [.5, .3, .2]
    weigths = [.4, .7, .2]
    output = activate(inputs, weigths)
    print(output)