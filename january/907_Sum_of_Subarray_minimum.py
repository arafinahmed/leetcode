from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        result = 0
        arr = [0] + arr + [0]

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                j = stack.pop()
                k = stack[-1]
                result += arr[j] * (i - j) * (j - k)
            stack.append(i)

        return result % MOD