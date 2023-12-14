class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        resLen = 0
        ln = len(s)
        for i in range(ln):
            # odd length
            l, r = i, i
            while l>=0 and r<ln and s[l]==s[r]:
                count += 1

                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l>=0 and r<ln and s[l]==s[r]:
                count += 1

                l -= 1
                r += 1

        return count