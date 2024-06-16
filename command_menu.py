from data_sorting import get_sorted_list, sort_numbers, sort_lists
from data_filtering import filter_on_list, filter_on_strings

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
    while True:
        print(f"La colonne {choosen_column} n'existe pas dans la liste.")
        print(file_processor.columns)
        choosen_column = input("La colonne sur laquelle appliquer le tri : ")
        if choosen_column in file_processor.columns:
            break
        
    column_type = file_processor.columns_type[choosen_column]
    column_data = file_processor.getColumnDataByName(choosen_column)
    choosen_order = int(input("Dans quel ordre trier les données ?\n1 - croissant\n2 - décroissant\n-> "))
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
    
    choosen_column = input("La colonne sur laquelle appliquer le filtre : ")
    while True:
        print(f"La colonne {choosen_column} n'existe pas dans la liste.")
        print(file_processor.columns)
        choosen_column = input("La colonne sur laquelle appliquer le tri : ")
        if choosen_column in file_processor.columns:
            break
        
    column = file_processor.getColumnDataByName(choosen_column)
    column_type = file_processor.columns_type[choosen_column]
    
    if column_type is str:
        filter_operation = int(input("Quel type de filtre appliquer ? \n1 - contient  \n2 - commence par  \n3 - se termine par  \n4 - mots de même taille \n-> "))   
        choosen_filter_word = input("Mot à utiliser pour le filtre : ")
        filtered_list = filter_on_strings(column, choosen_filter_word, filter_operation)

    elif column_type is list:
        filter_operation = int(input("Quel type de filtre appliquer ? \n1 - nombre d'élements  \n2 - minimum  \n3 - maximum\n-> "))   
        filtered_list = filter_on_list(file_processor.type, column, filter_operation)

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
        
        
    