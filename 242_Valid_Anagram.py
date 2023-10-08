class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        anagram_dict = [0 for i in range(135)]
        if len(s) != len(t):
            return False
        
        for char in s:
            anagram_dict[ord(char)] += 1

        for char in t:
            anagram_dict[ord(char)] -= 1
            
        for i in range(120):
            if anagram_dict[i] != 0:
                return False    
        return True
                
sol = Solution()
print(sol.isAnagram("nl", "cx"))