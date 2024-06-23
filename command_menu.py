import sys
from data_sorting import sort_numbers, sort_lists, sort_strings
from data_filtering import filter_on_booleans_by_search, filter_on_numbers_by_search, filter_on_list, filter_on_numbers_by_comparison, filter_on_strings_by_search, filter_on_strings_by_comparison


ON_WHICH_COLUMN_APPLY_FILTER_PROMPT = "Sur quelle colonne appliquer le filtre ?\n-> "
ON_WHICH_COLUMN_APPLY_SORT_PROMPT = "Sur quelle colonne appliquer le tri ?\n-> "

WHICH_FILTER_TYPE_APPLY_PROMPT = "Quel type de filtre appliquer ? \n1 - Recherche dans une colonne \n2 - Comparaison entre colonnes\n-> "
WHICH_FILTER_TYPE_APPLY_ON_STRING_PROMPT = "Quel filtre appliquer ? \n1 - contient  \n2 - commence par  \n3 - se termine par  \n4 - mots de même taille \n-> "
WHICH_FILTER_TYPE_APPLY_ON_LIST_PROMPT = "Quel filtre appliquer ? \n1 - par nombre d'élements  \n2 - taille minimum  \n3 - taille maximum\n4 - de taille moyenne\n5 - moins de la taille moyenne\n6 - plus de la taille moyenne\n-> "
WHICH_FILTER_TYPE_APPLY_ON_NUMBER_PROMPT = "Quel filtre appliquer ? \n1 - moins que la moyenne\n2 - plus que la moyenne\n3 - dans la moyenne\n4 - 25% plus haut\n5 - 25% plus bas\n6 - est inférieur à\n7 - est supérieur à\n8 - est égal à\n-> "
WHICH_FILTER_TYPE_APPLY_ON_BOOLEAN_PROMPT = "Quel filtre appliquer ? \n1 - valeurs vraies \n2 - valeurs fausses \n-> "
WHICH_ORDER_SORT_DATA_PROMPT = "Dans quel ordre trier les données ?\n1 - croissant\n2 - décroissant\n-> "
WHICH_COMPARISON_FILTER_TYPE_TO_APPLY_ON_STRING_PROMPT = "Quel type de comparaison appliquer ? \n1 - est avant  \n2 - est après  \n3 - est de même longueur \n-> "
WHICH_COMPARISON_FILTER_TYPE_TO_APPLY_ON_NUMBERS_PROMPT = "Quel type de comparaison appliquer ? \n1 - est inférieur  \n2 - est supérieur  \n3 - est égal \n-> "

def prompt_user(file_processor):
    choice = operation_number_input("1 - Filtrer \n2 - Trier \n3 - Statistiques \n4 - Quitter\n-> ", valid_operation_numbers=4)
    if choice == 1:
        prompt_filter(file_processor)
    elif choice == 2:
        prompt_sort(file_processor)  
    elif choice == 3:
        file_processor.displayFileStatistics()
    elif choice == 4:
        print("Fin de programme.")
        sys.exit(0)
        
        
        
        
        
def prompt_sort(file_processor, sub_items_to_sort=None):
    print("Listes des colonnes : ")
    file_processor.showColumns()
    
    choosen_column = column_name_input(ON_WHICH_COLUMN_APPLY_SORT_PROMPT, file_processor.columns)
        
    column_type = file_processor.getColumnTypeByName(choosen_column)
    order = get_sort_order_from_input(operation_number_input(WHICH_ORDER_SORT_DATA_PROMPT, valid_operation_numbers=2))
    
    if column_type is int or column_type is float:
        sorted_file_processor, sub_items_to_sort = sort_numbers(file_processor, choosen_column, order_by=order, sub_items_to_sort=sub_items_to_sort)
        
    elif column_type is str:
        sorted_file_processor, sub_items_to_sort = sort_strings(file_processor, choosen_column, order_by=order, sub_items_to_sort=sub_items_to_sort)
        
    elif column_type is list:
        sorted_file_processor, sub_items_to_sort = sort_lists(file_processor, choosen_column, order_by=order, sub_items_to_sort=sub_items_to_sort)    
        
    print(sorted_file_processor.content)
    if len(sub_items_to_sort) > 1:    
        print(f"{len(sub_items_to_sort)} sous-ensembles à re-trier ont été trouvés.")
        user_action = int(input("Appliquer un nouveau tri ?\n1 - oui \n2 - non\n-> "))
        if user_action == 1:
            prompt_sort(sorted_file_processor, sub_items_to_sort)
        elif user_action == 2:
            prompt_user(file_processor)
   
   
   
    
    
        
