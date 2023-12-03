from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [['.'] * n for _ in range(n)]

        def dfs(row):
            if row == n:
                res.append([''.join(row) for row in board])
                return
            
            for i in range(n):
                if i not in col and row + i not in posDiag and row - i not in negDiag:
                    col.add(i)
                    posDiag.add(row + i)
                    negDiag.add(row - i)
                    board[row][i] = 'Q'
                    dfs(row + 1)
                    col.remove(i)
                    posDiag.remove(row + i)
                    negDiag.remove(row - i)
                    board[row][i] = '.'

        dfs(0)
        return res