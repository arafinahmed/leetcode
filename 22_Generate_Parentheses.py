class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = ["("]
        for i in range(2*n-1):
            temp = []
            for s in ans:
                if s.count("(") < n:
                    temp.append(s+"(")
                if s.count(")") < s.count("("):
                    temp.append(s+")")
            ans = temp
        return ans
