from .models import Entry
from .cache import LRUManager
from .persistence import JsonSerializer

from typing import Any
import time


'''

set(self,key,value:Any, ttl=None)

'''
class KeyValueStore:
    def __init__(self):
        self.kvstore: dict[str,Entry] = {}
        self.ordered_dict = LRUManager()
        self.json_serializer = JsonSerializer()

    def set(self,key,value:Any, ttl=None):

        now = time.monotonic()

        entry = Entry(
            # key,
            value,
            created_at=now,
            expired_at=now + ttl if ttl else None,
            metadata={}
        )
        
        self.kvstore[key] = entry
        if not self.ordered_dict.is_full():
            self.ordered_dict.touch(key)
        else:
            self.ordered_dict.oldest_key()
            self.ordered_dict.touch(key)
        
        json_data = self.json_serializer.serialize(self.kvstore)
        data = self.json_serializer.deserializer(json_data)
        print(data)

        

    def get(self):
        pass

    def delete(self):
        pass

