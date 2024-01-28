from typing import List
import collections

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])

        # Precompute the prefix sum of each row.
        for row in matrix:
            for i in range(1, n):
                row[i] += row[i-1]

        count = 0

        # Iterate over all pairs of columns.
        for i in range(n):
            for j in range(i, n):

                c = collections.defaultdict(int)
                cur, c[0] = 0, 1

                for k in range(m):
                    cur += matrix[k][j] - (matrix[k][i-1] if i > 0 else 0)
                    count += c[cur - target]
                    c[cur] += 1
        
        return count