import json

class JSONFileProcessor:
    def __init__(self, file):
        self.file = file
        self.content = json.load(file)
        self.fields = {}
        self.fields_type = {}
        self.show_content()
        
    def show_content(self):
        for item in self.content:
            for field, value in item.items():
                if field not in self.fields:
                    self.fields[field] = [value]
                else:
                    self.fields[field].append(value)
                
        print(self.fields)        