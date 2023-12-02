from typing import List

from collections import Counter, deque

import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        task_count = Counter(tasks)
        maxHeap  = [ -task for task in task_count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1


            if maxHeap:
                task = 1 + heapq.heappop(maxHeap)
                if task < 0:
                    q.append([task, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

