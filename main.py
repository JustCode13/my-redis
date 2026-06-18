from kvstore import KeyValueStore
import datetime
import time

def main():
    kvstore = KeyValueStore()
    kvstore.set(
        "otp", 
        {"userid":"123","name":"tea","age":20},
        1
        )
    kvstore.set(
        "shoppingcart", 
        ["PC","Laptop","Bag"],
        1
        )   
    kvstore.get("otp")
    kvstore.delete("otp")


if __name__ == "__main__":
    main()
