from .models import Entry
from .cache import LRUManager
from typing import Any
import time

class KeyValueStore:
    def __init__(self):
        self.kvstore: dict[str,Entry] = {}
        self.ordered_dict = LRUManager()

    def set(self,key,value:Any, ttl=None):
        entry = Entry(
            # key,
            value,
            created_at=time.monotonic(),
            expired_at=time.monotonic() + ttl if ttl else None,
            metadata={}
        )
        
        self.kvstore[key] = entry
        self.ordered_dict.touch(key)


    def get(self):
        pass

    def delete(self):
        pass

