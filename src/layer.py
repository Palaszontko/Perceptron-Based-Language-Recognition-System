from dataHandler import DataHandler
import random

EPOCHES = 1000

class Layer:
    def __init__(self, perceptrons):
        self.perceptrons = perceptrons

    def learn(self, trainingSet):
        trainingSet = {lang: [DataHandler.changeCorrelationMapToList(DataHandler.getCorelationBetweenLettersInText(text)) for text in texts] for lang, texts in trainingSet.items()}
        
        for i in range(EPOCHES):
            for langPerceptron, perceptron in self.perceptrons.items():   
                random.shuffle(trainingSet[langPerceptron])
                for langText, texts in trainingSet.items():
                    for text in texts:
                        y = perceptron.compute(text)
                        decison = 1 if langPerceptron == langText else 0 
                        perceptron.learn(text, decison, y)

    def compute(self, input):
        results = {}
        normalizedInput = DataHandler.normalizeVector(input)

        for lang, perceptron in self.perceptrons.items():
            normalizedWeights = DataHandler.normalizeVector(perceptron.getWeights())
            results[lang] = DataHandler.scalarProduct(normalizedInput, normalizedWeights)    
        return max(results, key=results.get)

    
    def __str__(self):
        result = ""
        for language, perceptron in self.perceptrons.items():
            result += f"{language}: {perceptron}"
        


