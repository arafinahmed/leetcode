from typing import List

# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         if not board:
#             return False
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if self.dfs(board, i, j, word):
#                     return True
                
#         return False
    
#     def dfs(self, board, i, j, word):
#         if len(word) == 0:
#             return True
        
#         if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
#             return False
        
#         temp = board[i][j]
#         board[i][j] = "#"

#         res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])

#         board[i][j] = temp

#         return res
    
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n, ln = len(board), len(board[0]), len(word)

        def backtrack(i, j, idx):
            if idx == ln:
                return True
            
            for di, dj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                tmp, board[i][j] =  board[i][j], "#"
                if 0 <= di < m and 0 <= dj < n and board[di][dj] == word[idx]:
                    if backtrack(di, dj, idx+1):
                        return True
                board[i][j] = tmp
            
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 1):
                        return True
        return False