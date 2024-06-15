from error_types import FileTypeError
from command_menu import displayCommandMenu
from file_helper import getFileType
from get_data_processor import get_data_processor

def main():
    try:
        fileName = input("Veuillez saisir un nom de fichier à analyser : ")
        displayCommandMenu(get_file_processor(fileName))
    except FileTypeError as e:
        print(f"Erreur : {e}")


def get_file_processor(file_name):
    file_type = getFileType(file_name)
    return get_data_processor(file_name, file_type)
        
       
if __name__ == "__main__":
    main()