class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = dict()
        
        
        def dfs(index):
            for adj in graph[index]:    #for all connections to a given node
                if adj in colors:
                    if colors[adj] == colors[index]:  #if same color return False, not bipartite
                        return False                  #if not same color, continue to next connection  
                                                        
                else:               #adjacency is not yet colored
                    colors[adj] = colors[index] * -1    #color adjacency to be opposite of our given node
                    if not dfs(adj):        #checks to see if that adjacency can be colored that way
                        return False
            return True     #if all adjacecies pass the given node will also pass
        
        for node in range(len(graph)):
            if node not in colors:
                colors[node] = 1    #colors our node if it hasnt been colored yet
                if not dfs(node):   #if node is equal to any adjacencies or cannot be colored, we return False
                    return False
                
        return True