def filter_on_strings(string_list, value, operation, case_sensitive=False):
    if not case_sensitive:
        value_lower = value.lower()
        string_list = [string.lower() for string in string_list]
    else:
        value_lower = value
    
    if operation == "contains":
        return [string for string in string_list if value_lower in string.lower()]
    elif operation == "startswith":
        return [string for string in string_list if string.startswith(value_lower)]
    elif operation == "endswith":
        return [string for string in string_list if string.endswith(value_lower)]
    elif operation == "size":
        return [string for string in string_list if len(string) == len(value)]
    else:
        raise ValueError(f"Unknown operation: {operation}")