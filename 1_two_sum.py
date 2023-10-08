class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in nums:
            remainings = target - num
            if remainings in nums:
                if remainings == num:
                    if nums.count(num) > 1:
                        return [i for i, x in enumerate(nums) if x == num]
                else:
                    return [nums.index(num), nums.index(remainings)]