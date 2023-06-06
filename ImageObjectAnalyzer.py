# The class used to interact with the doi module
# Attributes:
#   folder_path: The path to the folder containing the images or videos
#   keywords: The keywords to check for in the images or videos

import os
from Helper import *

class ImageObjectAnalyzer:
    def __init__(self, keywords) -> None:
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
    
    def analyzeImages(self, folder_path):
        command = 'python doi/doi.py detect ' + folder_path + ' --classes ' + self.getKeywords() + '--nogpu'
        os.system(command)