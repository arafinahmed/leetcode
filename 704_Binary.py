from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, l2 = 0, len(nums)-1, len(nums)

        while l <= r and r < l2:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                return m
        return -1
        