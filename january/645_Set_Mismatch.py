from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = [0] + nums
        nums = sorted(nums)
        missing = 0

        for i in range(1, n + 1):
            if nums[i] == nums[i - 1]:
                duplicate = nums[i]
            elif nums[i] - nums[i - 1] > 1:
                missing = nums[i - 1] + 1

        if nums[-1] != n:
            missing = n

        return [duplicate, missing]
        