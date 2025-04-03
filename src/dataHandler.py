import os
import string

class DataHandler:
    @staticmethod
    def getLanguagesMapToListOfTexts(path: str):
        languagesTextMap = {}

        for dir in os.listdir(path):
            languagesTextMap[dir] = []
            for file in os.listdir(f"{path}/{dir}"):
                with open(f"{path}/{dir}/{file}", "r") as f:
                    languagesTextMap[dir].append(f.read().strip().replace("\n", " ").lower())

        return languagesTextMap
    @staticmethod
    def getCorelationBetweenLettersInText(text: str):
        lettersCount = sum([1 for x in text if x in string.ascii_lowercase])
        return {x : text.count(x) / lettersCount * 100 for x in string.ascii_lowercase} 
    @staticmethod
    def changeCorrelationMapToList(correlationMap: dict):
        return [correlationMap[x] for x in string.ascii_lowercase]

    @staticmethod
    def normalizeVector(vector):
        vectorLength = sum([x**2 for x in vector ]) ** 0.5
        return [x / vectorLength for x in vector]
    
    @staticmethod
    def scalarProduct(a, b):
        return sum(x * y for x,y in zip(a,b))       
    
    

