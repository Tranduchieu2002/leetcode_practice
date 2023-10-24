class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * n
        for i in range(n):
            if leftChild[i] != -1:
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                indegree[rightChild[i]] += 1
        root = None
        for i in range(n):
            if indegree[i] == 0:
                if root is None:
                    root = i
                else:
                    return False
                
        if root is None:
            return False
        visited = [False] * n
        q = [root]
        while q:
            cur = q.pop()
            if visited[cur] == True:
                return False
            visited[cur] = True
            if leftChild[cur] != -1:
                q.append(leftChild[cur])
            if rightChild[cur] != -1:
                q.append(rightChild[cur])
        return sum(visited) == n