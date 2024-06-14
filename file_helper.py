from error_types import NoExtensionError, UnsupportedFileTypeError

  
def getFileType(fileName):
    if '.' not in fileName:
        raise NoExtensionError("Le fichier n'a pas d'extension.")
    
    fileType = fileName.split('.')[-1]
    if fileType not in ['csv', 'json']:
        raise UnsupportedFileTypeError(f"Le type de fichier '{fileType}' n'est pas pris en charge.")
    return fileType

def get_data_type(column):
    if all(elem in {'0', '1'} for elem in column[:10]):
        if all(elem in {'0', '1'} for elem in column):
            return bool
        
    elif column[0].isdigit():
        return int
    
    elif column[0].lower() in ['true', 'false']:
        return bool
