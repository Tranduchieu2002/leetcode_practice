
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.sizes = 0
        self.is_end_of_word = False
        self.word = ""

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
        node.sizes += 1
        node.word = word
        node.is_end_of_word = True

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        self.ans = 0
        trie = Trie()

        for word in words:
            trie.insert(word)

        def dfs(node, counter):
            if node is not None and node.is_end_of_word:
                self.ans += (len(node.word) * node.sizes)
                
            for i in range(26):
                child = node.children[i]
                
                if child is not None and i in counter and counter[i] > 0:
                    counter[i] -= 1
                    dfs(child, counter)
                    counter[i] += 1
                
                    continue
        counter = defaultdict(int)
        for c in chars:
            index = ord(c) - ord('a')
            counter[index] += 1

        root = trie.root
        dfs(root, counter)
        return self.ans
