from file_helper import multiple_string_values_to_float, multiple_string_values_to_list

def sort_numbers(data, filetype, order_by="ASC"):
    if filetype == 'csv':
        data = multiple_string_values_to_float(data) 
          
    return get_sorted_list(data, order_by)



def sort_lists(data, filetype, order_by="ASC"):
    if filetype == 'csv':
        data = [multiple_string_values_to_list(l) for l in data] 
    
    return get_sorted_list(data, order_by, key=len)
    


def get_sorted_list(data, order_by="ASC", key=None):
    if order_by == "ASC":
        return sorted(data, key=key)
    else:
        return sorted(data, reverse=True, key=key)

    