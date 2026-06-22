---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
what problem does it solves? ^ZYTLxABk

1. fast data lookup ^5GnqiEga

Files ^OX1Hzp3Y

Databases ^eHRJ9CtV

By Key ^Rfduhzxy

Searching Through ^SImZvcDD

slow ^ZtNRTkDh

fast ^Lh3gaZGe

slow ^mFqgQjW9

What is Cache? ^myoaF5qd

Supermarket = slow, far away (database) ^vfwdBlUo

Refrigerator = fast, nearby (cache) ^tXCG0yRA

Food you use often is kept in the fridge so you don't go to the supermarket every time. ^nkGrDpad

set(
    key,
    value,
    ttl=None
)
 ^lXi41cBm

set(
   "otp", 
    {"userid":"123","name":"tea","age":20}
    ) ^6OZnSCOP

It means instead of storing only:

store["otp"] = "123456"

we store extra information too:

Entry
├── key = "otp"
├── value = "123456"
├── created_time
├── expire_time
└── metadata ^XBeR8EPW

Example:

entry = Entry(
    key="otp",
    value="123456",
    expire_time=...
) ^rJdN4D7y

Entry is usually a dataclass or class.
 ^0pER5p4R

Acquire lock

Before touching shared data:

with self.lock:

Purpose:

Prevent two threads modifying data together.lock ^EYxLgXzi

Put entry inside dictionary

Store:

self.store["otp:user123"] = entry

Dictionary becomes:

{
 "otp:user123": Entry(...)
}

Dictionary gives O(1) lookup. ^q3bBxgSE

Update LRU

Also add key to OrderedDict.

self.lru["otp:user123"] = None

LRU:

otp:user123

Newest item always goes to end. ^jyoABXKw

Save to disk

Convert dict into JSON.

Temporary file:

cache.tmp

Write data there.

Then:

os.replace(
    temp_file,
    real_file
)

Now:

store.json

contains:

{
 "otp:user123":"648291"
}

Even after restart data survives. ^5vQBTnej

weak ref ^lTUcqgEg

OBJ ^vtqeV0jL

user ^chSNOG3d

user2 ^yrf9h9TZ

OBJ ^8LhDvotx

user ^rS0xmTtN

user2 ^trHIQ4tG

weakref ^5vTNze9t

ref = 2 ^PLYTvrkV

ref = 1 ^9K3DQmvW

# Main storage dictionary

data = {
    "username": {
        "value": "tea",
        "created_at": 1750123456.12,
        "expire_at": 1750127056.12,   # None if no TTL
        "type": "string"
    },

    "age": {
        "value": 20,
        "created_at": 1750123460.55,
        "expire_at": None,
        "type": "integer"
    },

    "session:abc123": {
        "value": {
            "user_id": 42,
            "role": "admin"
        },
        "created_at": 1750123470.80,
        "expire_at": 1750127070.80,
        "type": "dict"
    }
} ^pT0RoSlP

In memory key-value database with persistence ^cMZ9nxd6

set ^LuVZDepT

get ^rHEBAKnd

del ^2IDf7GcU

key_value_store/
│
├── main.py
│   └── Example usage / testing
│
├── kvstore/
│   │
│   ├── __init__.py
│   │
│   ├── store.py
│   │   └── class KeyValueStore
│   │       ├── __init__()
│   │       ├── set(key, value, ttl=None)
│   │       ├── get(key)
│   │       ├── delete(key)
│   │       ├── exists(key)
│   │       ├── clear()
│   │       ├── size()
│   │       ├── _evict_if_needed()
│   │       ├── _is_expired(entry)
│   │       ├── _remove_key(key)
│   │       ├── _load()
│   │       ├── _save()
│   │       └── close()
│   │
│   ├── models/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   └── entry.py
│   │       └── @dataclass Entry
│   │           ├── key
│   │           ├── value
│   │           ├── created_at
│   │           ├── expire_at
│   │           └── metadata
│   │
│   ├── cache/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   └── lru_cache.py
│   │       └── class LRUManager
│   │           ├── __init__()
│   │           ├── touch(key)
│   │           ├── remove(key)
│   │           ├── oldest_key()
│   │           ├── is_full()
│   │           └── size()
│   │
│   ├── persistence/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   ├── serializer.py
│   │   │   └── class JsonSerializer
│   │   │       ├── serialize()
│   │   │       └── deserialize()
│   │   │
│   │   └── storage.py
│   │       └── class FileStorage
│   │           ├── __init__()
│   │           ├── save()
│   │           ├── load()
│   │           ├── _write_temp()
│   │           └── _atomic_replace()
│   │
│   ├── ttl/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   └── expiration.py
│   │       └── class ExpirationManager
│   │           ├── calculate_expire_time()
│   │           ├── is_expired()
│   │           └── remaining_time()
│   │
│   ├── workers/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   └── sweeper.py
│   │       └── class SweeperThread
│   │           ├── __init__()
│   │           ├── start()
│   │           ├── stop()
│   │           ├── run()
│   │           └── _cleanup_expired()
│   │
│   ├── retry/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   ├── backoff.py
│   │   │   └── class ExponentialBackoff
│   │   │       ├── next_delay()
│   │   │       └── reset()
│   │   │
│   │   └── decorators.py
│   │       ├── retry()
│   │       └── with_jitter()
│   │
│   ├── utils/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   ├── clock.py
│   │   │   └── monotonic_now()
│   │   │
│   │   ├── logger.py
│   │   │   └── get_logger()
│   │   │
│   │   └── locks.py
│   │       └── create_lock()
│   │
│   ├── references/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   └── weakrefs.py
│   │       └── class WeakReferencePool
│   │           ├── add()
│   │           ├── get()
│   │           └── remove()
│   │
│   └── exceptions/
│       │
│       ├── __init__.py
│       │
│       └── errors.py
│           ├── StorageError
│           ├── SerializationError
│           └── KeyExpiredError
│
└── tests/
    │
    ├── test_store.py
    ├── test_lru.py
    ├── test_ttl.py
    ├── test_storage.py
    └── test_retry.py ^yPbVXbUR

PROGRAM START

1. Create empty dict
   → key -> Entry object storage.

2. Create empty OrderedDict
   → used for LRU (Least Recently Used) order.

3. Create RLock
   → protects shared data.

4. Start background daemon thread
   → periodically removes expired keys.

5. Load saved file from disk
   → restore old data into memory.

----------------------------------------

USER CALLS

set(key, value, ttl=None)

6. Parameters are:
   → key = identifier
   → value = actual data
   → ttl = expiration seconds (optional)

7. Create Entry object
   → a small object holding:
      value
      created_time
      expire_time

8. Put Entry into dict
   → dict[key] = Entry

9. Update LRU order
   → OrderedDict[key] = None
   → newest keys go to the end.

10. Check cache size limit
    → if too many keys, remove oldest one.

11. Save current data
    → convert Entry objects into JSON/Pickle data.

12. Write data to temporary file.

13. Replace old file with temp file
    → os.replace() makes saving crash-safe.

----------------------------------------

USER CALLS

get(key)

14. Find key inside dict.

15. Get Entry object
    → contains value, created_time, expire_time.

16. Check if expired
    → compare expire_time with time.monotonic().

17. If expired
    → delete from dict and OrderedDict.

18. Otherwise
    → move key to end of OrderedDict.
    → marks it as recently used.

19. Return Entry.value.

----------------------------------------

USER CALLS

delete(key)

20. Remove key from dict.

21. Remove same key from OrderedDict.

22. Save changes to disk.

----------------------------------------

BACKGROUND THREAD

23. Sleep for some seconds.

24. Scan all entries.

25. Check expiration times.

26. Remove expired entries from dict.

27. Remove same keys from OrderedDict.

28. Save changes if something was deleted.

29. Repeat forever.

----------------------------------------

IF CACHE IS FULL

30. OrderedDict keeps keys like:

   A B C D

31. User accesses B

   A C D B

32. Need space for E

33. Remove first key A
    → least recently used (LRU).

34. Remove A from dict too.

35. Insert E.

----------------------------------------

PROGRAM CLOSES

36. Latest data already exists in file.

----------------------------------------

NEXT PROGRAM START

37. Load file.

38. Recreate Entry objects.

39. Put them back into dict.

40. Continue working normally. ^Y6CnFg7A

set(self,key,value:Any, ttl=None) ^ewStr175

set("otp",{"userid":"123","name":"tea","age":20}) ^dUBAkdZu

value: Any
created_at: float
expired_at: float | None
metadata: dict[str,Any] ^ZybnH82M

Entry dataclass ^Xi46mE9x

LRUManager class ^HyAYO04m

touch - moves a key  to the end otherwise creates it ^aAf8JaWd

init - initialize ordereddict and max_size ^5dyL3o5D

remove - if key is there, remove it ^cZpslXHW

oldest-key - returns oldest, first key ^7bmY2VmV

is_full - return true or false ^NiUsPRHF

size - returns length of ordereddict ^wYO8r7cA

get_keys - returns all keys in list format ^R8qVcc0r

key_value_store/
│
├── main.py
│   └── Example usage / testing
│
├── kvstore/
│   │
│   ├── __init__.py
│   │
│   ├── store.py
│   │   └── class KeyValueStore
│   │       │
│   │       ├── _data: dict[str, Entry]
│   │       ├── _lru: OrderedDict[str, None]
│   │       ├── _lock: threading.RLock
│   │       ├── _storage: StorageEngine
│   │       ├── _cleaner: ExpiryCleaner
│   │       ├── _max_size: int
│   │       ├── _default_ttl: float | None
│   │       │
│   │       ├── __init__(
│   │       │       file_path: str,
│   │       │       max_size: int = 1000,
│   │       │       default_ttl: float | None = None
│   │       │   )
│   │       │
│   │       ├── set(
│   │       │       key: str,
│   │       │       value: Any,
│   │       │       ttl: float | None = None
│   │       │   ) -> None
│   │       │
│   │       ├── get(key: str) -> Any | None
│   │       ├── delete(key: str) -> bool
│   │       ├── exists(key: str) -> bool
│   │       ├── clear() -> None
│   │       ├── size() -> int
│   │       ├── keys() -> list[str]
│   │       ├── values() -> list[Any]
│   │       ├── items() -> list[tuple[str, Any]]
│   │       ├── close() -> None
│   │       │
│   │       ├── _is_expired(entry: Entry) -> bool
│   │       ├── _remove_key(key: str) -> None
│   │       ├── _update_lru(key: str) -> None
│   │       ├── _evict_if_needed() -> None
│   │       ├── _load() -> None
│   │       └── _save() -> None
│   │
│   ├── models/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   └── entry.py
│   │       └── @dataclass Entry
│   │           ├── key: str
│   │           ├── value: Any
│   │           ├── created_at: float
│   │           ├── expire_at: float | None
│   │           └── metadata: dict[str, Any]
│   │
│   ├── persistence/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   ├── storage.py
│   │   │   └── class StorageEngine
│   │   │       ├── file_path: Path
│   │   │       ├── serializer: Serializer
│   │   │       ├── save(data: dict[str, Entry]) -> None
│   │   │       ├── load() -> dict[str, Entry]
│   │   │       ├── _write_temp_file(payload: str | bytes) -> Path
│   │   │       └── _atomic_replace(temp_file: Path) -> None
│   │   │
│   │   ├── serializers/
│   │   │   │
│   │   │   ├── json_serializer.py
│   │   │   │   └── class JsonSerializer
│   │   │   │       ├── serialize(data: dict[str, Entry]) -> str
│   │   │   │       └── deserialize(raw: str) -> dict[str, Entry]
│   │   │   │
│   │   │   └── pickle_serializer.py
│   │   │       └── class PickleSerializer
│   │   │           ├── serialize(data: dict[str, Entry]) -> bytes
│   │   │           └── deserialize(raw: bytes) -> dict[str, Entry]
│   │
│   ├── cache/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   └── lru_cache.py
│   │       └── class LRUManager
│   │           ├── _order: OrderedDict[str, None]
│   │           ├── touch(key: str) -> None
│   │           ├── remove(key: str) -> None
│   │           ├── oldest() -> str | None
│   │           ├── size() -> int
│   │           └── clear() -> None
│   │
│   ├── threads/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   └── cleaner.py
│   │       └── class ExpiryCleaner
│   │           ├── interval: float
│   │           ├── thread: threading.Thread
│   │           ├── running: bool
│   │           ├── start() -> None
│   │           ├── stop() -> None
│   │           └── _run() -> None
│   │
│   ├── decorators/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   ├── retry.py
│   │   │   └── retry(
│   │   │           retries: int,
│   │   │           base_delay: float
│   │   │       )
│   │   │
│   │   └── synchronized.py
│   │       └── synchronized(lock: threading.RLock)
│   │
│   ├── utils/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   ├── time_utils.py
│   │   │   ├── now() -> float
│   │   │   ├── expiry_from_ttl(ttl: float | None) -> float | None
│   │   │   └── is_expired(expire_at: float | None) -> bool
│   │   │
│   │   ├── backoff.py
│   │   │   ├── exponential_delay(
│   │   │   │       attempt: int
│   │   │   │   ) -> float
│   │   │   └── random_jitter() -> float
│   │   │
│   │   ├── weakrefs.py
│   │   │   └── create_weak_reference(obj: Any) -> weakref.ref
│   │   │
│   │   └── logger.py
│   │       └── logger: logging.Logger
│   │
│   ├── exceptions/
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   └── errors.py
│   │       ├── class KVStoreError(Exception)
│   │       ├── class SerializationError(KVStoreError)
│   │       ├── class PersistenceError(KVStoreError)
│   │       └── class KeyExpiredError(KVStoreError)
│   │
│   └── types/
│       │
│       ├── __init__.py
│       │
│       └── aliases.py
│           ├── Key = str
│           ├── Value = Any
│           ├── Metadata = dict[str, Any]
│           └── StoreData = dict[str, Entry]
│
└── tests/
    │
    ├── test_store.py
    ├── test_lru.py
    ├── test_persistence.py
    ├── test_serializers.py
    ├── test_expiry.py
    └── test_retry.py ^OkSWk4xs

serialize and encode
and deserialize decode
using json or pickle ^iXC21bTk

add to_dict in Entry class ^Y2j4DqBL

storage.py

save

save to temp.json first
then replace it with
data.json

load

load data.json file 
and desrialize it and return data

write_temp

get data and serialize and store 
in temp.json file

_atomic_replace

replace temp.json with data.json ^9C2sBCIl

store.py


get method


remove if key is expired

touch the key

and return entry obj


delete method

delete key from kvstore

remove from ordereddict

save new kvstore data in file

 ^Ebm5wiNF

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

    return decorator ^rYdJfmWg

from retry import retry

counter = 0


@retry(retries=3, base_delay=2)
def fetch_data():
    global counter

    counter += 1

    print(f"Calling API... attempt {counter}")

    if counter < 3:
        raise ConnectionError("Network error")

    return "Data received"


result = fetch_data()

print(result) ^DeSzZ0vX

def greet():
    print("Before")
    print("Hello")
    print("After") ^64gBREdY

def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper ^ILRWbwNt

@my_decorator
def greet():
    print("Hello") ^vesumT9c

%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebR4ARniaOiCEfQQOKGZuAG1wMFAwYogSbggALQBNABUAGUwAQQAhAGsU4shYRHKoLCgOksxuZwSADjixhIBWHgBOABYABmmA

Zim56YB2fhKYEdWlse05zdWt7dW5niXVgDZdyAoSdW5V+8epBEJlaW4eBafazKYLcJafZhQUhsVoIADCbHwbFI5QAxAkEBiMYNIJpcNhWspoUIOMQEUiURIodZmHBcIEsjiIAAzQj4fAAZVgoIkgg8TMh0NhAHUXpJ/hCoTCEFyYDz0Hyyp9ib8OOEcmgEp82HTsGp9pqluCCpAicI4ABJYga1D5TqQQgAKUaNWUACs7tgAOLKIStLYwVZwKoACS

qAEc4RATQBdT7M8gZK3cDhCdmfQikrDlXBLJnE0lq5g21Ppk0QMIIYjcBKnMZbOZbBanT6MFjsLia5utpisTgAOU4Yhrdx4WzGd0ntYzzAAImk+tW0MyCGFPpphKSAKLBDJZG25OPloRwYi4Rc18czOZ3LZbO4JBIPctIglV7gr/Br8t9TADCQUJI56oHA0KaLuqDEGw4SoGoqB8owzAAPz5pQNT9OUgHAaBdgQVBMFwQh4QofGnBQByhBGOIvDG

p0LJkQAYrg+hsgaqCrJ8v5QI0RDKJ26DBMyAw9qQUDmAQPE/Px0A6kyehZLgmZMMmaClvg2qkD8mYEOhf6YUBUAgWBeHQcwsGGURyFMrgQhQGwABK4SUdRUJCAgnxEGqIbfL8/6oEkfDlkBzC6VAdSZu0y6ru5L4RSmab4AUAC+uxFCUZQSNMXocOGhBbsouBMt01HQBhnzDGgow8Hc2jvOsCxrNMSwLHeayfGxzg8O82h3BOTZjEcSzjqsDWfM8

xCvGgPA8GMnySD5fxTYC5bAvKtElIK0rksiaJYpiSDrvihIFmSiI7VS5AcLS9KZMJ5asuysryhWiJKuWm0imKErvVKsJPSVirVsqwiquqNbarq+o1kanxmieVoHiaDrOq6Hrer6/qBsGYaRtGnRHnRCbMQgKmoGpGZZhV6C4Ak+absQRYlglEIIO+moXIsYznFsWrlm2fb8asCQcXzvYdoOHDDl26xc0sXXTDO87BBeUVfjFdEbiSxA7ukt0HgTJ

