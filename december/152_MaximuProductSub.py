from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        imax = imin = res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax

            
            imax = max(nums[i], imax*nums[i])
            imin = min(nums[i], imin*nums[i])

            res = max(res, imax)
        
        return res