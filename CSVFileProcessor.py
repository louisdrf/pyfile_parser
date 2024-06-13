import csv
from file_helper import getDataType
class CSVFileProcessor:
    def __init__(self, file):
        self.file = file
        self.reader = None
        self.columns = []
        self.columnsType = {}
        self.content = None
        
        self.setReader()
        self.setColumnsDataType()
        print(self.columnsType)
        
        
    def setReader(self):
        self.file.seek(0)
        self.reader = csv.DictReader(self.file)
        self.content = list(self.reader)  
        self.columns = self.reader.fieldnames
        
        
    def setColumnsDataType(self):
        if not self.content:
            return
        for column in self.columns:
            firstColumnValue = self.content[0][column]
            self.columnsType[column] = getDataType(firstColumnValue)
            
    
    def getColumnDataByName(self, columnName):
        if columnName not in self.columns:
            raise ValueError(f"La colonne '{columnName}' n'existe pas dans le fichier.")
        
        return [row[columnName] for row in self.content]
    
        
