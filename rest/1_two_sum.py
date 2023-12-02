class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        l = len(nums)
        for i in range(l):
            num_map[nums[i]] = i

        for i in range(l):
            remaining = target - nums[i]
            if remaining in num_map and num_map[remaining] != i:
                return [i, num_map[remaining]]
        
        return []