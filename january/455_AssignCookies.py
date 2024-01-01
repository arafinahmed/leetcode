from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        count = 0
        start = 0
        
        while count < len(s) and start < len(g):
            if g[count] <= s[start]:
                count += 1
            start += 1

        return count
        