QnmeKv+Ve0w3neD5Ph5bBvkuqCft+dFceUSQO6EhnG7gqBIjCJ6oRQoWu9o7uQpB57e77rT+6RWQUVR/zrZAzKMcxrFvJx/SSXx5SCXddFtmJ7jZ9JdlwHJZGKWqpCk+T5bIlpHA6RhEhuyuYdez7bB++XQK2Q5TkJ2grnqyUnkIN5PyLf58RzaEoXhRwkXu2rHlxapCXJal5YZegHIWvoFT0Ngs6zkV8AlS75UjAkzXaI+T53usCRbGObXlh1T6

rNo0wtWMLWrC6osC4y06LjUmqbJOXwp5+VrNoLm7wEjzDGBMKYAJnx0VWtRKBH14RnUpOgdE+1sSHQJHDUk20CHQEutdBk+cSgPU5NyAGr0gY/SFAgUUE1xRTUlBw/65RAZ0z8JIRm4N66Q1gNDKBcNLTWjyEjUoKN3Seh9H6AMQZQwRijLGeMiYSb2zrnRTMxBswSFwDwYRhYwYbzLHRSs9t1hjifGMc2IkBbcAWMsdx4shzUSFo+c4CxebGLnA

uNmK8nYlE1tuXcesFH2jSsY+2EBiAAFk4RbmIAARX7NMHEJRio5lINCKgSMUpIySelFJrQH7TGmAANWFAUroF9imlLxp0CpiSkYOhSV6AA0ggNMyg4BzBadANp5iSlsDKfaJKujjynnPBEl+Ew5b3hWE+BWL5bawnto7UeXQW57xCKISQmZlCoBqJIFU4plRoRORADkZzsAXI4Fcm5dymQpzjs5EcP8xybImKsaYt4thDVjlAJiLF8BsRFs7LOvF

pJ5yZIXcS+AS69Fkp8eSUQlI10Mczeuml/DNz0hIF59I3mXOubckG9yVr90cqwIeqAR5ry8gtWBs8grz36IvZehzOXLzUlvAoSTSg1LSQgN0/YORVGaOfHoEhAjYCiB80E19KozSSLMScEwH6bESKAvYYJtANRuHMFY95/6HHeHMMaX1NRPh6pOO4YLmzBOWKOOa3LobfxaokOY/8JyALQUCTV2C+FbXwbtYhB1yx4jISdShvQaF0joT8tkTC5Qs

P5DGz63Dvr2N+jKZhgjWHCNBsWcRdEdT4ihoaGRxI5GI3tEol0Kj0bqKxlo3GizCb6NrsS4xlMcyrCsQzGxqAqmTJVexE03SNqs3tveaYriUELARSUfmHYayJB8QOPx3ABq3ESK4x1O8wnKwicKpN9MdZ7myAkzoVTWkLtKnpR41TygAHkAAaCQQxGDgKsKonTijLuKO+qV5RBnDPwKM8ZP6P0lXpB08pg7DbLJNmsm4Y47hbI9SK+Kdix57LvdF

OeIUBXr0iQgcVMGd4pMA8B0D4HlWXzKuWKmnU1j3zmO8NYE4FgoPGDuyAbFlj33E2MENNwjQQpvE64taAiN+pgf8U1kAsFgkLXgik8a9pMmTcdemaaLo0kzbdbNj0K28irQZrhEDAqlv4Q5hUTnyx3LEZqCGjapHNthq2hGr70rKLRmozGmicY6Pxno4mI7yMOnHeYhYU6/Nk1HSu1ZRxrj/xWEewWOxRbtmPZLai8xrX3AbDs0JSsEAm3vRrR9c

T9x5ANpAI2Kz7ZrOvOCq2pW6Kvn2R+ajP4nkMTZOEAOQcJDTeCDkKF8cqtQN+dCtOcKM6Tb/FiiQYgshMDRUwIuElkXlBYsQYgWryx4qrspaVsr5WKqZA3Ml+B5voEW7NvudkWX/OHqQNynKJ7+s1LyuiwUF70Za2PejYqoPb2SbnKADSGkAH0OR1FaM0R0yhZwY+YBUOYzA7gAAUEAZc4lM9AaqNUgkTXRPjPN75LFOHcBqEwPWzGG2aiH/9b5L

A9dcBYvVbhXFUxAx8xwVj1MfC1MX7PJdBXB/5W4FrX61lDXccNSDI2M/0+w2NRmJBEJM6Q8zWtLPoGpFdGzjJ4w5oEY5gtxui2uYMy7rzbu6K+ZnSEkoDa9RBfVy280YW0B2mMZF1RGMNHY20ZBrrLJh1EpS6UNL1N8nAy1lludRS0CrCXSzCJZ6Fdc2KzWRYxWJZSxohulBEwa/Xsa81ibrWtZPviVHypvT53ce/f33eGAQz2UdHMOEaPINgGg4

UYfKT0mZJyXkiZhfqYzLmV07D3XcOrKvKOJYSChr69ikvMj6ldl23G6vPltG/yCpv2EJj8+UcSAnuPyf0+aefqvrxkYk42gRw00Rw/8jUKws0H8nieqd4t8G6oKuuVqGCJQ4CPC6ukBUOauAIBua0BmNuEA5u+0pmR05Cp0putuGaN0ju90zunmL0vuG0ZaLmaBbmjBHmealaDBkA/uta/mEigWbEQuIWEe8iveHaToXaUW8efacWyeiWSY6el+Y

6piVMEAuAdwmWM6RiuWfWDYzUQ0A0kmDAYsnAp6fOkAe6FW9eNwA0riI0oKis4SByHe0SbWusHWUeKePWeGZsFs94j45hEAo2VGt+iKFK6As4EceIYQy2Pmjy4REAkRUQ0Rv290ZEq2icUKMK6cRemce2F2B2t0x2IkZ2mKBR6AV2N2TOJQ92BKpMQRaOmO2OuO+OhOxOpOFOVOb2pK2kn2TySRuAKRsRmCzKg8LkwORyQRSkk8vkNYkOJQ0OdG5

+qsUSkAnkoqm8SOEqLG5QjocIcAAAqvoJIESHAOTpIM0GMABtkrOK0BQP2HABUFxuUPTnptqv5OsD1EgjcO8BOOzgAu1OapakgrfIsAsIkDMPJlLmgY+DVO6h6pzosAkD6qwZAPNFpoaIGlriGmJogRGitFGkbu5ibudIQntCQkmiQamnGlZvblQfQsnLQRwa7m9MSR7iwV7nQUIrnjWjaIHpAMHk2mHsIfDKIbaIohIajHHr2rFknjvqnklooRT

CoTmFsJobwbOoouvsXl0qXn1lcJsEfjcPVruiYfxOMPycYeVhwHXtRFsAadMMLCNI4bes4aEa4V3u1i+mIW+v3uvl+gyb+hIPZMyMQEIJIEYJgPsOUj+rBiPrUo+PUk0mvrTmoZvjPgsglkssbPvlMIfsfjzKiVMcsdlhnsEW6asVIPyg/rDtFC/pKiPiGWGRGVGc8VSDxsziOEsCcA1GsF/ELB6kVlAWgDJuMBMD8ecBurMEWagdwK/JprMUtDg

dGu7oZqSQQeSdUbiFSRZjSRQdZvSXZrms9NyaucwSWmwdKN7vQaySUDwXyQFiHoITDOWLIpHuKeIbHj2jFongOlmUOoqRfsqWYtTGMOqUzBng4onBOMiQ2FCWVh4kXoEZYTaSelNEcOsDzGJkYYQDek1iEZWTEtrF6frJ8N4bmQNpbAETbNfisZMS7BIM0DAKgEMvsA8oHE8kxSxQgGxWkX8myjcFkVtvCnkdxOURAIdn0CiCURivthUSQFURXAp

HUSknsYcccacecZcdcbcfcY8d0Y3OSn5BAFxaxdZKMayuMSDmfmDhiTPEWYsTWSWXDmsQjpsbPsjkGegAhiMmMm2Rvh0u8Z1FsD/Fuk2GLqcHBTMICZVMLCFVhWsNuggZOEYbOZqPWEAacMEp6kLrcCaWiWrsLHEE+JOACHMEgk1EJkWXpmgDgmWvgYQRSRrDudbnudQgeVmk7vZsyT7reQIEwc6rwJyT1TeWwn7gyllpaYKaHkIa+aFmKdHhFpI

dKT+f2vFsUCnkTAoUBTvFnmoShj5vTPnlqbTjwCXu9Kup4n1PcObMhWadXpaShbaTWMiYAhugCDhXhe3u6biG4c+qRdmb1peOsoRlsk2KRrYkoRRrRQxp8HAGwJmN6R+Z0ItcUEnGjUjF1mAKjWAKMBlezkiTlUaHlahkVffO6mVRVcrmdfaDGPKZCPSFAM0CYpctwHOmkM+vUfvIfMfKfAUhAPoGwKYuUMiJoGoPzayJgFWOTgjYyD6Z0N2U1Ef

qTUAcTWrerUaDTfjOdXRJkMQMzaSKzWgOzV6fUa0DKnKgqkqj+gLULSVKLeLTbZLdLbLX5DjYrUaPyRjbTTrYwYzY0JvvNLgEqeWHrQHaUkHSkhhrMkyEEBuBQARZMYLYwGkiQDLYjcwKKOoN3nLbDXfjDs5XWVscxm/ugEvlkrkjnj+KmdHVQEFeMPAlss4l1MLk2IEZ/OcNoAlfYclbrtCdwDVF4o6fadsHLM1EYeiYuR8d/PUvUssAVsLNutV

YSbVXgW1Y1VuRAGZqQfgXbrQrZl1cefmn1RWANWpkNaudeaeeNSIpNY+UKbNXRG+QtRKV+dFgnmtXIfdGnjtcoSBWoY0OBWzSdQulrR5RdasubAEeOJXghfuoaBgaadac9ehUfrWEghCi6fhRWZMURTnUjYeGRXvroXmTcAWV1BDaWVDWsZRjg3Da7e2ijb0ujWAEsJjT+jjYPQ1C/KChCjcNuqTd1LPb/OzrqvYWA2AHTf+X7aJAbY4B8sAx2hz

bdFzQfEfCfGfDbYLcLRIA7YGSyIQFLcQOnbne7T/J7aTZjb7ZAHrXI0bZqUo6bSkvgI0VjjjnjgTkTiTmTpTtTooto/baQGLfo87cY67eFmjeY8rcw1Y7qT9P7YHSECHbraSOHbMpHe0jHZ8HHbMonZ8MnQgKnWExnVnZIPg0/pMY5WFLWWrPWTsRIAmTMI0s0j/uhumfXd2bfPMNNELPaUgkRjphAB3fFciYlcJu6qlYNdrkAb1DdfLoWQ5YVYA

uTZOHPYcEcE2PlWoSvagHVRwg1ZucQSmrueQe1XSZ1TQd1Sed5myZwoNUWbglfTc3eRNQHvfTNS+U/fNYw0tVKd+R/bIfKVtQYr/elHtbgNbYdXnjOgXqddYxWJdZqCNI+DwGCoenA6YZqLMLXmhf5PJgEk1GLlg99YRX9T3raF4cQ8DU+GQzcK/Ig65SWdoTQzDS5RAPDRnRE+7ahmw7TRw70tM8LlzDzsPd8YI8Ve6ms0aPWA1LExtZKIzXYwo

8bYoso1kKozzRo/zQEyLUE47YoqEyY27cw1E17WAEkBrZa5rXK+Ayk/rSzcqw47rU47sfsUcScaQGcRcVcTcXcQ8U8Vo3bbq8ExLYYy7YjRE6w6azyza9BqfQkxHUk6CzY6k4k8HZk3XaHfgPHXk+WAU0U0a5nWoGU16RUzRgXUKkXba6/l5ZUFAP2PZDUK0LOIys7KmX/p2TqmJm6vUreERqcKcHLDFagM4HcHMPEBCkNPaeVdamO4EWlagGJgu

dPNgQSYbqvauQcwmkc1bhQm1XvQ7gyQY1c8fWNZeeyRef1ewdc1wRAPeXWkHpIs+eHqKT88jMtf8zIXKdI8nD/ZDcBaobgFGLntYhqcywi5A3eNO1/FXuplAk9bi3AecMGg2MS7m53rEu4QQ5SzmSQ5Rf4S/DRWNnRaJYIkiJm37vEcZcwORz8ukYDjREJbCiJbtmJVJLnAgEJCdqJLJeJWXEpfitXMltQxAO9r0V9hWLR39gPJZdwByjZTMdPAF

OW0sZWz9cWRseyHU6XQLQxOGMoNkm6MKAdW27/h2UMCMP/F3feIWaOGcBssO84PaRarVr8X8S1G4uWAu0u6rnZau5gjs3sySVQhvTuzvfu5QRc4TEyTeyfbguebwpfVyc89wa8xqVNU+9IiKW2hE52n8+/V+3+fK9/YBf+7tSqeYpo1C6BxBSJ1BWgOVX8V1Ki7B6gANDi5Vgeo6VMGLoEbhW3uhx6Zh/9Z1kQ7h9S+bINtRVfsR3nWEdR1J3ERx

QkTR1k3xeRAx4Jet9kdtrkax3JUEZx0e+isXHxzindpXCpcm6Jz0U3H0St4tyMf9mMXJxMaDopzyg5dWdU4Xep+sRftp7W3UJIKsAVBUF6Jvf6R2xZ5qGOF3c1/WOcM1HO0YR1FZ7/OONhSgsTfOV54NT55gX54MzVbs2vac6F5buF6cwe4eYfU87e/F/c8NbF2e6l7fW8/wU+Vl3NSIW+3l92gV7KUV5I/ISC2V3/YB1uEA+LzoTWFA7eKPXdda

dwCGh1/XsiQCENCNLcGh3Qw+p6VhwDXRORXh5N1RYRzN4N8cgke3Ee+QMt8Zbb3R/xWtkxzkexKJQd6ijJad+x1SOd3RLUUJ8k0Hrd0ZeUE79JwDmyvJyNtMYVfMWid94/iR2fpp4lMXTW30pdjAGwLgAxNMOGKzwPr0OZ5AFTP/AsCcHLDeLcK/IcLj3RB1Ki1XxcMLHLIkGCvXwyxAAuy4su35P5yUCT0F7CFuxbpScc61dT5FwfZc0fZwXF2f

Z7klyNdfS8+z+l+88+9l++ajRAABluNgABvoBjlAGf2OA0p6Gkl6JoFUAgK0PQF/QBdtTL6lhV9TAxNL1Q3qXL9sqPaNAxb8RUOQAlBv5G3QNRyq2wPrl9St5b0yWHhClmNyBrswpgFwLmK/GFxXoRstDMtqx3KDCgDIsEMyHCHxDzQSIS3CToQOAi4VUApAt5AgAoGEx6OAldbKnGY47Z5uXvI7tx1KIHd+OuKS7sH2u5ic7uVAogbQPoHkDzKz

3WTkDmspx8uUdlZTvnVU54DFB6fQHtnwkBLwvQpAWcHSGL5Q8y+EAKmH0x/j1JTgNhCYC1GHajgeohWevpOEVwkY8e59dYOOyqotQHwU5YJIszsqN9h+gXMnuuQp6T9d2ZBdcjTyi4MIYup7AUMvw5Kr8We1aURBz3rSZdgsPPV9rl0P7H9T+5/KAJf2v6397+j/Z/gwj/Y/9yu/9XAF6G/7gd6uHxVFkaGExbMUKbwFrqAMQ7VR5gMwJBNgPSiw

C9eGHYiobwiZxkUkaSXAAsEIBpIeAXoYYh2n9K10MysZBfDmA5ANIBkmSJYJoBTKfpVhWGH9hABN7Ut0ByHLAURzgEMVvs3cYgKgFz5CBUAQgMIKgDYBCRMgxA1ALCDgCGRMwAAHSyDzQHYmkYgMoAQDwQ2Ajw4QJBE4AAByQyMoGhF2QgR6gSEcwBPBMB9A9IWEIZAQBthmKYkDINoDmxTZ7hMI54a8MhEfC+gHAb4b8P+H0j0RoIkgBCKhGUi4

RHAREagGRHsoURIIzEYgFIA4jSAeI1AASKYBEjCAJI53ht1YFu9duHvfbuJW95lY+BZ3XuBd2UrCC3+N3Qyvd2MoMQKRTwl4W8NpFfDaBjI2CMyJBEJg2RGI6EaaKgjcikRKIgURiKxEijcRTWCUYSPZQyiEApIqPi91T6KDbKU9FQVDmT41NKy/3SGloLgw6CtwzIAZByDdDhg2A/lO9ggHVRvF/8aAc2FXynY3gbC2wQlo5xfh6pLB1UbZIAjH

D90poDYWqMEntQ8wecj4AfjWG3Q9QbwRGepE4jKpGER+IQkLoc0p7UkZ+HVOftFxPaL9i+jPc+g8zLT08T697PghkIELc8vmvPXIUfxP5n8L+WwK/tgBv538H+T/IFlUPA4mJahIYb/rCwXQ6lM+AgRFqgCEx2dAEY7VrmQzV7URxgwuQBBcDvC691BQ3MYSN3lpZ9Ck7bMvrW3oDMgKA+tfAAcSzExk+89obQegGmGzD5hiwg4W00wzzJ5SZw1A

