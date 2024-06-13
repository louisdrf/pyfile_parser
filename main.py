from error_types import FileTypeError
from CSV_parser import getCSVDataProcessor
from command_menu import displayCommandMenu
from file_helper import getFileType


def main():
    try:
        fileName = input("Veuillez saisir un nom de fichier à analyser : ")
        parseFile(fileName)
        displayCommandMenu()
    except FileTypeError as e:
        print(f"Erreur : {e}")


def parseFile(fileName):
    fileType = getFileType(fileName)
    if fileType == 'csv':
        CSVDataProcessor = getCSVDataProcessor(fileName)
        columnName = input('nom de col : ')
        print(CSVDataProcessor.getColumnDataByName(columnName))
    #elif fileType == 'json':
        #parseJSON(fileName)
        
       
if __name__ == "__main__":
    main()