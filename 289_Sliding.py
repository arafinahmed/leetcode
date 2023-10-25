
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        ans_list = [nums[0]]
        for i in range(k):
            queue.append(nums[i])
            if nums[i] > ans_list[0]:
                ans_list[0] = nums[i]

        max_in_window = ans_list[0]
        for i in range(k, len(nums)):
            first = queue.pop(0)
            queue.append(nums[i])
            if nums[i] >= max_in_window:
                max_in_window = nums[i]
            elif first == max_in_window:
                max_in_window = max(queue)
            
            ans_list.append(max_in_window)

        return ans_list
        