import csv

class CSVFile:
    def __init__(self, file):
        self.file = file
        self.reader = None
        self.columns = []
        self.content = None
        
        
    def setReader(self):
        self.file.seek(0)
        self.reader = csv.DictReader(self.file)
        self.content = list(self.reader)  
        self.columns = self.reader.fieldnames
    
    def getColumnDataByName(self, columnName):
        print([row[columnName] for row in self.content])
