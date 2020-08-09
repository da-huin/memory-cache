import time


class MemoryCache():
    """
    It is a package that simply stores and uses a cache in memory.

    Use it like the code below:

    ```python
    import memory_cache
    import time
    import random

    cache = memory_cache.MemoryCache()

    cache_time = 10
    working_time = 4
    while True:
        print("\n=== Press any key to get started. ===")
        input()

        key = "fruit"
        data = cache.get(key)

        if data == None:
            print(f"working for {working_time} seconds ...")

            time.sleep(working_time)

            data = {"name": "apple", "price": "120"}
            cache.put(key, data, cache_time=cache_time)

            print("working complete!")
        else:
            print("cached!")

        print(data)
    ```
    """    
    def __init__(self):
        self.cache = {}

    def put(self, key, value, cache_time=-1):
        """
        **Parameters**

        * `key`: str

            It is a key for storing data and finding data.

        * `value`: any type

            The data to be saved.

        * `cache_time`: int (default: -1)

            Cache time. If this value is -1, it is not cached
        """
        self.cache[key] = {
            "value": value,
            "cache_time": cache_time,
            "put_time": time.time(),
        }

    def get(self, key):
        """
        **Parameters**

        * `key`: str

            It is a key for storing data and finding data.        
        """

        if key not in self.cache:
            return None

        if not self._is_exist_key(key):
            return None

        if self._is_expired(key):
            return None
        
        return self._get_cache_piece(key)["value"]

    def _is_exist_key(self, key):
        if key not in self.cache:
            return False
        return True

    def _get_cache_piece(self, key):
        return self.cache[key]

    def _is_expired(self, key):

        cache_piece = self._get_cache_piece(key)
        cache_time = cache_piece["cache_time"]
        put_time = cache_piece["put_time"]
        if cache_time == -1:
            return False

        if (time.time() - put_time) > cache_time:
            return True
        return False
