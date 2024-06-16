def sort_list(list, order_by="ASC"): 
    if order_by == "ASC":
        return sorted(list)
    else:
        return sorted(list, reverse=True)
    
    
    