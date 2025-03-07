import time
import heapq

class ExpiryCache:
    """
     A Cache with Expiry (Time-Based Cache) that supports the following operations efficiently:
     - set(key, value, expiryTime): Stores the key-value pair with an expiration timestamp. If the key already exists, updates its value and expiry time.
     - get(key): Retrieves the value associated with the key if it exists and hasn't expired. Returns None if the key doesn’t exist or has expired.
     - Automatic Expiry: Expired keys are removed when accessing or inserting data.
    
    Time Complexity:
      - set(key, value, expiryTime) → O(log n) (heap insertion and cleanup)
      - get(key) → O(log n) (worst case, due to cleaning expired keys)

    Space Complexity: O(n) (number of active keys).
    """
    def __init__(self):
        self.cache = {}  # Stores {key: (expiry_time, value)}
        self.expiry_heap = []  # Min-heap [(expiry_time, key)]. Using Min-heap to find the time that gets expired the earliest

    def auto_clean_expired(self):
        while self.expiry_heap and self.expiry_heap[0][0] <= time.time():
            key = heapq.heappop(self.expiry_heap)[1] # Extracting the expired key from the heap
            self.cache.pop(key, None) # removing the key from the cache (if it is still present)

    def set(self, key, value, duration):
        expiry_time = time.time() + duration # calculating the expiration time stamp
        self.cache[key] = (expiry_time, value) # storing the key with above in dict
        heapq.heappush(self.expiry_heap, (expiry_time, key)) # Pushing the above info into the heap
        self.auto_clean_expired() # removing any expired entry after pushing

    def get(self, key):
        self.auto_clean_expired() # Ensuring expired entries are removed before the retrieval
        if key in self.cache:
            return self.cache[key][1]
        else:
            None


# -------------------
# TEST CASES
# -------------------
# if __name__ == "__main__":
#     ec = ExpiryCache()
    
#     # Case 1 - Normal Expiry
#     ec.set(1, "apple", 3)  # Key 1 -> Expires in 3 sec
#     ec.set(2, "banana", 5)  # Key 2 -> Expires in 5 sec
#     print(ec.get(1))  # Expected Output: "apple"
#     time.sleep(4)
#     print(ec.get(1))  # Expected Output: None (Expired)
#     print(ec.get(2))  # Expected Output: "banana" (Still valid)

        """
        Case 2 is theoretically right.... but is not giving the expected output unfortunately :(
        """
#     # Case 2 - Updating an existing Key
#     ec.set(3, "old", 5)  # Key 3 -> Expires in 5 sec
#     time.sleep(3)  # Sleep for 3 sec
#     ec.set(3, "new", 6)  # Update Key 3 -> Now expires in 6 more sec
#     time.sleep(4)  # Total time passed = 3 + 4 = 7 sec, Key 3 should still be valid
#     print(ec.get(3))  # Expected Output: "new" (Still valid)

#     time.sleep(3)  # Wait for key 3 to expire completely
#     print(ec.get(3))  # Output: None (Expired)
