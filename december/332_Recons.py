from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}

        for src, dst in tickets:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = [dst]

        for src in graph:
            graph[src].sort(reverse=True)

        stack = ['JFK']
        itinerary = []

        while stack:

            elem = stack[-1]

            if elem in graph and graph[elem]:
                stack.append(graph[elem].pop())
            else:
                itinerary.append(stack.pop())
        
        return itinerary[::-1]
                
