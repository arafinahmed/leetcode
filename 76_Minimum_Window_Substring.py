class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "": return ""

        from collections import Counter
        
        countT = Counter(t)
        hm = {}
        
        match, need = 0, len(countT)

        result = [-1, -1]
        reslen = len(s)+10

        l = 0

        for r in range(len(s)):
            c = s[r]

            hm[c] = 1 + hm.get(c, 0)

            if c in countT and hm[c] == countT[c]:
                match += 1
            
            while match == need:
                if r-l+1 < reslen:
                    result = [l, r]
                    reslen = r-l+1

                hm[s[l]] -= 1
                if s[l] in countT and hm[s[l]] < countT[s[l]]:
                    match -= 1
                
                l += 1
        
        
        l, r = result
        return s[l:r+1] if reslen != len(s)+10 else ""




s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
