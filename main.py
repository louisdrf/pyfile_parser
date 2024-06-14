from error_types import FileTypeError
from CSV_parser import getCSVDataProcessor
from command_menu import displayCommandMenu
from file_helper import getFileType


def main():
    try:
        fileName = input("Veuillez saisir un nom de fichier à analyser : ")
        displayCommandMenu(get_file_processor(fileName))
    except FileTypeError as e:
        print(f"Erreur : {e}")


def get_file_processor(fileName):
    fileType = getFileType(fileName)
    if fileType == 'csv':
        return getCSVDataProcessor(fileName)
        
    #elif fileType == 'json':
        #parseJSON(fileName)
        
       
if __name__ == "__main__":
    main()