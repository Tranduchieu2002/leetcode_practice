class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n, q = len(equations), len(queries)
        ans = []
        mp = {}
        
        
        for i in range(n):
            (e1, e2) = equations[i]
            if e1 not in mp:
                mp[e1] = []
            if e2 not in mp:
                mp[e2] = []
            mp[e1].append((e2, values[i]))
            mp[e1].append((e1, 1.0))
            
            mp[e2].append((e1, 1 / values[i]))
            mp[e2].append((e2, 1.0))
        
        for q in queries:
            x1 , x2  = q
            if x1 not in mp or x2 not in mp:
                ans.append(-1)
                continue
            st = [(x1, 1.0)]
            visited = set()
            val = float('inf')
            while st:
                (u, curVal) = st.pop()
                visited.add(u)
                
                if u == x2:
                    val = curVal
                    break
                for (v, w) in mp.get(u, []):
                    if v not in visited:
                        st.append((v, curVal * w))
#                      x1 = 2 * b => b = {a , c}
            if val != float('inf'):
                ans.append(val)
            else:
                ans.append(-1)
            
        return ans