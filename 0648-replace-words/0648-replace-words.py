class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # Use an array to store the children of the node
        self.is_end_of_word = False
        self.word = ''

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
        node.word = word
        
    def search(self, word: str) -> str:
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                return ''
            
            if node.children[index].is_end_of_word:
                return node.children[index].word
            node = node.children[index]
        
        return node.word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for w in dictionary:
            trie.insert(w)
        words = sentence.split()
        ans = []
        for w in words:
            found = trie.search(w)
            if found:
                ans.append(found)
            else:
                ans.append(w)
            
        return ' '.join(ans)