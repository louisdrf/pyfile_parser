import csv

class CSVFile:
    def __init__(self, file):
        self.file = file
        self.reader = None
        self.columns = []
        self.content = None
        
        
    def setCSVReader(self):
        self.reader = csv.DictReader(self.file)
        
    def setColumnNames(self):
        self.columns = list(dict(list(self.reader)[0]).keys())