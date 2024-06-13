from CSVFile import CSVFile

def parseCSV(fileName):
    try:
        with open(fileName, 'r', newline='', encoding='utf-8') as csvfile:
            file = CSVFile(csvfile)
            file.setReader()
            file.getColumnDataByName('pokedex_number')
        return file
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fileName}' n'a pas été trouvé.")
    except IOError:
        print(f"Erreur : Problème de lecture du fichier '{fileName}'.")