import json
from file_helper import get_json_data_type
class JSONFileProcessor:
    def __init__(self, file):
        self.file = file
        self.fields = {}
        self.fields_type = {}
        self.content = json.load(file)
        self.group_fields(self.content)
        self.group_fields_by_type(self.content)
        
        print(self.fields_type)
        
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
    
    
    def group_fields_by_type(self, json_data, fields_type=None): 
        if fields_type is None:
            fields_type = self.fields_type
        
        if isinstance(json_data, dict):
            json_data = [json_data]
        
        for item in json_data:
            for field, value in item.items():
                field_type = get_json_data_type(value)
                if isinstance(value, dict):
                    self.group_fields_by_type([value], fields_type)
                else:
                    if field not in fields_type:
                        fields_type[field] = field_type
                    else:
                        pass