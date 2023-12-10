from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}

        while pq:
            t, x, y = heapq.heappop(pq)

            if x == y == n - 1:
                return t

            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= i < n and 0 <= j < n and (i, j) not in seen:
                    seen.add((i, j))
                    heapq.heappush(pq, (max(t, grid[i][j]), i, j))