def prompt_filter(file_processor):
    print("Listes des colonnes : ")
    file_processor.showColumns()
    
    choosen_column = column_name_input(ON_WHICH_COLUMN_APPLY_FILTER_PROMPT, file_processor.columns)
    column_type = file_processor.getColumnTypeByName(choosen_column)

    if column_type is str:
        filtered_list = get_filtered_string_list_from_prompt(file_processor, choosen_column)

    elif column_type is list:
        filtered_list = get_filtered_lists_from_prompt(file_processor, choosen_column)
        
    elif column_type is int:
        filtered_list = get_filtered_numbers_list_from_prompt(file_processor, choosen_column)
        
    elif column_type is bool:
        filtered_list = get_filtered_booleans_list_from_prompt(file_processor, choosen_column)
        
    print(filtered_list)

def get_filtered_booleans_list_from_prompt(file_processor, choosen_column):
        filter_operation = operation_number_input(WHICH_FILTER_TYPE_APPLY_ON_BOOLEAN_PROMPT, valid_operation_numbers=2) 
        return filter_on_booleans_by_search(file_processor, choosen_column, filter_operation)

def get_filtered_numbers_list_from_prompt(file_processor, choosen_column):
    filter_type = operation_number_input(WHICH_FILTER_TYPE_APPLY_PROMPT, valid_operation_numbers=2)

    if filter_type == 1:
        filter_operation = operation_number_input(WHICH_FILTER_TYPE_APPLY_ON_NUMBER_PROMPT, valid_operation_numbers=8) 
        return filter_on_numbers_by_search(file_processor, choosen_column, filter_operation)
    else:
        comparable_column_names = file_processor.getColumnsNameByTypeExcludingOne(int, choosen_column)
        print(comparable_column_names)
        second_choosen_column = column_name_input("Par rapport à quelle colonne faire la comparaison ?\n-> ", comparable_column_names)
        filter_operation = operation_number_input(WHICH_COMPARISON_FILTER_TYPE_TO_APPLY_ON_NUMBERS_PROMPT, valid_operation_numbers=3)

        return filter_on_numbers_by_comparison(file_processor, choosen_column, second_choosen_column, filter_operation)

def get_filtered_lists_from_prompt(file_processor, column_name):
    filter_operation = operation_number_input(WHICH_FILTER_TYPE_APPLY_ON_LIST_PROMPT, valid_operation_numbers=6) 
    return filter_on_list(file_processor, column_name, filter_operation)

def get_filtered_string_list_from_prompt(file_processor, choosen_column):
    filter_type = operation_number_input(WHICH_FILTER_TYPE_APPLY_PROMPT, valid_operation_numbers=2)
        
    if filter_type == 1: # filter on one column
        filter_operation = operation_number_input(WHICH_FILTER_TYPE_APPLY_ON_STRING_PROMPT, valid_operation_numbers=4)
        
        return filter_on_strings_by_search(file_processor, choosen_column, filter_operation)
        
        
    elif filter_type == 2: # filter by comparing 2 columns
        comparable_column_names = file_processor.getColumnsNameByTypeExcludingOne(str, choosen_column)
        print(comparable_column_names)
        second_choosen_column = column_name_input("Par rapport à quelle colonne faire la comparaison ?\n-> ", comparable_column_names)
        filter_operation = operation_number_input(WHICH_COMPARISON_FILTER_TYPE_TO_APPLY_ON_STRING_PROMPT, valid_operation_numbers=3)
        
        return filter_on_strings_by_comparison(file_processor, choosen_column, second_choosen_column, filter_operation)

def get_sort_order_from_input(number):
    if number == 1:
        return "ASC"
    elif number == 2:
        return "DESC"
    else:
        raise ValueError(f"Unknown operation number: {number}")
    
def operation_number_input(input_content, valid_operation_numbers):
    operation_number = int(input(input_content))
    
    while operation_number not in range(valid_operation_numbers + 1):
        print(f"L'opération portant le numéro {operation_number} n'existe pas.")
        operation_number = int(input(input_content))
        
    return operation_number
        
def column_name_input(input_content, columns_list):
    column = input(input_content)
    
    while column not in columns_list:
        print(f"La colonne {column} n'existe pas dans la liste.")
        print(columns_list)
        column = input(input_content)
        
    return column