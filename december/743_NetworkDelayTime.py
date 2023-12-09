from typing import List

import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append((v, w))

        visited = set()
        minHeap = [(0, k)]

        while minHeap:
            time, node = heapq.heappop(minHeap)
            visited.add(node)

            if len(visited) == n:
                return time
            
            for nei, neiTime in graph[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (time+neiTime, nei))

        return -1