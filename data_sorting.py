from collections import defaultdict
from file_helper import toList
from get_data_processor import get_data_processor

def get_sub_items_to_sort(file_processor, column_name):
    sub_items = defaultdict(list)
    
    for row in file_processor.content:
        current_value = float(row[column_name])
        sub_items[current_value].append(row)
    
    return [group for group in sub_items.values() if len(group) > 1]


def sort_numbers(file_processor, column_name, order_by="ASC", sub_items_to_sort=None):
    reverse = order_by != "ASC" 
    if sub_items_to_sort is None:
        sorted_content = sorted(file_processor.content, key=lambda row: float(row[column_name]), reverse=reverse)
    else:
        sorted_content = file_processor.content[:]
        
        for sub_item in sub_items_to_sort:
            sorted_sub_item = sorted(sub_item, key=lambda row: float(row[column_name]), reverse=reverse)
            for i in range(len(file_processor.content)):
                if file_processor.content[i] in sub_item:
                    sorted_content[i:i+len(sub_item)] = sorted_sub_item
                    break   
    
    new_file_processor = get_data_processor(file_processor.filename, file_processor.type)
    new_file_processor.content = sorted_content
    
    sub_items_to_sort = get_sub_items_to_sort(new_file_processor, column_name)
    return new_file_processor, sub_items_to_sort



def sort_lists(file_processor, column_name, order_by="ASC", sub_items_to_sort=None):    
    reverse = order_by != "ASC"
    
    if sub_items_to_sort is None:
        sorted_content = sorted(file_processor.content, key=lambda row: len(toList(row[column_name])), reverse=reverse)
    else:
        sorted_content = file_processor.content[:]
        
        for sub_item in sub_items_to_sort:
            sorted_sub_item = sorted(file_processor.content, key=lambda row: len(toList(row[column_name])), reverse=reverse)
            for i in range(len(file_processor.content)):
                if file_processor.content[i] in sub_item:
                    sorted_content[i:i+len(sub_item)] = sorted_sub_item
                    break   

    new_file_processor = get_data_processor(file_processor.filename, file_processor.type)
    new_file_processor.content = sorted_content
    sub_items_to_sort = get_sub_items_to_sort(new_file_processor, column_name)
    return new_file_processor, sub_items_to_sort



def sort_strings(file_processor, column_name, order_by="ASC", sub_items_to_sort=None):
    reverse = order_by != "ASC"
    
    if sub_items_to_sort is None:
        sorted_content = sorted(file_processor.content, key=lambda row: row[column_name], reverse=reverse)
    else:
        sorted_content = file_processor.content[:]
        
        for sub_item in sub_items_to_sort:
            sorted_sub_item = sorted(file_processor.content, key=lambda row: row[column_name], reverse=reverse)
            for i in range(len(file_processor.content)):
                if file_processor.content[i] in sub_item:
                    sorted_content[i:i+len(sub_item)] = sorted_sub_item
                    break   

    new_file_processor = get_data_processor(file_processor.filename, file_processor.type)
    new_file_processor.content = sorted_content
    sub_items_to_sort = get_sub_items_to_sort(new_file_processor, column_name)
    return new_file_processor, sub_items_to_sort