S/HgKYDvxafa7uWTAlJ978P3NTs/kz4NkUkCEpCc0BQlZjWmpfIfJ21QAPhx2/UB8FcC8RyxPOTfG+F1C7pDRRwDqUcF0xnL3MZoXYkcj3xHGbt16448IVTyiGz9qCs4hfiyQXGJDL2p9a9vEJ5JpCt+nPB+p8xKDP0+eeQg8YUOKGnjShF4iob+1K7VCJeOYC0A0Jyyvi8st4ZEisBVwFx7qWLdoWaTAENROc00RsFAn65OE6J8Ag3pBKQGA0fC

aAnnBsmFzXCRhhSJ5ByC9GijxRAAXngjkdqAQIlcKQFQCUBcAzFAABRewUiAASjJEJFSpwo8qb6KqmrcKA1Ad2A1KamtT2poQBAF1JWybc2BWQHbixy4HiVJKxRdUbxz97yVrst2QPkIMezlAOAKYtMRmO4kkoDREnXqdiJ9GGRBpNU0aY1IoDNTUAbUqIlNJmlMpZBDHWPvDiUGRjE+VZBiSnzm4/TNBLE+pugAGQhgoASwZwEICWBehMA/YEMK

MFhmrBCAGORoAMn2E8TVUuYhnDtJh7vjmx9nQCfMHOBTBKxt4eBFcASnrAHwR+FsG4NczNjkWbY//p2N86RiexY7ScHLkHHNhhxwQzSeT20nNUp+e7KcecxnGxC5xxkhIRwgS4X1bmq44vuuP8jb9txDk75nuPyGHiihx4koeePKFXifJN48Fo6AfEgN/E8LJoU+HQYtQIUSvRCrwEAGRTkGiHTYDeD8GWkUprpNKXgxIoTC/SsEvieIRSRQAAMc

IL0EsBgD2RAG6EnpJhKTHUwthOwrcHsIIkZsMyJEqlmRIuGUTBhjLdPoVLSlVMgZhyRMSPgjlRyY5cc7MdD3L4q9TgPULqB6imD1gPU5wSsXAlOBOkbwT4ENMakbEuyoEk9aeATyCHrtSews0IaLOiQtUJZek6cQZJllGTeqJkhWUz2SGWSoWvJB9gKUyHClshOXKCQf33EFCjxJ4s8WUMvEnDgWwnADjmAGSBTIKb4iEubDBRdygBicQZgh064j

ktcSmFvA1lSlhjwJ+DI3jhnG55y8pzdEuWAut7GVHI9oiEeQDsgNSqptvWqRwDVD0hNArUvAAwPemUcHe5QZBaSiYDnhkQqATBR7BGm4KgmBCsgdNLlEZF0KiopacVPyKbSJKRRaSutN945wJAlRAmZACD77SJAkM6GbDPhmIzkZCQVGejMxnYyzpH2CTuQp+CUL0FNC0OFAHoVnJ8Fz0whfNGIXD8LKX0t7gpwT5fdAZsYyYvGKoaVyphMwuYQs

KWFoYs57xJsDVHmZjhhciJcYI50SDwJzYgCYXH4sbD3hh5j8eIPYR4ZgoMev8VSagHHA/wkq1wU4LwwBCWkNJtzcfkQQnEnMl5UsleYyVlnrz5Z0oRWcuIsnzjUhd9WyR8xfYnzkaJQZyRfP1lXyPJxsu+deKCmZ4P+ahOoJbOWFws4m9iN8a/DvBYD3grXYWI9VimIcHwW6X+M6VbygLgZv1DKeS0IbZSKK66JqM4ktIOLwOtEhBeywYZctmGMb

PlkjBxoxKuo26eJR6g846ZigqS1ZVcGqxZLgkNrFPAzVkYOtlAijZ1lh3qKHTUx6YzMdqyDa6M9WITMNsU1MYmslaZrBILG2yakglWwKlVo4zBUpJdB+gwwTCp0boA9GobIxka0jYe1ommE3ltrXGUyNuIabEPim2IBpNAISbaZIFSzY5sipkAfNmnQYalNym5ysuXYqcWbDthuwlRaZ0Ilrd+Jj4YXLVCODNhrUoaYWD30/jHBXqtwXqH/GmVgp

olgBZYMEhsH3AxcE4ZAgVQCFV8JgPMURq9VFbLkiS57NcmOO3aFLp+xS/eqUuPZrzRqlSi9ol2VnJdb2asjLluKyE7ichp89pXrLcnXzPJJs1/r5LBaDLcAaSEZXKv+A2y3xL8EXKFKFhzL0WbsgWGAIfiJB5YyJUCecoDnjDPCyAnKQWvqQbItuGgmibgPOUctEBqNbljE1uX2gcaowE1c1HGAfVOcvUScKhibDwJnEjq7dKKz+UKtAVhtR1ibX

xXlApFMMuGQjKRkoyhAaMjGVjJJWBMQ2TtRFVSqglRtUVljH2oyrZXYqQVJQNVlAHBWtA9BBg9NoG1JU3dz1BrS9eE2vU0qzW9KjajbKiCiQOVGTPUWHRZWeLeVuTflbbRTpCqSmxbUVZsoBkVsKmkqiQABmaAIB7IYwLcOThabV0zOocxuQ127IMyNmAIOrLWCLLSZ2cFqXXE1GnbsbNgw8mmckpmjqShZeSrSZ6p0mTifVh7I8irKDV3MlxzPH

eTfT3kbjH2Uao+TGpaX78tgN/KoI0H7AAYGIboTgDwGaA1AeYQgDHI6FIBqkU1YvNNe/1qHk4X5dXfNVeGqhKZ4OUU/yPMD/EjhCWmwe0j319nYN/ZCA7Dk2ooqH4QC/8QuUES7VYbbhEAC0IZAyA0gbRkIJJu8OZDwR0FtKTgHCmQBAigRkIZEAgFyAAjROsgMrTGB0VlakEI0MFGVoK0cAE6WW4rRKL/DkAbRKcb0WJE4D8i2A+WjgECK3BZBS

AMAIEYABxSQAACkk2n4TxWq3la4ADWjgFNpm30ACAbkebbVvilLaVtqAbAIEF6xn9AxE26bW1rgCEBAgR2jIECMAAopKdoyBRAvY3U4yoltQDJaroqWvoMHQy0tbNIHyd4RwDy2NaitgQUrQtsq2bbHl9WiAI1ua0g7IR/QDrZmC604ietzI7uANqG0jaxty207bCGYpVSytbACrTDtx2rb1tkIwnRAC23Q6TtM2/bSEEXBXaEAdOs7RdoQDM7bt

92prMHQjisK5pHCzgVwrY5CKBIPAn3udh4UCDtRgnCRbZv1FqKnkr297WZEzBpbvtHw37TlsB0wBMdV0dBSVqJ0k6qtVOmnXcCW1Ai4dButrdSE63IhUdHYPrXruG1Qgcdu2/HfNuJ2LbSdu2tbb4Ep2oAatUO83T7tO0M7DtxIlnWTrZ2XbI9XOmbQ9t51RAZBMnCxQoJ+kRilO/08Vb9zjFuUtOYMnTqQEdDEB+wCwWcAGHrkmCqY2wJIDeCCR

+LBcNa4couxmBAEZoY7ITBulHAXBJmS4lSZzKU69QXVG7ITSLJE1iyIhu9fSUe0YRSbnMW80NWvxS53s0uD5RpTv2Pl79FEmmr0Npt036bDNxm0zeZss1eSFSqas2RmuySObf+6FR0ii25xzKeY3mrsFzBDTTla1WG+tZlN2XG9c5psUhh31VXRazlcWp5FuEwDMQfACAPXbdFG06KXdo2lqUCNQBoHZtMACqUbu93YL0DqAP3W5CwPU7g9ZW3A+

gawDnbY9gYiqdoFoNAjTF3BKjuUEgPQHggcB7HYgex0oH6R6B/HUQa92kHUD6BggwgCINm7BDPBtAxQfZ3M6aDdBjgAwfogu9Mi23YSkLsQXcCuOEusolLoD41E9phKEQWH0NHMGoD+gGA+wdd2cHXd3BvA3wewMSG8DIhsQyQZoBCGpDmASgxzsj1yHtA9BlPdHysr2L4+yg7PTGNz3BGmW7lZdKxPKBLA4AW4eyNMDgALB7IVeqjaYOrxV9yqM

wXqK4iHpwFh294b+JRJmCotLgIAsBPjyNWD6/IE83TIJrdX5Kmq888WZEKoTRDpZZSgNevyvZVLF9bq+fbvOsnr7NxXPaNVrN3Gnzd9++vTQZo4BGaTNCQMzRZqs29LTZ/S28YBzSMgdp0YHfpU0PuBywv444OZc1Ff3+QmoQsU1eDXWV+y61IWyBbvmgWAGaWwBqLfAvAMJEkDzFWga8KEAEA4UjU8OFEGwD4BQgZkahWCYhN+GuA7FCTj8e+H/

HATzFb2F7GhPFh3hDUjE8wFhP86FRqhjgXt2Wk8K1RbsjUboa1G7SdRcu8DqIPD4SBETfxzESieBPonwTmJqExydxNAiAjoY9lJYvDEfc5iNinDecpOXRHPKWEiAAxFnBegjAQgRoFAHDDZjXihJd4jcHiA4kmwwuIqrWEGbwpWNk6+qPqrQZ96IE9YPVFry6a5GgEyS3nD/AbBdNuYjYAfQFynmj93VxmApaJqKUdGZ9kmsNUv03mybt5dSqyQ0

rGN2Tml2+jtDMZ01zGj9SxlY2fus0PyahgHDkNmpglPi81ZecEuzjHZrKy18DASTFPdn/zeAFwWvV6i/1ssf9OyjCWHPKBVAKAkB5oEsEGKZzuVMdY4cV3/0vH+so4LqK4gfCDMJTZZWLWyxz1MTGMhe2tvgAAyEBgk2AZoPoHSNHs+ME4aYLEqQTNgPqXUF/S3u3QhVyqoKBjeOFuACMmZMJLxMkuRLE9GjfRsfsJon6T7dJ/p5ebPriHhmzyAx

58+WmX3hq19+80TofMfqTHY1rSyAM0AxzhhJAAyOoFsH7AIAKAAyEUcQDuDRxmgaSYgLTDTOsqBltQmoLfogYkNrqLfM49aqtLlrcWnOAwrcHgogL7j3+x46Nz2V4ceYDfUcLYMt7Ib4tYQKALYd4M8UyDaBkQ2JfZRQB8AFUiWFHo6m8n4TTyQS8JbQP47JLEl9w1JZktyX6Dil9bmwsY6En3eRhLiJoeO6nYNpoumSFSf0M0nDDeo+kyYd5BNZ

VLGBjSxTsksyAdLnAeS/pae6p6Y+gpjPcKYhyim1B4p/PRn2raxGJAdwP9BUA4Acg4Qf6BzTjNtzV6ACEKE4PaU731hxw44aLdJmqi1RxgjpITHVumg98F21UHc5aZmhCscSDY2o92MfMenRx3plo9uTaPT6vzgZoC8Gf6Ohml9KQiM+kOU3jHVNkF9TYolgvwXELyF1C+hf0CYXsLuF/C+scv2bHwWBxUixMtWR5kxMzYCcK13DQXHDgD+2+MLD

rMuEtlw3HZThxQGvGuL7OPqD3zANssBLrl9ww4ZoCB7BtHAYAGVupFgiyt+W4g6sEEMQAm4120neDa+1Q3ogLOlADcCShaXFD9vCTipZ+vg6/rWloG6cLCCg2UAQeyG24ehvEwwbZWhG+TaRtg3Ub6N/E672MtKjTLSKUk+LoEWS7rL0u6k7Locvy6nLWN765Id+sjT8bwNomyQCpsQ2obMN5G/DZCCI2IR9NpYGjckOoBFDNkT6WyjZbjxQr9lF

Tk5VnOUNEcMV8GQLThD4K5gDSCoFmfSs5i8x6pgsSO2tRxBbwz8C4LVbHCo83g8mLU0RheVH5m81Vwao6R3PCYLhiQEaNVD40AhqZ7wFYGOFcS3UtmuSpo6+Z9PvmxNn5kpd+fKWBqF9w1wY0GdVkgWlNB8lTRBdNDazT5c1hC0hZQtoWMLWFoQDhbwvn775hFrYzmAaTZmPFRePM/bAIxmqmN1FjodLAuNjl2c/TECXcaC0PHtlvapszp1bPtnO

zsq0ZYcPTJ9mReHF84e33vAMbTb/Sj67dew0RWGMeG9AGvcwAdmuzDt1YUFWfi1R1gKwa4Fsn/jUW2ITUJIK4lrDy56kw0S0guyuA7ndcncr8YOR5zJKQqY7PqBCgV6jNsWa7XAjPI9VvnWjU+iLn1bp6l3pN1SuTb+YU0jHQL01TfWpr36bU+lGeHu+YnI030auz6ge7wCHs1gZW/8adj3wnvq4jCf89XvxrEybofZww4LUvdC37285h9ni+9ai

ufG2WPaghncuuUDqf22NXpGA56g3V3g1UaB/UhnW9iEHrdR0r2QkZSN+zTKp9bitBWc0Uk+gK2zABtt23T1wbfVh2kNZAboL5rHlqawxWh0sVQK5hxgBdYLY5TCppUyqZ/Vnq3H0XSlZ47MZXAX4JqXqEqtvjrBJMkTRJ1rktWpPGLfj0tAm3SZcr5dcGxNumx7MUcX12bJDaXPCMm282bAVDUiuyAirS2dFa+xAC3BVBMAdQZQABksAbmmQVMUE

juYbDbohMPDMNMOwLOxKBowSZEmOW7A3nuA2wai2PMH7WxUHK5MfbPIn1YOPz6aXB/PyGO3NCHYZuWWNZslRmmlu/F+h2hqD2QYAGOaYIQD/TMhOJzQZgF04WCaAQwcwC0AsByAEXrudD6mABj2uy80ADYYBGGnc3K8po49xZZWfQYAgJgTUG6+pwbO9rHrza4c+CTRZQIz76neLY0GwDhghA7OruASEa2EautkIuyEIBpT/bmAQEQIA8K9h67ng

6geCEEGZDaBRseu8nCIHhphBBXgQRgFkHZQUABRB260G9qFqEBmQMAWlJ3DsgQj0RpAfl3sme3lBSX5Lyl6NhpecdWtDLpl1chZc3R2XEcTl8Wx5f4A+XArxrUK89ZsBRXTr8V7dClcyukmZkbRoq+Vf/bVXbAdV/NE1ejYmbKh5gQtLUPEnhd5l3gVZdLh6GxFBh9M/WmMMSc9XFLwIFS9aBGu6X/Ixl+8nNesuqwIJ3ADa+5dhB7XWrgkIK+Fe

uvYD7ryUZK6gDSv2UtyH1/K8cBKuVXEcfkSG6YC1v2gIYuQQKfT2MtM9n3I24xLSkTnorMRi2xQHoDMBsk5OTAF09VN4z8xiqlYD4sdKtCCsFw4dnVvviepp2YmURtRYXYGpaoguBqP5vBJfzCeU9UFOO3kxQCLYYUjHiPunk7OMHWd/ZzncOd53+ro1v88XYAsnON+im9WRvs1k12pj0FiAA86ecvO3nHzr51UB+d/OAXQLzazZqv21CIMux46l

vetkPqIOfWcZ7w29StdfU3Q5F5el7aTqMXpLcR08dOEAGhz00fF4fhPuTnWW59mc7hvnPSnwwqwTQM0EwDKAOQUvB2w3MyOahrUSQaF0JgbBjPXEJ7jdCcBlwzQISk4VXss6LwqYWrReU/O6bQf/vOrm9besB9pK+r87PRlfYuJX4jX5NMH0hxXbAtV37JiHqC/vwYiaADis4DgABgQAVAFg/YKoBjnJxpI0k/Yf5wBkwAbWLH3kra7Q/BatsN+T

DvUbbNRaQk/BRZHh67KQa0XkXg7a4NNGb3MWF7rFjj+xYHNPWePAIX+JzHkfn34tQr/ERwbV0kBIRjgdVB2HpA46gRXIYrXrurd8v4dYOr3cgBBu1aIdVU+A6N44CzhzAaOkb6gE0C5iDA4QPXUDfpHYH5vRNxb9wB+MtTaD2gBSxwHVtAj1vQ3zgFt9UCIRUAf6FqQkA6ldwe4wYygU8m68SjevV0fr5BA2/DfRtjW8b4EEm+8vtAM347wt66hL

fAfruxrQ9828IGdvegDIPIEa2HfA9C2k70wDO9oALvV3m73d7W9g+nvCBl7zBHe+ffvv0cOAL96jfyjmbbPxaeoYDLxvtD/A5NxJVTeEWhb/32yCj4QN9fTEoPx703Ah8A2ofTbgG1N7h8G7ZvsgIn6QDO8m7xfq39H+D+YpY+9vuPgG/j4R+nekf53rg+T6BGU+9fNP5inT7MgM+vvUcE8Kz7MU62gj73axTO/Lnn353HT/QM0EkD9gMkmdLd07

