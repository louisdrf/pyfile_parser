from file_helper import multiple_string_values_to_list

def filter_on_strings(string_list, value, operation, case_sensitive=False):
    if not case_sensitive:
        value_lower = value.lower()
        string_list = [string.lower() for string in string_list]
    else:
        value_lower = value
    
    if operation == "contains":
        return [string for string in string_list if value_lower in string.lower()]
    elif operation == "startswith":
        return [string for string in string_list if string.startswith(value_lower)]
    elif operation == "endswith":
        return [string for string in string_list if string.endswith(value_lower)]
    elif operation == "size":
        return [string for string in string_list if len(string) == len(value)]
    else:
        raise ValueError(f"Unknown operation: {operation}")
    

def filter_on_number_of_elements(column, number, file_type):
    if file_type == 'csv':
        column = [multiple_string_values_to_list(l) for l in column]

    return [val for val in column if len(val) == number]