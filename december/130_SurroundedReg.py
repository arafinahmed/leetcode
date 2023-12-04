from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # 1. Find all 'O's on the border and mark them as 'B'
        # 2. Find all 'O's in the middle and mark them as 'X'
        # 3. Find all 'B's and mark them back to 'O'
        
        if not board or not board[0]: return

        rows, cols = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O': return

            board[i][j] = 'U'

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i == 0 or i == rows - 1 or j == 0 or j == cols - 1):
                    dfs(i, j)

        for i in range(1, rows-1):
            for j in range(1, cols-1):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'U':
                    board[i][j] = 'O'
