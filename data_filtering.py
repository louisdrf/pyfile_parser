from file_helper import multiple_string_values_to_list

def filter_on_strings_by_search(string_list, value, operation, case_sensitive=False):
    if not case_sensitive:
        value_lower = value.lower()
        string_list = [string.lower() for string in string_list]
    else:
        value_lower = value
    
    if operation == 1:   # contains
        return [string for string in string_list if value_lower in string.lower()]
    elif operation == 2: # startswith
        return [string for string in string_list if string.startswith(value_lower)]
    elif operation == 3: # endswith
        return [string for string in string_list if string.endswith(value_lower)]
    elif operation == 4: # size
        return [string for string in string_list if len(string) == len(value)]        
    else:
        raise ValueError(f"Unknown operation: {operation}")
    
    
    
    
def filter_on_strings_by_comparison(first_string_list, second_string_list, operation):
    return None
    
    
    
    

def filter_on_list(file_type, column, operation):
    if file_type == 'csv':
            column = [multiple_string_values_to_list(l) for l in column]

    if operation == 1: # nombre d'élements
        number = int(input("Nombre voulu d'éléments dans chaque liste : "))        
        return [l for l in column if len(l) == number]

    elif operation == 2: # minimum
        minimum_elem = min(len(liste) for liste in column)
        return [l for l in column if len(l) == minimum_elem]

    elif operation == 3: # maximum
        maximum_elem = max(len(liste) for liste in column)
        return [l for l in column if len(l) == maximum_elem]