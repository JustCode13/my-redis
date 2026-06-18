from kvstore import KeyValueStore
import datetime
import time

def main():
    kvstore = KeyValueStore()
    kvstore.set(
        "otp", 
        {"userid":"123","name":"tea","age":20}
        )



if __name__ == "__main__":
    main()
