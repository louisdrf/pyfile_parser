from file_helper import multiple_string_values_to_list

def display_number_statistics(number_list):
    number_list = [float(num) for num in number_list if num.strip().replace('.', '', 1).isdigit()]
    average = float(sum(number_list) / len(number_list))
    print(f"max : {max(number_list)} / min : {min(number_list)} / moyenne : {average:.2f}")
    
    
def display_bool_statistics(bool_list):
    total = len(bool_list)
    
    if bool_list[0] in {'0', '1'}:
        count_falses = bool_list.count('0')
        count_trues = bool_list.count('1')
    else:
        count_falses = bool_list.count("false")
        count_trues = bool_list.count("true")

    falses = (count_falses / total) * 100
    trues = (count_trues / total) * 100
    
    print(f"faux : {falses:.1f} % | vrais : {trues:.1f} %")
    
    
def display_list_statistics(list_of_lists):
    lists_size = [len(multiple_string_values_to_list(l)) for l in list_of_lists]
    number_of_lists = len(list_of_lists)
    total_lists_size = sum(lists_size)
    
    average_list_size = float(total_lists_size / number_of_lists)
    
    print(f"taille max : {max(lists_size)} / taille min : {min(lists_size)} / taille moyenne : {average_list_size:.1f}")