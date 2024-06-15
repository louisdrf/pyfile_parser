import csv
from file_helper import convert_to_boolean, get_data_type, multiple_string_values_to_list
from getDataStatistics import display_number_statistics, display_bool_statistics, display_list_statistics
class CSVFileProcessor:
    def __init__(self, file):
        self.file = file
        self.reader = None
        self.columns = []
        self.columns_type = {}
        self.content = None
        
        self.setReader()
        self.setColumnsDataType()
    
    def displayFileStatistics(self):
        for columnName, columnType in  self.columns_type.items():
            print(columnName)
            
            if columnType is int:
                number_list = [float(num) for num in self.getColumnDataByName(columnName) if num.strip().replace('.', '', 1).isdigit()] # convert string number value to float
                display_number_statistics(number_list)     
            
            if columnType is bool:
                bools_list = [convert_to_boolean(string_bool) for string_bool in self.getColumnDataByName(columnName)] # convert string bool like "true" or "0" to bool
                display_bool_statistics(bools_list)
            
            if columnType is list:
                lists = [multiple_string_values_to_list(l) for l in self.getColumnDataByName(columnName)] # convert separated string values to list
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
            
    
    def getColumnDataByName(self, columnName):
        if columnName not in self.columns:
            raise ValueError(f"La colonne '{columnName}' n'existe pas dans le fichier.")
        
        return [row[columnName] for row in self.content]
    
        
