import threading
import time


class SweeperThread:
    def __init__(self,store):
        self.store = store
        self.interval = 30
        self.event = threading.Event()
        self.thread = None
        
    def start(self):
        if self.thread and self.thread.is_alive():
            return
        self.event.clear()
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()

    def stop(self):
        self.event.set()

        if self.thread:
            self.thread.join()

    def run (self):
        while not self.event.wait(timeout=self.interval):
            try:
                self._cleanup_expired()
            except Exception as e:
                print(f"Sweeper error: {e}")


    def _cleanup_expired(self):
        expired_keys = []

        with self.store.lock:
            for key, entry in self.store.kvstore.items():
                is_expired = self.store.expiration_manager.is_expired(entry.expired_at)
                if is_expired:
                    expired_keys.append(key)

            for key in expired_keys:
                self.store._remove_key(key)

        if expired_keys:
            self.store._save()
 