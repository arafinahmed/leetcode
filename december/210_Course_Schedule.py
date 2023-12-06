from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = [[] for _ in range(numCourses)]
        self.visited = [0 for _ in range(numCourses)]
        self.order = []

        for course, pre in prerequisites:
            self.graph[course].append(pre)

        for i in range(numCourses):
            if not self.dfs(i):
                return []
        
        return self.order[::-1]
    
    def dfs(self, node):
        if self.visited[node] == -1:
            return False
        
        if self.visited[node] == 1:
            return True
        
        self.visited[node] = -1

        for neighbor in self.graph[node]:
            if not self.dfs(neighbor):
                return False
        
        self.visited[node] = 1
        self.order.append(node)
        return True
