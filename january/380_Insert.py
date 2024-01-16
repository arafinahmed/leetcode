import random
class RandomizedSet:

    def __init__(self):
        self.data_map = {}
        self.data = []
        

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True
        
        

    def remove(self, val: int) -> bool:

        if val not in self.data_map:
            return False
        
        last_item = self.data[-1]
        removed_index = self.data_map[val]

        if last_item == val:
            self.data.pop()
            del self.data_map[val]
            return True

        self.data.pop(removed_index)
        self.data.insert(removed_index, last_item)
        self.data.pop()
        self.data_map[last_item] = removed_index

        del self.data_map[val]

        return True
        

        


    def getRandom(self) -> int:
        return random.choice(self.data)