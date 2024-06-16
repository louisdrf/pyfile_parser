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
    
    
   
    
def filter_on_strings_by_comparison(first_string_list, second_string_list, operation, case_sensitive=False):
    if len(first_string_list) != len(second_string_list):
        raise ValueError("Les listes doivent avoir la même longueur")
    
    if not case_sensitive:
        first_string_list = [string.lower() for string in first_string_list]
        second_string_list = [string.lower() for string in second_string_list]
    
    if operation == 1:  # first string before second one
        return [first for first, second in zip(first_string_list, second_string_list) if first < second]
    elif operation == 2:  # second string before first one
        return [first for first, second in zip(first_string_list, second_string_list) if first > second]
    elif operation == 3:  # first and second string have the same size
        return [first for first, second in zip(first_string_list, second_string_list) if len(first) == len(second)]
    
    
    

def filter_on_list(file_type, column, operation):
    if file_type == 'csv':
            column = [multiple_string_values_to_list(l) for l in column]

    if operation == 1:   # nombre d'élements
        number = int(input("Nombre voulu d'éléments dans chaque liste : "))        
        return [l for l in column if len(l) == number]

    elif operation == 2: # minimum
        minimum_elem = min(len(liste) for liste in column)
        return [l for l in column if len(l) == minimum_elem]

    elif operation == 3: # maximum
        maximum_elem = max(len(liste) for liste in column)
        return [l for l in column if len(l) == maximum_elem]

    

def filter_on_ints(number_list, operation):
    number_list = [float(val) for val in number_list]
    average = float(sum(number_list) / len(number_list))
    
    if operation == 1:   # moins que la moyenne
        return [number for number in number_list if number < average]

    elif operation == 2: # plus que la moyenne
        return [number for number in number_list if number > average]

    

def filter_on_ints_by_comparison(first_number_list, second_number_list, operation):
    first_number_list = [float(val) for val in first_number_list]
    second_number_list = [float(val) for val in second_number_list]

    if operation == 1:  # first number smaller than second one
        return [first for first, second in zip(first_number_list, second_number_list) if first < second]
    
    if operation == 2:  # first number bgger than second one
        return [first for first, second in zip(first_number_list, second_number_list) if first > second]
    
    if operation == 3:  # first number bigger than second one
        return [first for first, second in zip(first_number_list, second_number_list) if first == second]
        