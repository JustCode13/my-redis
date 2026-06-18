from .models import Entry
from .cache import LRUManager
from .persistence import FileStorage

from typing import Any
import time


'''

set(self,key,value:Any, ttl=None)

'''
class KeyValueStore:
    def __init__(self):
        self.kvstore: dict[str,Entry] = {}
        self.ordered_dict = LRUManager()
        self.file_storage = FileStorage()

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
        
        self.file_storage.save(self.kvstore)
        self.kvstore = self.file_storage.load()
        

    def get(self):
        pass

    def delete(self):
        pass

