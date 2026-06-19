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

        

    def get(self,key):
        if key not in self.kvstore:
            return None
        
        entry_obj = self.kvstore[key]
        now = time.monotonic()

        if entry_obj.expired_at is not None and now > entry_obj.expired_at:
                print(f"key: {key} has been expired.")
                del self.kvstore[key]
                self.ordered_dict.remove(key)
                return None
        else:
            self.ordered_dict.touch(key)
            return entry_obj.value


    def delete(self,key):
        if key not in self.kvstore:
            return False
        
        del self.kvstore[key]

        self.ordered_dict.remove(key)

        self.file_storage.save(self.kvstore)    
    
        return True
    
    def exists(self,key):
        if key not in self.kvstore:
            return {"exists": False}
        
        entry_obj = self.kvstore[key]
        now = time.monotonic()

        if entry_obj.expired_at is not None and now > entry_obj.expired_at:

            del self.kvstore[key]

            self.ordered_dict.remove(key)

            self.file_storage.save(self.kvstore) 

            return {"exists":True,"expired":True}
        
        return {"exists":True,"expired":False}
        

    def clear(self):
        self.kvstore = {}
        self.ordered_dict.remove_all()
        self.file_storage.save(self.kvstore)
            

    def size(self):
        kvstore_size = len(self.kvstore)
        return kvstore_size

    def _evict_if_needed(self):
        if self.ordered_dict.is_full():
            self.ordered_dict.oldest_key()
        else:
            return
        
    def _is_expired(self, entry):
        now = time.monotonic()
        if entry.expired_at is not None:
            if now > entry.expired_at:
                return True
        else:
            return False
        
    def _remove_key(self,key):
        if key not in self.kvstore:
            return False
        
        del self.kvstore[key]

        self.ordered_dict.remove(key)

        self.file_storage.save(self.kvstore)
        
        return True