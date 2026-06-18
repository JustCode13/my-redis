from .serializer import JsonSerializer, PickleSerializer
from ..models import Entry

import os

class FileStorage:
    def __init__(self,file_path="data.json"):
        self.file_path = file_path
        self.json_serializer = JsonSerializer()
        self.pickle_serializer = PickleSerializer()

    def save(self,data: dict[str,Entry]):
        json_encoded_data = self.json_serializer.serialize(data)

        with open("temp.json","wb") as file:
            file.write(json_encoded_data)

        os.replace("temp.json",self.file_path)

        
