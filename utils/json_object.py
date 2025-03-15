import json

class JSONObject:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, "r") as f:
            return json.load(f)
        
    def get(self, key):
        return self.read()[key]