cNzvFxgXiFucLjWBDRjj5xlvXVFqiep7gXMdBIEuM+oA1g8VYJJzjfda5/4yS+4OOxfgQEXEgua4GnafPmTguNnsLvZ/3Kge8HA1jeUNbc8l32/9S8a5XcmvV2IAjk3LkF5C9heIvUXmL3F4S9JeUvndmhyJ1BdqFCA/dkvoPco+2yLVPe2s9/Ia6/ykX6vddErhGjUXAtJLXBmxcbWSPXjeLtr/UY06dqhP6nET+07E/JyIAboXPi0AAwDJKnLD

gMkM7/A9SMcC9y56Ggwe2vtkXhTAgmDzIx+KTrSooEg1Mhx8anOL+6emzRrZ4Ly7RiB6OeYHh54AWZzu57EOnnpGYTW0Zrc588SwMQAUAYXncDcQ4YHcDMADEHMCdQpABQAUALyBjjz+Gxpl4ZqboBC7BS9sI2BWqD7nC7OyjpFPZQMGDK9ZseF/g15X+TXri68eGwBcAdexLk8gHEe+KgB1A9kAcSNaPEIICNS12Bgb8ib3qQCmIbLuj6wmhWrD

74AwOGr5wAGvlr46KulgDY6BBxHrpzeiPpDYA2TduED/CfQPoCNS+AI9IwAZkMiIwQdkID7EA7vowakKEgJoE5k2gboH6BX4NCLB0Dwh7pRBf6OYFMAVYFYHA6tgfYFm+xPhb7a+rgUCLuBnger7eBjWn4FhwagOkDBBoQeEGmQpgXrSxBShuz6RuDCOwImWnvKqKc25Jom7Yotlim72WabqHznSGgVoHuBqQYYEZBJgdkG5BlgRt7WBV0EUFCAD

gU4FlBLgb5aNaVQY1peB5vj4FAi9QQEFNBBAC0G8ibQVEEdBfJmO7fSk7gbZRiCxHU5zuUVh04wADSPQDk4KYvgABSDtmqZR+Ltqi7HAYKNrgFeCkl0KSSReN1AIEvZOeYt0FvFUbn0lVCcBjg3DKOCzATUD3zrObwPYLgkT8E/DNQriIETp2AFhgFN+fpjgESabfuB6nO/5vX5/Q+Dpc6jGZATc5b6dznRBUBNAQBh0BjQAwFMBLATwBsBHARzr

cBGXov7gsI7tVx7GNoI+IUeL4lR4jgVqjTK3GJZpiwCSCyhWb14qyt4JcwAWqI6L291ti5haeHHi4qBWzPO5qBlZC/5X2b/iPjTA9ANkjGaaoPwEKemVuZ4Tg8QPWDWo3gj7bDsqLN/DTQ8zDkaTcjYMPIcaOVtcDkS3TDeDRa+IepiBCDRu1boOjfl6qLyudrgH0h+AcyEyaXflB6shwxqQH9+5AVyGceXdiC7gs+AAIEqhULoOQTgKCIi7wu/k

FRKahqFMi5d8KCACCx289uf7rgl/llKKB4WqGE8w5YraH0UJUrgCMApgY4DMAebgDYIgHAIXDS+TIlEGOgHIH+j9g6wehDmGyIFt4PQivkCLGKQYlADmGjWsKCaQfQOW4dueQbuHzQHAJ4G4mgQD4D4gCAG5aBBcABjhHhklgdr4AP4TNh6WvgbMiTeButoBugggADYnhQgsb5AipvoT61BJNhACc4zeAkBLalPluASujUp8INSgQACqew/bpiKk

AZgIhCdBmNtOGzhUQfOGLhQIsuGrhg3uuHQim4duG7h6QPDTkACBkeF66p4doDnhi2gDZXhjQbeEauQYo1o3ImQM+HaAr4eCZiAn4exGARwQH+EhAAEUeHARZwaBHA64EZBGcAjWkHxwRgNqgYlBmvhb7g2qEX0IYRjWlhFfCuALhGoA+EZBqERUQPBAiApEeECdBG2IZbtqvQdG5EmyoiSbWWZJkgwUmPNgL7iKAtnSYZulEfS7QiNEY1r0Rp2G

uE2iG4VuE7h4kexEHhXETNg8RzCnxEXhgkdeEDe/bqJEPhkkUcEvhCAG+FyRWll+GKR7kFpb/hdUepGoUFAGBHFaEEVBF6RsEQd5GRiEScEy25keVSWRANtZH0itkVJT2R/gYzS3hxEW5G4mDwQxx62IRn9LhWxth8FRGBeubY6cn2AcRkuygPlCDO0fnaiyY5VkVRTqc9rCEjsiTicDY8B7gAi3wodufSmeL7iuxtWVnhnbj6mDt1bYOksjmHHO

xYYyGQe+YdB5s8sHpGoD+fnkP612yHjUDYAFgEUIDIA0PQAhgmABjgcAcAHCBwgAJpoDOAkoYR7bWGapE5yhWWI0JviTUKipDQxXh5pisjHury/wczgn6fUA3MhpYuEjiOGcWH8uTHFm0NLNyfWTyAnS4ArQJNHMgOrgBAhAQsYEAixs0gSac+Mbv5FxugwVoZc2OhqFFjBgvhMHC+UUQkQCxEsZxwLRQVhO7FkU7iKa++digJ4LuUpu/7k4dQLU

D0AYon3aehGRsM6nAO5q6bboGqrTKOcASLVCJSuuNcA8yDYOaZoEJfmZ4uyaAR1Zm4c8t9EHODnnSH/RPfkXaFhwMQDEkBffj54QxMZtyElAsMfDE8AiMUsDIxqMejGYx2MbjHAueokv70gdYU0JgoRGHbIWeZXqWa1gfDgf7/iawI2DNgr1LIGDh8gcOFQKzXleAcwraolSThpHLjKZaVUpYhKWCRJLE6KU8QZYC6LNpwoaGisRZY8cgikm5qx4

UZMECkWscZSzxk8frFe+ViqEarRs7pFYbRFsdsQ6ccwAMirAs4Nkj6A9AAw45mg+Jub/Ah+LVC3gZ6E1APgnfF7FHApVkfj+arcsn6ohFpoMxJhYcVs6uqlIZnZdWW9FgG9WrfvHEMhbqoQHd+aCaDFeecHtc4UO01rGZ0QOcUYAIxSMSjFoxGMVjGDEZcQR47xRFoBzuKq+tCz7Gr8hEjOC+nrx4/iwSFPaNgj4DVjNWtXgOH68poWzH9xzakPF

cx45lOadeTyAfH+QosXTiccOirTDSxHPj5GbYfkWzbcKgUUMHBRIwf7xbxQvkYbTBM8UolVSKiR9KBWx8UKY++qgmtEXxoMltG1s+gOXoMQzINMAcA65kCHbuztoqqLAQkg1DkyXenkbMaIwKiwgBqzJsD6mM0FEo5+ZVr6HHWAzGJjoM95vCHIkUwOMCbIvDAJpph1npHF7O0cc35nMf0YZIgx+YRglFhCcSWFpx5Dgh5QxSHvvzEJpCQXHkJxc

VQk4xeMXQmVxdvEdQwsVsm8BsOLqFV4hohZnMoSSjcVYTUQuIWsBvuIjszFiOIiW+ywYxglRrwSypggANISwG6DDKCcr6RJyI+AkBVAHACGAMQVQLODzxScisI728yOsL7JKSMDgJAjoBUDCgboIAyoYa/gFS9mxEicKkSz1pzHhS45nI58WtTrYoRGHTvQDrJmydsmHRoIXLBV8mFJaabAA0MIFBKd8IcCNcNfqOBzsSku4JrOWBG9HbOH0bs5f

RiCT1Y4OKCaUkpxBAUyGPMVKUwlgxGshMb+eM1vc5wxJCXnFkJRcZQmlxnSd3bgsQgNXFvye5hujLA7XLv5TWFhK3Eq8aLihxbMZ/nAKsxnHr8n9YEiQCmjx+AhIB/oeOAokQAWqRbKqJPQcnB9BrNgME8Kq0vwrDBG8ZdgKUoiurH829RC4mzgbiR4leJqiuJxPIeqUfGvchsfra2J0YqCn1OHagmKOhKSOGCFMcwMiLMguSGMBug2SIKFpIHAG

MCwyCwAGwUaJUMCG2pVMOEkhUojDNCzApIUWZBK2wBahJSaTrOxySWzH3yuICSSGhJJGwJaRQJTpKVbJJmSURjZJ4cemH5JJKXZ40hscbTyoJeYa55JCRARc7VJVzhyH4JzKYQnZxbKc0mFxFCSXHUJvKdWEZqT/KR59J5HgMkb++aisAn4XMCg4dh/wBQy0x1EANC9sYmMemCJCqUOGo0yySHKBk0pmMDA8s4PQDE6wwLskl0zZsGRwg+AAsBuJ

9ADwA1A4YPZB1AQgHMD2QDSEID6AS5l/zvJVyURIPq0EtKZ/oUAG6BjAs4HCAAYFAEYAtAjoABghgboDwDRANQAxDYA3Zp8lb4UGDnKDmg8f8kjx1EnqJEudoe8Gv+TiY+nPpr6VADDAjse/EIuD4F3QjQd4OORTKRVmElyw1MrXxD01UF4i8W4CWgQfAocUPyph70XAmfRgHoUm9pLfiUmryZSUOlmStKVUkkOpYenHlhlDlnGQATSRyktJXKYu

kdJ5cfLqVxf/kwm5e8uk0KJAzUC3yrOcytOonp0MM3Fywokt3HCJEEg9bmh5wrAqvwoBtInqBCRJ6nTxxlHFkLxMseolc+sbivFmpfCgm5Wpwijamb028aGnhpkadGmxp8aYmnJpqaem4mJCWdqmjuaepEbGxYVqbERG5sR05vIHIP2B/oXoKsBGC96YAGagg5KVaBI26PqpboqKSFSOk6KXwxTqDHnJlXUfGgSmwJ+YVSGZh2AX2kxC3RrpmmSI

apgl5hEaoykSp9SQF6KIlmfnHzpbSTyn2ZRHoBzcZxMVoQHG+ao6QeohZGKmHphoNFr8O/iKSGNgUDEFmjCECo15iJ+ypzExJRZExlThCRCDY6pkOQansKS8dz5mWq8Vlnc2m8QJwPYEUf0oi+EOUTZep8gvVkvBYRgGnrRjiYu5F6HIEsCYA+gDUD1sMKfxLTQznBui96basLgGmN8DeA/wfCYVY9hxxpWn48eIfikdpeSWSQFJpKT9Hia/aZSm

GZ6CTSkridKXtnweTKYdkspRCbOlWZZ2dylLpl2QTG1CvFIw7yh13E0KF+teiND7+rYdeAXG7ciMkbMv2eAqByUEpMJkKP6X+nMgAGUBkgZYGRBlQZMGeRlpkCGVRk/J3HrRmbAkieqnzc5QNDl/eWOWtJs+XkfNIaJ/QSqIc2SsZanI5owajlXcjlnvFh52ObVkGxeOX6lvBhOQ4kA8IaeUAwApAMyBzAkgHMA1AFWa/G8SvGW2ECYQrL1BlUbt

pAEjst8GkrhU8sJzj2kF6cPIaYimQtmj6RKQB4IJPad6rZhccRLlYJ5SdLm1Ko6UZk1J4FpDHD+p8idmcpC6e0k0JaXhfr4xvAbUJGAgqashfwSTtw7UxKIRMmdh9eKJL6mvZNbl3WIWWaHX+KqXRncxLLLzEyJkeaQAXJd5EwYSAINr/lGpyhrDmyxmiaak6JSeXonZZtuGFFGJGeVVlZ5TAEAVqE5irnne+p8U1mBpIMsXlsZ7/lCAhgFoNkgL

AUAPUI8ZfWbwBjg47CJLNQ4JIYQ1Gl0c4BV8XiPapCwxuQ1Bc4A+aPL85MCSPmqZxKepki5McVpnT5OmXSl6Z22ZUmz5cuXgl1Ja+TDEq5p2a0nq5dmbQl8pgypoBGgx+Y4i/EiwKiwthzshJhT2gdj2FpOD+elKLJQcncn/oqGehmYZ2Gbhn4ZhGcRmkZ3uUcLfJu+cqmB5w8e/kxaT/pWTxagBVDlE2KBZ5GLxYBfHkBRKKLomSp68SnkGJaeb

qKC2meQAUhFOOeO555mBXYnnxWGgH4l5mUPQA1A/YFRBzAR7CskN5rXnEDK4DYIORjOWzB1DdQwmXOxa4X4kHGnokCTwWWehKfwVj5mAWSm/RohRtniFW2UrI7ZxAdgnGZtSQrnyFjSYoWb552RrlqFK6f/SaFFibrkkx92REizATygPIGFpZuEk8Ji9JikwC8ySaFP5oic8YDxaAm/lSJ/heDnGUOsZLE6pjxXrEw5RlhEUmpCeZAVrxIUSjmCC

GscYmK62seLFPFOedYkhW+efRJimuRZ8H5F6AIcnHJpyecnZiT9i7a7FFqIvRHWdMh5yViGVIgRQcfhA2A4prmC1Cv2/mc2AQoywFsxQJVfPUjVQ5MkLD1gimLX65Jo+RmG+mk+bSHi5YhZLnUpQMQZnSF5drgkTpchdDGzFucUoU2Z2+cukVxe1JoUoFJ0GR45qU0IMkfE3xExovZV+TWAOEvmTRquIF6LJlDCpxfV6WFCgYDkcxQeWqkMZ8umD

n0MnLFBL9qdKuwzKOmEgxpklQmM1BJSVJahhMFFgvSXAOTJUaDTAy6vEyrq8jDiolOATmuoRlG6rY6XYrie4meJLjnCr/q7joBoRswGj46oq+TkyrQaxTuBylORTuU4UZsdNU4J0yGoKrNORbNnRtOWGvaEVycJRAD2Qjuf+mAZwGaBngZkGdBmEAsGWmkIatOUBKhUjOWOA3AuuFqo3wVnB6jNcT2RsCliw8sGHmMrylVRnp+jqHE1QtwHwnY8b

1JEoC5bJV2mCFE+VmFcl62f6qbZIZknEClu2UKXgxpmQQnmZKHnMXWZW+RdlLFspRoW3Aq/uvhgMcbDXEsFfZApmvZ/kIzIdhYApFTjgdnEaHGl9Zjek4u+yhFk6lQaTaXRZlZIo5vsjpfaBgae9kOq9IC5YSwgIy5XLj5UxQKOxAEASCGiGEqLJEohlBTmGX2MsZSoz3JZORTlU5/YMmVkq8KhSrhsyKphKgavjverKhtjIE7WOVTpuoSAYaWkg

RpHwsVlxp4YAmlJpQgCmlsVf6jE6xCcThmVeOLDCBo5l/VIU6cqxZQWWpsZTlHTtMiGuWVpSlZYWytOWHCCnQlDZXgUj4DyU8kvJbyX2UVOFBVWLMFHgjxYRUYDtM4qqACObC7psFNsg8acPKCgPwmFDMDG595tJKbAHqExrTlMDrwV/ue5ULndpSCeSnaZQxbyVz5/JTLk5VMhSKXTFYpcdmPlaubZk75WFZUI8B0oe+V+M6xRunKlrDtukRI5w

ENhHG3mefm6h/4sGEmon+v2HXpvcX/rml4Wa2ojlsjpfEh5JQKhVXKdKjcpqOONELB1WjYCMlEl00Kx69IVUBajd6IaC4gmF5wM6XYVmEoOXhVgSJaaJUbyrjS1aJwAkoJVUDvUjUVljkJWRl9rNGVBOr6g6kJlLqUpXkqF6mpXcVGFdGwCs2lfGxQa8GrBqGVRZcZU8qzrHyrmVjToUxoa+4FZXPoNlZfZ2VJObWwoZaGRhlYZOGXjhOFRGcoAk

ZZGY/YmVA5Q1BfEhwF4gNWCBEUalWTYBkoz2RGBODEl8md1CRamtJshmFocRVQlpCYRrzkymzLuU9F7JdnaaZxSYMWnlwxeeXDpYxYvmpx46WWGchZmXzwb5T5QsWqFu+VWFvlKxSsCflYysqGHGfeeqqQxPDo8oXGZMkEnrA5hYqkA5lxeInwVgRDaHAp3apcoOlKjk6WDqTDMdVt68mHBRDQVXtJnWqxFUgjbVE4LtVTqQrBuiHVPtfaCp+nNR

sh1xOvJtV81aqmOyC1BVrKz8VVVTpW0V66qqwhOFBIQXEFpBT9UcVf1VxXGsPFVmWe0INYJVvVwlTYxF1EAOJWSVUaf2AxpMlXJXlZ5damWxOVddSpA1PFSDUEReZfpX9KhZXpXQ1CqlU5w15yhZXCqGGrWXTmLGQ6H2VKSLOCpiwftMBpIDsa5WKJkfpmly8AmD3o84o5t/HjllUJahd0j2ePRTsradEozQ38IaREY1XqCjZU9prMBsa5VP8TdM

