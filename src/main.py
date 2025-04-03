from dataHandler import DataHandler
from perceptron import Perceptron
from layer import Layer
import time
import os

ALPHA = 0.1
THRESHOLD = 0.5

def main():
    time.start = time.time()

    data = DataHandler.getLanguagesMapToListOfTexts("data")

    languages = data.keys()

    perceptrons = {}

    for language in languages:
        perceptron = Perceptron(THRESHOLD, ALPHA)
        perceptrons[language] = perceptron

    layer = Layer(perceptrons)

    layer.learn(data)

    for _ , _, filenames in os.walk('test'):
        for file in filenames:
            with open(f'test/{file}', 'r') as f:
                print(f'{file.ljust(40, "-")}> {layer.compute(DataHandler.changeCorrelationMapToList(DataHandler.getCorelationBetweenLettersInText(f.read())))}')

    print(f'Time taken: {round(time.time() - time.start, 3)}s')
if __name__ == "__main__":
    main()