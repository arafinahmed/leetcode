from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    total = self.dfs(grid, i, j)
                    count = max(count, total)
        return count
    
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid[0]) or \
            grid[i][j] == 0:
            return 0
        
        grid[i][j] = 0

        right = self.dfs(grid, i+1, j)
        left = self.dfs(grid, i-1, j)
        up = self.dfs(grid, i, j+1)
        down = self.dfs(grid, i, j-1)

        return right + left + up + down + 1
        