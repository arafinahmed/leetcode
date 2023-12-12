from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, prev2, curr = 0, 0, 0

        for i in nums:
            curr = max(prev, i+prev2)
            prev2 = prev
            prev = curr

        return curr