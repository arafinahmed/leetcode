class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        @lru_cache(None)
        def dfs(i, j, k):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if k == 0:
                return 0
            return dfs(i - 1, j, k - 1) + dfs(i + 1, j, k - 1) + dfs(i, j - 1, k - 1) + dfs(i, j + 1, k - 1)
        
        return dfs(startRow, startColumn, maxMove) % (10**9 + 7)