from error_types import FileTypeError
from CSV.get_csv_processor import getCSVDataProcessor
from command_menu import displayCommandMenu
from file_helper import getFileType
from JSON.get_json_processor import getJSONDataProcessor

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
    elif fileType == 'json':
        return getJSONDataProcessor(fileName)
        
       
if __name__ == "__main__":
    main()