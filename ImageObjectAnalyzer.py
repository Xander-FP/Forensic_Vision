# The class used to interact with the doi module
# Attributes:
#   folder_path: The path to the folder containing the images or videos
#   keywords: The keywords to check for in the images or videos

import os

class ImageObjectAnalyzer:
    def __init__(self, folder_path) -> None:
        self.__folder_path = folder_path
        self.__keywords = []

    def __init__(self, folder_path, keywords) -> None:
        self.__folder_path = folder_path
        self.__keywords = keywords

    def addKeyword(self, keyword):
        self.__keywords.append(keyword)

    def removeKeyword(self, keyword):
        self.__keywords.remove(keyword)

    def getKeywords(self):
        res = ''
        for keyword in self.__keywords:
            # Check if keyword has spaces
            if ' ' in keyword:
                keyword = '"' + keyword + '"'
            res += keyword + ' '
        return res
    
    def analyzeImages(self):
        command = 'python doi/doi.py detect ' + self.__folder_path + ' --classes ' + self.getKeywords() + '--nogpu'
        print(command)
        os.system(command)