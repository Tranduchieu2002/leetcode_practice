class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # Use an array to store the children of the node
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

    def isValid(self,s: str, i, j, isCheck = False):
        node = self.root
        for k in range(i , j + 1):
            c = s[k]
            index = ord(c) - ord('a')
            if node.children[index] is None:
                return True
            if node.children[index].is_end_of_word:
                return False
            node = node.children[index]
        return True
            

    
class Solution:
    def __init__(self):
        self.trie = Trie()
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        for c in forbidden:
            self.trie.insert(c)
        n = len(word)
        ans = 0
        j = n - 1
        for i in range(n - 1, -1, - 1):
            # print('J' , j, "I", i)
            while not self.trie.isValid(word, i, j):
                j -= 1
            ans = max(ans,j - i + 1)
        
        return ans
        