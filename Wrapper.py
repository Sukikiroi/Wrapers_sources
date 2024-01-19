import csv
import requests
import xml.etree.ElementTree as ET

class DataWrapper:
    def __init__(self, data=None):
        self.data = data

    def load_csv(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            self.data = list(reader)

    def load_api(self, api_url):
        response = requests.get(api_url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print(f"Failed to fetch data from API. Status code: {response.status_code}")

    def load_xml(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        self.data = self._parse_xml(root)

    def wrappe_csv_table(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            self.data = list(reader)

    def wrappe_api_table(self, api_url):
        response = requests.get(api_url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print(f"Failed to fetch data from API. Status code: {response.status_code}")

    def wrappe_xml_table(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        self.data = self._parse_xml(root)

    def decision_making(self):
       """
        This method is a placeholder for the decision-making logic.
        It should be implemented to dynamically choose between two data sources based on certain criteria.
       """
     
       pass

 

# Example usage:
wrapper = DataWrapper()

# Load data from CSV
wrapper.load_csv('data.csv')

# Save data to XML
wrapper.save_xml('data.xml')

# Load data from API
wrapper.load_api('https://api.example.com/data')

# Save data to CSV
wrapper.save_csv('new_data.csv')
