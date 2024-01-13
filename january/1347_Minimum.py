from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        char_count = Counter(t)
        for char in s:
            if char in char_count:
                char_count[char] -= 1
        ans = 0
        for x in char_count:
            if char_count[x] > 0:
                ans += char_count[x]
        return ans