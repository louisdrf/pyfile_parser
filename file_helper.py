from error_types import NoExtensionError, UnsupportedFileTypeError

  
def getFileType(fileName):
    if '.' not in fileName:
        raise NoExtensionError("Le fichier n'a pas d'extension.")
    
    fileType = fileName.split('.')[-1]
    if fileType not in ['csv', 'json']:
        raise UnsupportedFileTypeError(f"Le type de fichier '{fileType}' n'est pas pris en charge.")
    return fileType

def getDataType(value):
    if value.isdigit():
        return int
    elif value.lower() in ['true', 'false']:
        return bool
