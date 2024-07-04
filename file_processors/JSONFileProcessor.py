import json
from file_helper import get_json_data_type
from getDataStatistics import display_number_statistics, display_bool_statistics, display_list_statistics

class JSONFileProcessor:
    def __init__(self, filename, file):
        self.filename= filename
        self.file = file
        self.type = 'json'
        self.columns = []
        self.columns_data = {}
        self.columns_type = {}
        self.content = json.load(file)
        self.group_columns(self.content)
        self.group_columns_by_type(self.content)
        
        
        print(self.content)
                        
    
    def displayFileStatistics(self):
        for column_name, column_type in  self.columns_type.items():
            print(column_name)
            
            if column_type is int or column_type is float:
                display_number_statistics(self.getColumnDataByName(column_name))     
            
            if column_type is bool:
                display_bool_statistics(self.getColumnDataByName(column_name))
            
            if column_type is list:
                display_list_statistics(self.getColumnDataByName(column_name))
            
            else:
                pass
    
        
    def group_columns(self, json_data, columns=None):
        if columns is None:
            columns = self.columns_data
        
        if isinstance(json_data, dict):
            json_data = [json_data]

        for item in json_data:
            for column, value in item.items():
                if isinstance(value, dict):
                    self.group_columns([value], columns)
                else:
                    if column not in columns:
                        columns[column] = [value]
                    else:
                        columns[column].append(value)
        
        return columns
    
    
    def group_columns_by_type(self, json_data, columns_type=None): 
        if columns_type is None:
            columns_type = self.columns_type
        
        if isinstance(json_data, dict):
            json_data = [json_data]
        
        for item in json_data:
            for column, value in item.items():
                column_type = get_json_data_type(value)
                if isinstance(value, dict):
                    self.group_columns_by_type([value], columns_type)
                else:
                    if column not in columns_type:
                        self.columns.append(column)
                        columns_type[column] = column_type
                    else:
                        pass
     
    def showColumns(self):
        print(f"Composées de nombres : {self.getColumnsNameByType(int)}")
        print(f"\nComposées de chaînes de caractères : {self.getColumnsNameByType(str)}")
        print(f"\nComposées de booléens : {self.getColumnsNameByType(bool)}")
        print(f"\nComposées de listes : {self.getColumnsNameByType(list)}")
                    
                    
    def getColumnDataByName(self, column_name):
        return [item for item in self.columns_data[column_name]]
    
    def getColumnTypeByName(self, column_name):
        return self.columns_type[column_name]
    
    def getColumnsNameByType(self, type):
        return [column for column, column_type in self.columns_type.items() if column_type == type]
    
    def getColumnsNameByTypeExcludingOne(self, type, excluded_column_name):
       return [column_name for column_name, column_type in self.columns_type.items() if column_type == type and column_name != excluded_column_name]