from collections import OrderedDict

class LRUManager:
    def __init__(self):
        self.ordered_dict = OrderedDict()
        self.max_size = 5

    def touch(self,key):
        if key in self.ordered_dict:
            self.ordered_dict.move_to_end(key)

        self.ordered_dict[key] = None
        print(self.ordered_dict)


    def remove(self,key):
        if key in self.ordered_dict:
            self.ordered_dict.pop(key)

    def oldest_key(self):
        old_key = list(self.ordered_dict.keys())[0]
        self.ordered_dict.popitem(last=False)
        return old_key
    
    def is_full(self):
        if len(self.ordered_dict) == self.max_size:
            return True
        else:
            return False
        
    def size(self):
        return len(self.ordered_dict)
    
    def get_keys(self):
        keys = self.ordered_dict.keys()
        return list(keys)
