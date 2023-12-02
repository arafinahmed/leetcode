class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operands = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token not in operands:
                stack.append(int(token))
                print(stack[-1])
            else:
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                elif token == "/":
                    stack.append(int(left*1.0 / right))
        return stack[-1]