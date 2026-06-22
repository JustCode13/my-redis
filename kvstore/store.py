from .models import Entry
from .cache import LRUManager
from .persistence import FileStorage
from .ttl import ExpirationManager
from .workers import SweeperThread
from .utils import create_lock, create_simple_lock, monotonic_now, error_logger, info_logger
from .references import WeakReferencePool

from typing import Any
import threading
import time


'''

set(self,key,value:Any, ttl=None)

'''
class KeyValueStore:
    def __init__(self):
        self.kvstore: dict[str,Entry] = {}
        self.ordered_dict = LRUManager()
        self.file_storage = FileStorage()
        self.expiration_manager = ExpirationManager()
        self.weak_reference_pool = WeakReferencePool()
        self.lock = create_lock()
        self.sweeper = SweeperThread(self)
        self.sweeper.start()

    def set(self,key,value:Any, ttl=None):
        try:
            entry = Entry(
                # key,
                value,
                created_at=self.expiration_manager.current_time(),
                expired_at=self.expiration_manager.calculate_expire_time(ttl),
                metadata={}
            )
            with self.lock:
                self.kvstore[key] = entry
                self.weak_reference_pool.add(key)
                if not self.ordered_dict.is_full():
                    self.ordered_dict.touch(key)
                else:
                    oldest_key = self.ordered_dict.oldest_key()
                    del self.kvstore[oldest_key]

                    self.weak_reference_pool.remove(key)

                    self.ordered_dict.touch(key)
                
            self.file_storage.save(self.kvstore)
        except Exception as e:
            error_logger(e)

        

    def get(self,key):
        if key not in self.kvstore:
            return None
        
        entry_obj = self.kvstore[key]
        now = monotonic_now()

        if entry_obj.expired_at is not None and now > entry_obj.expired_at:
                with self.lock:
                    info_logger(f"key: {key} has been expired.")
                    del self.kvstore[key]

                    self.weak_reference_pool.remove(key)

                    self.ordered_dict.remove(key)
                    
                    return None
        else:
            with self.lock:
                self.ordered_dict.touch(key)
            return entry_obj.value


    def delete(self,key):
        if key not in self.kvstore:
            return False
        with self.lock:
            del self.kvstore[key]

            self.weak_reference_pool.remove(key)

            self.ordered_dict.remove(key)

        self.file_storage.save(self.kvstore)    
    
        return True
    
    def exists(self,key):
        if key not in self.kvstore:
            return {"exists": False}
        
        entry_obj = self.kvstore[key]
        now = monotonic_now()

        if entry_obj.expired_at is not None and now > entry_obj.expired_at:
            with self.lock:
                del self.kvstore[key]

                self.weak_reference_pool.remove(key)

                self.ordered_dict.remove(key)

            self.file_storage.save(self.kvstore) 

            return {"exists":True,"expired":True}
        
        return {"exists":True,"expired":False}
        

    def clear(self):
        with self.lock:
            self.kvstore = {}
            self.ordered_dict.remove_all()
        self.file_storage.save(self.kvstore)
            

    def size(self):
        kvstore_size = len(self.kvstore)
        return kvstore_size

    def _evict_if_needed(self):
        if self.ordered_dict.is_full():
            with self.lock:
                self.ordered_dict.oldest_key()
        else:
            return
        
    def _is_expired(self, entry):
        now = monotonic_now()
        if entry.expired_at is not None:
            if now > entry.expired_at:
                return True
        else:
            return False
        
    def _remove_key(self,key):
        if key not in self.kvstore:
            return False
        
        with self.lock:
            del self.kvstore[key]

            self.weak_reference_pool.remove(key)

            self.ordered_dict.remove(key)

        self.file_storage.save(self.kvstore)

        return True
    
    def _load(self):
        self.kvstore = self.file_storage.load()

        now = monotonic_now()

        for k, v in self.kvstore.items():
            if v.expired_at is not None and now > v.expired_at:
                with self.lock:
                    del self.kvstore[key]

                    self.weak_reference_pool.remove(key)

                    self.ordered_dict.remove(key)

        keys = list(self.kvstore.keys())
        with self.lock:
            self.ordered_dict.remove_all()
        
        with self.lock:
            for key in keys:
                self.ordered_dict.touch(key)
        
    def _save(self):
        self.file_storage.save(self.kvstore)

    def close(self):
        self.sweeper.stop()