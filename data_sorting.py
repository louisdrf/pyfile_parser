from file_helper import toList


def sort_numbers(file_processor, column_name, order_by="ASC"):
    reverse = order_by != "ASC"
      
    return sorted(file_processor.content, key=lambda row: float(row[column_name]), reverse=reverse)



def sort_lists(file_processor, column_name, order_by="ASC"):    
    reverse = order_by != "ASC"
    
    return sorted(file_processor.content, key=lambda row: len(toList(row[column_name])), reverse=reverse)



def sort_strings(file_processor, column_name, order_by="ASC"):
    reverse = order_by != "ASC"
    
    return sorted(file_processor.content, key=lambda row: row[column_name], reverse=reverse)