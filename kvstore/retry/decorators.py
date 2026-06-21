import time
import random
from functools import wraps
from .backoff import ExponentialBackoff
from ..utils import info_logger


def retry(
    retries: int = 3,
    backoff=None,
    exceptions=(Exception,)
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            b = backoff or ExponentialBackoff()

            for attempt in range(1, retries + 1):
                try:
                    result = func(*args, **kwargs)
                    b.reset()
                    return result

                except exceptions as e:
                    info_logger(f"Attempt {attempt} failed: {e}")

                    if attempt == retries:
                        raise
                    
                    delay = with_jitter(b.next_delay())
                    time.sleep(delay)

        return wrapper

    return decorator


def with_jitter(delay: float):
    return delay + random.uniform(0,2)