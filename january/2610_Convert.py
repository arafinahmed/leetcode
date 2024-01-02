from typing import List
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        numsarray = [0]*(len(nums)+1)
        sum = 0
        result = []
        for num in nums:
            numsarray[num] += 1
            sum += 1

        while sum:
            row = []
            for i in range(1, len(nums)+1):
                if numsarray[i] > 0:
                    sum -= 1
                    numsarray[i] -= 1
                    row.append(i)

            result.append(row)
        
        return result
            




        