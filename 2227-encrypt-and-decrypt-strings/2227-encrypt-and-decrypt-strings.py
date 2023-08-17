class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False
        self.match = 0

class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word: str) -> None:
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end_of_word = True
        node.match += 1
        
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                return 0
            node = node.children[index]
        
        return node.match
    def search_many(self, word):
        return True 


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.dic = {}
        for i in range(len(keys)):
            index = ord(keys[i]) - ord('a')
            self.dic[keys[i]] = values[i]
        self.trie = Trie()
        for d in dictionary:
            enKey = self.encrypt(d)
            self.trie.insert(enKey)
        

    def encrypt(self, word: str) -> str:
        ans = ""
        for w in word:
            if w not in self.dic:
                return ''
            ans += self.dic[w]
        return ans

    def decrypt(self, word: str) -> int:
        return self.trie.search(word)
        


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)