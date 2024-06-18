import csv
from file_helper import get_data_type, multiple_string_values_to_boolean, multiple_string_values_to_float, toList
from getDataStatistics import display_number_statistics, display_bool_statistics, display_list_statistics
class CSVFileProcessor:
    def __init__(self, file):
        self.file = file
        self.type = 'csv'
        self.reader = None
        self.columns = []
        self.columns_type = {}
        self.content = None
        
        self.setReader()
        self.setColumnsDataType()
    
    def displayFileStatistics(self):
        for columnName, columnType in  self.columns_type.items():
            print(columnName)
            column_data = self.getColumnDataByName(columnName)
            
            if columnType is int:
                number_list = multiple_string_values_to_float(column_data)
                display_number_statistics(number_list)     
            
            if columnType is bool:
                bools_list = multiple_string_values_to_boolean(column_data)
                display_bool_statistics(bools_list)
            
            if columnType is list:
                lists = [toList(l) for l in column_data] 
                display_list_statistics(lists)
            
        
    def setReader(self):
        self.file.seek(0)
        self.reader = csv.DictReader(self.file)
        self.content = list(self.reader)  
        self.columns = self.reader.fieldnames
        
        
    def setColumnsDataType(self):
        if not self.content:
            return
        for column in self.columns:
            col_elems = self.getColumnDataByName(column)
            self.columns_type[column] = get_data_type(col_elems)
            
    
    def showColumns(self):
        print(f"Composées de nombres : {self.getColumnsNameByType(int)}")
        print(f"\nComposées de chaînes de caractères : {self.getColumnsNameByType(str)}")
        print(f"\nComposées de booléens : {self.getColumnsNameByType(bool)}")
        print(f"\nComposées de listes : {self.getColumnsNameByType(list)}")
     
        
    def getColumnDataByName(self, columnName):
        return [row[columnName] for row in self.content]
    
    def getColumnTypeByName(self, column_name):
        return self.columns_type[column_name]
    
    def getColumnsNameByType(self, type):
       return [column_name for column_name, column_type in self.columns_type.items() if column_type == type]
   
    def getColumnsNameByTypeExcludingOne(self, type, excluded_column_name):
       return [column_name for column_name, column_type in self.columns_type.items() if column_type == type and column_name != excluded_column_name]
    
        
