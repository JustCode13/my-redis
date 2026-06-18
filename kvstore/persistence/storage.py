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

    def load(self):
        with open(self.file_path,"rb") as file:
            json_encoded_data = file.read()

        json_data = json_encoded_data.decode("utf-8")
        data = self.json_serializer.deserializer(json_data)

        return data

    def write_temp(self,data:dict[str,Entry]):
        json_encoded_data = self.json_serializer.serialize(data)

        with open("temp.json","wb") as file:
            file.write(json_encoded_data)

    def _atomic_replace(self):
        os.replace("temp.json",self.file_path)