class TrieNode:
    def __init__(self):
        self.children = [None] * 26
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

    def searchByDot(self, node, word):
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for child in node.children:
                    if child is not None:
                        if self.searchByDot(child, word[i+1:]):
                            return True
                return False
            index = ord(c) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True  

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.searchByDot(self.trie.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
