class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        char_dict = {}
        max_len = 0
        first_idx = 0
        for i in range(n):
            if s[i] not in char_dict or char_dict[s[i]] < first_idx:
                char_dict[s[i]] = i
                max_len = max(max_len, i - first_idx + 1)
            else:
                first_idx = char_dict[s[i]] + 1
                char_dict[s[i]] = i
        
        return max_len
    
sol = Solution()
print(sol.lengthOfLongestSubstring("tmmzuxt"))