from error_types import FileTypeError, NoExtensionError, UnsupportedFileTypeError

def main():
    try:
        fileName = input("Veuillez saisir un nom de fichier à analyser : ")
        parseFile(fileName)
        displayCommandMenu()
    except FileTypeError as e:
        print(f"Erreur : {e}")



def parseFile(fileName):
    fileType = getFileType(fileName)
    if fileType == None:
        return
    if fileType == 'csv':
        parseCSV(fileName)
    elif fileType == 'json':
        parseJSON(fileName)
        
    
def displayCommandMenu():
    print("Option 1 : ")
    print("Option 2 : ")
    
    
def getFileType(fileName):
    if '.' not in fileName:
        raise NoExtensionError("Le fichier n'a pas d'extension.")
    fileType = fileName.split('.')[-1]
    if fileType not in ['csv', 'json']:
        raise UnsupportedFileTypeError(f"Le type de fichier '{fileType}' n'est pas pris en charge.")
    return fileType


def parseJSON(fileName):
    print("parse JSON")
    
def parseCSV(fileName):
    print("parse CSV")
    
    
if __name__ == "__main__":
    main()