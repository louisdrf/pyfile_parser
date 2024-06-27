from collections import defaultdict
import xml.etree.ElementTree as ET

from file_helper import get_xml_data_type


class XMLFileProcessor:
    def __init__(self, filename, file):
        self.filename= filename
        self.file = file
        self.type = 'xml'
        self.columns = []
        self.columns_data = defaultdict(list)
        self.columns_type = {}
        self.content = self.read_file()
        self.group_columns(self.content)
        self.group_columns_by_type(self.content)
        
        print(self.columns_data)
        print(self.columns_type)
        
        
    def read_file(self):
        tree = ET.parse(self.file)
        root = tree.getroot()
        content = []
        
        for elem in root.findall('.//'):
            row = elem.attrib.copy()
            for child in elem:
                row[child.tag] = child.text
            content.append(row)
        
        return content
    
    def get_columns(self, xml_data):
        for item in xml_data:
            for column, value in item.items():
                if column not in self.columns:
                    self.columns.append(column)
    
    
    def group_columns(self, xml_data):
        for item in xml_data:
            print(item.items())
            for column, value in item.items():
                self.columns_data[column].append(value)
                
    
    def group_columns_by_type(self, xml_data):
        for item in xml_data:
            for column, value in item.items():
                column_type = get_xml_data_type(value)
                if column not in self.columns_type:
                    self.columns.append(column)
                    self.columns_type[column] = column_type
    