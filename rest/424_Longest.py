class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dict_letter = {}
        for i in range(ord('A'), ord('Z') + 1):
            dict_letter[chr(i)] = 0
        
        n = len(s)
        max_len = 0
        maxCharCount = 0
        start = 0

        for end in range(n):
            dict_letter[s[end]] += 1
            maxCharCount = max(maxCharCount, dict_letter[s[end]])
            
            if end - start + 1 - maxCharCount > k:
                dict_letter[s[start]] -= 1
                start += 1
            
            max_len = max(max_len, end - start + 1)
        return max_len

        


sol = Solution()
print(sol.characterReplacement("ABAB", 2))