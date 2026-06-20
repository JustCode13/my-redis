

import time
from functools import wraps


def retry(
    retries: int = 3,
    base_delay: float = 1,
    exceptions=(Exception,)
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)

                except exceptions as e:
                    print(f"Attempt {attempt} failed: {e}")

                    if attempt == retries:
                        raise

                    time.sleep(base_delay)

        return wrapper

    return decorator