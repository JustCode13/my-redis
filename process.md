Store.py

created a class name "KeyValueStore" because it relates with project and is a main class

    __init__

    Initializes "kvstore" dict, and also "LRMManager" class

    set(self,key,value:Any, ttl=None)
    takes 3 arguments, gives value, created_at, expired_at, metada if to "Entry" class

    add that key in "kvstore" dict and give value "entry" obj
    and also add that key inside "ordered_dict" obj


entry.py 

it creates a dataclass name "Entry" which holds value, created_at, expired_at, metadata

lru_cache.py

creates an LRUManager class 

    init

    holds ordered_dict objc 
    and max_size which is five 

    