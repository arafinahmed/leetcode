from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        set_n = set(range(1, n+1))
        set_nums = set(nums)

        missing = set_n - set_nums
        duplicate = sum(nums) - sum(set_nums)

        return [duplicate, missing.pop()]
        