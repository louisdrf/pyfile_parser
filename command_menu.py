from CSV.CSVFileProcessor import CSVFileProcessor
from data_filtering import filter_on_number_of_elements, filter_on_strings
from data_sorting import sort_list


def prompt_user(file_processor):
    print("1 - Filtrer")
    print("2 - Trier")
    print("3 - Statistiques")
    choice = int(input("-> "))

    if choice == 1:
        prompt_filter(file_processor)

    elif choice == 2:
        prompt_sort(file_processor)
        
    elif choice == 3:
        file_processor.displayFileStatistics()
        
        
        
def prompt_sort(file_processor):
    print("Liste des colonnes : ")
    print(file_processor.columns)
    choosen_column = input("La colonne sur laquelle appliquer le tri : ")
    column_type = file_processor.columns_type[choosen_column]
    column = file_processor.getColumnDataByName(choosen_column)
    choosen_order = int(input("Dans quel ordre trier les données ?\n1 - croissant\n2 - décroissant\n-> "))
    order = get_sort_order_from_input(choosen_order)
    
    print(sort_list(column, file_processor.type, column_type, order_by=order))
   
    
    
        
def prompt_filter(file_processor):
    print("Liste des colonnes : ")
    print(file_processor.columns)
    choosen_column = input("La colonne sur laquelle appliquer le filtre : ")
    column = file_processor.getColumnDataByName(choosen_column)
    column_type = file_processor.columns_type[choosen_column]
    
    if column_type is str:
        choosen_filter_operation = int(input("Quel type de filtre appliquer ? \n1 - contient  \n2 - commence par  \n3 - se termine par  \n4 - mots de même taille \n-> "))   
        choosen_filter_word = input("Mot à utiliser pour le filtre : ")
        operation = get_filter_operation_from_input(choosen_filter_operation)        
        print(filter_on_strings(column, choosen_filter_word, operation))

    elif column_type is list:  
        number_of_elements = int(input("Nombre voulu d'éléments dans chaque liste : "))
        filtered_list = filter_on_number_of_elements(column, number_of_elements, file_processor.type)
        print(filtered_list)

        
        
def get_filter_operation_from_input(number):
    if number == 1:
        return "contains"
    elif number == 2:
        return "startswith"
    elif number == 3:
        return "endswith"
    elif number == 4:
        return "size"
    else:
        raise ValueError(f"Unknown operation number: {number}")
    
    
def get_sort_order_from_input(number):
    if number == 1:
        return "ASC"
    elif number == 2:
        return "DESC"
    else:
        raise ValueError(f"Unknown operation number: {number}")
        
        
    