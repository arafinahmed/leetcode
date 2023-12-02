from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])


        l, r = 0, m-1
        while l < r:
            mid = (l+r)//2
            if matrix[0][mid] < target:
                l = mid+1
            elif matrix[0][mid] > target:
                r = mid
            else:
                return True
        col = (l+r)//2
        if matrix[0][col] == target:
            return True
        elif matrix[0][col] > target:
            col -= 1
        
        l, r = 0, n-1
        while l < r:
            mid = (l+r)//2
            if matrix[mid][0] < target:
                l = mid+1
            elif matrix[mid][0] > target:
                r = mid
            else:
                return True
        row = (l+r)//2
        if matrix[row][0] == target:
            return True
        elif matrix[row][0] > target:
            row -= 1
        return False
    
x = Solution()
print(x.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11))
