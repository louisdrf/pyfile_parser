import csv

def parseCSV(fileName):
    try:
        with open(fileName, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            content = [row for row in reader]
        return content
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fileName}' n'a pas été trouvé.")
    except IOError:
        print(f"Erreur : Problème de lecture du fichier '{fileName}'.")