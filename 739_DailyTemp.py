class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        l = len(temperatures)
        stack = []
        ans = [0] * l
        for i in range(l-1, -1, -1):
            if i == l-1:
                ans[i] = 0
                stack.append((temperatures[i], i))
            else:
                while stack and stack[-1][0] <= temperatures[i]:
                    stack.pop()
                if stack:
                    ans[i] = stack[-1][1] - i
                else:
                    ans[i] = 0
                stack.append((temperatures[i], i))

        return ans
            