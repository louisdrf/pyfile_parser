from error_types import NoExtensionError, UnsupportedFileTypeError
  
def getFileType(file_name):
    if '.' not in file_name:
        raise NoExtensionError("Le fichier n'a pas d'extension.")
    
    file_type = file_name.split('.')[-1]
    if file_type not in ['csv', 'json']:
        raise UnsupportedFileTypeError(f"Le type de fichier '{file_type}' n'est pas pris en charge.")
    return file_type


def get_data_type(column):
    if is_list(column[0]): 
            return list 
        
    elif all(elem in {'0', '1'} for elem in column[:10]):
        if all(elem in {'0', '1'} for elem in column):
            return bool
        
    elif column[0].isdigit():
        return int
    
    elif column[0].lower() in ['true', 'false']:
        return bool


def is_list(value): 
    if '\n' in value or ',' in value or ';' in value or (value.startswith("[") and value.endswith("]")):
        return True
    return False


def multiple_string_values_to_list(value):
    try:
        value = eval(value)
    except (ValueError, SyntaxError):
        pass
    
    if '\n' in value:
        value = value.split('\n')
        
    if ',' in value:
        value = value.split(',')

    return value
