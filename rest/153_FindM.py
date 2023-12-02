from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            mid = (l+r)//2
            if nums[l] < nums[r]:
                r = mid
            elif nums[r] > nums[mid]:
                r = mid
            else:
                l = mid + 1
        return nums[l]