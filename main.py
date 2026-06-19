from kvstore import KeyValueStore
import datetime
import time

def main():
    store = KeyValueStore()
    store.set(
        "otp", 
        {"userid":"123","name":"tea","age":20},
        )
    store.set(
        "shoppingcart", 
        ["PC","Laptop","Bag"],
        1
        )   
    
    
    
    


if __name__ == "__main__":
    main()
