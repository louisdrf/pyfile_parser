def filter_on_strings(string_list, value, operation="contains"):
    if operation == "contains":
        return [string for string in string_list if value in string]
    if operation == "startswith":
        return [string for string in string_list if string.startswith(value)]
    if operation == "endswith":
        return [string for string in string_list if string.endswith(value)]
    if operation == "same size":
        return [string for string in string_list if len(string) == len(value)]
    else:
        raise ValueError(f"Unknown operation on string filter: {operation}")