from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        def helper(res, list1):
            result.append(res)

            if not list1:
                return
            
            for j in range(len(list1)):
                helper(res+[list1[j]], list1[j+1:])
        helper([], nums)
        return result
        