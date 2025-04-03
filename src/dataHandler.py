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



    
    

