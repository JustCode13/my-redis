import weakref
from typing import Any

class WeakReferencePool:
    def __init__(self):
        self.store = {}

    def add(self, key, obj):
        self.store[key] = weakref.ref(obj)

    def get(self, key):
        ref = self.store.get(key)
        return ref() if ref else None

    def remove(self, key):
        self.store.pop(key, None)