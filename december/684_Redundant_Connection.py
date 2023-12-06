from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {v:-1 for v in range(1, len(edges)+1)}

        def find(u):

            if parent[u] != -1:
                parent[u] = find(parent[u])
                return parent[u]
            
            return u
        
        def union(u, v):
            p_u = find(u)
            p_v = find(v)

            if p_u == p_v:
                return True
            
            parent[p_u] = p_v
            return False
        
        redundant = None

        for u, v in edges:
            if union(u, v):
                return [u, v]

    