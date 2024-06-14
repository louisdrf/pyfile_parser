def filter_on_strings(string_list, value, operation="contains", case_sensitive=False):
    if not case_sensitive:
        value = value.lower()
        string_list = [string.lower() for string in string_list]
    
    if operation == "contains":
        return [string for string in string_list if value in string]
    elif operation == "startswith":
        return [string for string in string_list if string.startswith(value)]
    elif operation == "endswith":
        return [string for string in string_list if string.endswith(value)]
    else:
        raise ValueError(f"Unknown operation: {operation}")
    
