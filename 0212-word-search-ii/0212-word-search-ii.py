class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False
        self.word  = ''

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
        node.word = word
        node.is_end_of_word = True
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
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

class Solution:
    def __init__(self):
        self.trie = Trie()
    def dfs(i):
        return 
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m =  len(board), len(board[0])
        d = [[0 , 1], [0, -1], [1, 0], [-1, 0]]
        ans = []
        for w in words:
            self.trie.insert(w)
        def backtrack(i, j, res, root):
            if i < 0 or j < 0 or i == n or j == m or board[i][j] == '':
                return
            index = ord(board[i][j]) - ord('a')
            if root.children[index] is None:
                return
            root = root.children[index]
            temp = board[i][j]
            if root.is_end_of_word:
                ans.append(root.word)
                root.is_end_of_word = False
            board[i][j] = ''
            for (x, y) in d:
                dx, dy =  x + i, y + j
                backtrack(dx, dy, res + temp , root)
            
            board[i][j] = temp
        for i in range(n):
            for j in range(m):
                backtrack(i, j, "", self.trie.root)
                
        return ans
        