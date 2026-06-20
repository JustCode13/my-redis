

class ExponentialBackoff:
    def __init__(self,initial_delay=1,factor=2,max_delay=60):
        self.initial_delay = initial_delay
        self.factor = factor
        self.max_delay = max_delay

    def next_delay(self):   
        current_delay = self.initial_delay
        self.initial_delay *= self.factor
        return current_delay if current_delay < 60 else 60
    
    def reset(self):
        self.initial_delay = 1