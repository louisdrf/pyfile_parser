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
        self.group_columns_data(self.content)
        self.group_columns_by_type(self.content)
        
        print(self.columns_data)
        print(self.columns_type)
        
        
    def read_file(self):
        tree = ET.parse(self.file)
        root = tree.getroot()
        content = []
        for elem in root.findall('.//'):
            row = elem.attrib.copy()
            row.update(self.parse_element(elem))
            content.append(row)
        return content

    def parse_element(self, element):
        data = {}
        for child in element:
            if len(child) > 0:
                data.update(self.parse_element(child))
            else:
                data[child.tag] = child.text
        return data
    
    def get_columns(self, xml_data):
        for item in xml_data:
            for column, _ in item.items():
                if column not in self.columns:
                    self.columns.append(column)
    
    def group_columns_data(self, xml_data):
        for item in xml_data:
            for column, value in item.items():
                self.columns_data[column].append(value)
    
    def group_columns_by_type(self, xml_data):
        for item in xml_data:
            for column, value in item.items():
                column_type = get_xml_data_type(value)
                if column not in self.columns_type:
                    self.columns.append(column)
                    self.columns_type[column] = column_type
    