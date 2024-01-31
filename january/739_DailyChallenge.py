from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            curr_temp = temperatures[i]

            while stack and curr_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index

            stack.append(i)

        return result