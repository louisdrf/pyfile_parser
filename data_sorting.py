from file_helper import multiple_string_values_to_float, multiple_string_values_to_list

def sort_numbers(file_processor, column_name, order_by="ASC"):
    data = file_processor.getColumnDataByName(column_name)
    
    if file_processor.type == 'csv':
        data = multiple_string_values_to_float(data) 
          
    return get_sorted_list(data, order_by)



def sort_lists(file_processor, column_name, order_by="ASC"):
    data = file_processor.getColumnDataByName(column_name)
    
    if file_processor.type == 'csv':
        data = [multiple_string_values_to_list(l) for l in data] 
    
    return get_sorted_list(data, order_by, key=len)
    


def get_sorted_list(data, order_by="ASC", key=None):
    if order_by == "ASC":
        return sorted(data, key=key)
    else:
        return sorted(data, reverse=True, key=key)

