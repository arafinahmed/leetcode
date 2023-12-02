# class MinStack:

#     def __init__(self):
#         self.__stack = []
#         self.__min_stack = []
        

#     def push(self, val: int) -> None:
#         self.__stack.append(val)
#         if len(self.__min_stack) == 0 or val <= self.__min_stack[-1]:
#             self.__min_stack.append(val)
        

#     def pop(self) -> None:
#         out = self.__stack.pop()
#         if out == self.__min_stack[-1]:
#             self.__min_stack.pop()
        

#     def top(self) -> int:
#         return self.__stack[-1]
        

#     def getMin(self) -> int:
#         return self.__min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



class MinStack:

    def __init__(self):
        self.__stack = []
        

    def push(self, val: int) -> None:
        if len(self.__stack) == 0:
            self.__stack.append((val, val))
        else:
            self.__stack.append((val, min(val, self.__stack[-1][1])))
        

    def pop(self) -> None:
        if len(self.__stack) != 0:
            self.__stack.pop()
        

    def top(self) -> int:
        return self.__stack[-1][0]
        

    def getMin(self) -> int:
        return self.__stack[-1][1]