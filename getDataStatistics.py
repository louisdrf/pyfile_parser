def display_number_statistics(number_list):
    average = float(sum(number_list) / len(number_list))
    print(f"max : {max(number_list)} / min : {min(number_list)} / moyenne : {average:.2f}")
    
    
def display_bool_statistics(bool_list):
    total = len(bool_list)
    count_trues = sum(bool_list)
    count_falses = total - count_trues

    trues_percentage = (count_trues / total) * 100
    falses_percentage = (count_falses / total) * 100
    
    print(f"faux : {falses_percentage:.1f} % | vrais : {trues_percentage:.1f} %")
    
    
def display_list_statistics(list_of_lists):
    lists_size = [len(l) for l in list_of_lists]
    number_of_lists = len(list_of_lists)
    total_lists_size = sum(lists_size)
    
    average_list_size = float(total_lists_size / number_of_lists)
    
    print(f"taille max : {max(lists_size)} / taille min : {min(lists_size)} / taille moyenne : {average_list_size:.1f}")