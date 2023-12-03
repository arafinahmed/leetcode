from typing import List

# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
        
#         if not digits:
#             return []
        
#         res = []
#         self.dfs(digits, 0, [], res)
#         return res
    
#     def dfs(self, digits, index, path, res):
#         if index == len(digits):
#             res.append(''.join(path))
#             return
        
#         for c in self.getLetters(digits[index]):
#             path.append(c)
#             self.dfs(digits, index + 1, path, res)
#             path.pop()

#     def getLetters(self, digit):
#         if digit == '2':
#             return 'abc'
#         elif digit == '3':
#             return 'def'
#         elif digit == '4':
#             return 'ghi'
#         elif digit == '5':
#             return 'jkl'
#         elif digit == '6':
#             return 'mno'
#         elif digit == '7':
#             return 'pqrs'
#         elif digit == '8':
#             return 'tuv'
#         elif digit == '9':
#             return 'wxyz'
#         else:
#             return ''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl', 
            '6': 'mno', 
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz'
        }

        if len(digits) == 0:
            return []
        
        if len(digits) == 1:
            return list(mapping[digits[0]])
        
        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]

        return [s + c for s in prev for c in additional]