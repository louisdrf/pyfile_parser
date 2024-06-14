import csv
from file_helper import get_data_type
from getDataStatistics import displayNumberStatistics, displayBoolStatistics
class CSVFileProcessor:
    def __init__(self, file):
        self.file = file
        self.reader = None
        self.columns = []
        self.columnsType = {}
        self.content = None
        
        self.setReader()
        self.setColumnsDataType()
        self.displayFileStatistics()
    
    def displayFileStatistics(self):
        for columnName, columnType in  self.columnsType.items():
            if columnType is int:
                print(columnName)
                displayNumberStatistics(self.getColumnDataByName(columnName))     
            
            if columnType is bool:
                print(columnName)
                displayBoolStatistics(self.getColumnDataByName(columnName))
            
        
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
            self.columnsType[column] = get_data_type(col_elems)
            
    
    def getColumnDataByName(self, columnName):
        if columnName not in self.columns:
            raise ValueError(f"La colonne '{columnName}' n'existe pas dans le fichier.")
        
        return [row[columnName] for row in self.content]
    
        
