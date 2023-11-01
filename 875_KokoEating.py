from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(piles, k, h):
            return sum((p-1)//k+1 for p in piles) <= h
        
        l, r = 1, max(piles)
        while l < r:
            mid = (l+r)//2
            if canEat(piles, mid, h):
                r = mid
            else:
                l = mid+1
        return l