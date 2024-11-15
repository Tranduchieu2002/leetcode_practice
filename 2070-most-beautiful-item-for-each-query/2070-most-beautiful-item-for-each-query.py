class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        items.sort()
        
        indexed_queries = []
        max_beauty_indice = 0
        for i, (price, beauty) in enumerate(items):
            max_beauty_indice = max(beauty, max_beauty_indice)
            items[i][1] = max_beauty_indice
            
        for i, q in enumerate(queries):
            indexed_queries.append((q, i))
        indexed_queries.sort()
        
        ans = [0] * len(indexed_queries)
        j, n = 0, len(items)
        for query, i in indexed_queries:
            
            
            while j < len(items) and items[j][0] <= query:
                j += 1
            
            beauty = 0
            if j > 0:
                beauty = items[j - 1][1]
            ans[i] = beauty
        
        return ans
                