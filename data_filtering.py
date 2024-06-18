from file_helper import multiple_string_values_to_list

def filter_on_strings_by_search(file_processor, column_name, operation):
    value_to_compare_wtih = input("Mot à utiliser pour filtrer : ")
    
    if operation == 1:   # contains
        return [row for row in file_processor.content if value_to_compare_wtih in row[column_name]]
    elif operation == 2: # startswith
        return [row for row in file_processor.content if row[column_name].startswith(value_to_compare_wtih)]
    elif operation == 3: # endswith
        return [row for row in file_processor.content if row[column_name].endswith(value_to_compare_wtih)]
    elif operation == 4: # size
        return [row for row in file_processor.content if len(row[column_name]) == len(value_to_compare_wtih)]        
    
    
   
    
def filter_on_strings_by_comparison(file_processor, first_column_name, second_column_name, operation):
    first_column_data = file_processor.getColumnDataByName(first_column_name)
    second_column_data = file_processor.getColumnDataByName(second_column_name)
    
    if len(first_column_data) != len(second_column_data):
        raise ValueError("Les listes à comparer doivent avoir la même longueur.")

    if operation == 1:  # first string before second one
        return [row for row in file_processor.content if row[first_column_name] < row[second_column_name]]
    elif operation == 2:  # second string before first one
        return [row for row in file_processor.content if row[first_column_name] > row[second_column_name]]
    elif operation == 3:  # first and second string have the same size
        return [row for row in file_processor.content if len(row[first_column_name]) == len(row[second_column_name])]
    


    
    
def filter_on_list(file_processor, column_name, operation):
    column_data = file_processor.getColumnDataByName(column_name)
    if file_processor.type == 'csv':
            column_data = [multiple_string_values_to_list(l) for l in column_data]

    if operation == 1:   # nombre d'élements
        number = int(input("Nombre voulu d'éléments dans chaque liste : "))        
        return [l for l in column_data if len(l) == number]

    elif operation == 2: # minimum
        minimum_elem = min(len(liste) for liste in column_data)
        return [l for l in column_data if len(l) == minimum_elem]

    elif operation == 3: # maximum
        maximum_elem = max(len(liste) for liste in column_data)
        return [l for l in column_data if len(l) == maximum_elem]

    
    

def filter_on_numbers(file_processor, column_name, operation):
    
    column_data = [float(val) for val in file_processor.getColumnDataByName(column_name)]
    average = float(sum(column_data) / len(column_data))
    
    if operation == 1:   # moins que la moyenne
        return [row for row in file_processor.content if float(row[column_name]) < average]

    elif operation == 2: # plus que la moyenne
        return [row for row in file_processor.content if float(row[column_name]) > average]

    


def filter_on_numbers_by_comparison(file_processor, first_column_name, second_column_name, operation):
    first_column_data = file_processor.getColumnDataByName(first_column_name)
    second_column_data = file_processor.getColumnDataByName(second_column_name)
    
    if len(first_column_data) != len(second_column_data):
        raise ValueError("Les listes à comparer doivent avoir la même longueur.")
    

    if operation == 1:  # first number smaller than second one
        return [row for row in file_processor.content if row[first_column_name] < row[second_column_name]]
    
    if operation == 2:  # first number bigger than second one
        return [row for row in file_processor.content if row[first_column_name] > row[second_column_name]]
    
    if operation == 3:  # first and second number are the same
        return [row for row in file_processor.content if row[first_column_name] == row[second_column_name]]
        