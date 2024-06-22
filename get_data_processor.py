import sys
from file_processors.CSVFileProcessor import CSVFileProcessor
from file_processors.JSONFileProcessor import JSONFileProcessor

def get_data_processor(file_name, file_type):
    try:
        if file_type == 'csv':
            with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
                return CSVFileProcessor(file_name, csvfile)
        elif file_type == 'json':
            with open(file_name, 'r', encoding='utf-8') as jsonfile:
                return JSONFileProcessor(file_name, jsonfile)
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_name}' n'a pas été trouvé.")
        sys.exit(1)
    except IOError:
        print(f"Erreur : Problème de lecture du fichier '{file_name}'.")
        sys.exit(1)