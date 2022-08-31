class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = { src : [] for src, dst in tickets}
        #intializes a dictionary with each 'from' location in tickets as a key with an empty list as the value
        
        
        tickets.sort()
        #sorts the tickets to lexical order, so that if we return an answer, the first result should be in lexical order
        
        for src, dst in tickets:
            adj[src].append(dst)
        #puts each 'to' location as an directed edge from the source inside the corresponding hashmap's list of edges
            
        res = ['JFK']
        #initializes the answer with the first location which will always be JFK
        
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                
                if dfs(v):
                    return True
                
                adj[src].insert(i, v)
                res.pop() 
            return False
        
        dfs('JFK')
        return res