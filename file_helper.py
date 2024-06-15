from error_types import NoExtensionError, UnsupportedFileTypeError
  
def getFileType(file_name):
    if '.' not in file_name:
        raise NoExtensionError("Le fichier n'a pas d'extension.")
    
    file_type = file_name.split('.')[-1]
    if file_type not in ['csv', 'json']:
        raise UnsupportedFileTypeError(f"Le type de fichier '{file_type}' n'est pas pris en charge.")
    return file_type


def get_json_data_type(value):
    if isinstance(value, str):
        return str
    elif isinstance(value, bool):
        return bool
    elif isinstance(value, int):
        return int
    elif isinstance(value, float):
        return float
    elif isinstance(value, list):
        return list
    else:
        pass


def get_data_type(column):
    if is_list(column[0]): 
        return list 
        
    elif column[0].lower() in ['true', 'false']:
        return bool

    elif all(elem in {'0', '1'} for elem in column):
        return bool
        
    elif column[0].isdigit() or is_float(column[0]):
        return int


def is_list(value): 
    if '\n' in value or ',' in value or ';' in value or (value.startswith("[") and value.endswith("]")):
        return True
    return False


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def convert_to_boolean(value):
    if value in {"true", "1"}:
        return True
    elif value in {"false", "0"}:
        return False
    else:
        raise ValueError(f"Cannot convert value '{value}' to boolean")


def multiple_string_values_to_list(value):
    try:
        value = eval(value)
    except (ValueError, SyntaxError):
        pass
    
    separators = [',' , ';', ':', '\n']
    for sep in separators:
        if sep in value:
            value = value.split(sep)

    return value
