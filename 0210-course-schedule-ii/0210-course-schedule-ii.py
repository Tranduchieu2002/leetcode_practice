class Solution:
    def findOrder(self, numCourses: int, p: List[List[int]]) -> List[int]:
        adj = {}
        ans, indegree = [], [0] * numCourses
        visited = [False] * numCourses
        q = set()
        n = len(p)
        for course, needed in p:
            adj.setdefault(needed, []).append(course)
            indegree[course] += 1
        for i in range(numCourses):
            if indegree[i] == 0:
                q.add(i)
        # print(adj)
        while q:
            u = q.pop()
            ans.append(u)
            visited[u] = True
            for v in adj.get(u, []):
                if not visited[v] and indegree[v] > 0:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.add(v)
        if len(ans) == numCourses:
            return ans
        return []