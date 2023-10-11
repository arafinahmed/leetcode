class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        best = 0

        for num in nums:
            if num - 1 not in nums:
                y = num + 1
                while y in nums:
                    y += 1
                best = max(best, y - num)
        return best

# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums_dict = {}
#         best = 0

#         for num in nums:
#             nums_dict[num] = 1
        
#         for key in nums_dict:
#             if key - 1 not in nums_dict:
#                 y = key + 1
#                 while y in nums_dict:
#                     y += 1
#                 best = max(best, y - key)
#         return best