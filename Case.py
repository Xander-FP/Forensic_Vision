# The class used to keep track of all the information for analysing the images or videos in a case
# Attributes:

from Helper import isTrue
from ImageObjectAnalyzer import ImageObjectAnalyzer
from FakeImageDetector import FakeImageDetector
from PreProcessor import PreProcessor
import os

class Case:
    def __init__(self,name) -> None:
        self.__name = name
        self.__flag_object = isTrue(input("Do you want to perform object detection? (y/n): "))
        self.__flag_fake = isTrue(input("Do you want to perform image tampering analysis? (y/n): "))
        self.__initModules()

    def analyzeImages(self, folder_path):
        # Check if the folder path is valid
        if not os.path.isdir(folder_path):
            print('Invalid directory path: ' + os.path.abspath(folder_path))
            return
        
        # Prepare the images
        pre_processor = PreProcessor()
        processed_path = pre_processor.convertToJpeg(folder_path)

        # Perform the analysis
        if self.__flag_object:
            self.__object_analyzer.analyzeImages(processed_path)

        if self.__flag_object and self.__flag_fake:
            # Get user input to determine on what folder to perform the analysis
            print('Do you want to perform tamper analysis on all the images or only on the identified images?')
            print('1. All the images')
            print('2. Identified images')
            print('skip')
            choice = input('Enter your choice: ')
            if choice == '1':
                self.__fake_detector.analyzeImages(processed_path)
            elif choice == '2':
                self.__fake_detector.analyzeImages('results')
        
        if self.__flag_fake:
            self.__fake_detector.analyzeImages(processed_path)
        
        # Clean up the processed images
        pre_processor.cleanUp()

    def __initModules(self):
        if self.__flag_object:
            # Get input from user for the object analyzer
            keywords = input("Enter the keywords to check (comma seperated): ").split(",")
            keywords = [keyword.strip() for keyword in keywords]
            self.__object_analyzer = ImageObjectAnalyzer(keywords=keywords)
        if self.__flag_fake:
            # Get input from user for the 
            self.__fake_detector = FakeImageDetector()
            pass