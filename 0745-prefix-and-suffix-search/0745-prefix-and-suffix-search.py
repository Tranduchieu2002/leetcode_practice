class TrieNode:
    def __init__(self):
        self.children = [None] * 27
        self.sizes = 0
        self.index = -1
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, i = -1) -> None:
        node = self.root
        after_braket = False
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
                node.sizes += 1
            node = node.children[index]
            if after_braket:
                node.index = i
            if c == '{':
                after_braket = True
        node.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                return -1
            node = node.children[index]
        return node.index

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 0:
#             return ""
#         if len(strs) == 1:
#             return strs[0]

#         trie = Trie()
#         for s in strs:
#             trie.insert(s)

#         return trie.searchLongest(strs[0])
    def modify_insert(self, word, index):
        n = len(word)
        for j, val in enumerate(word):
            subs = word[n - j - 1:] + '{' + word
            self.insert(subs, index)
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        
        for i, word in enumerate(words):            
            self.trie.modify_insert(word, i)
    
    def f(self, pref: str, suff: str) -> int:
        word = suff + '{' + pref
        return self.trie.search(word)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)