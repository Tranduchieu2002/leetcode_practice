class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        total_tickets = len(tickets)
        
        for ticket in tickets:
            adj[ticket[0]].append(ticket[1])
        
        for key in adj:
            adj[key].sort(reverse= True)
            
        ans = []
        st = ['JFK']
        while st:
            top = st[-1]
            neighbors = adj.get(top, [])
            
            if not neighbors:
                ans.append(st.pop())
                continue
    
            topNeighbor = neighbors.pop()
            st.append(topNeighbor)
        
        return ans[::-1]
        