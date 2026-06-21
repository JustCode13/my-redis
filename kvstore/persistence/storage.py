from .serializer import JsonSerializer, PickleSerializer
from ..models import Entry
from ..retry import retry

import os

class FileStorage:
    def __init__(self,file_path="data.json"):
        self.file_path = file_path
        self.json_serializer = JsonSerializer()
        self.pickle_serializer = PickleSerializer()

    @retry(retries=3)
    def save(self,data: dict[str,Entry]):
        json_data = self.json_serializer.serialize(data)

        with open("temp.json","w") as file:
            file.write(json_data)
            file.flush()
            os.fsync(file.fileno()) # when we open a file it gets a number, so we are getting that number with file.fileno and saying os.fsync to write data into that file


        os.replace("temp.json",self.file_path)
        return True

    @retry(retries=3)
    def load(self):
        with open(self.file_path,"r") as file:
            json_data = file.read()

        data = self.json_serializer.deserializer(json_data)

        return data

    def write_temp(self,data:dict[str,Entry]):
        json_data = self.json_serializer.serialize(data)

        with open("temp.json","w") as file:
            file.write(json_data)
            file.flush()
            os.fsync(file.fileno())

    @retry(retries=3)
    def _atomic_replace(self):
        os.replace("temp.json",self.file_path)



# Python buffer -> OS buffer -> Disk