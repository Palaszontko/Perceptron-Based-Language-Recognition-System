import random

WEIGHTS_SIZE = 26

class Perceptron:
    def __init__(self, threshold, alpha):
        self.threshold = threshold
        self.alpha = alpha
        self.setRandomWeightsAndthreshold(WEIGHTS_SIZE)
        
    def calculateNet(self, input):
        net = 0
        for i in range(len(input)):
            net += input[i] * self.weights[i]
        return net - self.threshold
    
    def setRandomWeightsAndthreshold(self, weightsSize : int):
        'Set random weights and threshold'
        self.weights = [random.uniform(-5,5) for _ in range(weightsSize)]
        self.threshold = random.uniform(-5,5)
    
    def compute(self, input):
        net = self.calculateNet(input)
        if net >= 0:
            return 1
        else:
            return 0
        
    def learn(self, input, decision, y):
        'Delta rule'
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + (decision - y) * self.alpha * input[i]

        self.threshold = self.threshold - (decision - y) * self.alpha

    def getWeights(self):
        return self.weights

    def __str__(self):
        return f"Perceptron(threshold={self.threshold}, alpha={self.alpha}, weights={self.weights})"