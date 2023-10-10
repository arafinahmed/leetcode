class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_dict = [{} for _ in range(9)]
        col_dict = [{} for _ in range(9)]
        region_dict = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_dict[i]:
                        return False
                    else:
                        row_dict[i][board[i][j]] = 1
                    
                    if board[i][j] in col_dict[j]:
                        return False
                    else:
                        col_dict[j][board[i][j]] = 1

                    if board[i][j] in region_dict[i//3+(j//3)*3]:
                        return False
                    else:
                        region_dict[i//3+(j//3)*3][board[i][j]] = 1
        return True