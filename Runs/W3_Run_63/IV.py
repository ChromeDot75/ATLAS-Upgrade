#GETTING IV RESULTS
import json

class JsonReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.current_values = []

    def read_json_file(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            if "CURRENT" in data and isinstance(data["CURRENT"], list):
                self.current_values = [float(line.strip()) for line in data["CURRENT"]]

if __name__ == "__main__":
    file_path = "N:\\CERN\W3_Run_63\\results\\SN20USBHX2001092_UNKNOWN_20231009_63_18_MODULE_IV_AMAC.json"
    json_reader = JsonReader(file_path)
    json_reader.read_json_file()
    print("Current values:", json_reader.current_values)
    
    
    