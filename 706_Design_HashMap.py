class MyHashMap:

    def __init__(self):
        self.dict = {}

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value
        

    def get(self, key: int) -> int:
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if key in self.dict.keys():
            del self.dict[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# This is more slower.
# class MyHashMap:

#     def __init__(self):
#         self.dict = [None] * 1000001

#     def put(self, key: int, value: int) -> None:
#         self.dict[key] = value
        

#     def get(self, key: int) -> int:
#         if self.dict[key] == None: 
#             return -1
#         else:
#             return self.dict[key]
        

#     def remove(self, key: int) -> None:
#         self.dict[key] = None