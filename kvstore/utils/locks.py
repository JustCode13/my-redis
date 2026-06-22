import threading


def create_lock():
    return threading.RLock()


def create_simple_lock():
    return threading.Lock()

