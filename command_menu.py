from data_sorting import get_sorted_list, sort_numbers, sort_lists
from data_filtering import filter_on_list, filter_on_strings_by_search, filter_on_strings_by_comparison


ON_WHICH_COLUMN_APPLY_OPERATION_PROMPT = "Sur quelle colonne appliquer le filtre ?\n-> "
WHICH_FILTER_TYPE_APPLY_PROMPT = "Quel type de filtre appliquer ? \n1 - Recherche dans une colonne \n2 - Comparaison entre colonnes\n-> "
WHICH_FILTER_TYPE_APPLY_ON_STRING_PROMPT = "Quel type de filtre appliquer ? \n1 - contient  \n2 - commence par  \n3 - se termine par  \n4 - mots de même taille \n-> "
WHICH_FILTER_TYPE_APPLY_ON_LIST_PROMPT = "Quel type de filtre appliquer ? \n1 - nombre d'élements  \n2 - minimum  \n3 - maximum\n-> "
WHICH_ORDER_SORT_DATA_PROMPT = "Dans quel ordre trier les données ?\n1 - croissant\n2 - décroissant\n-> "
WHICH_COMPARISON_FILTER_TYPE_TO_APPLY_PROMPT = "Quel type de comparaison appliquer ? \n1 - est avant  \n2 - est après  \n3 - est de même longueur \n-> "


def prompt_user(file_processor):
    choice = operation_number_input("1 - Filtrer \n2 - Trier \n3 - Statistiques \n-> ", valid_operation_numbers=[1, 2, 3])
    if choice == 1:
        prompt_filter(file_processor)
    elif choice == 2:
        prompt_sort(file_processor)  
    elif choice == 3:
        file_processor.displayFileStatistics()
        
        
        
def prompt_sort(file_processor):
    print("Liste des colonnes : ")
    print(file_processor.columns)
    
    choosen_column = column_name_input(ON_WHICH_COLUMN_APPLY_OPERATION_PROMPT, file_processor.columns)
        
    column_type = file_processor.columns_type[choosen_column]
    column_data = file_processor.getColumnDataByName(choosen_column)
    choosen_order = operation_number_input(WHICH_ORDER_SORT_DATA_PROMPT, valid_operation_numbers=[1, 2])
    order = get_sort_order_from_input(choosen_order)
    
    if column_type is int or column_type is float:
        print(sort_numbers(column_data, file_processor.type, order_by=order))
        
    elif column_type is str:
        print(get_sorted_list(column_data, order_by=order))
        
    elif column_type is list:
        print(sort_lists(column_data, file_processor.type, order_by=order))
   
    
    
        
def prompt_filter(file_processor):
    print("Liste des colonnes : ")
    print(file_processor.columns)
    
    choosen_column = column_name_input(ON_WHICH_COLUMN_APPLY_OPERATION_PROMPT, file_processor.columns)
    column_data = file_processor.getColumnDataByName(choosen_column)
    print(file_processor.columns_type)
    column_type = file_processor.columns_type[choosen_column]

    if column_type is str:
        filter_type = operation_number_input(WHICH_FILTER_TYPE_APPLY_PROMPT, valid_operation_numbers=[1, 2])
        
        if filter_type == 1:
            filter_operation = operation_number_input(WHICH_FILTER_TYPE_APPLY_ON_STRING_PROMPT, valid_operation_numbers=[1, 2, 3, 4])
            choosen_filter_word = input("Mot à utiliser pour le filtre : ")
            filtered_list = filter_on_strings_by_search(column_data, choosen_filter_word, filter_operation)
            
        elif filter_type == 2: 
            print(file_processor.getColumnsNameByType(str))
            second_column_data = column_name_input("Par rapport à quelle colonne faire la comparaison ?\n-> ", file_processor.getColumnsNameByType(str))
            filter_comparison_operation = operation_number_input(WHICH_COMPARISON_FILTER_TYPE_TO_APPLY_PROMPT, valid_operation_numbers=[1, 2, 3])
            filtered_list = filter_on_strings_by_comparison(column_data, second_column_data, filter_comparison_operation)

         
    elif column_type is list:
        filter_operation = operation_number_input(WHICH_FILTER_TYPE_APPLY_ON_LIST_PROMPT, valid_operation_numbers=[1, 2, 3]) 
        filtered_list = filter_on_list(file_processor.type, column_data, filter_operation)

    elif column_type is int:
        # TODO
        print("todo")

    print(filtered_list)




def get_sort_order_from_input(number):
    if number == 1:
        return "ASC"
    elif number == 2:
        return "DESC"
    else:
        raise ValueError(f"Unknown operation number: {number}")
    


def operation_number_input(input_content, valid_operation_numbers):
    operation_number = int(input(input_content))
    
    while operation_number not in valid_operation_numbers:
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