from CSV.CSVFileProcessor import CSVFileProcessor
from JSON.JSONFileProcessor import JSONFileProcessor

def get_data_processor(file_name, file_type):
    try:
        if file_type == 'csv':
            with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
                return CSVFileProcessor(csvfile)
        elif file_type == 'json':
            with open(file_name, 'r', encoding='utf-8') as jsonfile:
                return JSONFileProcessor(jsonfile)
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_name}' n'a pas été trouvé.")
    except IOError:
        print(f"Erreur : Problème de lecture du fichier '{file_name}'.")