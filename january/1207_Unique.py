from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        element = set()
        occurances = {}
        occurance_set = set()
        for num in arr:
            element.add(num)
            occurances[num] = occurances.get(num, 0) + 1

        for x in occurances.values():
            occurance_set.add(x)

        return len(element) == len(occurance_set)