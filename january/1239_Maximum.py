from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(s):
            return len(s) == len(set(s))

        def backtrack(i, s):
            if i == len(arr):
                return len(s)

            if not is_unique(s + arr[i]):
                return backtrack(i + 1, s)

            return max(backtrack(i + 1, s + arr[i]), backtrack(i + 1, s))

        return backtrack(0, "")