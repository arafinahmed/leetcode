# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         count = 0
#         resLen = 0
#         ln = len(s)
#         for i in range(ln):
#             # odd length
#             l, r = i, i
#             while l>=0 and r<ln and s[l]==s[r]:
#                 count += 1

#                 l -= 1
#                 r += 1
            
#             # even length
#             l, r = i, i + 1
#             while l>=0 and r<ln and s[l]==s[r]:
#                 count += 1

#                 l -= 1
#                 r += 1

#         return count


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        count = 0

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and ((j-i+1) < 3 or dp[i+1][j-1])
                count += dp[i][j]

        return count