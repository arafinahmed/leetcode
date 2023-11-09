class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.stack.remove(key)
            self.stack.append(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.stack.remove(key)
        elif len(self.stack) == self.capacity:
            del self.cache[self.stack.pop(0)]
        self.stack.append(key)
        self.cache[key] = value
        return None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)