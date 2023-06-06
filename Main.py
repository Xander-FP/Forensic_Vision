from Case import Case
from Helper import isTrue

def main():
    print()
    print("Welcome to the Image Analysis Tool")
    name = input("Enter the name of the case: ")
    folder = input("Enter the path to the folder with the images to analyze: ")
    case = Case(name)
    case.analyzeImages(folder)
    store = isTrue(input("Do you want to store the results? (y/n): "))
    

if __name__ == "__main__":
    main()