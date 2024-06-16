from file_helper import multiple_string_values_to_float

def sort_list(data, filetype, datatype, order_by="ASC"):
    if filetype == 'csv':
        if datatype is int or datatype is float:
            data = multiple_string_values_to_float(data)
        
    if order_by == "ASC":
        return sorted(data)
    else:
        return sorted(data, reverse=True)
    
    
    