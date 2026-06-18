from ..models import Entry

import json
import pickle
from typing import Any

class JsonSerializer:
    def __init__(self):
        pass

    def serialize(self,data:dict[str,Entry]):
        json_data = json.dumps({k: v.to_dict() for k, v in data.items()})
        json_encoded_data = json_data.encode("utf-8")
        return json_encoded_data

    def deserializer(self,json_data: str):
        data = json.loads(json_data)
        
        result: dict[str:Entry] = {}

        for key, value in data.items():
            result[key] = Entry(
                value=value["value"],
                created_at=value["created_at"],
                expired_at=value["expired_at"],
                metadata=value["metadata"],
            )

        return result

class PickleSerializer:
    def __init__(self):
        pass

    def serialize(self,data:dict[str,Entry]):
        json_data = pickle.dumps(({k: v.to_dict() for k, v in data.items()}))
        
        return json_data
    

    def deserializer(self,json_data: str):
        data = pickle.loads(json_data)
        
        result: dict[str:Entry] = {}

        for key, value in data.items():
            result[key] = Entry(
                value=value["value"],
                created_at=value["created_at"],
                expired_at=value["expired_at"],
                metadata=value["metadata"],
            )

        return result