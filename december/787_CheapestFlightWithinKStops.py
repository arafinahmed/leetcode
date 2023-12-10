from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        minHeap = [(0, src, k + 1)]
        dist = [[float('inf')] * (k + 2) for _ in range(n)]

        for u, v, w in flights:
            graph[u].append((v, w))

        while minHeap:
            cost, u, stops = heapq.heappop(minHeap)
            if u == dst:
                return cost
            
            if stops > 0:
                for v, w in graph[u]:
                    if cost + w < dist[v][stops - 1]:
                        dist[v][stops - 1] = cost + w
                        heapq.heappush(minHeap, (cost + w, v, stops - 1))


        return -1
            

        
