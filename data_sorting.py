from file_helper import multiple_string_values_to_list

def sort_numbers(file_processor, column_name, order_by="ASC"):
    reverse = order_by != "ASC"
      
    return sorted(file_processor.content, key=lambda row: float(row[column_name]), reverse=reverse)



def sort_lists(file_processor, column_name, order_by="ASC"):    
    reverse = order_by != "ASC"
    
    return sorted(file_processor.content, key=lambda row: len(list(row[column_name])), reverse=reverse)


