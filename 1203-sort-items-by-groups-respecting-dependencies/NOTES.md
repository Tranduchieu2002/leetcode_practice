for i in range(n):
to_i = group[i]
for from_item in beforeItems[i]:
from_j = group[from_item]
if to_i != from_j and to_i not in adj_group_set[from_j]:
adj_group_set[from_j].add(to_i)
deg_group[to_i] += 1
adj_item[from_item].append(i)
deg_item[i] += 1
print(adj_item, deg_item)
print(deg_group, adj_group_set)
sort_group = self.topo_sort(adj_group_set, deg_group, m)
sort_item = self.topo_sort(adj_item, deg_item, n)
​
if not sort_group or not sort_item:
return []
​
item_gp = [[] for _ in range(m)]
for i in sort_item:
item_gp[group[i]].append(i)
​
ans = []
for i in sort_group:
ans.extend(item_gp[i])
​
return ans
[[], [], [], [4], [], [2], [1, 3, 4], []] [0, 1, 1, 1, 2, 0, 0, 0]
[0, 0, 0, 1, 0] [{3}, set(), set(), set(), set()]
​
​
[[], [4], [4], [0, 4], []] [1, 0, 0, 0, 3]
[set(), {0}, {0}] [3, 0, 0]
​
[[], [4], [4], [0, 4], []] [1, 0, 0, 0, 3]
[2, 0, 0] [set(), {0}, {0}]