9GV0WLZuCMtkclR5WtldG0tTlUSFoxVIVXlm/OyHK1k6YrnTpFmWVXKFFVTKUOZcpcLgG1uZi1V9YPgviwPgexVqEgk5ub8RhSkKANUsxMFWFl5yNxebFTVUJejVVsmNdKZwANQEsD2QbAByD4AaVgfUABQVN0zfwfCZcBy46DO3QAEwSv/xqq/8K3LRaN7vf5QJqESLVLZ8CX0Wi5U+dyXZVs+dA01KV5LLnXl+2YP4zFiiLgCOgRgDQFQAs4Gw

DV54YMKAY4woOGBzABmtMAbgmDVdnlAmhWqTrpLCU5oRI/DOCQocJDfxBdV5XtYTR156JBUbK0FUNWwVnFkaDzOtaUw0ABZuKgDTCmYL9pI2a4fr6NancFVL4+6BpLZMA8tmDazoWlngZlaIhmU3U2Stm4Ya2lTRJQHaTOueBlN5EkaR1aNUPrgVNRTRgCeGMhq02Xgv9n4pgo98HwDoGqIKgByWsEJlocA0IjUD1APTWgbU2F8DU3mSlyEtp4GK

UI1qNNdNmzRLNBPtU2ZEBzWVrh6LTVABtNFwB01K4FgpJaNN0hpdqDNaAHJZ3NvTcVBrNiNAgCoKmzegbbNANo00xEAsMgCDE2ACT7lNDTb01HNxtAc2NNINhjjS2niHwAwtvTdCDBAazcHQsQg2qTp4GWza83LNTTYzpVgGOE82mwwzYJndk7XCc19NXhsS0XNQzUaSOyFLeCBUt7zdwBlajET81oG6tklA6pkzRk30iIOtk2MRuTQDb5N4LbC1

E2pTfs0Qt+LVC0E+NNni0E+ZzUS0kt7TWbpjNirWVoPNHOqq1XN0gaM364EzVM2+WMzWTDzNizTK3ytqzWy3rNHyJy2oAfzVpZlaezdC2WtVTRTplNglFS3KtxALS2XNZLTc36OVLdq1+t3AC80st1rWgBlanzd83YtvzdgpOtCLMWAdgwLZoCgtpkeK04tsrR63StWbVm3FNpAPC3EAZTeCSKtjTai0K2BPhi2AicbVm1/NebUq3NNKrXS3swAb

dlaUtbrdS0DNLbaS0Mtifo3SatA+Gs0cttbQ602+EbqAUpZcsVoki60RVAWxFvxann/F9qZrGIFaTfy1ZN7IsK32+eTf24FNibSDZStrrQ23ut/ums0Kt3rU22+turQG0GtSLZ20htN7X213tI0mgaTN0zYq5mt1yBa0ntQ7Ta2CgGzaO2OtGts60q2ubXm2ntbkJ63MtnbT62htrbdc1EYtzcG39NjzT23htnbay1RtmeH0CxtWlsB0At6oCm0g

tYLYU35tDADm3HtDbb01wtCLSOT3t1HSi2Iglbc63EAmLfa24tl7YS3XtPbWq2PK7bTB2/tj7bx16tfigJ2DtWHQT4jt+HeO1gl3qZkUrRWBUTm4FbDe/70A+AOGADIVQBUA44EfvjKb0fGOsxxA6zOp5EYoBABX84I7AlIySzYLrgPRVwEcDDyo5j7F2EIBLWIUyocYWT+VlVHeCEYl6ZPIqZajWpnj5GVQMXaNkDbo0jF+jSyEFVRjfLkHZpjR

2jmNljVkA2NdjQ41ONLjWwBuNaEq+VYN75WBS+NCof0nr+RtZMptVDUIND0eTsr4jIuIBBCh1Qp/saEml5xUqkB5aAok2bl1Fi7U4CdxUp2sZqnSPiniJOBwCYAmFjTmEynUIjxAEjeG9SWwujo5wQoozuOrAEe7mixRh3iEPmqNwDeo3UhnJeA1+qc+jLWd+ctbA3jF9KTgk3lKtXeWVhC/o/ISAmhfJ63ZfjXfo0QntveCbdgFdcAXGqzkVRN4

ttbQ0v5g8Yk1XNF0TzE3CSuvSIZAgtAgb46zgCIbluKRKgBcukgCBBiwaWp1zxZ5QBaBQ96QMiDMUcPQj2TSbwij1o97YBj3Dgbxd5HAFceZ8VRFHHPO1Wki7QkXLtaOXQmY5L2rj0w9BPTxTw9FOoj1TSyPba7CirABT2b02tlYnydGBYp3ZFfvn9ywlG9eUAcgPABaBzA5OPgBbgR+WTUw1k3caTHArmopjbIPMJGEt6nUCGgJ2UwCJiiSsSbN

kjkAmDNBBo5wLWDi49YDFXHAVwNryF++FYLKslotfuUhd/RWLknlR3VA1RdRDgrUTFy+b56Zxt3TVX3d6AJoW9lDVRqSKhuavg1y8vZMAnU9NFqWYhxIFbiys11NUSUA9cTXQ3PWQZb1w1eOBYxnIVkxDNUe1c1ao5pe6jphKBJCSfXzG9LveYSh1M0LVBCYPqCeZtez4uBonCBEVY4vV4/Y0KOR49YRZT1MGiWXZMZZXAL1lrDZbEj4CwHCCEZ9

jfoDMAyrnDEcgzgPoBbAboEThnEKJeTW69e7u3r2kBXqMxKZQzGEklW9Jf2zqe5VKcY5+lqrp7bFkJOVYdxySsEgqq/sZjxrIFjMlXoBu3StnIJWVRF2DpYfec4VKbIWQ4r5MffbV75XSdg0MQZBc93Fdm6SqXp9XYJaiXA2fTw7Cw5ZuE3/ihVq2q3wgzPKk0NpfUD0ddcuEfiHAjDa7VYa9fdBboVCtLHXFAONJ/1QC2SlOS1gf/b0gAD6KdVD

ADl5kfiPVedUzTPVBla9Xhl+udP3g1L1TP39lc9TU5iqa9RjVr9KSGJg6gMAMoAhg/YM4BzAzIMlb3xj0r6AcgcJgI2ol/Ep1BJ2PUEJmdyS5Szk6oY7I3Sj0bVYzXcaH/fxkE0FVhuj+hWKaX4BQ9MrwxCwdfLxpgDEcWlUHloXUH0QNIfZF2y1+mflWCl8DUgPR9FAagM61+XXrUMQ+9cn04DTVd+WvdXTLWlrAxA9TFJKupbn4cFL8LZ0l9pp

X3EO1+yhX0eC1oUCm9dn+epwcDfap7UYVPAy332gYuBawDswmPJjI8fYZhLOAQsPECRDlwGk6caMg6DVyDjdRP3yDBxioNGV13HP3FOPubPXN189XWU6Dq/dfFA8QgLbbzgHDRN3UaHeWiw3VL8DeC84MdlfUjsEwxaiGEzYaGEpUPOU9HcFdlPxmeythENCXufZNt31UEA6A2rZIheF2pDsA+kOSFycbF3ZD3nlMUJdYpdQ5x9GZl43wy2hdqXN

g+hOFStcQmJbWlUTYGdbUNCya12oDXhYwOzAiwDNng9/FspZNYOqYJYTtufkkC64vTA6hd8oJILppZPPojl8+mookW0mGOSkUKgnI3J2450vVnpnxcvXnqXxHTqQAhgW4M0CYypIA8NKeTw+bA9QHfHTLTDKdYwXvA42bMD5GiwCEMwhiAUCPJKoI+bDgj/UOFI5Kdfjt3BdGjcIWS1iIz+YR9uVReWZDcDQynxdJjTiOi86A++X3iRXfrlCpuqJ

7J3m4qTwyW1KwNujNQawE11QV59nbVmlHQwk3pjVQyk3xa6rjqlljbxY6RaOAo2A6hS7OCKPyx6Wd8VI5KsX8Uy6bPau1AlxlBWOWJgRlL0nxMvf6m2V/vgr2DdKSCr1b1WwF6DYAu1uQX10zw1ElmdPtjZxBKneW/DCsSUhjwNxTwINTWoTo3Xoujg0G6NQjcQ52kJDAfZo3HlKQwGMIDEHsGML5t40vlK1Jmdd1TpC1LiNSh8fVvRLAgIdgPxj

J+bqgOyFnbEXOyNhMYW6mTJSgitD9I/mNceNGUyPMjlRmyNpS8WqYi1hWPRIBoTPI1WP8jPDLWMOq0WhtipZjY2KOJ5PxfomwFhiQCUIFXY+UBYTCoxkVKj07rL1mx1pWbZjjpeeTiaADSABjBeOxgI2KefGPMDgk8QEk6JOrNc4Inud4PEDzO+WGTK/w9ozuNohmzi9F+QvxMPkpVfveeM+jRSZ0aHdN44XZ3jp3WiNZDYY7IXFVDSR+P75tVXr

X6pf43l5vyntH/Di4rXCdYNDdLN0zpjcqc12xNbQ8NUFj1LG9ZXgHMn0MQ9CRPjoY4IhkTgG6CgECKAAQKSs6OIpmDaAcADjpxT6BndozaLBuYbBAZotk0KA7KP4EbNHAAlPR6j/PDqxTJU+galT6U2ga7aGOPC0cAagA1MpTaU9VPxT6Brtrw6rUx1NoGtU6gCZTe2tybcU3wRToK+vU6gD9TeBvVONTzUxjgtSN3v1NTTnU6doqW6lvgaeW2lr

Ja+Wi09VN5tu2uq4tS+OrtN9T+06dpoT+FEdM8UJ05NNnTM2lgC4U2QFdMwAN08tN1TYesED0gC0xNNvTqAF1POQ301VOnTWbfVMEiG3vC3MgaMauhVggM0tN3TqAPC3MAGONq3EALUit6vT8MxjiBABTBjj46z0xjMgzp2hjhIgwdLDN7ThMzNpE4M4R+EEzOLYNNgmjbmTN9TE07toBMX4JVNwzzM0DO3T705TOzT5/Bjg9T3M0tM/TGU6dore

Qs5zN0zp2gAAC7JhCaoAPxqLOMd7ujxTKz1Hb7oetws4x1/TYele1+t2syrPizqHTq0XNhs9R2DTiel7A/TLM2HrMKHM+TOTT6szNOZgc05LOOzNU47ODTdgWZq8RqU+rN4G9M8NPuB0wk3DfN5sw20uzTUwLNMzPMxrOnaprpID4zAc/DPYzCNcnMRz8M4iCmIkILjM8Usc79PTTp2rhQ/hCUAXM6zg05ZQFztszNoi9j05kBiADs8DNOz5s1HN

uz/s+bOezzc11NMAVgEQBUQmrh3NSz/U0HMKzjoFBEvImkAQDOQpAOrO/TPc1PP9zNM3PN5tg0znO9z081RDlzXM1LOVz6Ckjbuzzc4HMfTCsz9hQ+dNpnMUzCM/zMNT28/HMzazANTN3zkc6dokzqM7TMvzlMxQCFRZ/OxHPzq80TNUKLENgBYzlUbJHLzwszXPaWTc3HNdzcc23MCzh87Avqzg0w83ngHYEgu/To85iaQGlBugucAoc0jazzl8

zi27a7gNgBpgKyMjMmzzOv/NXzJcyjN0L0szNrYzVcJci0Lr01AvSuYor2AwLIs63NEzN84LNDzHsygurTCdJVFDuIi0fNiz9OsNMcgEi8KJfISTCnNXzDU67MxzH8/DMERTC0XMPzZcLosrTLCySCGLaBoNMY4YJiECpg34YwucL3M7tqBArunwvtTAi3zMaLLU9IvILri9t5HQHwny6eLu8yfM4Lnhr5ZZAfc80C+LzIMyArzV82qB/gGOGhPN

Sd81guna+Ea5a0zcCyPPnTu3mgrIguJgEupzTWMgZaLZi6doo9GOG6BqAUlNXP2Lp2rZBsgEQHPPOzgi+4vCLbU83OZLRi0NN7ImC17P3anAMTqcA5gGjGzIyS80szaSIMoCoKvS83ODT6rsTPBuqCmMvmz3s3sj5L7S3HPHz9Ok20LLBIDUv9TDi5xx5BlWI0udz4y9fOtLMyy3OBLM2i8XMg6y6osDTQS2ZDCg4scgrHLYgDLSIgjy3otGB78z

8tdLh0yUvMLk0QUz7Lsi21piAfwh2CnLv03Au/L6i9HMeLGy3gbwrEK0wDQgLAEgufzqAOfMQiW4DMjELhc10uTzfc5RD4Lh0oSsTTDbYNOsUuC+zrawVKyVPx6hU5CCnLqK1pa7afQLnPdTHc78vcr5/D7NCz/K/4Fn80lsKtdLAq9FMHhEIhKulLM2lKuOLo2q1M6pEU1FMVT8U4lNVwSC4NPZTMBnlPsiBUwKvFTpU+7oruMUzbO1Lbi0ittL

lqwcurT4EQUvyrQ0wrOsUDSGNMG6jywgu3zwKz3NCW60xJZbTclr6unah08dNer2S7egZzUs78sPTbK9GuOzvy5YtfTIaw/MAzqawjNgz6qBDNQzVYDDMZriM9QteGqM+jMRrlM2nOMAeczAAJrMi7zMIzb80wv1Tj84wBMLQc4zN2L9qwnp207M00veLiK+3MbL/Czcs6+Vy1suoAcsxHA4mis9joArda/jqzrus+TpntJC0mv6zrTSutdLwnQu

uWzPOtbOQLVq3tr2zva1LPertq2csrLr88DgWLuUU6sgrU6yHPWARCwuunrpi4uuFubyDWubLhS2CvhrG63WvZzoq3jPArvyyXPMgZc8BsQrVcx2tdLdc2L3OLO847OnrVy50t1rUtpvNSLg630tyLY8xPMbzS80Ssez2i3hvprMSyCvrzi8yRvnrw64K2yrt62OtTrZ8/vMq2f62+v9rmi8+urTT8xBt1rDa9xusb3840G/z5hq+vmLQC8MsyR7

4eCt1r3lvBvXLiGy0s2ryG2Iv3TqHRSujrEK1Ov0raCh2CEL4czGvwz5C5Qt9ARazIaR6r67toMLJs/8ssbg06wuuzHyBwt2rXS9wuwgLALJsobrG0ItKbF6w/OKLGG48vYLZkAouswSi527B0HG9atzT5mw6uM00W/os6gcW/ZEmLfG+YvJr1iyZtsuUm2+tKrMAO5vnLbG8ivHr8mzNpmYfi8hsabw07guhLYkAQARLBIH4ukbvy3Evn8iS9Ws

ZLACywvhA6S0VuzL2S3oC5LWK3RtdLOW62tlLxbBUtVLTAFlu7a9Sz2tUbxWxcuKbt6x5tkLo2OVvOrgtHM12QTUyAtzNFAMssnrr84sv+bncxCvzLky0ssZLym7m4PLJC/TM7Lo2NNupLRywyBiAsK6It9rXm8tvXbdy7dv6bzq1OuvLgse8uvbCAF8v4AEW38uJbQK9uvPbYK9BvOrbgJVFo6721m1ordawVtnrcK9SvorhK39s6zu2nisIABK

5is47V86SubzFKyTvIgZOyCt0rVm9TtErLKwKvsrLiyKs8rjqzjrs7gq8Dhyrb61KveWfO1yuirNG0GJ8rEK4qtFLMACqtU9secRMztvPsrH8+VEyu2Al7qeFM8UkUxTrSrgQBzNaryU54u6rZhvquvC+U6ytiQdrcytlT5q8Vp8LUC5juYLUC7yuYbAO8NNurHq8Vplri21FsZra06JYbT/uiNLeW202qAZrYa9dNe7F030Cfr888bOPTzADHsG

bn06QCNrq05Rv/brG1mvn8irrmumI1mxnv1Tlm8Wtoz2OgWsVrHOnjO/rBe0TO8bXu1TMtrwK22thAT212toTqO14uHbkW4gvfbPmyOtDbzqxOugmlWzOssbqsy7v3zAe1B2j7es9x0GzGe7Gs0L66/PsQrVsxHBObda6eF5bn25cs97w6z7PXrDAupuu7Csw+thzTAJDuY7iW4nOJ7Rs51s/rEe9PszaAG7nNAbkO6BvgbsO2mtbzCO2+uwbdIo

3M9b8CwpsDrgB52s8uFGwPPrbTy9huYm485wAU7+G41tdLaG0vPJLHW5BBdbEBxAvDz126LtH70By6uYmjGzKtR6y+xjtCLiW82vYHia/DO17j+wjMCbxm1+EibgC3ZDALoC1VHUHCG9JvSWW+53ve73e+PsebqC6pto6+B4FuKzohzpuPremzQdXzhm+CbGbIbWZt8bFm0jO2Ln+6CtsLDmyofr7b6y5u8LoB10sO7u+1hvwQfm4PPj79G/IsWH

yi+Fv0Hl+6ocxbokJQcGLTh8YscALB5TNpbJ4Blv5reh4ctOLRh+Qc77Qh+culbUS1AcSHVW2qBhLtW5EvRLp27Ev9ACS0EBJL7W1m22bXW0JZXbve6Yj9bVCoNtWHw21Lujbty+NuVLMgFNs/7M22JBzbOB9vtLbYR94sMzBIFEf9LW20Mu7boy7kf8HF2ydvDzZ201gLLUy9UfBHBB6Nj47tawQfKtuy60At7wsR8vhAfBwtsmHzR8Ou/b4h88

