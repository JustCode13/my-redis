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
            self.ordered_dict.touch("hello")
        else:
            self.ordered_dict.oldest_key()
            self.ordered_dict.touch(key)
            self.ordered_dict.touch("hello")

        
        self.file_storage.save(self.kvstore)

        print(self.kvstore["otp"].created_at)
        print(self.kvstore["otp"].expired_at)
        

    def get(self,key):
        if key in self.kvstore:
            entry_obj = self.kvstore[key]
            now = time.monotonic()

            if not entry_obj.expired_at is None and now > entry_obj.expired_at:
                    print(f"key: {key} has been expired.")
                    self.kvstore.pop(key)
                    self.ordered_dict.remove(key)
            else:
                self.ordered_dict.touch(key)
                return self.kvstore[key]
        else:
            print(f"key {key} doesn't exists.")

    def delete(self):
        pass

