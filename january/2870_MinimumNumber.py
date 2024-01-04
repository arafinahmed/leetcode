from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        numdict = {}
        count = 0
        for num in nums:
            numdict[num] = numdict.get(num, 0) + 1           
        
        for value in numdict.values():
            print(value)
            if value % 3 == 0:
                count += value // 3
            elif (value-2) % 3 == 0 and value > 3:
                count += ((value//3) +1)
            elif (value-4) % 3 == 0 and value > 3:
                count += ((value//3) +1)
            elif value == 2:
                count += 1
            else:
                return -1
        return count