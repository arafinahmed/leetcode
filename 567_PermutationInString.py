class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        counter, w = Counter(s1), len(s1)
        
        len_s2 = len(s2)
        
        for i in range(len_s2):
            if s2[i] in counter:
                counter[s2[i]] -= 1
            
            if i >= w and s2[i-w] in counter:
                counter[s2[i-w]] += 1

            if all(val ==0 for val in counter.values()):
                return True
            
        return False

sol = Solution()
sol.checkInclusion("ab", "eidbaooo")