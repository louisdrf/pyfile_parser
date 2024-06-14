from csv_data_filtering import filter_on_strings

def displayCommandMenu(file_processor):
    print("1 - Filtrer")
    print("2 - Trier")
    print("3 - Statistiques")
    choice = int(input())
    if choice == 1:
        print("Liste des colonnes : ")
        print(file_processor.columns)
        choosen_column = input("La colonne sur laquelle appliquer le filtre : ")
        choosen_filter_operation = input("Quel type de filtre appliquer ? \n1 - contains  \n2 - startswith  \n3 - endswith  \n4 - size \n-> ")
        filter = "contains"
        if choosen_filter_operation == 1:
            filter = "contains"
        if choosen_filter_operation == 2:
            filter = "startswith"
        if choosen_filter_operation == 3:
            filter = "endswith"
        if choosen_filter_operation == 4:
            filter = "size"
        choosen_filter_word = input("Mot à utiliser pour le filtre : ")
        print(filter_on_strings(file_processor.getColumnDataByName(choosen_column), choosen_filter_word, filter))
        
        
        
    