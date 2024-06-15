from JSON.JSONFileProcessor import JSONFileProcessor

def getJSONDataProcessor(fileName):
    try:
        with open(fileName, 'r', encoding='utf-8') as jsonfile:
            file = JSONFileProcessor(jsonfile)
        return file
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fileName}' n'a pas été trouvé.")
    except IOError:
        print(f"Erreur : Problème de lecture du fichier '{fileName}'.")