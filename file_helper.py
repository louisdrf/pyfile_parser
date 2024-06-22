import csv
import json
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
    elif isinstance(value, int) or isinstance(value, float):
        return int
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

    else:
        return str


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
    if value in {"true", "1", True}:
        return True
    elif value in {"false", "0", False}:
        return False
    else:
        raise ValueError(f"Cannot convert value '{value}' to boolean")



def multiple_string_values_to_float(string_floats_list):
    return [float(num) for num in string_floats_list if num.strip().replace('.', '', 1).isdigit()]


def multiple_string_values_to_boolean(string_booleans_list):
    return [convert_to_boolean(string_bool) for string_bool in string_booleans_list]


def toList(separated_values):
    if isinstance(separated_values, list):
        return separated_values
    
    try:
        value = eval(separated_values)
    except (ValueError, SyntaxError):
        pass
    
    separators = [',' , ';', ':', '\n']
    for sep in separators:
        if sep in value:
            value = value.split(sep)

    return value


def get_average_list_size(lists):
    lists_size = [len(l) for l in lists]
    number_of_lists = len(lists)
    total_lists_size = sum(lists_size)
    
    return float(total_lists_size / number_of_lists)


def save_result_into_file(file_name, file_type, result_list):
    fieldnames = result_list[0].keys()

    if file_type == 1: # CSV
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for row in result_list:
                writer.writerow(row)

    elif file_type == 2: # Json
            with open(file_name, 'w') as jsonfile:
                json.dump(result_list, jsonfile, indent=4)
    
    print(f"Data has been saved to {file_name}")