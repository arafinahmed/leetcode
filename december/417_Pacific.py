from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []

        rows, cols = len(heights), len(heights[0])
        p_visited = set()
        a_visited = set()
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            
            visited.add((i, j))

            for x, y in direction:
                new_i, new_j = i + x, j + y

                if 0 <= new_i < rows and 0 <= new_j < cols and \
                    heights[new_i][new_j] >= heights[i][j]:
                    traverse(new_i, new_j, visited)

        for row in range(rows):
            traverse(row, 0, p_visited)
            traverse(row, cols - 1, a_visited)

        for col in range(cols):
            traverse(0, col, p_visited)
            traverse(rows - 1, col, a_visited)

        return list(a_visited & p_visited)

            

        