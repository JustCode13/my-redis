import time

class ExpirationManager:
    def __init__(self):
        pass

    def calculate_expire_time(ttl: float | None):
        now = time.monotonic()
        if ttl is not None:
            return now + ttl
        else:
            return None