from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A
        
        m, n = len(A), len(B)
        total, half_len = m + n, (m + n) // 2
        left, right = 0, m - 1

        while True:
            i = (left + right) // 2 #A
            j = half_len - i - 2 #B

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1]  if i+1 < m else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if j+1 < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1