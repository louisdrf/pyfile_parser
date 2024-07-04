from collections import defaultdict
from file_helper import toFloat, toList
from get_data_processor import get_data_processor


def sort_lists(file_processor, column_name, order_by="ASC", sub_items_to_sort=None):
    return generic_sort(file_processor, column_name, order_by, sub_items_to_sort, key_func=lambda row, col: len(toList(row[col])))

def sort_strings(file_processor, column_name, order_by="ASC", sub_items_to_sort=None):
    return generic_sort(file_processor, column_name, order_by, sub_items_to_sort, key_func=lambda row, col: row[col])

def sort_numbers(file_processor, column_name, order_by="ASC", sub_items_to_sort=None):
    return generic_sort(file_processor, column_name, order_by, sub_items_to_sort, key_func=lambda row, col: toFloat(row[col]))


def generic_sort(file_processor, column_name, order_by="ASC", sub_items_to_sort=None, key_func=lambda row, col: row[col]):
    print(file_processor.columns_data)
    reverse = order_by != "ASC" 
    if sub_items_to_sort is None: # créer un nouveau file processor avec le contenu trié
        sorted_content = sorted(file_processor.content, key=lambda row: key_func(row, column_name), reverse=reverse)
        new_file_processor = get_data_processor(file_processor.filename, file_processor.type)
        new_file_processor.content = sorted_content
    
        sub_items_to_sort = get_sub_items_to_sort(new_file_processor, column_name)
        return new_file_processor, sub_items_to_sort
    
    else:
        sorted_content = file_processor.content[:]
        sub_sub_items_to_sort = []
         
        for sub_item in sub_items_to_sort:
            sorted_sub_item = sorted(sub_item, key=lambda row: key_func(row, column_name), reverse=reverse)
            for i in range(len(file_processor.content)):
                if file_processor.content[i] in sub_item:
                    sorted_content[i:i+len(sub_item)] = sorted_sub_item # on remplace le sous ensemble à trier par le sous_ensemble trié dans le contenu initial
                    break   
            sub_sub_items_file_processor = get_data_processor(file_processor.filename, file_processor.type)
            sub_sub_items_file_processor.content = sorted_sub_item
            sub_sub_items_to_sort.extend(get_sub_items_to_sort(sub_sub_items_file_processor, column_name)) # récupérer les sous ensembles du sous ensemble
                    
    new_file_processor = get_data_processor(file_processor.filename, file_processor.type)
    new_file_processor.content = sorted_content
    
    return new_file_processor, sub_sub_items_to_sort



def get_sub_items_to_sort(file_processor, column_name):
    sub_items = defaultdict(list)
    column_type = file_processor.getColumnTypeByName(column_name)
    
    for row in file_processor.content:
        if column_type is str:
             current_value = row[column_name]
        elif column_type is list:
             current_value = len(toList(row[column_name]))
        elif column_type is int or column_type is float:
             current_value = float(row[column_name])
             
        sub_items[current_value].append(row)
    
    return [group for group in sub_items.values() if len(group) > 1]