uoAQO60Ag7Dc2DvdwEO/QcZB0O91s2bcO+nM/7Ih1Cso7MCxyvczCK19sorLiykv3TeO9ivwzRO4zu07vywgfkraOj8ePH6B/TvFrQJ6VODTLO5VMPH3Ozrti7XO5KuirQq+LvSboq4Lson/OyLtMb8J1paQnoqzlsy7vY/yZPBRsfjkqjrE4hXsTeg/+itAHIMKCtACwJgCMJ5RRQULDRJT8MAOxRuM7vwl0WEo3RwsCk4d6iQBqEOjFpmAkLEa

uMEg29AXd0VBdAhReO+jek055nlJ3RkMPjhk0+MINL40g0zFVk9GO2TJQzl565DkyfmNgtRXuPipFIw0OvDvQuOTQT/2bBOMjLan2L7mJY08hqr2uxqtW7rM9quG7p2nqu5Tpu4avm7Jq6zrlTFq/utgHaxwEcOr7UbesSH7u/7rjTJCx5sIrHLmuG5AgoCNI/GMYHXs+zaADkEWB+QRt6ZnUICNJyWuZyQv1TArh26yulyNoAgZeyHXui7aAN8c

fISkHXtpbTAKT6odMAD+lWL5+1WdEzOIqjGWUaAIjR17piCuBpghQtJbLgJM4ZAAAPsa1qgjy6mfGHFB2ud5tR4Rjh0g6gGgBZnW51m0jnROM5DjnkruYnE02Chnu/TU5zZAuMYq/gDznefEucrnAeq4E3n6BsCvrnqGyLafnWbfjoHnZZ0ec4tIhmgCNAHADADXnch1+toG3ls+fAQy59M1VSH5zBf9TX3s4AAAfG+drnXu+Hu66WWqQAYX2FxB

fMUSF/sFDnM2lHsfhgF4RfEX23kcde7ca09O0XgoPRcbg3y5RdDTZyAtMjs2F6hfTH/09/t8XyUV7v46Ce/RdEAkIKWekAlZ9XtLrbkBJciXUl1AC5ApF3JcwXFm4EFKXWFz7CPTuQFAAngwQDJcjS6lxpeCXH0+2siXAl7BdybFl5TNF7DKyXuu6pPqXsiXHF8cfyXCM+XtVrz00BdEX1lxRdeXGOORTEzwOH5d0XgV6udcXyM2YDZrOe2qB5r7

81FekHmlzXt58yV7pc2XbxwjNUHvF1ldBXrx10tsz7e0OurHzx+MeoL2Olsczag+/iDD7qPvQesXUIJDtgXqAKReQ7cHeeAIXZs2QdvrwnT1eoA5F9Fd9XO649rWuGZ1mftXkF+Zd2Xv++j3/7CACsfdzwB4IfjHXU9iftHMB0FvYnw2v4CpXHS/DM7ne55IBoA5OOeCSASB7+dYHpAK2fEbA81ddvreV+meMRJl9Ouu6MYPRfZXaVxMsZX+V9he

vXU1zmePX9U4wfeGCkUeEtSdIHKAZX/l0NfbeMANyv0X51+oCPXom2wfibYC5Ju1R3EagAo3kgF9eFXHS+csoHM86Vcfbgx3Ws6RHAETj3XAx4Ru9b216gBwHSVnTcEbh1/ZfgHZK1vMvXJZ0DfY6n1yJeCgpGzlfkb3Nx+H28/l/ReA3ZZ+9ejas1w0eU3BB+doEgwQLTc3XUB9YcKz5OOYCtAwQP8cPXSRxPuk3PNxNcy3pANmcC37F4jfhAj1

2Oti36Gy1KS3CN0jciX5t5bcfXMZ/TpHr82ytdd7hW77dxz3s1et+zxR8fuYmp+0+sOHyIBYEFnKwcWfqob1xWeQ71+81cBXBVyNcwXvy+XsRXbFyleQ7z+zkdC3UIPDffXt+/BDprIlxOcXHcizxeE3md9wf87YW9aDLXQB/7dY7FN2YddnlhwFvbHWm32efT1cG/tHYJEQQA9XKd83fDwzd/Wd2HxbfQfA4OCpchoAHl5Ds6L9dwde2Xvy0Vpw

A/1zhc133l8lv53kZ10v5HB4egrk3jd1GcVXgd2AcEny2xCsjbdt+gZKrhAPt7JR0FxzfUdKRKkfgmBF8yALnj170dmHu/ZLD0oTU1RAxB/ewQcgPbyNCDgPMMzWfqAdZx8gNndQHsg1HdS3UcX3c11fehH61wnOBiIV1g9QHu2ntu73/9y+ekbu2g81POCYAYCPnLUvBcOwC56Xc7TIlxQ+IXe90reDTjl5lsDXzDy+esPoe+5eMXN910sRH/i0

IebrIS7Ec1bAEa1vcGSt79PngX4VADnnvVwzdxz9Fxw8aPn97ZvWAUEKfyVH1S9o8APYj3WubH99wDs7LOsaAvMgSxy1J2AboOBeQX9F3cvSRnHJVdHboxz3d3b3j6gpoAF2/WdoPPj17eQryOzCut3uD00deP7x5itTHtl6tuurDSAr6M7LUpAa3HHYBmtTrBt1TuErLUgMgpPBuozvZPw05Tjk9i12k+FPqT4SuN72x6CcMrVT0U/FaJT3oeQn

F8O3sPHse+3efHjd2OvTzU0gk84rrFDorC3wJ1fPur/ujoodX4z6QunaMqONfORVUu7fTXMALNc0rp2gr4DEOiis/A3Vu3idsr0J2zuInHO3GcInqJ7nPIn5z5ie5zf+wcdC7CcyLts3t27Cc0PfOwc/n8d9zrl/58QegAen/unCd670eklMcAOq/6fG7gZ4/PBnxq5bumreOjbu67YT9GfH3qG5zvXbU64mduQyZzeeTnZt3zey3ez8Ff5nZgUW

fEA6Pkne+WCt5jOIP09yg+Nn1LjFctnuK7tftnDd4k9Ez3dz2eUGA9wOfs37L5TMnnY56JcxXd5zOePng18Ncb32OzFebnKZ9uczYu5xdf+XH97Ze/Tgr2efJRyiVecgXeBqK8PnTDzo9CP750TeqvX57hdcX2NnK8AXPFMq86vwhhTouPUF3a9wXc5wI+cPyF1w9oXX50fc4vXF/hdS3Il6RdGvke+Ei53UIOxeiPXl8xcJ7adxG+cXXl8msp76

917tQbVd1kBiXPFDpfYXKlzJdUvV8yIZZvel9JfqXXu40E79u9zm+GXMBm9dmXXuwzPN7ybymd17vDzDMrerl67pxvnlz9feXePZWuV7Nr5FcZ3Ur5jOhXPs2G/p3/Fya/dPma3FfZ7kM4ld57u92XdzPlM7xs+vMF+Yt5Xjb2Vd1rJV1E8bneD+Y8EHEs1A+DTdV5psj7fV2Pv+XrVw6+rPnV2utqPbr7o+b30jzS3dXz78G/73q+1EBoAKzyW8

ov81xU8HH+7yEcxPR7xtckHW14Qc7XJB3tcdnRt78vHXSr3jcXXIN6tNs3d1zdfofD80/O83id/zcfX275o+/La77pe7PAtzh8MHP8zjczYUN81JvzcN8uf4Krt7pf43aN6wcGAmN5weMPEN9lGof6gMR/E33iybeGHRtx5tgH1N+rfi3vj0o8VbOG/Ads3It0RtYHL0r++TXBL1bfF3fL0rf23mB+LdO3lAAG/kf+Lxbdy3azyLekbg0yrd63HO

qJ+yfJH/J+YmOt6rcygSn4h8qfBn/h+qXhH/LfW33K0/fOrDt6gfO3LH+EDS3pnx7fy3YT5vv4PPT6YeM3PsCHc3rYdzMfBzugbpuDnV70TMx33ZyS95BZL5F9vnebxPup3A73ndDvkOznexv679Me/Lhd7veCgX79l9f7NM2m8vvxK67t13tX3Ndcrzd9g8rbq1wHeK3Xd4Pf030x9Ee9n/Z9YBZfWd10ufNo90+fPvE97K5T3yD8oDaAs91V8k

gTUx8jL3kb3N+ovsW0J+vvqLwlsnfnXwQdYzh95V+Afu2qfcDbA3/lvX3I337eTRrutB+P3Hn1m0v3b94jQqvfV9/etb4999+a2sT/BAwAoD3A/OQkD6l+VzkP7A9DLEDy1I0v636g/oPYT7NtPfjRyAcQfBDxkBEPDSyQ+naZD6Y+UPRt9Q+9nP4dCAFC0low+uvhr5K9k/7r1O9mHLbyWuL7T74z9vnnb3F8+L9W5EdWP/VzI+3Qfcz/dJLyn1

m0qP7EU+/V3cn2gbM/HX2YeXQhjxNtVHSb+w9mPr323fI9IJZxwJPw67Me2PksQ49OPjr2496/fLpLHg//Rw58Tf/j3l9BPKDyE+yHjd5T+ZPnANj/8HyL9r9ZLcT3kv4HST5ibVPxT/k8ZPET5wClPCs7k+An+TyH8tPtT3W9lPC1wcdNPNT5it1PTNw09suaf6H8Z/bTwnMdP9x0VdqLL33m3o7BBwM8xEvTyu8jTozy1ezPvy5M8baVUjM+Xf

u2gs9J63sMs9FfAH5d+DTWz3u0afZn4S/M7/gaztczsJ87ucrjz5c+87GJ8Lu3PKf5VgPPCq0883XLzyc/n8bzxicfPoCx9+pTPI9n1ET07RAVzt5EzAU2WUo+jkZ4HPeUD/PbkIC+arwL76cbLRu6waQiQZ5CJGrRU7C9hnCL0tckXmX83frGdAgFcsEzjxRm/uWhPdk28RXni8CPpp9PbjFdiXoWcCvuS8prsndkAXsg1vkkx6zvS9FwsFcmXm

2d9rp2cxvrddJDty9pvkPcYruq8qIOo9Jzpxx7zrOclvtz9l3l09u3pftnXg7AFXiddbXla8cWrQDYDJq9LzjDAuAXq9mARK83znsE2XnCszXrACvLpa9/zji007gD9y/nm02rqRdVAWjs82ga8WHpK9pAcO9tAQr8evtK8vLv69B3iRdILs19u3tRdx3rz8uLtG87ASI943t29E3ku9WflfNU3rpc5ft29xLhW99LoKASvr8sC3v4Di3jNdS3tp

dQgapcq3sZcprrW8uLvW82vrd9fXsFd2fs5dRtO29RtPYDgrj5d+3gRcKvpO8ZASO898GFchAE4DkgRwCs9jmsF3vmsTAdS8/rhd90DvXskgYUCpXlAs93nz8ffp3dEvie84frLN5ZjgtL3od831mndb3v7pHXg+9Z9h+8dHpDt+HqwCPARbNudIs8K3MP9TLuEC7vqdo7npVhQPp5tD3r79kDptchfhIdiAQh9dPl0tkPvucBPpddQfgvMZPlh8

ZPlR9nrvACfPogC/PnUDObmR8AbkV9CXo58MdmDchNt+FIbtDdGPoRd4bmF9mAMjc0PqD90blx8QFhJs5IrR82DFcDGgZfdkDs893NiX9YFl0spPvZ8oDn78YPszdcNth9xPp59Hbt583rjmd6LmM95fmRt9Po7dnbgUDVgeZ8Svju8sQc6sbPmrdcQUL8tbs59dbvrd3PmcDPAXTc1PisCKPkR93LjbdmAIF8CDsF8AZqF9JQRF8EASP9KPhsDv

bgwIdgUhsEvkHdL1r7MUvr3cmbpHdXfqd9WNrl9yAagDVgkqDyzpS8U7sIAP1jV8KgXV8Sjvft8geG93gRPsGvlSCS7pK9V7pXdvAem997m4CLvlAskHj64NQUN8O7sJ9DfmQCargSD+7lQDZvo6C61gt8/dCD8WvrWckmDgDg6DPdm7tt9F7nt8GLi4DEwU9dHIu4CigeXdt7qWDDAYsDy1jd9WgWE8HvoUcvfuVc9gd0Cdfl88rPs9sbDNKDfv

vIB37tKCgfmkc/7lr9fgWD8j3vD8ofkj8qwDGCYHmA8Yfij9sAemCswXS80HgSAMHjNosfmGD4vuscFtpHpCfl+BifjNpSfpr9yfkrdKfty9qfvQ9vLPT8WAXoCefseCWfmWDtQTNo0gXMDbwcGtnAV29IwQtsJHgeCztNVsxfgo9Jfji1pfuYZZfv6CaQYr8OwSwsDHvQ9jHtUd7wUr9UQRY9Lfgb8u7jY9xYnY9TfpoBnHqs8LfoLFJYh49Ejv

sDnVrb8Ywbb9AnostgnsdsdPlAskdtCtPfpuCBDsN9WwfiCMVgH8oHkH8zIPH9AgGk9w/vRCFDEn9o/vdc8npisCns08eIYn8Egcn9gPpVhc/gn98/n48s/jxQtNlWA5IRJCFIayD2nogBOnpiCnji2C0drTtBplX93Ip4thnnNpBpA392/qdooAdM9ILr8culp38xWv+91gf39Nngbptnj39LQcyDn/h88J/i3Mp/mi8NbIv8edkIBV/ubtdzsv

8xAGFCpVvZ9N/hc9t/r2d3nrP9PnlLtCTgFY+xoqMBxsqN+ujCV1Ro2UqgHcA4QBwAGIMoAtgC5UmqoI0XbJ1AuoDPR6LPFV4qvf4WNCI1xwGTJK+EtVARhAgzOqX4l6NCN9mLCNxavt0ERsH0DJr0YgxsZNLyud1Cqog1RSpZMoxuoU9as/I4xiadh7EnYmmJrxWuOi53JlsgLVKChvJjmNMXID12YsDQCMJshHsrcV+hgEV/vPZBOsnHI0kLis

agI0BG2I1o3YHCAm2hKJQIcxQOWpIZAAEmEJgV0uiJiceeMk3aYkQBscQDoEb0Jl+zFHNBCdzNm6Bl+h1IgeEXWmSCBxGekdQBCAYcEcgklCBMBxDCAxAC+8poPWC38HBhhLVQA+APcMv0JwgfQHVQZkAtcbLnLc6wSr4zL2mih5StcePVtEsrnJhZPXYAg3lZM5ezMgKMwwMPJgBsO5m0CGV3gg1M0RhM2FBEBgFB8C4U5hDkVa02c1vCiNGhE0

PXx66wWcAmsK1h2sJ1husL1h+sO1hjWgOIcnnsgdAkaAdQDqAHIEKC/q392ga2D2wa0a0NUFQ++iCkoZkBugA2jhhJgSqk/XjCWrIEHOnsIR6VUnxAhlwIA5bk5h3lh0UaCzR0PLnkgcrkce/EIIAN3iBEIVGJhKyHM+7wmwheMk5h3sGYAOInZAGcLdAQMMkA2cyXuPTWqaELTg6ceghayh2O0ANmOAeNzF8TJiyAsUQ28nMNeu+Om18SswBs47

FQAiQTTh7gSxMFgU5h0MMK+idw7hBgM5haoAToYcHEuNwVMCLIg6Cz0O7IdAnmgBIEPWDAgruVED0uLEFhhnsM/adkFVh1gB56YQRGk5e3eE+ABzmhkF8s6wUfAIcA5A1Mz20IgDoQYcI1sv0Pkgq4QBhmcOphyUWYiqUQUALn1s+9MOehYMKEiN4SDchU33CnEWYoR4RvhRMMcgnB3PhksNympPS/C3ALRar8PeEFUR4+X3hxEsIBphM4VpQ+2l

CAkgGcAj83seGsINhlCKoRBsKNhJsLNhFsKthANnwuScI4AyJBDg02FJAJgUl8A3jWCz0JFhEPEMgn8MLh6qC0sb8Ngik+3cge2n1mkehGkNcJJEz0KdhcIFXhQsU/aKM1ERe2gMANmBj03hkDEQvW5ckem0Am20GWO2wWmN8JThFoEy0aiIwR1F2lhQQUYijUk4RI8IKCANgbob3g1czwDCA6iIKYSwWhEetB+0TiN4RGCPKkqukMgoQEmiWMOY

oCMJvhPcMcghl1IA9Ih+M2gBEMFCOoRqSNSRtCMSM9CMtheTVDev6yBEmplJhvb0hEHujoediMCR+SLdgjkG8Rj8wyAJgVKR+XwtBUAHWC00DvhD8LeQwIEiCLcIXCKSLSRvSP1hNLkaAcIAGQXoGuhBxH7As4GuQY+C3AjQFnAjWmkkuK2CAlUQdg1CkEAtSLCAscKFh+SMZhHIDwAY0Xzh8BlfumyIWMIsKURuYiFiUcMd0keiORJVkKR3iIFh

