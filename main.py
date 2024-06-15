from error_types import FileTypeError
from command_menu import prompt_user
from file_helper import getFileType
from get_data_processor import get_data_processor

def main():
    try:
        filename = input("Veuillez saisir un nom de fichier à analyser : ")
        file_processor = get_file_processor(filename)
        prompt_user(file_processor)

    except FileTypeError as e:
        print(f"Erreur : {e}")


def get_file_processor(file_name):
    file_type = getFileType(file_name)
    return get_data_processor(file_name, file_type)
        
       
if __name__ == "__main__":
    main()