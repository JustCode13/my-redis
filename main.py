from kvstore import KeyValueStore
import datetime
import time

def main():
    store = KeyValueStore()

    print("\n--- SET OPERATIONS ---")

    store.set("otp", {"userid": "123", "name": "tea", "age": 20})
    store.set("cart", ["PC", "Laptop", "Bag"], ttl=2)
    store.set("session", {"token": "abc123"}, ttl=5)
    store.set("user", "Tanmaya")
    store.set("temp", 999)

    print("Size after inserts:", store.size())

    print("\n--- GET OPERATIONS ---")

    print("otp:", store.get("otp"))
    print("cart:", store.get("cart"))
    print("user:", store.get("user"))

    print("\n--- EXISTS CHECK ---")

    print("exists otp:", store.exists("otp"))
    print("exists random:", store.exists("random_key"))

    print("\n--- DELETE OPERATION ---")

    store.delete("otp")
    print("exists otp after delete:", store.exists("otp"))

    print("\n--- TTL TEST (wait 3 seconds) ---")

    import time
    time.sleep(3)

    try:
        print("cart after expiry:", store.get("cart"))
    except Exception as e:
        print("cart expired:", e)

    print("\n--- LRU TEST ---")

    store.set("A", 1)
    store.set("B", 2)
    store.set("C", 3)

    store.get("A")  # A becomes recent
    store.get("B")  # B becomes recent

    store.set("D", 4)  # should evict LRU if max_size reached

    print("A:", store.get("A"))
    print("B:", store.get("B"))
    print("C:", store.get("C"))
    print("D:", store.get("D"))

    print("\n--- SIZE CHECK ---")
    print("Final size:", store.size())

    print("\n--- PERSISTENCE TEST ---")
    store._save()
    store._load()

    print("After reload:")
    print("user:", store.get("user"))
    print("session:", store.get("session"))

    print("\n--- CLEANUP ---")
    store.clear()
    print("Size after clear:", store.size())


if __name__ == "__main__":
    main()
    
    