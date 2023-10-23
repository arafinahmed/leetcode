class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        counter, w, match = Counter(s1), len(s1), 0
        
        len_s2 = len(s2)
        
        for i in range(len_s2):
            if s2[i] in counter:
                if not counter[s2[i]]:
                    match -= 1
                counter[s2[i]] -= 1
                if not counter[s2[i]]:
                    match += 1
            
            if i >= w and s2[i-w] in counter:
                if not counter[s2[i-w]]:
                    match -= 1
                counter[s2[i-w]] += 1
                if not counter[s2[i-w]]:
                    match += 1

            if match == len(counter):
                return True
        return False

sol = Solution()
sol.checkInclusion("ab", "eidbaooo")