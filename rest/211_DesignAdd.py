class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
        

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root)
    
    def dfs(self, word, node):
        cur = node
        for i, c in enumerate(word):
            if c == '.':
                for child in cur.children:
                    if self.dfs(word[i+1:], cur.children[child]):
                        return True
                return False
            elif c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)