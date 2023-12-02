
# from typing import List

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         queue = []
#         ans_list = [nums[0]]
#         for i in range(k):
#             queue.append(nums[i])
#             if nums[i] > ans_list[0]:
#                 ans_list[0] = nums[i]

#         max_in_window = ans_list[0]
#         for i in range(k, len(nums)):
#             first = queue.pop(0)
#             queue.append(nums[i])
#             if nums[i] >= max_in_window:
#                 max_in_window = nums[i]
#             elif first == max_in_window:
#                 max_in_window = max(queue)
            
#             ans_list.append(max_in_window)

#         return ans_list
        

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        queue_index = collections.deque()
        ans_list = []

        for i, n in enumerate(nums):
            while queue_index and nums[queue_index[-1]] < n:
                queue_index.pop()
            queue_index.append(i)
            
            if queue_index[0] == i-k:
                queue_index.popleft()
            
            if i >= k-1:
                ans_list.append(nums[queue_index[0]])

        return ans_list
