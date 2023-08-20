class Solution:
    def topo_sort(self, adj, deg, sz):
        q = deque()
        
        for i in range(sz):
            if deg[i] == 0:
                q.append(i)
        ans = []
        while q:
            u = q.popleft()
            ans.append(u)
            for neigh_bor in adj[u]:
                deg[neigh_bor] -= 1
                if deg[neigh_bor] == 0:
                    q.append(neigh_bor)
        for i in range(sz):
            if deg[i] > 0:
                return []
        return ans
            

    def sortItems(self, n, m, group, beforeItems):
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        adj_item = [[] for _ in range(n)]
        deg_group = [0] * m
        deg_item = [0] * n
        adj_group = [set() for _ in range(m)]
        for i in range(n):
            to_i = group[i]
            for before_i in beforeItems[i]:
                to_j = group[before_i]
                
                if to_i != to_j and to_i not in adj_group[to_j]:
                    adj_group[to_j].add(to_i)
                    deg_group[to_i] += 1
                adj_item[before_i].append(i)
                deg_item[i] += 1
        
        # print(adj_item,deg_item)
        # print( adj_group,deg_group)
        sort_item = self.topo_sort(adj_item, deg_item, n)
        sort_group = self.topo_sort(adj_group, deg_group, m)
        # print(sort_item, sort_group)
        if not sort_item or not sort_group:
            return []
        ans = []
        items_ans = [[] for _ in range(m)]
        for i in sort_item:
            items_ans[group[i]].append(i)
        for i in sort_group:
            ans.extend(items_ans[i])

        return ans
