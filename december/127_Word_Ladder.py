from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        wordList.append(beginWord)
        graph = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                graph[pattern].append(word)

        visited = set([beginWord])
        q = deque([beginWord])
        level = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: return level

                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]

                    for neighbor in graph[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)

            level += 1
        
        return 0

