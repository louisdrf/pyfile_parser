from CSVFileProcessor import CSVFileProcessor

def getCSVDataProcessor(fileName):
    try:
        with open(fileName, 'r', newline='', encoding='utf-8') as csvfile:
            file = CSVFileProcessor(csvfile)
            print(file.columns)
        return file
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fileName}' n'a pas été trouvé.")
    except IOError:
        print(f"Erreur : Problème de lecture du fichier '{fileName}'.")