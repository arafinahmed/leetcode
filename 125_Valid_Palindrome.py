class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s = s.lower()
        main_str = ''
        for char in s:
            if char.isalnum():
                s = main_str + char.lower()
        
        print(main_str)
        print(main_str[::-1])
        return main_str == main_str[::-1]