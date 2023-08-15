class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.sizes = 0
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
                node.sizes += 1
            node = node.children[index]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node.is_end_of_word

    def searchLongest(self, word: str):
        ans = ''
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if( not node.children[index] 
            or node.is_end_of_word
            or node.sizes > 1 ):
                return ans
            ans += c
            node = node.children[index]
        return ans

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True  

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        trie = Trie()
        for s in strs:
            trie.insert(s)

        return trie.searchLongest(strs[0])
