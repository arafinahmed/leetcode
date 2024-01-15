from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()        
        lossers = set()
        lossers_multiple = set()

        for match in matches:
            players.add(match[0])
            if match[1] not in lossers:
                lossers.add(match[1])
            else:
                lossers_multiple.add(match[1])

        ans = []
        # print(players, lossers, lossers_multiple)
        ans.append(sorted(list((players - lossers) - lossers_multiple)))
        ans.append(sorted(list(lossers - lossers_multiple)))
        return ans
        
