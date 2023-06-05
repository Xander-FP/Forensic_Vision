# The class used to keep track of all the information for analysing the images or videos in a case
# Attributes:

from Helper import isTrue
from ImageObjectAnalyzer import ImageObjectAnalyzer
# from ImageIntegrityAnalyzer import ImageIntegrityAnalyzer

class Case:
    def __init__(self) -> None:
        self.__flag_object = isTrue(input("Do you want to perform object detection? (y/n): "))
        self.__flag_integrity = isTrue(input("Do you want to perform image integrity analysis? (y/n): "))
        self.__initModules()

    def analyzeImages(self):
        if self.__flag_integrity:
            # perform integrity analysis
            pass
        if self.__flag_object:
            self.__object_analyzer.analyzeImages()

    def analyzeVideos(self):
        pass

    def __initModules(self):
        if self.__flag_object:
            # Get input from user for the object analyzer
            folder_path = input("Enter the path to the folder with the images: ")
            keywords = input("Enter the keywords to check (comma seperated): ").split(",")
            keywords = [keyword.strip() for keyword in keywords]
            self.__object_analyzer = ImageObjectAnalyzer(folder_path=folder_path, keywords=keywords)
        if self.__flag_integrity:
            # Get input from user for the integrity analyzer
            # self.__integrity_analyzer = ImageIntegrityAnalyzer()
            pass