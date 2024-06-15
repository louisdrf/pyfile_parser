from data_filtering import filter_on_strings

def displayCommandMenu(file_processor):
    print("1 - Filtrer")
    print("2 - Trier")
    print("3 - Statistiques")
    choice = int(input())
    if choice == 1:
        print("Liste des colonnes : ")
        print(file_processor.columns)
        choosen_column = input("La colonne sur laquelle appliquer le filtre : ")
        choosen_filter_operation = int(input("Quel type de filtre appliquer ? \n1 - contient  \n2 - commence par  \n3 - se termine par  \n4 - mots de même taille \n-> "))   
        choosen_filter_word = input("Mot à utiliser pour le filtre : ")
        
        
        strings_list = file_processor.getColumnDataByName(choosen_column)
        operation = get_filter_operation_from_input(choosen_filter_operation)
        
        print(filter_on_strings(strings_list, choosen_filter_word, operation))
        
    elif choice == 3:
        file_processor.displayFileStatistics()
        
        
        
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
        
        
    