ByJgg9SMYizSJThVSIRq4sNqRs8PqRASPVQzSPrh98NnC7SI+QBEEy0qyKawxbmR6YSOouMQTmRMSMkWwEDpcbYB6RfSJRRWsMa0FoAYgZsLhAWo1QAFoA5AqAAYgBxAthjWkOAIcB+RhkFhAlUTMgs8KIAsID106BkaAqAGaAdAlQAsyIBsiw17hRNkakcMXVAMEGaAOzTQMjKLhArKKZRJKLBhKFjLc10DEAyyIakW4BJRcCKKR3AJYAFKLm0j

QHURn0zDgaqFugQJgRhqMN0CHUkJhjMLeRs4UZRTyI28fWkJhIsJx6RNkERyKNRRKKKdc10JGRjQDuhcIDqAf6Dk8jCKBE9wBDgdQBWQHcH7cBAFlczFGjeNojQRIMKBE9qKjRzgDqCW4AAwNQDxuTqNuh90MehNQBJRKcLQe32hgRJKPrhmMLehQiLxkRyKuAIcAB86IiCCZmB/ha4QZhy8OXCFuw20Lm1pQczW9E7IGl2OqXJwSaJdRKaKehLi

JDgr0JJhkMLXCnMI90/0I4MgMPVQwMOaRvaIhhH0IaRMMM5huqKRhA8JakaMI9ghSIiRnKKrA+MJWChMKnRJMLJhP0KMgxOkLR8EFLcVriiADMLvhjkX5+EQnDgbMMXBc909hwom5hGKCBMfMO0RmQUze6wRFhmaIeEVByQRkIjNRcsIPRCsJzcSsM7gKsLe0ePWVWjWmjR9qIyRpsLhA5sOyRSvlcsAa02m9sJ2mjsJLR9IGJgrsMak0PiHR5kN

ggpiF9hr92IWAcP56QcPVQAJnwAL8M9hEcOW8Uh1606yM4AccJ1Am3nwALCJThfaLThBaJERB6JzhecNoxY6MMgxcIvhpcIha5cKzalcNrhWbTkRUeiBE9cIB8TcOoircIPR7cJ4oncJH2QIh7hfcJvCA8NNBw8Pjuo8NUu48JQuFF09hU8P8CgsLnhUQQXhpIBvhNaOUR68MFEzkG3hagHUR+8O7gb2iPhgsNPhiqMLuAOgjRrCLdgAKMhEFCxK

Qnrj3WeBjERK4USifGOyAlaJYi/YH/hfIKKi56OARIcFAR6WO9gdmIyiUCPDRsCJDg8CPAWiCPDReiNR6qCLUiGCNdcHj2wRPmLwR4sLMA/2iIRLLlIRtkWCxsGNRR8GKyRXqOBRNsJemz0MZhHCI/RvxmB8UvmeRfCJDgAiPThImPUR+kQkRI0hkxGQFkRNCwMRCiN7RzmNURVm3mxmiJug2iOZ0FWIDEJIiMR223MApiOeh5iMsRO2OsR4SFsR

SUQMes6JMxN8PrhKGVDcHiKj0MWPlcs4SyCviM4RmunJRsJi+xwSPMgjUjMgWqKyAOqNxh0SOKxTWBEACSOquySJgxXWL6RPWMQxDCJyRUazyRCxmXhxqOKRc2jNRvyLmRlSMVRNSPxx0CJp+T2OcR+SLBhYWL20QEGBRZkFUx3SORxKOLSRAyKGRIyL/QYyImRNQCmRMyLmRRMN4aIWxlRUIjWRu3lJA1yO2RuyOCCtGIeR1yJORzmIuRvWiuRz

SKdheOPfR4vkOR92MmxoMNeRpOOJgNmO+RxmOpxCxn+RbSIZxEIlV0oKL286gFpQj0jMg0KOaRcKMQACKOK0SKNZxbOOoR6KMxRiGOxRW4FxR+KMJRxKPZRy8PJRs2ipRNmNpRx4UkMjKOZRwqLZR3qLdgOMKYA3KLe2MRFFR/zUFRLKImR/KPZR4qNXQ8EF1AAGOoUcqPZRCqO8RrIGVRJgTVRGCI1RhkAhx0lkiRuML1RBxANRJKKNRiqNNRlO

PsRB8MtRIcGtR8WLtRXuP6RANnbRN0M7RbqI9RW4D6xPqO0C/qKci3sCDRSTBDRmAHj2YaOzRANhHx6SN8CcaITR4+OdRd0I5AD0O7R3qIzRYsM3x3qNzRuYnzRo6K/h2QEJhPcNLR80HLRR0ErRuuKBEMmDoEZEEzA9aORArQEbR9uhRMHkRYEaiRp68uzP+DPQv+8RUom1/3Z6sowgAB+OTRx+NTRz0N3RacIHRX0M9hw6OwuCWInRcyPQJN4Q

HR5KPnRLeMXRugVRh6MMMgmMO1RzFBTxeMMHhQ7hJRhBMhE+6MfR0ICphiWNphZbi9gF6KZhokGvRpBFvRm23vRnMKfRCrncAr6KKR/MKs2gsK/RvqLFhf6PKxgGMXCnsJAxNIgvhysObhkGO56w+O3xOsLRxSGL6xfuygui2KDWmGIBsTsPOuLsN7A+GMV82BKIxPsLEgfsPIxaBl+hgcO5RIcNox0WLcJ2lkjhTGIFaEuLYxCcM4xjWm4xt+Ks

Mc2IEx8ECExBcKLhJcL2+ZcK1m0mOkRsmJxa8mMa0SmMbhQPlUx/GM9hGmLWe1hjl8OmJDgemMhEBmJWCRmNJe5LzMxe90sxqFmsxs8L5EdmJBEi8JcRTmLORLmIxEbmKIAO8M8xmWgPhPmKsB4l38x3iMCx18OehoWLaRT8Kixa+wwR78Pixd+OERiWIgxyWNSxrnyARLiJARhUREiKInyxh4RmwRWMKRCCKVhR4SOxVWKAiNWKwR4C14uuCJgg

za0IR5ADaxZCM6x+hMoRhhIxxTCNQxD+yBEbCIJRJiC4R42J4RROJcR/CN9ECWN2xOojMgga2WxkiPkxN8MURW2Ouxxa12x5hn2x8mPOJgYkMRAyzOx2AAuxLiKux76PURNiMJxoSMcRJuPKRrCNex7iNwon2M9h3iN+x0QX8RFJJBJwONxEISLBx4SNoJZoinBz0LhRcSIRxH3yRxW+LeJNCIBsxsMyR6OOQxQIlsB2OIKRGuJKRPeMpJwSluR7

yLJxdSMpxgOLmRtOItxHSKZxXSNaAehNFJMaIBsOo05xoyPGRkyPsg0yMTxCxiFxiyLgAouLBRMcNYxUuLvhMuMBMWuPcicyMVxnROVxzIkDE1yPVxiqPuRI2m1xpJJeRsOOqRhuK+RmpJZJTSLmR5uMBRluJBRYuPBR9uKhRThGdxsONdxhkERRTBJFJxpN1hPuKxROKLxRBKKJRdQBJRYePjJEeLkAUeMIAdKIFR7VyZROeJJRyeK5R+IHTxfK

ObJQqJFReeO9RBeMlRxeNFxZeO9RFePeRVeJnhqqPVRVBK5JkOObxZbmXR+qMNRUZPeR3eJlhveO7g/eNxRGwQEJW4CNJopMdRE+NdR7qM9RJKKdhfqIFWt4WXxwdFXx6+Myal+JcARZOLJu+PjRiaJPJXaLTR7KPPxWaMOJOaNhxyrVmx9+KLRT+LF8ZaOvR7+MpJX+NrRv+MhEDaP+0TaKExraIYmJJ19SWRSHGLDXl6eUMV67+A4CUIHIk+o0

M6QmG8GLfGvAW6BUmlnSdIIVEOAvYXtIOjgBAgzFAcz0QlORPF6hDfn96OkwlqSpzwC53T0a4fUfGitS1OWIwjGDSUUQRgBXcDEGIAXoDGAJySWAdQAOI0wGUA+gASAAyB4AFQFWADmk1yB+VUImhUKeRI0LEUwD3cdnVcmU9myStBQmA9p1ty7QzgmVxTKsSJFvgmDDYGfMRW4rlim81AHUsYF00B5hND2XIzcpvLg8poli8pkFyD20lhD2LCll

2DYwV24oyV2ko1Z66eWSKa7TlGQlncpnlIde3lIwxvlNQpwVmeCkJQvs9iVyhxOWpOmEwOIOo1aAxAAqAAqTnGVUKuMMzECSMwD1U2vA8G4Ag1wCYWVwA7HkwIU1FOaBEbw82XYpL5m9Ge3TAaQ0OvGBdlGh/FPgGGpyEpOQwzieQ1PkElKYC0lNkpDEHkpilOUpqlPUpmlI8aWuV0p8lIMp/kBmAHnEScLcVNyQ7GtO5wFjC9wFZGDoB8muY0Oh

I1TIkl6FkmTlNCm7I1cpQljFsBNhBsdHVJsctkpsyEQvaahDA6yAFRsGNn/yyVJQMuNmoAX1KlsxbWQiZ3lqkFNlhsitlwAytgVsoNKP+cu1P+XxXP+LY2V2cBM7G6u2o431ihpMNN7mcNPBsCNLK0R7VqaqNNpswNIxp2VJ9Sy0WyhLE2aybE0lMVw2lMFQBgAmgGOSEwCzU1VP4kLUACgHXSg4Ojh8yl0SKocDghG8sEyU9Yxz8/GmSULFOUys

py9G8py4pg0L9Gw0LGpLnjgGI6UEpkfWfGIlNXyJVQ7QswniM+gC3AmgHDAMADSQjQBDAzEBgAFoAtA6EABc21J0pBI37AhpzZ4LmVJiESH76jNVqwP4mH0DQx5khqD0IVlIbUNlKdOT1PGAiwEJctfTHi6AA0BdkMlgj7xB+KM1pakgNcCP71FBkX3UuOqVTpOOi6uXPzMeWdOmBb4IouedL/eBdJmumNKipkBIkAQUQXaFEyv+8VKSKkUSSpFH

XGB973TpUwLLp5Pwrpg9IfBUehrpqwMLpTNIU6rNMwpBVKWiOFI4m+GmXMdwCtpcwBuyFUMEmniFnU79nbiDMRs47eX6Y47ExC7fDiqjnTiSmpRtUU9Hv6FITlOvRSGp8I21po1Oc8DPH1p8tUNpF3UmKyAzmpyHgtpcACtpNtLtpDtKdpLtLdpGWG0pNk12pf6H2p46l1wLUA3Kp1jOp+fWRcYuFNUXiGzGMTTup9AyOhj1KLE8dM+6yE3OU8Wk

RMAwMYSFEW+MHBhIZDdLhyoowRyZEzxpcVPbGCVK7ptE0ZMFDMnW3JnSKaFJZpzE1npORXnpRVK5p7/kdAYwFwopAEaAf6EFp9gwv6jw2+I21T1UZVAuAHtmapcVHXK8mAah9wBiSbRSmg1aUiy9qn08HnGpKauHiozYV6gXJ0Ys9/hvp6tLvpkA0yqUtSRGfFNfpZ3UDGU0O1OM0IC8ep3mhu1Jv0S0KdYdeTwGZXTLwEDhTsVp0AqyJBCaFamp

qjJXcyUdN/08TUCmRYkSkVDUpOp9iTp5YEGGLpQwq81Wb6ONDzS8PAUw9LAY0q5XmGxjKtUHcm149UDGA6wzH6OwwzwDdSUGeXj2GUNQOGkNWnqGg1OGWg3OGheXXqi9PQAIYBgAjQCqAf6GagrqQ3pXoU809SHgQi9Dbo0ynNGVFKaYM3TAI/ihEYCjSmY33S26p40FyG5GFyLMKgGdjJGhetJRGMDRMmoY0u6xjVNpYlI7QFQGmAhBVnAztKMA

CQDgAboC06wyAWAx/EwyUvHAZX400K/E1KG/4z6wxpBGSIKFOs0pxAmtXQEcOpiySNA1upB0KwZD1NeMT1I/kg+VepKEyeQhoNTxOJh1SaLOxMHDMip1DJImtDObGEo0pMBNLV2YglRZGXxkO6LJxZRJ0eCOVNJOeVJX62FIEZn6WlMuAEaAzIDGAjoFwAwoB6ylGgbyjlPhSYSmEmnOCuMw7Hb4O5ggIlXVWY89AHy9/SgS19M9GMI0GpNjLC6O

tOfpg1mDURzImhzjLi65k2xGFzLogVzJuZdzIeZTzPv4ClTeZh/A9pEDIJG9tnsmrmUcmo5m1wfdHFSswB1C5A2rwA0C40L1KNKGDJhZfkziZODNtGp9LdOCRETmI7G+xMEG9gHunnhrRP+xNJLeEyrRCROqXDZzgEjZbsJMCsbIR08bPextJKkRhLWTZuLI+Ky8VImhLNipxLI7p0o1v+CBNTZ6bOBMMbJaJ2bIeExOlzZibKbahbJpZdWSYmJs

TZp2BSLkKnWKp6AGwAFQDkAi5hDAL8X/8m9MNA94FkwBpGbCc9ENKUmG1KRozyM+WEtGDvS0Zi7Gz68rI0m4A2VZcI12Z/o11pL9MOZ0XUAspk1OZ4Y3OZR2UuZ1zItAtzItA9zMeZzzItZkcitZnzPxGD3SWAJFh8Z/tP1ILsRr4szNBZWoWWU5DQ+6hZiLItAzpGDpxjp7XXspkAjBQidL66GqUUS3iLTZn7Q90tAlEioxPeRKlTvY4NJzEaHN

NamHKZxobkkRZ8Lw5YRWSy4BOxp9PWbpMRSZ6bdN5sdllV2NEyJpLxEVR6HMy0JHLvCgQBw5s4Tw5EvQyhjEyyhPDILyw4yZZA7MEZI+C2AmgH0AVQB4ADSH0APtI+SlUN3cM7IkwdYG3Mv8EXZD/S7A4mQasIuEAQ4JH5Gw8nikfVI2ZqVS2Z6VUD6WjTVZKp01ZZ7LKSLjJNpKA1PkRrPvZJrOfZ5rNeZb7I+ZeXU8aX7NnG9rL/Z0BGEmNLBO

pzsgdUxhStUg8mSk0LPY8AbLL6/WARZIbOcpX+WMohd2cAw6Pe+8OMhMF8P8CI0inJKqO+ecQQk4WXJy5jizy5iCMK5SqOnJpXK6CMeUbpONKgJ9DIrZjDM7pMo27pFXLm0abKq58SPy5l8KK5F2nq5nDLpZ6FMHG4nKwpao2ZZWfHf8/YEIAOMPbRJySIp0MGc4PqBKoXMHBIwCDFZbfVHKaLE5wD7g3QPGiRZrFKvpu7PiG1nMSGtnKvG+k2PZ

GrILC40JDGk0N1ZRVX1ZN7MNZd7IfZT7LNZLzMtZ/nO1qd3U/ZCfSWAKnMVKd2VYS9sFhc+5ntIrXFfgZAzBZ/4lHAXMCusRLFpGZxRg5/k1spzalS5iHNDZxlHf2+cL65cOPiRGRSxMDGB1ShPNoxxPIFJZPOoUhyCoZxbPhy7NjLZyeVbGS7Q65VbJE4d/wkAVPIjZ/XOZEExHJ5DPKnp3bMayvbOU6waVwp6AAoAgzLGAlmmwA5UL8ZGVidia

3MDQupgNQMdh25LegapIVGFYZDAHIUrLM5gCAs5gDT4Kt9LFqQHm4pAZlzCDjNPZAlKmpRtOEpX9IrCuXA8533NNZL7N857zOtZXzKWAE7OcyxpwdZJ+T9ijlK6pwHOAE11Jz6kyXYcywCOAsFChZ+0MS5ME1g58E3g5iLKQ5F0PuKgiDcxNPOq5wQA+Q3Lk10poKrAjES5GufNy5A3J9gmQGUARfMy0JfOuwG3kZ5U7XAKLXPo5jPRO4MBPbpnP

Jv+3PIQJllH55JPI+0BfNr5qPWL5xmLL5ovNE5PbN4Zqo0iMs3Nis6AGmAxABgAdQFWA2XSq4ozNV507LiAl7gWcXiCup/gylptYh/gBpCup4uCdIUYXFOl9Nei/VK9MnFPvph7Ps5x3Uc5DvNGhLnJd5qtTd5X3K85v3NfZPvI/Zfki/Z4Ll/ZmxX1IgCHGAxDRq6IHKA50fOvy1EBnYtYngcMTNCyDA3T5aXORZhDKeQGiwjZGi3FujBLZc9iM

exggMp50c1wF0c3wFDfKIFnCJIFRbJb5kRQVidDKJZqsRJZbHLJZCRBwF6HIoF6GwIFpfPNRxAtwAo53+QU/JsSGFKm5c9JHGC9MtipY2GOs8Lz5VfM9Js8MyaKlxlRqOmb5NHNb5dHLF0HfMssl/2Y50pmI04YAaQcMSWAFqWV5anMJkjlLiAEgz8ELNW38YrM/kMzCQQaLktMk4HnYYdmv50CHO5d/JAaA0OGpj9Lu5AaiAgbyBEAm9GgalpG1

