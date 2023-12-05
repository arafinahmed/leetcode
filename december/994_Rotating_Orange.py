from typing import List

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return -1

        rows, cols = len(grid), len(grid[0])

        fresh_count = 0

        rotten = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1

        minutes_passed = 0

        while rotten and fresh_count > 0:
            minutes_passed += 1

            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_x, new_y = x + dx, y + dy

                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                        fresh_count -= 1
                        grid[new_x][new_y] = 2
                        rotten.append((new_x, new_y))

        return minutes_passed if fresh_count == 0 else -1
         