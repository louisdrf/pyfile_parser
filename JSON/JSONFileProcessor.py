import json

class JSONFileProcessor:
    def __init__(self, file):
        self.file = file
        self.fields = {}
        self.fields_type = {}
        self.content = json.load(file)
        self.group_fields(self.content)
        
        
    def group_fields(self, json_data, fields=None):
        if fields is None:
            fields = self.fields
        
        if isinstance(json_data, dict):
            json_data = [json_data]

        for item in json_data:
            for field, value in item.items():
                if isinstance(value, dict):
                    self.group_fields([value], fields)
                else:
                    if field not in fields:
                        fields[field] = [value]
                    else:
                        fields[field].append(value)
        
        return fields