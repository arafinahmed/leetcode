class Solution(object):
    def majorityElement(self, nums):
        ans = {}
        for i in nums:
            if i in ans.keys():
                ans[i] += 1
            else:
                ans[i] = 1
        return [ i for i in ans.keys() if ans[i] > len(nums) / 3]