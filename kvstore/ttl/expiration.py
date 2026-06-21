import time
from ..utils import monotonic_now

class ExpirationManager:
    def __init__(self):
        pass

    def calculate_expire_time(self,ttl: float | None):
        if ttl is not None:
            return self.current_time() + ttl
        else:
            return None
        
    def current_time(self):
        return monotonic_now()
    
    def is_expired(self,expired_time: float | None):
        if expired_time is not None and self.current_time() > expired_time:
            return True
        else:
            return False
        
    def remaining_time(self,expired_time: float | None):
        if expired_time is None:
            return None
        elif self.current_time() < expired_time:
            return expired_time - self.current_time()
        
        else:
            return 0