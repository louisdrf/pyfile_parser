from collections import defaultdict
import xml.etree.ElementTree as ET

from file_helper import get_xml_data_type, multiple_string_values_to_boolean, multiple_string_values_to_float, toList
from getDataStatistics import display_bool_statistics, display_list_statistics, display_number_statistics


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
                    
                    
    def displayFileStatistics(self):
        for column_name, column_type in self.columns_type.items():
            if column_type is not str:
                print(column_name)
                
            column_data = self.getColumnDataByName(column_name)
            
            if column_type in {int, float}:
                number_list = multiple_string_values_to_float(column_data)
                display_number_statistics(number_list)  
                   
            elif column_type is bool:
                bools_list = multiple_string_values_to_boolean(column_data)
                display_bool_statistics(bools_list)
                
            elif column_type is list:
                lists = [toList(l) for l in column_data] 
                display_list_statistics(lists)
            else:
                pass
    
    def showColumns(self):
        print(f"Composées de nombres : {self.getColumnsNameByType(int)}")
        print(f"\nComposées de chaînes de caractères : {self.getColumnsNameByType(str)}")
        print(f"\nComposées de booléens : {self.getColumnsNameByType(bool)}")
        print(f"\nComposées de listes : {self.getColumnsNameByType(list)}")
                    
    def getColumnDataByName(self, column_name):
        return self.columns_data[column_name]
    
    def getColumnTypeByName(self, column_name):
        return self.columns_type[column_name]
    
    def getColumnsNameByType(self, type):
        return [column for column, column_type in self.columns_type.items() if column_type == type]
    
    def getColumnsNameByTypeExcludingOne(self, type, excluded_column_name):
        return [column_name for column_name, column_type in self.columns_type.items() if column_type == type and column_name != excluded_column_name]
    