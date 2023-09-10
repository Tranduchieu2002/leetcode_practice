class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n, q = len(equations), len(queries)
        results = []
#         Sử dụng tính chất hoán vị của phép nhân  + bfs để tim ra được hàng biến trùng nhau
        equations_dict = {}
        for i in range(n):
            (e1, e2) = equations[i]
            if e1 not in equations_dict:
                equations_dict[e1] = []
            if e2 not in equations_dict:
                equations_dict[e2] = []
            equations_dict[e1].append((e2, values[i]))
            equations_dict[e2].append((e1, 1 / values[i]))
        
        # Evaluate queries
        for query in queries:
            x1, x2 = query
            if x1 not in equations_dict or x2 not in equations_dict:
                results.append(-1.0)
                continue
            stack = [(x1, 1.0)]
            visited = set()
            result = float('inf')
            while stack:
                (u, current_value) = stack.pop()
                visited.add(u)
                if u == x2:
                    result = current_value
                    break
                for (v, w) in equations_dict.get(u, []):
                    if v not in visited:
                        stack.append((v, current_value * w))
            if result != float('inf'):
                results.append(result)
            else:
                results.append(-1.0)
        
        return results
