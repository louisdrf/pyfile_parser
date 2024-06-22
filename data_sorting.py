from file_helper import toList
from get_data_processor import get_data_processor


def sort_numbers(file_processor, column_name, order_by="ASC"):
    reverse = order_by != "ASC" 
    sorted_content = sorted(file_processor.content, key=lambda row: float(row[column_name]), reverse=reverse)
    
    new_file_processor = get_data_processor(file_processor.filename, file_processor.type)
    new_file_processor.content = sorted_content
    return new_file_processor



def sort_lists(file_processor, column_name, order_by="ASC"):    
    reverse = order_by != "ASC"
    sorted_content =  sorted(file_processor.content, key=lambda row: len(toList(row[column_name])), reverse=reverse)

    new_file_processor = get_data_processor(file_processor.filename, file_processor.type)
    new_file_processor.content = sorted_content
    return new_file_processor



def sort_strings(file_processor, column_name, order_by="ASC"):
    reverse = order_by != "ASC"
    sorted_content = sorted(file_processor.content, key=lambda row: row[column_name], reverse=reverse)

    new_file_processor = get_data_processor(file_processor.filename, file_processor.type)
    new_file_processor.content = sorted_content
    return new_file_processor