Z79I/5uQxC5YAv+AsJBNyhhXv8H2SACzeHBIt8GS5V4Fx5p3JupSfMmIiXU+5xrMfZnvJ85/3PP0eYxsptpRK4n4wl55ynyypLIZM6AHmWcgsr5H2kUFmbzDRKgpR054HLGsgo6F8graF+cKUF9Ii6FQBKPYE3JnpHvkl6mUKAFIPJI8HNM2iPTI/8RgDuAYOyWABxA0I2vROGBo2hcJwBbyoKCMpZ6VEySLBnZ6QtuAskhs4t4HnKbCIjq2Siiq

+5lDpqkwHop/LN4bcgx4sDJ8F/UKt5WtJ4ptvMDGE1INpjvI/pUfVmprvNgmBQ0C5IPNryvtKD5qfX8Z1bEECKzmuMSuEsp4qV8KKQvUw8BB05RnivSdAyS5aAqepfsVLaCwpE4VQrog6TKOqmTKb6udTGGnQBNQ8CDHYdwsSo/sQZYxQB8Ub7j7Yvgi5OVTMcik/UnqUZXqZrmUaZrTIhq7KlUGxwycyOTDMq2gy6Zug2k5KSGYAYwGFAXoFgA8

nPP6OvRkZ/UBLSwElWcYJAkCOvOuMPsTOAGPEt6xItt6eLGKo8mHeok5BnYz7jO5Wen5GCmCEwKCAKsJVE+F+7L8FD9N+FA6Tt5qp1RGkQqBF0QtBFX/PBFQPNmF340KgPjLhFzVQCZ9sBM5CfhAQP4ipi3VRWc5VlvAyCBQFz+WwZ8LI/kEIxFO/bJr6yHPJF7tU4Gww24G3tV4GArAmAsmCRSh5igY6nhVojoubwMsFdFk4B5FirBqZInDqZ9j

Cn6ulXn6Cg3UGblUX6Zw1XqsosuGLLPf8hAEjkiQE0ATbFW56FB7Eh/P7EoKET8lpEEI+nnvgr8B5kBqHmcTFPuYqAU86y9F96FvIf5KrOSGgQoc5j3LVOBjXRGZkze5olPcZc0OWKu1M3sMIo2KkPKbkSPA74ITQPQkXMR5D1Hf000GmgmYouK2PIoozHheUrgkwFXxmJpWBwcRDwgbmdtCBEj2NlBW8NPupiCBErwlpQ1N3J5HIM3oZDNgl+As

exiEowlTcE4RqEoG8u3lIlWEv+0OEuoUeEvUFXQQgJbfO0F0BPZ5LPR758BO7pon3glgPj0ApEpQldIKXmGB34lUeholVyDolDUgYlIgohKYguYaEgsk5UvKWFCnLdA5enDAzQGGUQtMJkBGDiAehSaYnDjBQJvSlp8yngQkAlRYVanQEKzPcE24y8Ft/Ms5Wkyu5Cp10mNvJ9F/wscZxzJe5GI2FK00Ismj4uqF1kz953E2gZDsgqsNNR/E4fLg

FFajHMUWhYG6PJa6mPMDZOYqRSiuCMIZIuF0OYGMCdkASW5qMyaiJgxZGE2pgmUrYA2UvHRuUo4M+UqSyYBKYltHMYFrPOgKXfP0FdqQ7GDQucshUoeEWUvsRZUqsMFUvShxJ3G53DJn54gr4ZkgoX5FtkkAjoFD8AGFB5pNSkZGooNGI5m/ghwFgo2vGcQUEqoptFPgQ5VEEkmtC9K0SjZyVopQZ9LD+I11l5q1YydFLYtDQazLN5mkxPF2k0f5

tjKPZ6rI78r/Mmp7/Ne5Pkve56mg8Zz4oJGM0t+ZTdQ+SFQzIsy7LHoSKVOs4TNxYEJBCl38RAlbXTT5zHhXFZour6SFSLF01RLFQw0b6XtQWqArH2lmwEOl/GjriGTnNYZ0ubFLosulZjnpovIs7FmKkUGPYt2GfYvzK/IrFF+wyHFplWX6Fw1qYjZThADEAoA61TCC6ou2FWaRcQLnBboVJWtGYPSXZsPCQ6ywHAquuF86fDGiUWjmWAizhRcb

otDiK7KpKNfHmApjJZKgXSsZlvI0yPwpclM+WRGfoq1Zz3J1ZXkqu6Op0jG/kv1Ou1LLszCTKGyvKBl+1j6w32XCqGYvFS/nQj5YAlysADgW6cUt8mKfKx5sdMRZwSBCZyMtOUqTOLF9pVLFmMpGGFYtpFxQD5G2vBVl5VESAktPtAzgA1lu6XjCOsvbF+dQjKCgz5FkFGFF/YqZlg4oX6bMuQ0jLOYk0vIgAk+B4AzAGaAcIAtA6EwEmYzPpKga

BkypVCnY3gjFZmYx/gb/UQcKCF/iIDiQCKtNslfkArE9ktuljks1p/gu9FJst9FL0sBFb0qtlZzLc5NlIhFO1IJG+Et6SL3WBlULkr4ZITCapZjL8FxjbSeLizluQr9ZyfISlmQvbkh4zL850LCm1HEOBq3ioOwOgfheWPMMHUV60xXLREj4UmiCCLggKPRlJEcAAV0EUB0GV0a0b83phOErOJyEvIl4QDglcEEexAvJfhluho+7EUa06rhvJnCJ

4lj2Ph0/1kyaX4WgV4aMa0tLVhBHB3AWjWnhB9LnYilCtJ6vBOpuXI0/lP8sYAXCpiiECJZ8SCpG5Zs3RE9IkYVoOIgVpICgV1N3gVcCoBsCCrYVUEXKxKCvZcaCvwFGCs4RWCr3WOCsE2X4XwVvok7gJCrpuvEtIVQInIVzCoEV6CKBENCvYOjCoYVWN2lRFCpwlrCskVUEUYlJ/00FtUtxpzArbGfNmalbAsaFp9Cg+Hc0K01Mx4V88LMVCiqA

VwIi+EoivAVxbEgV56KkVsipkVQIjkVzisAVUsKUVGB2YA6CrJJDwg0VcxK0VTBzwVXxMXxRisMVJCut0JiuZE4SvSVFippuYmzhBdioUxHAFEVDioUVTioSVLipkluVLkl+VOGlikscUjZVIAaSAWA5OAOI8vKroFUIcG2koGgIVFRcnfD/imPAcFzchcQ4JGVl+qgES3VMWyjaWrF7cTs45Rg74SMtVpQDSVZGtPulqrKfpl4oqSHkstld4o+l

D4q+lT4t1qu1Kli9rOjFrsshcbXCrELfGTFzsl05GIrbC8mFWlaPNxF0HOspocrg5l6HWQ9elYG0EoUc6MoyZCtCyZNIq4GKct2VNMn/qhyl7Chcs2GgopLl1MtDKzKhZlag3FF0yvaZ0os6ZEnPrlSwutp+gGmAzwH7ASfXMFU7N4AfsXZyHBUx4c9Eka6VFSUveiqot4BpqB6S2VReCUaauGtG7orOVZ4rs5lypf5V4v9FFsqiF70tcZvkseVd

ss8ZBI2BUoAo/F6FDCkvYWAl3suSFUqXUwQeS9kqItBVGPPBViUpS55sD80WVHx5giEChuiqS04KKFojWiBEFHO45c2loEViLREtoMqxIInnWANkwVQ/J18BcLdVWYFvQkGPUArqtFad2MVJMsPDOMAPdViqPqRVArUxwStnCU8J+EAAK0JVCoBsHCrOe4aoIVD2mLhc91sV3iIw5XqpkJKJIBs4bJZEgasyVWCpW8YapgVNiJLVMaplJcaoJxlO

MTVgQHLVk5Mpxaav4xGashEWat7VOWI3xlxP8s6iSa5eLOipTAvLZLAsrZvfI0g3EsdVJSqjVpavDVHqq4R1aoZWjWjrVAarVmQavUVIaubVTj3DVbapdVZaojV+FA1JCaoAB/atnCqaon56aqugD8LHVOavAx9Imqx06t0waBXBKPSsm58kv6VM3Kk5E4ocqVQGIAjoGZA+gGFAmqs7l2/JHY45FCoQeTeohwG/sbwBEwm0qRIgowpKHULQIEKD

5yIIwsZirL6hHou+FS8uNlPJTSGZsqc5hjU3lV7O3lWPN3lntK/Z2XjfFEPP8afWHKsyHB/c4qSOVkUoL6v9mRYik1KACXLkC+IuzF/WFrFMDKiyqMsQU5QBlEHEUMgVcPqRYG0lgB8K/AsEEgRhkG/muADkAl6qUSX3zwMPYPUeOig4gWlgHBv90Gu5iUksdEJR2FUnSeOAAj+HAGoAN3g6kHsPQMU5xElZ92RALUg012AE81BzRlm+mrkAAWpJ

AQWoOaPmrC1wohakAACp6QMoBmACNJ4tfFq7iElqIQV5rGOkjCQIX8Iw0ZdAIRB95/MVCBtcQABqfyDBay1oNtFy7ItRjpYKwLUJazLWpa9LWPSUgDJalhE6zdIkua/LUOamFack+wldavNqgQRGgBasrRKmVR6zoPLVQAJKDuwGbDEAY2gIANGwQATrVDarNqftabU0KKqRmaurVDa8gC0k5slra9AwGImjghbFqTWa5qSran74hq2LWDnBqIhq

hsHoKSnm6a47FR6dTWRarTWq6F7VhaqUGtq4zWlHe7Wlav74XnD3hWaqaTi/IcGCPOzVaWPrWe/JzV8QtHTua+gzZajA6ZaR7X+awLVVahtqha8gDhazHXRapRK3alPaJa9rUpa1ABpajLWk6rHU6zXLVVHUCEFajpHFa976aQGCAVaz7wo6rrW1a6rU6zBrWRaprWk6lrWU6jrWHarrUOa8J78Qt2H8wjnVHakbVZAMbUQACbUy/KbV06v4Szal

cDzaxbXLaq7VHatAwbalXU3SbbVFLQ5HS6nXVoGfbWeIrPGm617Vw+B0nna8HWtbbXWmam7W464USHajRU5LQo6uK41IlsglmeKxdXeKljm+KxKksM9ADKa5ECqa2uHvazTVHHL7Uqa5Hq4637U5IzLQma5+5G64HU3SUHUa2C7WQ64CDQ6jWyw6q6Dw6nrWI6jzUo6nzXo6lPaY6k3XjrH7URayWA3eBtoxal3VTbEnXJawXVtajrXV6vAy06yb

WZNQrUfhLUDM68rWVarvU6AjIG7ahtq86yWD86tvXk61rWZax3U6zMXUF6yXUSiUfWMdWXVCWaJYK6/XXK61R5q6xSDBABbWzoJbVlaRfVravXWTaiqSG6oHXG+K3U/fRSAW6ifU6ArEmnayqJ26sIAQ68/WtC+PUGa13WW6n/UV6sbnM036STCkDVz8lrKNlecAcgIwAVAAuIgCxDUN5ESbQOGlhCYWvgHi3k4QhLujc4b7K18S/k5+Okr2mN0w

ynE5XkayVUHsh6XP80Pr2816Ur6IMW3lN8ax9GoXhizQor+LVXcaucgtCT+RFMrUp29S2r1WRmqwyhkZwc2sWa8TwVpSxTUSAepE5bHTVx6nLZdREkATRKqRLAcNUyzEbY9giqQcQHxaf61rYVSHgA3eHzX2PKABvIBJYRwBaYo6kEB2AUOF6ARQ13ajWw2Gke6oAMrXmJQ7Wb6+XWkCdkC0oRoDk4C0BXeRqS764AAOGqSha6w7WftII2p4gAA8

7EGr15ushEy4TVAMvjSeZWhQsbbn/xEoipWK2rd1IarK02zy1RhAEYAcNO3V4QBnOOiiMNJhq9ggMyBEbhvwiM5zBpvz1TwMsJkNYeoEJ8hoBs4RowUuzFUN6hrT1zAE0NI0mz1ehoMNSiTKNkgFMNUQHMNWlksNeIFox7RsO17RqcNLhoANbhu31Hhs8gVyG8NvhtoM/hsm1gRs3AwRrP1oRsy08xqiNqwBiNj+riNnAASNsf1EhyRqawLm3SNp

O0yNABqwVORv7ceRoKNFugBsNRpcYpRqaw5RrMNLCOqNxRpcYihio5VUrcVDAqbGfurZ5+NOXVXEpD1DRqCCTRpe1rRpgitho6NKhpgVahtKOGhq0NAxv0Nnasy0IxrGNuAAmNGtimN1hr2NdhrwM8xucN/kFcNf2i31ZWlWNXhp8Nfhs21uxvRNIRoANYRqpNDUhONZxrzZ8RrxkHYCSNEABSN9xrYhs8yeNgOvhxBPlyNuYm+AHxtJ0tisxEPx

swUfxtGNFRsBNjJqduwJqgAWtgA1/Y1EFwGr6VEBpJFHTk5wygGaA1pOIA8wq35DeQWGBnM7iV5lBQ9Yl050mCupbGlqwGyHSFm7KqsytOosljNOV1jIoNFyovFsquuVAYo3ldyuVVn0qocTysKGu1LsG/0uD5QgTdslJVgFPDn1FSDPV40gVbEQhsdOIhveoRGEwE9qswmSiSJArMByOKOrcNZWlpcnuyeNeBjrNEAG8g7IDYABxo1sLZvZZUlD

P1OqR81VZvSWtZt1N9ZuNcfaqbN6BhbNbZqRAnZubNI5oV1uET7NdAo0FkJtLZ0Jvql7EtgJcJsJp7AuMoA5sCAQ5q0sLZobN45ob1k5vnN05o7NE5rQM3ZsXNK2uAN09LE54BopOUcs5pEGpSQFoB0CwoE0A9xDKKvWSCo9pG7IQTU5w3xC38a4s8Q55niAPhReUMuAI1/wBBZ08tasEqtDNnoqf5MquoNdGrf5dBqVVrnO/pLGrDF6aj1qp0lT

NoXPZgXiAAcCAQj5KzjEC/4vQoNMgHID4ELNqfLsptYtr0PJwIZMEromSiX0ATzgr1deqC1ZesJ1zeqTe1euPNY5uRsZ5qzajWsktOLVvNvZuvNP+qJ1/Zu4tvFo916Cn4t1OrQMTer/11R1Et85pPNEloOa0loOaclvP2ClqwVSluXN1UvcVUJta5Xio55PiqYZXXIRNPmp4tqRwKO6lqr1Wlm0tcADi1mltkt+lvEts5u3OfOpktc5tG142rvN

MlostwlofNYvMNstQsKp4Grm5I+EQgUGRqAcwD+lzKrGZYTNMlozDbSiDg+Fx5lqwd7jyohnj8E/psopN/L8gKYW2Yx4v1lp4rDN54uVOkZvnyN4ovZn9JiFIYp3lBFrs0u1LVi4PKPlbsrnIxDTa8SEyotU0HeyRqra4xRhGgWniDlmDKk1cLJk1JZrIY8mqz5ydIgAMszctFesJNvIgPNNZqPNF5qCAM5vvNBUq2tO1rUtNOyzAmWkHNh1q7Nx

1vbNS5sqlhqWstq5t91dlv91DlsD1TlurZ3dO2tqlo8t11v3N1ZrJN4Vrl1ZWkvNz1t6ltLJANDWQSts/JfNBYsGVs+HAABMDUIvlq5AKyBBU0ABfxJUDPAYokGADAFfuFADq2l4zNwUS0ptrypqIMxPVYgQS5AZBpQtYilptb6kCCZNsVO1GokoLNsS06QEWwT0qJtEWLoQPNv0ADNswtBQC5tkWLpt6QFFtMXTQSEtqFtgQW4ajGpptkttZt6Q

D/Qn/OZtqtuFtxol8iDAvltKjECCutu6Ck7QNtUtspyLPPXNZtrVtItvLljMvIw1tuFtw2mZlTTNZlKtoVt6QA5UNQFTIJ0AFt3NqNt+iG4a8oG0IFYH20iIEXMbwHTG8CEAt2TmwoQ5A2gYdvZAEGC7YFwF9CtRWDqZqsgARgG7g65mEqPdLcgcxAkwvHhfwjtsVth8ptAgfKJtRIBIAs6q1kNdr6A5cELEuwChiJADSQdtGG0gxCP1YEhbt8I0

lQzQGzmLxGUAeIBakwpxGko9t4AhHF2YP8EUMjkF9A4JioQ7WuHtLdDHtLA14Aq9sVoXUhLtgttugMtoQAGtpR2oLD3yjkCzAf2hjK/jk7tESBJOYJkIAjdpE5dEHlsxpqDwtkHHgj9oFUPolIA/YGJgr9oFo79o7t4EEvtExBLtImOYAtgwM1bdtMQf9q7tYCjUIQ3kYANQCOOz6lU51bhFNphFxQrwjYO3toXQ0coU1iJpeQwQBl8c7g9gpLjE

gcDoQdSkubt84QvttaP6AMqFTA3drFo0ZXJwJv1B25QEyAF9rPY4muxUkDoAd6enE1RTEUcoDt8tlyG4d9sBHg4AG6Qx7FmwxtAWQSUCAAA=
```
%%