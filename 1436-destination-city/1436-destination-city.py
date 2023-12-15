class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        dest = defaultdict(list)
        visited = set()
        for (A, B) in paths:
            dest[A].append(B)
        ans = ""
        def dfs(cur_city):
            if cur_city not in dest:
                return cur_city
            visited.add(cur_city)
            for nei in dest[cur_city]:
                if nei not in visited:
                    return dfs(nei)
        ans = dfs(paths[0][0])
        return ans