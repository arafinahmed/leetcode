from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s&1:
            return False
        
        target_sum = s // 2

        dp = [True] + [False] * (target_sum+1)

        for num in nums:
            for j in range(target_sum, num-1, -1):
                dp[j] = dp[j] or dp[j-num]

        return dp[target_sum]
        