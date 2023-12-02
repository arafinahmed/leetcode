# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         # s = s.lower()
#         main_str = ''
#         for char in s:
#             if char.isalnum():
#                 main_str += char.lower()
        
#         print(main_str)
#         print(main_str[::-1])
#         return main_str == main_str[::-1]


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum(): 
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1; r -= 1
        return True